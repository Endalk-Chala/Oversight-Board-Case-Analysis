# Meta Oversight Board Case Selection Analysis

## Introduction

The Meta Oversight Board was conceived as an independent, quasi-judicial body to review and remediate Facebook and Instagram’s content moderation decisions. Since its inception, it has been both lauded for enhancing transparency and criticized for its pace and scope. Journalistic accounts — for example, Casey Newton’s exposé on the Board’s sluggishness in 2023 (Newton, 2023) — and advocacy reports — such as Robera Hamda’s analysis of the Dangerous Individuals and Organizations list’s impact on Oromo users in Ethiopia (Hamda, 2021) — highlight persistent concerns about delays and demographic blind spots. 

Academic critiques further nuance this picture. Evelyn Douek (2024) observes that, despite acquiring institutional legitimacy, the Board often sidesteps the toughest questions and lacks clear metrics to evaluate its substantive impact. Wong & Floridi (2022) map the Board’s strengths in transparency and policy influence alongside weaknesses in jurisdictional limits and diversity. These scholarly insights underscore the need to scrutinize how the Board selects cases for review.

This project interrogates the proportionality and representativeness of the Board’s case selection, both by topic and geographic region, to reveal any systematic discrepancies that may undermine its legitimacy and efficacy.

## Research Questions

1. **Topical Proportionality**  
   - What is the distribution of Oversight Board decisions across content-policy topics (e.g., Hateful Conduct, Dangerous Organizations, Freedom of Expression)?  
   - Are certain topics over- or under-represented relative to the prevalence of reported moderation disputes on those issues?

2. **Geographic Representativeness**  
   - How are cases distributed by the geographic region of the content origin or affected users?  
   - Do certain regions (e.g., Global South vs. Global North) receive disproportionately fewer or slower reviews?

3. **Discrepancy Analysis**  
   - Which topics or regions exhibit the greatest deviation from expected proportionality?  
   - What patterns emerge in the Board’s selection that may reflect institutional, cultural, or operational biases?

4. **Impact on Vulnerable Communities**  
   - How frequently are cases affecting marginalized or at-risk groups (e.g., ethnic minorities, LGBTQIA+ communities, health-related content) selected?  
   - Do these patterns align with the Oversight Board’s mandate to protect freedom of expression and human rights?

## Methodology

1. **Data Collection**  
   - **Scraping Oversight Board Decisions**: Programmatically harvest all publicly available decisions from the Board’s website (`https://www.oversightboard.com/decision/`), including metadata (slug, title, date, topics, categories, outcome) and full decision text.  
   - **Enrichment**: For each decision URL, extract additional fields such as geographic region(s) mentioned and standardized topic classifications from within the decision body.

2. **Data Cleaning & Structuring**  
   - Consolidate multi-row decision texts into single “body” fields.  
   - Normalize metadata columns (e.g., date formats, topic labels, region names).  
   - Handle missing or inconsistent category/outcome entries by cross-referencing with official decision pages.

3. **Quantitative Analysis**  
   - **Descriptive Statistics**: Compute frequency distributions for topics and regions.  
   - **Proportionality Metrics**: Compare observed frequencies to baseline distributions (e.g., volume of user appeals by topic/region where available).  
   - **Discrepancy Indices**: Calculate statistical measures (e.g., chi-square, Gini coefficients) to identify over/under-representation.

4. **Visualization & Interpretation**  
   - Generate bar charts, heatmaps, and geographic maps to illustrate selection patterns.  
   - Contextualize findings with qualitative insights from Board mandates and external critiques.

5. **Reproducibility**  
   - All data-processing and analysis scripts are tracked in this repository.  
   - A `requirements.txt` captures environment dependencies.  
   - Jupyter notebooks accompany each analysis step with narrative explanations.

---

*References*  
- Douek, E. (2024). “The Meta Oversight Board and the Empty Promise of Legitimacy.” *Harvard Journal of Law & Technology*, 37(2).  
- Hamda, R. (2021). “Facebook’s ‘Dangerous Individuals and Organizations’ List Concerns Oromo Users in Ethiopia.” *Global Voices*.  
- Newton, C. (2023). “Meta’s Oversight Board Is Too Slow.” *The Verge*.  
- Wong, D., & Floridi, L. (2022). “Meta’s Oversight Board: A Review and Critical Assessment.” *Philosophy & Technology*.  
