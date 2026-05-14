import json
import pandas as pd
import pyarrow.parquet as pq

# For sentiment analysis
from nltk.sentiment import SentimentIntensityAnalyzer
import nltk

pf = pq.ParquetFile("metadata.parquet")

nltk.download('vader_lexicon') # Download the VADER lexicon for sentiment analysis

def parse_json_field(entry):
    if entry is None:
        return []
    try:
        return json.loads(entry)
    except:
        return []

#cleans hashtags and checks for exact matches
def has_exact_tag(tags_json, targets):
    tags = parse_json_field(tags_json)
    targets = set(t.lower().lstrip('#') for t in targets)
    return any(str(t).lower().lstrip('#') in targets for t in tags)

## Parses the engagement_metrics field, which is a JSON string containing various metrics like likes, shares, etc.
def parse_engagement(entry):
    if entry is None:
        return {}
    if isinstance(entry, str):
        try:
            parsed = json.loads(entry)
            return parsed if isinstance(parsed, dict) else {}
        except:
            return {}
    if isinstance(entry, dict):
        return entry
    return {}


# columns to read from parquet file
cols = ['video_id', 'web_url', 'creator', 'description', 'hashtags',
        'comments', 'engagement_metrics', 'date_posted', 'language']

booktok_chunks = []
dancetok_chunks = []

print("scanning shofo...")

for i, batch in enumerate(pf.iter_batches(batch_size=10_000, columns=cols)):
    chunk = batch.to_pandas()

    booktok_chunks.append(
        chunk[
            chunk['hashtags'].apply(
                lambda x: has_exact_tag( #change from substring to exact match
                    x,
                    ["booktok", "bookrecs", "books", "reading", "reader", "bookreview", "bookrecommendation", "currentlyreading", "bibliophile"]
                )
            )
        ]
    )

    dancetok_chunks.append(
        chunk[
            chunk['hashtags'].apply(
                lambda x: has_exact_tag(
                    x,
                    ["dance", "choreo", "dancer", "dancetok", "dancing", "choreography", "hiphop", "ballet", "contemporary", "salsa", "tango", "ballroom", "streetdance", "breakdance", "kpopdance", "latindance", "jazzdance", "tapdance", "folkdance", "traditionaldance", "dancemusic", "dancechallenge", "dancetrend", "dancemoves", "dancetutorial", "danceduets", "dancesolo", "dancecover", "danceduo", "dancerecital", "danceperformance", "danceclass", "danceworkshop", "dancefestival", "dancecompetition", "danceshowcase", "danceday", "danceweekend", "dancevibes"]
                )
            )
        ]
    )

    print(f"  batch {i+1} done")

booktok = pd.concat(booktok_chunks, ignore_index=True)
dancetok = pd.concat(dancetok_chunks, ignore_index=True)

print(f"\nBookTok videos: {len(booktok)}")
print(f"DanceTok-related videos: {len(dancetok)}")

# Parse comments and hashtags
#separate comments into individual rows, and extract text from comments
booktok['comments_parsed'] = booktok['comments'].apply(parse_json_field)
dancetok['comments_parsed'] = dancetok['comments'].apply(parse_json_field)

booktok = booktok.explode("comments_parsed")
dancetok = dancetok.explode("comments_parsed")

booktok["comment_text"] = booktok["comments_parsed"].apply(
    lambda x: x.get("text", "") if isinstance(x, dict) else ""
)

dancetok["comment_text"] = dancetok["comments_parsed"].apply(
    lambda x: x.get("text", "") if isinstance(x, dict) else ""
)

# Parse hashtags into lists
booktok['hashtags_parsed'] = booktok['hashtags'].apply(parse_json_field)
dancetok['hashtags_parsed'] = dancetok['hashtags'].apply(parse_json_field)

# Create a caption field (using description, or empty string if description is missing)
booktok['caption'] = booktok['description'].fillna("")
dancetok['caption'] = dancetok['description'].fillna("")

## make table

# Make dataset labels
booktok['dataset_type'] = 'scaled_booktok'
dancetok['dataset_type'] = 'scaled_dancetok'

manual = pd.read_csv("manual_dataset.csv")

comment_cols = [
    "Comment 1",
    "Comment 2",
    "Comment 3",
    "Comment 4",
    "Comment 5"
]

type_cols = [
    "Comment Type",
    "Comment Type.1",
    "Comment Type.2",
    "Comment Type.3",
    "Comment Type.4"
]

rows = []

# Iterate through each row in the manual dataset and create a new row for each comment, while keeping the other data the same
for _, row in manual.iterrows():
    base_data = row.drop(labels=comment_cols + type_cols, errors="ignore").to_dict()

    for i in range(len(comment_cols)):
        comment = row.get(comment_cols[i])
        ctype = row.get(type_cols[i])

        if pd.notna(comment) and str(comment).strip() != "":
            rows.append({
                **base_data,
                "comment_text": str(comment).strip(),
                "comment_type": "" if pd.isna(ctype) else str(ctype).strip()
            })

manual = pd.DataFrame(rows)

if "Tok_Hashtag" in manual.columns:
    manual["Tok_Hashtag"] = manual["Tok_Hashtag"].fillna("")
else:
    manual["Tok_Hashtag"] = ""

if "description" in manual.columns:
    manual["caption"] = manual["description"].fillna("")
else:
    manual["caption"] = ""
manual["dataset_type"] = "manual"

# Put hashtags_parsed INTO existing manual column name
booktok['Tok_Hashtag'] = booktok['hashtags_parsed'].apply(
    lambda x: " | ".join(x) if isinstance(x, list) else ""
)

dancetok['Tok_Hashtag'] = dancetok['hashtags_parsed'].apply(
    lambda x: " | ".join(x) if isinstance(x, list) else ""
)

booktok["Video Link"] = booktok["web_url"]
dancetok["Video Link"] = dancetok["web_url"]


# combine datasets into one big table, with a column to indicate which dataset each row came from
combined = pd.concat(
    [manual, booktok, dancetok],
    ignore_index=True,
    sort=False
)

# REMOVE THE EXACT PROBLEM COLUMN
combined = combined.drop(columns=["Sheet1!I1"], errors="ignore")

# sentiment analysis on comments useing VADER

combined["comment_text"] = combined["comment_text"].fillna("")

sia = SentimentIntensityAnalyzer()

combined["sentiment_score"] = combined["comment_text"].apply(
    lambda x: sia.polarity_scores(str(x))["compound"]
)

def label_sentiment(score):
    if score >= 0.05:
        return "positive"
    elif score <= -0.05:
        return "negative"
    else:
        return "neutral"

combined["sentiment"] = combined["sentiment_score"].apply(label_sentiment)

# create clean sequential ID column (ONLY ONCE)
combined = combined.reset_index(drop=True)
combined.insert(0, "Sheet1l1", combined.index + 1)

cols = ["dataset_type"] + [c for c in combined.columns if c != "dataset_type"]
combined = combined[cols]

combined = combined.drop(columns=["video_id"], errors="ignore")
combined = combined.drop(columns=["web_url"], errors="ignore")

combined.to_csv("combined_dataset.csv", index=False)

print("\nCombined dataset saved!")
print(combined.head())

# separate BookTok and DanceTok videos
booktok = combined[combined["dataset_type"] == "scaled_booktok"]
dancetok = combined[combined["dataset_type"] == "scaled_dancetok"]

# sentiments value counts for each dataset
booktok_sentiments = booktok["sentiment"].value_counts()
dancetok_sentiments = dancetok["sentiment"].value_counts()

# print results
print("\nBookTok")
print(booktok_sentiments)

print("\nDanceTok")
print(dancetok_sentiments)

# if entry is missing, default to 0
book_pos = booktok_sentiments.get("positive", 0)
book_neg = booktok_sentiments.get("negative", 0)
book_neu = booktok_sentiments.get("neutral", 0)

dance_pos = dancetok_sentiments.get("positive", 0)
dance_neg = dancetok_sentiments.get("negative", 0)
dance_neu = dancetok_sentiments.get("neutral", 0)
