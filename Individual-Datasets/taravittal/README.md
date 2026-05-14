# AI and Student Discourse Dataset

## Overview
This project explores how students discuss and perceive the relationship between artificial intelligence (AI) tools and academic performance. Rather than attempting to measure the actual impact of AI on grades, this dataset focuses on student perspectives, attitudes, and experiences as expressed in online communities.

## Cultural Materials
The dataset consists of publicly available Reddit posts from student-focused communities such as r/college, r/GetStudying, and r/uiuc. These posts were selected because they reflect real student discussions about AI use in academic settings, including topics such as studying, assignments, grades, and academic integrity.

## Approach
This dataset was created from scratch through manual data collection and annotation. Each entry represents an individual Reddit post that mentions AI tools (primarily ChatGPT) in relation to academic work.

## Computational Tools
A Python-based command line interface (CLI) script was developed to assist in data collection. The script allows for structured data entry and automatically stores each entry in a CSV file.

Libraries used:
- Python (csv module)
- Rich (for formatted terminal output)

These tools helped standardize the data collection process and reduce formatting errors. However, the process still required manual interpretation and labeling, which introduces subjectivity.

## Data Structure
Each row in the dataset includes:
- id
- platform
- subreddit
- mentions_AI
- AI_tool
- sentiment
- mentions_grades
- link

## Interpretive Decisions
Several key decisions were made during dataset creation:

- Only posts that explicitly mention AI in an academic context were included
- Posts were labeled based on perceived sentiment (positive, negative, or mixed)
- Mentions of grades were determined based on explicit references to academic performance
- The dataset focuses on student perspectives rather than institutional or expert viewpoints

## Limitations
This dataset has several limitations:

- Reddit users are not representative of all students
- Posts are self-reported and may be exaggerated or incomplete
- Sentiment labeling is subjective
- The dataset does not measure actual academic outcomes, only perceptions

## Observations
Initial patterns suggest that student discussions of AI in education often fall into several themes:

- AI as a productivity tool
- Concerns about cheating and academic integrity
- Fear of being detected or penalized
- Tension between efficiency and genuine learning

These patterns highlight the complexity of how students understand and use AI in academic contexts.

## Next Steps
The next phase of this project will involve scaling the dataset using computational methods.

Possible approaches include:
- Web scraping Reddit posts using APIs
- Expanding keyword searches to collect larger datasets
- Using natural language processing (NLP) to classify sentiment automatically

As the dataset scales, interpretive decisions such as sentiment classification may be partially automated. However, this introduces challenges such as reduced accuracy and loss of nuance.

Additionally, larger datasets may reveal broader patterns but may obscure the detailed, interpretive work involved in manual data collection.

## Conclusion
This dataset serves as a first step in understanding how students culturally interpret AI in education. It highlights the importance of careful data creation and the role of interpretation in shaping datasets.
