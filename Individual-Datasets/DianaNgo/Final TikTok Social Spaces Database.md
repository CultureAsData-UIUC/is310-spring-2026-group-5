## Abstract

This project investigates TikTok culture through online communities of BookTok and DanceTok, analyzing how viewers engage within these social spaces through comments by matching hashtags and utilizing sentiment analysis. The dataset is a combination of manually collected TikTok data along with a computationally scaled dataset that is derived from the Shofo/shofo-tiktok-general-small dataset on Hugging Face. The overall dataset contains 4,810 comment entries, with indications on which comments were manually found and which were collected from the Shofo dataset when scaling. 

The programming was done through VS code, using python, hashtag filtering, and VADER sentiment analysis. For every entry the VADER sentiment analysis was able to categorize each comment on being positive, negative, or neutral. The manual data entries have a secondary categorization listed as “Comment Type”, labeling comments as a Opinion/Reaction, Question, Giving Advice/Help, or Other. 

The results indicated that both BookTok and DanceTok communities contain majority neutral comments. BookTok's sentiment analysis displayed an overall slightly stronger attitude of positive and negative comments compared to DanceTok. Meanwhile, DanceTok contained a significantly higher volume of video content and comment engagement. The dataset represents the challenges working with online culture as data, as media rich content have various restrictions such as API limitations, unrelated results, format inconsistencies, and overgeneralizations with Lexicon sentiment tools. 


## Introduction

This final dataset represents the culture of TikTok-made communities, specifically looking into the difference in engagement between BookTok and DanceTok. TikTok has been an emerging social media platform that engages a diverse range of communities, which range from subjects of cooking, studying, and hobbies. Among the range of “Tok’ communities, there is a lack of investigation on the way people engage with the content. Numeric metrics such as views, reposts, and saves are commonly recorded and analyzed, but do these quantitative analyses truly represent the attitudes and engagement of these social spaces on TikTok? This database observes the TikTok culture through curating and scraping cultural data, capturing both qualitative and quantitative patterns across BookTok and DanceTok online communities in effort to address differences in engagement across these social spaces . 



## Why BookTok & DanceTok?

I selected BookTok and DanceTok because these TikTok communities appear to be distinctly different topics of interest. BookTok discusses fandoms, recommendations, and theories while DanceTok focuses on trending music and choreography. I believed that observing these two communities provide prominent insights to how versatile communities are on TikTok, hoping to detect differences in participant engagement. 


**What was found:**
DanceTok videos were more abundant, while BookTok videos were more difficult to locate 
Total Entries: 4810 (245 rows weren’t counted in VADER sentiment analysis) 
BookTok:
Comment count: 392
252 neutral (64.29%)
93 positive (23.72%)
47 negative (11.99%)
DanceTok:
Comment count: 4,173
2987 neutral (71.58%)
779 positive (18.67%)
407 negative (9.75%)

The sentiment analysis shows that in both social spaces, BookTok and DanceTok, there are a majority of neutral comments, followed by positive comments. Notice there is a significant difference in the number of videos scraped between BookTok and DanceTok, with the DanceTok community having a higher video and comment count, indicating that the DanceTok culture may be more popular and circulated through the TikTok algorithm compared to BookTok, which tends to be more niche. 

Based on the sentiment analysis, there is a generally positive or neutral comment engagement for both communities, but BookTok has a slightly stronger opinion, as the neutral percentage relative to comment count is lower compared to the DanceTok neutral percentile. Although there is only a slight range of difference between sentiment percentile, the difference suggests that BookTok’s audience may have stronger opinions, where positive and negative comments are more detectable. Meanwhile, Dancetok comments tend to be more neutral, possibly due to the large volume of content causing more passive engagements to the trending dances and songs, rather than being fully invested in the content. 


## Story of TikTok Social Spaces Database

## The Initial Dataset:

Initially, I wanted this dataset to scrape the WayBack Machine to create a small-scale initial dataset. However, when I considered the challenges with missing and inconsistent data and long, unreliable wait times for generating archived data, I started to reconsider how I will approach my initial dataset. Similarly, I realized that my investigation into social spaces wouldn’t quite reflect my approach to utilizing WayBack Machine to see the progression of social media interfaces, as this doesn’t engage with the communities, but rather tackles the evolution of social media interfaces. At this point, I decided to pivot my research plan, aiming to collect 50 TikTok videos under their respective hashtags, measuring their engagement rates. Initially, I proposed that I would record 5 different hashtags, such as BeautyTok, DanceTok, BookTok, FoodTok, and GymTok. However, after consulting with Professor Zoe, I realized that my research scope is not defined, and I broadened my scope too widely. Although it would be great to cover these various TikTok communities, investigating this media-rich data with the goal of analyzing engagement between them wouldn’t be as insightful. In the case where I only search for quantitative data, such as the number of views, likes, shares, etc., this wide approach that incorporates multiple hashtags would be more suitable. However, the goal of this semester-long project is to explore how I am able to create and work with culture as data, and to seek that culture, I must funnel my focus on the qualitative data more directly, which guided my reasoning to condense my hashtag search to only BookTok and DanceTok.

Initial Dataset Plan:
Manually collected & recorded on Google Sheets
2 hashtags: #Booktok & #DanceTok
25 videos each
Download videos
Quantitative Data: Year, Likes, Comments (#)
Qualitative Data: Text of top 5 comments
Categorize each comment by “Comment Type”: Opinion/Reaction, Question, Giving Advice/Help, Other 

## Initial Dataset / Manual Collection:
As stated above, the initial dataset was manually collected. The data collection process took approximately 2-3 hours, ensuring that all data was collected at the same time so that videos’ metrics and top comments don’t differ depending on the date the data is collected. During the manual collection process, I equipped Google Spreadsheet tools to optimize the workflow, creating data validation rules for the numeric data, making data such as the year, likes, saves, and comment count, into pre-determined dropdown menus so that I don’t have to manually type in the data. However, one issue I encountered was deciphering the range for the numeric metrics, as I either under or overgeneralized groups, which caused a video with 500 comments to be grouped with a video with 2,000 comments because I set the range to end at 500+ comments. Attempting to optimize this workflow caused me to constantly change my ranges to accurately represent the video’s metrics. An alternative method would be to input the exact numeric count for each of the quantitative columns, but that manual implementation wouldn’t be feasible in the long-term. 

Additionally, I created a data validation rule for comment types, including: Opinion/Reaction, Question, Giving Advice/Help, and Other. These categories aimed to reflect the general variation of comments typically seen on social media. However, in hindsight, one major limitation for these categories is the amount of overlap between certain comments that qualify for both categories. Another issue emerged as the majority of the categories are Opinion/Reaction, which indicates an issue with over-generalization with these categories. 

Takeaways from Initial Dataset:
Manually recording data risks lower accuracy, inconsistencies, and overgeneralized records
Not feasible to scale to larger data (100+)
The manual dataset allows for more customization in labeling, columns, and ranges


## Scaling Dataset

As I approached the next step after creating my initial dataset, I worked on scaling my dataset through computation. I originally wanted to obtain TikTok data through an API, but this presented as a major issue as the TikTok API is non-accessible to the public. In light of this obstacle, I surfed the internet for an existing TikTok dataset that is similar to my goals from my initial dataset. I searched through Hugging Face, which is an online center that has various open datasets. Within my search, I considered a dataset with the following attributes.

Dataset Search Guidelines (HuggingFace):
Comments
Comment count
Video link
Hashtags

Eventually, I discovered the Shofo/shofo-tiktok-general-small dataset, which contains approximately 58k rows of videos including comments, engagement metrics, hashtags, and original video links. Although both my manual databases and the Shofo database have quantitative data, and initially prioritized the numeric metric, I decided to narrow my scope when conducting my scraping to focus on comments and hashtags, while also documenting the original video link for record purposes. 


## Computational Methods:
As for how I conducted the data scaling, I executed my final dataset through the Option 2 approach by auditing, merging, and analyzing. Instead of my original idea to utilize APIs, I used the pattern-matching approach using code to find keywords that are under BookTok and DanceTok. Originally, I only pattern-matched to hashtags “BookTok” and “DanceTok,” but the output was small, only scraping fewer than 8 BookTok videos and fewer than 100 DanceTok videos. After some iterations of hashtags filters, I added the following hashtags for the respective Tok communities: 

**BookTok:**
book", "read", "novel", "literature", "fiction", "reader", "bookstagram", "booklover", "bookish", "bookcommunity", "bookrecommendation", "bookreview", "booktube", "bookblogger", "bookaesthetic", "bookobsessed", "bookaddict", "booknerd", "bibliophile", "bookclub", "bookchallenge", "bookhaul", "currentlyreading", "tbr", "bookishfeatures", "bookshelf", "authorsoftiktok", "bookquotes", "bookart", "bookcover", "bookishhumor", "bookishmemes", "bookishlife", "bookishlove", "bookishthoughts", "bookishcommunity", "bookishworld", "bookishvibes", "bookishobsession", "bookishaddiction", "bookishnerd", "bookishreader", "bookishwriter"

**DanceTok:**
"dance", "choreo", "dancer", "dancetok", "dancing", "choreography", "hiphop", "ballet", "contemporary", "salsa", "tango", "ballroom", "streetdance", "breakdance", "kpopdance", "latin", "jazzdance", "tapdance", "folk", "traditionaldance", "dancemusic", "dancechallenge", "dancetrend", "dancemoves", "dancetutorial", "danceduets", "dancesolo", "dancecover", "danceduo", "dancerecital", "danceperformance", "danceclass", "danceworkshop", "dancefestival", "dancecompetition", "danceshowcase", "danceday", "danceweekend", "dancevibes"

Expanding the hashtags' scope successfully increased the number of videos connected with over 200 videos for BookTok and over 1000 videos for DanceTok. However, the disadvantage can be seen in the level or relevance that blurred my scraping as the following outputs were produced:

**BookTok Hashtags:** 
russellwestbrook         12
the notebook               8
BookTok                   7
YoSoyCreador              3
scrapbook                 3
scrapbooking              3
readySETgo                2
lightbrown                2
bookoflife                2
devinbooker               2
facebook                  1
icantbreathe              1
BookRecs                  1
dreads                    1
ReadySipGo                1
smuttbook                 1
GetReadyWithOldSpice      1
thenotebookedit           1
mindreading               1
beautifulnotbroken        1
CloudBread                1
laurasbooktalk            1
readingchair              1
greenbook                 1
readyplayerone            1
bakethisbread             1
soycreador                1
missyoualready            1
bookofbill                1
thebookoflife             1
menspreading              1
milkbread                 1
timothytreadwell          1
creadoradecontenido       1
lewatbranda               1
soycreadordecontenido     1
bookert                   1
jojosbizarreadventure     1
carpetbrushing            1
book                      1
spreadthegospel✝️😇        1
beready                   1
TikTokCookBook            1
popupbookofphobias        1
GetReadyWithMe            1
betweenthebread           1
books                     1

As you can see, unrelated videos were scraped, such as “dreads, Facebook, menspreading,” etc. In this circumstance, I ultimately decided to eliminate the noise by making my code find the exact text of that tag and limiting the amount of hashtags, which looks like this: 

**BookTok:**
"booktok", "bookrecs", "books", "reading", "reader", "bookreview", "bookrecommendation", "currentlyreading", "bibliophile"

**DanceTok:** 
"dance", "choreo", "dancer", "dancetok", "dancing", "choreography", "hiphop", "ballet", "contemporary", "salsa", "tango", "ballroom", "streetdance", "breakdance", "kpopdance", "latindance", "jazzdance", "tapdance", "folkdance", "traditionaldance", "dancemusic", "dancechallenge", "dancetrend", "dancemoves", "dancetutorial", "danceduets", "dancesolo", "dancecover", "danceduo", "dancerecital", "danceperformance", "danceclass", "danceworkshop", "dancefestival", "dancecompetition", "danceshowcase", "danceday", "danceweekend", "dancevibes"

With this trade-off, I prioritized the quality and relevance of the data collected rather than the volume. Although creating an exact tag filter and lowering the number of hashtags resulted in the original 280 videos total being lowered to 97 videos, these videos all represent the BookTok and DanceTok social spaces that increase the quality of the combined dataset. 


What changes occur when the project is scaled?

When scaling the project, combining my manual dataset with the Shofo dataset, I reconsidered how I structured the overall layout. Within my manual dataset, the structure reflected the following: 

| ![](manual%20dataset%20image.png) |
| :--: |
| <b>Figure 1.</b> Manual Dataset Image. |

Within the manual dataset, every entry was a video, and for each video was top 5 comments and their respective comment type. However, when analyzing the Shofo dataset, their comment column contains multiple comments within rows, which makes it difficult to compare the two videos and work with them. As a result, I decided to create separate columns for both manual comments and the Shofo dataset comments to make them more usable for analysis. 

Now, both the manual dataset and the scaled dataset have each entry as a comment. 

| ![](scaled%20dataset%20image.jpg) |
| :--: |
| <b>Figure 2.</b> Combined Dataset Image. |

What interpretive decisions were automated?

As mentioned previously, with the manual dataset, I created 4 comment type categories: Opinion/Reaction, Question, Giving Advice/Help, and Other. This categorization was a manual form of analysis, where I looked through each comment and determined from my own judgment which category(s) the comment fits into. The manual categorization allowed me to observe each individual comment with greater intention and analysis, but also took an extensive amount of time. As I embarked on scaling my project, I knew I wanted to mimic my manual comment type categorization through automation. After completing the “Critical Computing & Cultural Data: Building Principles Through Published Research” assignment where I conducted a literature review on “A Labelled Dataset for Sentiment Analysis of Videos on YouTube, TikTok, and Other Sources about the 2024 Outbreak of Measles” by Nirmalya Thakur et al., I learned about how they utilized VADER for sentiment analysis, TextBlob for subjectivity analysis, and DistilRoBERTa-base for fine-grained sentiment analysis for their investigation into social media content on 2024 measles outbreaks. From this literature review, I was inspired by their use of VADER for sentiment analysis and equipped this tool to automate comment type attitudes within my dataset. 

## What is VADER?

VADER is a lexicon-based tool for sentiment analysis that extracts subjective information from text, categorizing text as either neutral, positive, or negative. VADER is specifically used for analyzing social media text, which fits perfectly into observing social media comments. VADER is on a compound scale of -1 (most negative) to +1 (most positive). Implementing VADER was simple, and the sentiment analysis was extremely fast, doing what took me hours into seconds. However, VADER sentiment analysis has some downsides, as it observes each individual word within the comment’s text, causing it to struggle with sarcasm and doesn’t understand context. For example, in my combined dataset in entry 381, the comment is “Damn. He understood the assignment,” which had a sentiment score of -0.4019, which is categorized as negative. However, when understanding the context of the video, it is understood that the comment was meant as support, but VADER took words such as “Damn” as negative, skewing the sentiment score. Additionally, multiple comments within my combined data are in a different language, which VADER couldn’t understand and stated these comments as neutral.

Where does the Shofo dataset come from?
Link to Shofo Dataset: https://huggingface.co/datasets/Shofo/shofo-tiktok-general-small

Shofo is a company backed by Y-combinator (https://www.shofo.ai/). Shofo claims to be the World's Largest Video Library, providing access to custom datasets of video content that is cleaned, segmented, and primarily used for AI and social media research. The CEO of Sofo is Bryan Hong, who is also the co-founder along with Andre Braga, Braiden Dishman, and Alexzendor Misra, who can be found through their Y-combinator page: https://www.ycombinator.com/companies/shofo. These founders invested in Shofo with a mission to help AI labs obtain high-quality video data to train models in a feasible, efficient, and cost-effective way. On HuggingFace, Shofo’s dataset has approximately 15,000 downloads in the last month. Bryan Hong (CEO) states in the Shofo launch video posted on Jan 26, 2026, that the Shofo teams are “collecting, cleaning, labeling every post on social media to curate them into datasets that power the next generation of AI models” (0:21). Bryan Hong (CEO) provides an example of how the Shofo database can be used, “For example, AI labs can search for makeup videos narrated in Spanish with 500,000 likes whose top comments mention ‘natural’ or ‘glowing’ and get a curated dataset of exactly that,” (0:50). Although I am not utilizing the Shofo dataset to train AI, I used it to create a curated dataset that searches for videos of BookTok and DanceTok communities on TikTok. Overall, the Shofo dataset is a reliable database that derives from an existing company that focuses solely on providing the largest dataset of TikTok videos for researchers' use and is a great alternative to TikTok API.


## What were the technical challenges?

**1) Finding Databases that include comments**
	Locating databases that included comments from TikTok was extremely difficult. The majority of databases that scrape TikTok videos have numeric metrics with likes, shares, reshares, and comment count. Apart from the Shofo database, other datasets such as:
TikTok-Videos: https://huggingface.co/datasets/datahiveai/Tiktok-Videos
TikTok-trending-hashtags: https://huggingface.co/datasets/ronantakizawa/tiktok-trending-hashtags
Were considered as they contained two out of the three search guidelines, with these datasets containing hashtags and comment count, but no actual comments. Ultimately, I decided to only use the Shofo dataset, as the comments itself takes the largest priority in my research, as without it there is no sentiment analysis or true comparison of engagement on a qualitative level. 

**2) Accessing the Shofo Database**
The Shofo Database contains 57,960 videos, as it is the world's largest video library. I had various issues with accessing the Shofo Database because I structured my code to load all the data, then cut it into chunks, and then scraped the videos with BookTok and DanceTok hashtags. However, this method caused a long wait time, and in my case, the data didn’t load at all, even after clearing my cache. My first attempt was to try to access the Shofo Database by loading only a few rows at a time, but it still resulted in errors. Then I decided to only take the metadata from the Shofo Database, not download the videos themselves. This approach worked; I was able to access all the video information, but with the trade-off of not having a downloaded record of the videos as I did in my manual dataset. 

**3) Inconsistent Formatting**
When combining both the manual and scaled Shofo dataset, there were issues with inconsistent data and duplicated columns. The largest issue was converting the manual dataset to have every comment be an entry rather than every video, and separating the comments of the Shofo database to be its individual row. As for the duplicated columns, I was able to combine similar rows under one column and move the columns accordingly while deleting repetitive ones. 

**4) Finding relevant videos for BookTok**
BookTok hashtags output significantly lower results than under the DanceTok hashtag. When adjusting the exact tags for BookTok, I had issues with unrelated outputs. This issue may be due to BookTok being more niche while DanceTok is more general, as TikTok itself was originally a platform for lip syncing and dances. 

## Takeaways from Scaled Dataset:
Scraping a large dataset may restrict record-keeping of media-rich data (unable to download videos due to the large volume)
Sentiment Analysis is quicker, but can be overgeneralized 
Combining a manual and a scaled dataset causes issues with format and consistency 
More flexibility in locating videos under various hashtags 


## Differences between Initial (Manual Dataset & Scaled Dataset):
The construction of my manual dataset and scaled dataset offers various insights into the advantages and disadvantages in its approach of collecting cultural data. With my manual dataset, I was able to offer more attention to categorizing common types and utilizing my own judgments that understand context and justify the categorization. However, these judgments are inherently biased and can cause inconsistencies in data categorization. On the other hand, with the scaled dataset using Shofo, the VADER sentiment categorization creates a fixed scale that the comments are judged upon, which keeps consistency, but doesn’t have that contextual understanding humans do. Both the manual and scalable datasets have issues with overgeneralization and could benefit from a curated algorithm that makes more strict distinctions for these categories. 
Additionally, the manual dataset being small-scaled allowed me to download videos as a backup procedure if the video gets restricted or deleted, which did occur for one of my manually collected videos (listed as null) that was deleted. The manual dataset also allowed me to have direct access to the TikTok application since there were no API restrictions, and the platform itself is accessible to everyone. As for the scalable dataset, the videos couldn’t be downloaded because of the large size of the dataset, which doesn’t provide that second layer of archived security, so if TikTok were deleted, then the original link would become inaccessible. 
The scalable dataset’s greatest advantage was the ability to find videos under BookTok and DanceTok faster and collect more comments on a large-scale, compared to my manual dataset that only collected the top five comments of each video. Overall, the manual dataset proves beneficial in curating more customizable and contextual aspects of cultural data, but with the trade-off of time consumption, risks of inconsistency, and limited data entries. Meanwhile, the scaled dataset offers efficiency in data collection for more diverse hashtags, quicker numeric collection and sentiment analysis, and greater consistency, but struggles with understanding context.


## Reflection:

At the start of the semester, I had some prior experience coding in Java from taking CS124 and basic HTML/CSS from developing websites as a UX designer. Throughout the semester, I was able to not only learn how to code in Python, but also experience the ups and downs of working with culture as data. These are the various lessons I learned:

Quantitative Data is easy to collect, compared to capturing qualitative, media-rich data such as videos, literature, and films
Sentiment Analysis helps create consistent judgments, but Lexicon tools have issues replicating that human aspect of understanding context.
How to use an API and how certain corporations restricts API because of business and legal reasons
Cultural data can disappear if not properly recorded and archived 


## Qualifications & Limitations

Over the semester, the scale shaped the priorities and structure of the data. When scaling, I place further emphasis on the qualitative data I could collect through the Shofo database to truly reflect how I may capture culture within data that goes beyond the numeric metrics of social media spaces. 

This dataset should be understood as a fractional representation of social spaces within TikTok’s communities. This dataset captures real-time engagement and comments from TikTok’s viewers that were recorded through both manual and scaled data approaches. Consider that there are millions of other “Tok” social spaces that may be investigated, as this data only analyzes BookTok and DanceTok communities. As for limitations on VADER sentiment analysis, out of the 4810, 245 rows were not considered due to null entries, skewing the comment sentiment results. This dataset only partially represents the online social spaces of the BookTok and DanceTok communities based on the comments scraped during the timeframe of March 2026 to May 2026. Engagement rates, metrics, and comments may fluctuate in the future. 


## Ethical & Privacy Considerations

All posts on the TikTok platform were permitted for public viewing, so collecting and downloading these videos for academic use and observation is protected. However, it should be considered that creators may not expect for their videos to be archived in these datasets. All videos are linked to creator handles and tags which may expose personal information if already available on TikTok’s platforms. 


## Conclusion

Overall, this dataset analyzes the online social spaces of BookTok and DanceTok on the TikTok social media platform. The goal of this dataset is to analyze how engagement between online spaces interacts across different TikTok communities. This database contributes to the overall investigations into how people interact with emerging online platforms in the ways they contribute their opinions, critiques, and reactions that build these communities. The data collection itself serves as an attempt to investigate cultural attitudes and patterns and how these qualitative metrics can be measured. Moving forward, this dataset can continue to find more innovative ways to analyze the data collected that go beyond comment type categorization and Lexicon sentiment analysis, possibly considering more complex frameworks that can automate identities for comments and their contribution to the TikTok community culture. 

AI Usage Disclaimer: 
This project, under the permission of Professor Zoe and guidance of the AI Policy listed on the course website, I used ChatGPT to help debug and curate sections of my code, most notably for analyzing sentiment analysis, importing VADER, debugging function logic, and reformatting the CSV file. Ultimately, all data collection, research decisions, and writing were completed by me (the author), and all code was reviewed and cleaned if necessary. 
