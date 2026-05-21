## Collective Principles & Documentation 5%

Your group will collaboratively write a document with your group that synthesizes what you collectively learned about working with your particular type of cultural data. This is NOT a repeat of individual data essays—it’s methodological guidance and collective wisdom for future researchers.

Think of this as: Writing the documentation you wish had existed when you started this project. What should someone know before they attempt to represent music as data? Or social media? Or gaming culture? What principles emerged from your group’s diverse approaches to similar materials? At its core, this document should include a set of principles for working with your cultural topic as data. The document should also attempt to note how each member contributed to its format, and like all work, it will be submitted in your group’s collective GitHub repository.

Contributors: Diana Ngo, Tara, Zohra Hussaini, Haneen Odeh

---

## What we’ve learned

**Diana -**  
I’ve learned alternative methods for collecting data apart from APIs, understood and experimented with sentiment analysis tools, and discovered various challenges in recording media-rich data. Additionally, not only did I learn how to program in Python, but I was also able to experience how to collect data, clean it, and organize it for analysis. I also grew in understanding the limitations of collecting qualitative data, where legal restrictions and privacy concerns must be considered. When collecting TikTok data, I realized that digital spaces are more fluid, meaning that videos and images can become inaccessible over time, so documentation and archiving this data is crucial.

**Tara -**  
I learned different ways to turn online conversations, in this case about ChatGPT and education, into structured data that can be analyzed. I found that a lot of the discussions I found on Reddit often contained sarcasm, mixed opinions, or emotional responses that sentiment analysis tools like VADER do not always properly understand. I also learned that cleaning and organizing data is one of the most important parts of analysis. Many posts were repetitive, irrelevant, or missing important content. Most importantly, I learned that cultural data is not completely objective because people’s opinions about ChatGPT are often shaped by their personal experiences with academic stress or their understanding of AI.

**Zohra -**  
I learned that articles and online discussions about AI are not completely neutral. They show people’s opinions, worries, and ideas about students and technology. While making my dataset about AI plagiarism in education, I realized that turning articles into data takes interpretation. For example, deciding if an article was “positive” or “negative” was sometimes based on my own judgment. I also learned that even a smaller dataset can still show patterns in how people talk about AI. At the same time, my dataset did not show everything because it only focused on news articles and not real classroom experiences. This helped me understand that datasets are shaped by both the information collected and the person collecting it.

**Haneen -**
I learned that scholarly datasets are also highly interpretive, even when they appear more structured or objective than social media data. While creating my dataset about AI in K-12 education, I realized that categorizing articles into themes such as “productivity,” “ethics,” or “teacher attitudes” often depended on my own interpretation of abstracts and article summaries. I also learned that educational AI research changes very quickly, especially after the release of ChatGPT, which made it difficult to keep the dataset current.

In addition, I learned how computational tools can support humanities-oriented data work. Using Python to structure and update the dataset helped me organize large amounts of information more consistently. However, I also experienced how computational workflows can introduce problems such as formatting issues, metadata inconsistencies, and missing information during CSV conversion and data cleaning. This project helped me better understand the relationship between manual interpretation and computational organization in cultural datasets.

**What we learned together -**
Together, we learned that representing AI and social media culture as data is a highly interpretive process rather than a completely objective one. Across our projects, we experienced how online conversations (Reddit), articles, videos (TikTok), and discussions can be collected and transformed into structured datasets, but also how difficult it can be to accurately capture meaning, emotion, and context. We learned that sentiment analysis tools and coding methods can help identify patterns, yet they often struggle with sarcasm, mixed emotions, and emotions which commonly found in discussions about AI and education. We also discovered that cleaning, organizing, and filtering data is one of the most important and time consuming parts of the process because these online spaces often contain repetitive, irrelevant, or incomplete information. In addition, we recognized that digital media is constantly changing, with postsand discussions often gaining irrelevance over time, making documentation more essential. Most importantly, we learned that cultural datasets are shaped by both the limitations of the platforms being studied and by the decisions of the researcher that is collecting and interpreting the data.

---

## What people should know before attempting to represent social media and AI culture?

**Diana -**  
When approaching data collection for social media platforms, it’s important to know whether there is an accessible API available. For example, my selected platform, TikTok, did not have an open API so I could not collect data directly from the TikTok platform. Other social media platforms, such as X, charge money to access APIs, so it is important to understand how realistic the API approach is for collecting data. If an API is not available, data can be entered manually, but this approach is slow, inconsistent, and usually creates a small sample size. Another option is to use an existing database that already has metadata from the platform because this makes data more consistent and easier to access. Lastly, sentiment analysis tools such as VADER can help keep analysis consistent, but they also have limitations because they do not understand context like humans do.

**Tara -**  
People should know that sentiments on social media can be very difficult to interpret accurately. I learned from Reddit posts that online discussions about AI often include exaggeration, humor, or emotion, which can confuse data analysis tools. It is also important to understand that social media does not represent everyone equally. Certain groups of people are more active online than others. For example, Reddit users may have more experience with AI than people on other platforms. Projects like this also require a lot of time spent cleaning and organizing data while thinking about bias and ethics.

**Zohra -**  
People should know that AI culture changes very quickly, so data about it can become outdated fast. News articles and social media posts also do not always represent reality because they often focus on dramatic topics like cheating or academic dishonesty. This can make AI seem more negative than it really is. People should also know that categories like “positive,” “negative,” or “neutral” can be difficult to decide because everyone may interpret articles differently. It is important to look at the context behind the data and understand that people’s opinions about AI are shaped by their own experiences and emotions.

**Haneen -**

People should know that scholarly sources and educational discussions are not completely neutral representations of AI. Academic publications often focus on specific concerns such as academic integrity, cheating, ethics, or policy, which can shape how AI in education is represented overall. It is also important to recognize that educational research changes rapidly because new AI tools and debates emerge constantly.

Another important consideration is that datasets based on scholarly literature may still contain biases. English-language publications and Western educational perspectives are often overrepresented, while perspectives from other educational systems may be less visible. People should also understand that article abstracts do not always fully represent the complexity of the full source, meaning that categorization decisions involve interpretation and simplification.

---

## Principles of Approaches

**Tara -**  
I learned that finding the right dataset is an important part of the process because the quality of the dataset directly affects the quality of the analysis. For my project, I first explored Reddit discussions from students sharing their opinions on ChatGPT and education. Then, I found a larger dataset that matched the themes I wanted to analyze. After cleaning and organizing the data, I used VADER sentiment analysis to calculate a sentiment score between 1 and -1. Positive 1 represented the most positive responses, while -1 represented the most negative. I also learned that while tools like VADER can help identify patterns, they still require human interpretation because online conversations contain context that tools cannot fully understand.

**Zohra -**  
One important principle I learned is that organizing cultural data into categories can help show patterns, but human interpretation is still needed. For my project, I grouped articles by tone, topic, and focus group to make comparisons easier. I also learned that people should always think about bias in both the articles and the dataset itself. Since many news stories focused on cheating, the dataset may show AI in a more negative way. Another principle is that people should explain how they collected and organized their data so others can understand the strengths and limits of the dataset.

**Diana -**  

**Principle 1:** When selecting a dataset, understand where the dataset comes from, who created it, and why it was created.  

**Principle 2:** Understand the limitations of sentiment analysis tools and remember that they cannot fully understand human context or emotion.  

**Principle 3:** Check if the platforms or corporations being analyzed provide open access to information or APIs before beginning data collection.

**Haneen -**

**Principle 1:** Even scholarly and academic datasets require human interpretation. Categories such as “positive,” “negative,” or “main theme” are often subjective and should be documented clearly.

**Principle 2:** Computational organization tools such as Python and CSV workflows can improve consistency and scalability, but they also introduce challenges such as formatting problems, metadata inconsistencies, and data cleaning issues.

**Principle 3:** Educational AI research changes rapidly, so datasets about AI in education can become outdated quickly. Researchers should document when data was collected and recognize that scholarly conversations around AI evolve over time.

**Principle 4:** Researchers should think critically about which voices are represented in educational AI datasets. Academic publishing often reflects institutional, geographic, and language biases that shape the dataset itself.
