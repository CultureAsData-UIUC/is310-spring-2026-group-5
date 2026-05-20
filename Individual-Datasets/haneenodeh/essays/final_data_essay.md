# AI in K-12 Education as Data

## Introduction

This project examines how scholarly and academic sources discuss artificial intelligence in K-12 education between approximately 2020 and 2026. Initially, I was interested in studying whether AI improved student productivity directly. However, after considering the limitations of accessing student performance data and the ethical concerns surrounding educational data collection, I shifted the focus of the project toward how researchers, educators, and institutions discuss AI in educational settings.

Rather than attempting to measure productivity outcomes themselves, this dataset studies the scholarly conversation surrounding AI in education. The project focuses on themes such as personalized learning, academic integrity, teacher attitudes, student engagement, AI literacy, policy, and ethics. This approach allowed me to create a manageable but meaningful dataset that still reflects broader cultural and educational debates surrounding artificial intelligence.

This project connects to the broader group theme, “AI in Academic, Online, and Social Spaces,” by examining how AI technologies are interpreted and integrated within educational institutions.

---

# Creating the Dataset

The dataset was built using scholarly journal articles, conference papers, academic reports, and educational technology publications related to AI in K-12 education. Sources were collected primarily through Google Scholar, Springer, Wiley, ScienceDirect, ACM, MDPI, and other academic publishing platforms.

Each row in the dataset represents one scholarly source. Instead of downloading an existing dataset directly from Kaggle or another repository, I manually reviewed article abstracts and source descriptions and categorized them using interpretive labels.

The dataset includes categories such as:
- education level
- AI tool type
- main theme
- secondary theme
- overall tone
- benefits discussed
- concerns discussed
- student group
- manual notes

Many of these categories required interpretive decisions. For example, some articles discussed both productivity and ethics equally, making it difficult to identify a single “main theme.” In those situations, I selected the dominant theme and used a secondary theme column to preserve additional complexity.

---

# Computational Methods

Although the dataset relied heavily on manual annotation, computational tools played an important role in organizing and structuring the project. Python was used to:
- generate the CSV dataset,
- standardize dataset formatting,
- append article information,
- convert Excel spreadsheets into CSV format,
- and support reproducible data organization.

Using Python helped bridge the gap between manual interpretive labor and computational data practices. Even though the dataset itself is relatively small, the workflow demonstrates how computational methods can support humanities-oriented dataset creation.

The project also demonstrates how computational systems can introduce challenges. For example, exporting spreadsheet data into CSV format sometimes caused formatting problems and missing information, requiring additional debugging and data cleaning.

---

# Patterns and Observations

Several patterns appeared repeatedly throughout the dataset.

First, many scholarly sources framed AI as both an opportunity and a risk. Articles frequently discussed the benefits of personalized learning, automated support systems, adaptive instruction, and educational productivity. At the same time, many sources raised concerns about academic integrity, overreliance on AI systems, teacher preparedness, and ethical issues.

Second, ChatGPT and generative AI dominated the more recent literature, especially after 2023. Earlier sources focused more heavily on AI literacy, tutoring systems, adaptive learning environments, and automated assessment systems.

Third, teacher attitudes appeared frequently throughout the dataset. Many sources emphasized uncertainty surrounding classroom implementation and highlighted the need for professional development and institutional guidance.

---

# Limitations

This dataset has several important limitations.

Most importantly, the dataset does not directly measure actual student productivity or educational outcomes. Instead, it analyzes how scholarly literature discusses AI in educational settings.

Additionally, most sources were categorized primarily through abstracts and summaries rather than full-text reading. This means some themes or nuances may not be fully represented.

Some article metadata was incomplete or inconsistent across academic databases, particularly conference papers and web-hosted publications. Because of this, some author information and publication details required approximation or simplification.

Finally, the dataset reflects biases within academic publishing itself. English-language publications and Western educational perspectives were heavily represented compared to perspectives from other educational systems.

---

# Ethical Considerations

This project avoided collecting private educational data, student records, surveys, or social media content from minors. Instead, the dataset relies entirely on publicly accessible scholarly and academic publications.

However, ethical concerns still emerged throughout the project. Many articles discussed issues such as:
- algorithmic bias,
- unequal access to AI technologies,
- surveillance concerns,
- educational inequality,
- and the possibility of overdependence on AI systems.

These concerns influenced how I interpreted and categorized the dataset.

The project also reinforced the idea that datasets are never neutral. Even relatively small datasets involve interpretive decisions about what counts, what gets categorized, and what becomes visible through data structures.

---

# Conclusion

This project demonstrates how AI in education can be studied not only as a technical issue, but also as a cultural and interpretive phenomenon. By creating and annotating this dataset manually while also using computational tools for organization and formatting, I was able to explore the relationship between human interpretation and computational structure.

The dataset ultimately reflects broader debates about how educational institutions are adapting to rapidly changing AI technologies. It also highlights how difficult it can be to represent complex educational and cultural phenomena through structured data alone.
