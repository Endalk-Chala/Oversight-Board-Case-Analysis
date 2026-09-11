# Platform Oversight in Practice

Research materials for:

**Chala, Endalkachew H. (2026). “Platform Oversight in Practice: How Language Shapes Procedure, Not Outcome, in Meta’s Oversight Board.” _Journal of Online Trust and Safety_, 3(3).**  
[https://doi.org/10.54501/jots.v3i3.333](https://doi.org/10.54501/jots.v3i3.333)

## Study overview

This project examines how Meta’s Oversight Board distributes institutional attention across languages, regions, policy domains, and procedural pathways. The published study analyzes **147 Oversight Board decisions issued between 2020 and 2025**, coding geographic distribution, linguistic representation, policy domain, adjudicative outcomes, and review procedure.

The central finding is that **language shapes procedure more than outcome**. Adjudicative outcomes do not differ significantly by language or geopolitical classification, but English-language cases are more often resolved through summary reversal, while non-English cases proceed disproportionately to full panel review. The study therefore argues that the legitimacy of platform oversight cannot be evaluated through outcome parity or demographic representation alone; case selection and procedural routing also matter.

## Research questions

The published analysis asks how institutional oversight is structured across:

- geographic and linguistic representation;
- content-policy domains;
- adjudicative outcomes;
- summary versus full-panel review pathways; and
- Global North / Global South case distribution.

## Data and workflow

The repository contains the working data and collection/cleaning scripts used to build the case-level dataset from publicly available Oversight Board decisions.

```text
Oversight-Board-Case-Analysis/
├── README.md
├── CITATION.cff
├── LICENSE
└── data/
    ├── scrape_oversight_board.py
    ├── fetch_details.py
    ├── clean_analysis_ready.py
    ├── decisions_enriched.csv
    └── decisions_cleaned .csv
```

### Collection and preparation

The workflow:

1. collects publicly available Oversight Board decisions;
2. extracts decision metadata and full text;
3. enriches cases with variables used in the analysis;
4. cleans and standardizes the case-level dataset; and
5. supports the quantitative analysis reported in the published article.

## Scope and interpretation

The dataset represents the subset of disputes that entered the Oversight Board’s formal review process. It should therefore be interpreted as a record of **institutional attention and procedural filtering**, not as a representative sample of all content-moderation disputes on Meta platforms.

## Published article

**Platform Oversight in Practice: How Language Shapes Procedure, Not Outcome, in Meta’s Oversight Board**  
_Journal of Online Trust and Safety_, Vol. 3, No. 3 (2026)  
Published September 8, 2026  
DOI: [10.54501/jots.v3i3.333](https://doi.org/10.54501/jots.v3i3.333)

## Citation

Please cite the published article when using findings from this project. Citation metadata for the repository is also provided in [`CITATION.cff`](CITATION.cff).

## Author

**Endalkachew H. Chala**  
[ORCID](https://orcid.org/0000-0001-6210-6706) · [Academic website](https://endalk-chala.github.io/) · [GitHub](https://github.com/Endalk-Chala)

## License

See [`LICENSE`](LICENSE) for the repository license. Users should also respect any terms governing material originally published by the Meta Oversight Board.
