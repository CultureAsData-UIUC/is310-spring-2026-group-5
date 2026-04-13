**Diana Ngo’s Critical Computing & Cultural Data**

**Article:** A Labelled Dataset for Sentiment Analysis of Videos on YouTube, TikTok, and Other Sources about the 2024 Outbreak of Measles 

**Authors:** Nirmalya Thakur, Vanessa Su,Mingchen Shao ,Kesha A. Patel,Hongseok Jeong,Victoria Knieling, Andrew Bian

**Publication Venue:** 26th International Conference on Human-Computer Interaction (HCII 2024)

**Date/Year:** June 11, 2024

**URL:** https://huggingface.co/papers/2406.07693

**Link to code repository:** https://dx.doi.org/10.21227/40s8-xf63
**Hugging Face Search Prompt:** “TikTok”


**Part 1: AI Summary**

Claude Sonnet 4.6
Prompt: “Generate a 1–2 paragraph summary of this article.”
Output: 
“This paper presents a labeled dataset of 4,011 videos about the 2024 measles outbreak, collected from 264 websites between January 1 and May 31, 2024. YouTube and TikTok account for the largest shares of the data (48.6% and 15.2%, respectively), with the remainder drawn from Instagram, Facebook, and various news organizations. For each video, the dataset records the URL, title, description, and publication date. The authors then applied three NLP tools — VADER for overall sentiment, TextBlob for subjectivity, and DistilRoBERTa-base for fine-grain emotion classification — to both the titles and descriptions, adding the results as additional attributes to support machine learning research.

The analysis found that neutral sentiment dominated across both video titles (62.78%) and descriptions (40.46%), which the authors attribute largely to the factual, news-driven nature of many sources. Subjectivity analysis similarly showed that the majority of content was "least opinionated." Fine-grain sentiment analysis revealed fear as the most prevalent non-neutral emotion, particularly in video descriptions (26.18%). The paper argues the dataset fills a notable gap in the literature, as no prior work had compiled a video dataset specifically focused on the 2024 measles outbreak with sentiment and subjectivity labeling. The authors also outline a range of open research questions the dataset could support, from misinformation detection to topic modeling and content-based recommendation systems.”


**Part 2: My Critical Assessment**

The cultural data being analyzed is various video content from social media platforms and websites that pertain to the 2024 measles outbreaks with the majority of the content being analyzed is from YouTube and TikTok, 48.6% from YouTube and 15.2% from TikTok. Other platforms included Instagram, Facebook, and other websites from other global and local  news organizations. The dataset contains 4011 in total that were published on 264 websites from January 1, 2024, to May 31, 2024. The data from YouTube was collected through using a YouTube API, while as for the websites, the data was manually collected through using keywords such as “measles” and “MMR vaccine”  on Google to then visit each of the websites that the search query outputted. In the first version of the dataset, for each video post there was an attached URL, title, description, and the date of publication. It is important to note that for Tiktok, Instagram, and other news sources, the title and description columns contain the same text for those videos, rather than being distinct. The data preprocessing of the video titles and video descriptions was performed through Python 3.11.5 on a Microsoft Windows 10 Pro. Additionally, the data preprocessing included the removal of characters not in the alphabet, URLs, hashtags, user mentions, stop words, numbers, and detection of English words by using tokenization and stemming. Edge cases were defined as descriptions that met the search criteria but unrelated to ongoing outbreak of measles. Data that is missing is the reasoning behind why 4011 videos, what news sites were investigated, and consideration if the videos or content were AI-generated. This data captures the cultural phenomenon of how real-life events are interpreted and behaved within online social spaces. The data represent the social space phenomena well as it categorizes the untouched aspects of internet content in how negatively, positively, or neutral the content is through titles and descriptions and also how opinionated these videos are. However, this data doesn’t represent all social spaces holistically as it only focuses on the topic of the 2024 measles outbreak. Overall, the data does capture the complexity of important dimensions in how life events are discussed and behave online depending on the subjectivity of attitudes, text, and even platform. 

The computational methods that are being used are the data collection through YouTube API and the use of VADER for sentiment analysis, TextBlob for subjectivity analysis, and DistilRoBERTa-base for fine-grain sentiment analysis. Conceptually, these methods assist in collecting large amounts of content that focuses on the measles outbreak and defining the text of every video with greater accuracy than manually inputting titles and descriptions. The primary purpose of this form of computation was to be able to collect data about the content about the measles outbreak to gain a better understanding of how opinionated the content is and the overall attitudes that is being produced by these online content. The computation is enriching and analyzing the data collected and their research aims to address the research gaps in how previous datasets failed to attribute positive, negative, or neutral sentiments to the video descriptions and consider subjectivity. Moreover, the computation is analyzing data in order to discover patterns in how online content about measles 2024 outbreaks was framed. These computational goals of addressing the research gaps and discovering online content interpretation of real-world events such as the measles outbreak, shaped the data collection process as the research aimed for quantity in scalability in order to diversify different perspectives across multiple online platforms. The research also heavily incorporated tools such as VADER, TextBlob, and DistilRoBERTa-base in order to account for the research gaps that failed to categorize the subjectivity and attitudes of the online content itself. The result of the data states that “In this paper, the findings of sentiment analysis show that the percentage of  videos with neutral sentiment is higher than the percentage of videos with other sentiments,” where the authors acknowledge there are multiple reasons behind that claim as many the websites where the content was collected were news channels who are likely to display facts rather than opinions about the measles outbreak (Thakur et al. 12). For reference the dataset used the following sources: YouTube, TikTok, Instagram, Facebook, and cbsnews.com, nbcnews.com, msn.com, dailytelegraph.com.au,  apnews.com, cnn.com, and more. I believe the computation was necessary as the dataset needed to be largely scalable in order to obtain the vast amount of intent content that diversifies the perspective on the measles outbreak as a topic. The insights produced from this research would not be possible without the computation as the sample size of content collected would be smaller and therefore less holistic in capturing the true attitudes of content. 


**Part 3: What AI Missed**

Claude AI Sonnet 4.6 was able to recognize the details of the study including the number of videos, websites, research topic, timeframe, and NLP tools used. Additionally, the Claude AI was able to briefly summarize the analysis results, correctly stating that the neutral sentiments were the majority in both videos titles being 62.78% and descriptions being 40.46%. At the end of the generated output Claude addressed the goals of the study of highlighting the 2024 measles outbreak from a sentiment and subjectivity approach and to fill in literature gaps. However, Claude AI missed citation to the news website listed, oversimplying the sites to “various news organizations” (Claude AI Sonnet 4.6). Claude AI also did not provide reasoning towards why the researcher investigated the 2024 measles outbreak specifically, excluding the mention of COVID-19 and the prevalence of social media during the pandemic time that was heavily regarded in the research article. The main tradeoffs made through Claude AI are various sources and details about where the data was collected, the research questions, and the distinct purpose of the research itself. My AI prompt may have limited Claude AI to oversimply and concise the article naturally as I prompted it to generate only 1-2 paragraphs. However, even though there are overgeneralizations and missing details about the study, Claude AI did not make any inaccurate assumptions. I believe that Claude AI was decent at capturing the overall summary of the article and computational methodology, but fails in providing details in crucial sources stated in the article. 

---

**Tara Vittal’s Critical Computing & Cultural Data**

**Article Information**
- **Article:** Exploratory Computation in Digital Humanities: A Qualitative Evaluation Framework  
- **Authors:** Cindy Anh Nguyen, Alejandro Alvarado Rojas  
- **Publication Venue:** *Journal of Open Humanities Data*  
- **Date/Year:** 2026  
- **URL:** https://openhumanitiesdata.metajnl.com/articles/10.5334/johd.500  
- **Link to code repository:** Provided within article supplementary materials  
- **Search Prompt:** “digital humanities computation framework evaluation”  

**Part 1: AI Summary**

**ChatGPT Prompt:** “Generate a 1–2 paragraph summary of this article.”  

**Output:**  
This article introduces a qualitative evaluation framework for exploratory computation in digital humanities. The authors argue that computational methods in cultural research are often used in exploratory ways rather than strictly hypothesis-driven analysis, and therefore require different criteria for evaluation. The framework emphasizes interpretability, transparency, and the iterative relationship between data and method, encouraging researchers to critically reflect on how computational tools shape their findings.  
The paper also highlights how computational processes such as data cleaning, visualization, and pattern detection are not neutral but actively influence the construction of knowledge. By presenting examples from digital humanities projects, the authors demonstrate how exploratory computation can both reveal new insights and risk oversimplifying complex cultural phenomena. The framework aims to guide researchers in assessing when computational approaches are meaningful and when they may obscure important context.  

**Part 2: My Critical Assessment**

The cultural data being analyzed in this article consists broadly of digital humanities datasets such as textual archives, cultural records, and other forms of digitized cultural artifacts. Rather than focusing on a single dataset, the article discusses how researchers interact with cultural data at different stages, including cleaning, structuring, and analyzing it through computational tools. The data typically comes from digitized collections such as historical texts, archives, or online cultural content, and is often large-scale, requiring computational assistance to manage. However, what is missing from this data is the full depth of cultural meaning, context, and interpretation that cannot always be captured through structured or digitized formats. While the data represents cultural phenomena at scale, it risks flattening important nuances such as historical context, ambiguity, and subjective interpretation. As a result, the data captures patterns and trends but may not fully represent the richness and complexity of cultural experiences.  

The computational methods discussed include data processing, visualization, and exploratory analysis techniques commonly used in digital humanities. Conceptually, these methods are used not just to analyze data, but to explore it iteratively, allowing researchers to identify patterns, test ideas, and refine their understanding over time. The primary purpose of computation in this article is both augmentation and analysis, as it helps structure large datasets while also generating insights from them. The authors argue that computation is not neutral and actively shapes the research outcomes, influencing what patterns are visible and how conclusions are formed. These computational goals shape the data by prioritizing what can be measured and visualized, which may exclude less quantifiable aspects of culture. I believe computation is somewhat necessary in this context because the scale of digital humanities data would be difficult to manage manually. However, the same insights about interpretation and cultural meaning could potentially be explored through qualitative methods without heavy reliance on computation. Therefore, while computation adds efficiency and scalability, it also introduces tradeoffs in how cultural data is represented and understood.  

**Part 3: What AI Missed**

ChatGPT was able to recognize the main purpose of the article, including the focus on exploratory computation and the idea that computational methods shape research outcomes. It also correctly identified the importance of interpretability and the risks of oversimplifying cultural data. However, the AI summary oversimplifies the role of computation by presenting it as a general tool rather than emphasizing the iterative and experimental nature highlighted by the authors. It also does not fully address the tension between computational efficiency and the loss of cultural nuance, which is a central argument in the article. Additionally, the AI does not reference specific examples or discuss how the framework applies in practice within digital humanities research.  

Overall, while the AI summary captures the general idea of the article, it misses important nuance about how computation interacts with cultural data and the critical evaluation framework proposed by the authors.  


#### Zohra Hussaini Critical Computing & Cultural Data**

#### Article Information
- **Article:** Student or AI? Automated Detection of AI-generated Student Essays
- **Authors:** Amal Boutadjine, Fouzi Harrag, Khaled Shaalan  
- **Publication Venue:** Procedia Computer Science (7th International Conference on AI in Computational Linguistics)
- **Date/Year:** 2026  
- **URL:** https://www.sciencedirect.com/science/article/pii/S1877050926001134 
- **Search Prompt:** “AI generated essays detection dataset academic integrity ChatGPT”
