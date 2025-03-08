# LLM-Based Clinical Trial Information Extraction

## Overview

This project aims to improve clinical trial information retrieval using Large Language Models (LLMs). Our goal is to convert unstructured clinical trial descriptions into structured, searchable data, making clinical research more accessible and efficient.

## Course
- Biostatistics 285: Advanced Topics in Recent Developments *(Machine Learning: Healthcare, Economics, and LLM)*
- UCLA Fielding School of Public Health
- Winter Quarter 2025

## Motivation
Clinical trials play a crucial role in medical research and treatment development, yet trial search and recruitment remain time-consuming and inefficient. Manually processing eligibility criteria and trial descriptions is a major bottleneck. By using LLMs and retrieval models, we aim to automate the extraction and structuring of clinical trial information, reducing workload and enhancing search accuracy.

## Related Work  
Our project is inspired by recent advancements in NLP for clinical trials: 
- **[Distilling Large Language Models for Matching Patients to Clinical Trials](https://arxiv.org/abs/2312.09958)** - Investigates LLMs for structured trial matching.
- **[TrialGPT](https://github.com/ncbi-nlp/TrialGPT)**, an NLP framework for extracting clinical trial details. - An NLP model for extracting trial details, which inspired parts of our system.


## Objectives
- **Automate** the extraction of structured trial information using **LLMs.**
- **Enhance retrieval** by combining **keyword-based BM25 ranking with embedding-based MedCPT scoring.**
- **Develop a functional web-based interface** to allow users to query and retrieve trial details efficiently.

## Project Workflow

### System Architecture
1. **User Query:** Inputs a condition (e.g., "Type 2 Diabetes")
2. **Hybrid Retrieval:** BM25 + MedCPT embeddings rank trials based on relevance
3. **Ranking Fusion:** Scores combined for final ranking
4. **Output:** A ranked list of clinical trials with structured details

## **Technologies Used**
| **Component**   | **Technology**  |
|----------------|----------------|
| **Frontend**   | React |
| **Backend**    | Python (FastAPI) |
| **Models**     | GPT-4o and GPT-4o-mini |
| **Data Source** | [ClinicalTrials.gov](https://clinicaltrials.gov/) |

---

## **Datasets Used**
While we use a **synthetic dataset**, the original **TrialGPT framework** utilizes **publicly available clinical trial data**:

- **[ClinicalTrials.gov](https://clinicaltrials.gov/)** – Structured clinical trial eligibility criteria.
- **[SIGIR 2016 Corpus](https://data.csiro.au/collection/csiro:17152)** – A collection of trial-related documents.
- **[TREC Clinical Trials 2021 Corpus](https://www.trec-cds.org/2021.html)** – Benchmark dataset for trial retrieval research.
- **[TREC Clinical Trials 2022 Corpus](https://www.trec-cds.org/2022.html)** – An updated dataset for clinical trial search and ranking.

### **Downloading the Data**
To manually download the trial datasets, run the following commands:

```bash
wget -O dataset/trial_info.json https://ftp.ncbi.nlm.nih.gov/pub/lu/TrialGPT/trial_info.json
wget -O dataset/trec_2021/corpus.json https://ftp.ncbi.nlm.nih.gov/pub/lu/TrialGPT/trec_2021.json
wget -O dataset/trec_2022/corpus.json https://ftp.ncbi.nlm.nih.gov/pub/lu/TrialGPT/trec_2022.json
```



## Example Use Case
- **Input Example**: *"65-yead-old female Asian with Type 2 Diabetes"*
- **System Output**: Returns a **ranked** list of relevant trials, displaying key details such as **conditions, interventions, locations, and eligibility criteria.** 

## Challenges & Limitations
1. RAM Constraints & Technical Issues:
- Our system encountered segmentation faults due to insufficient memory when running on real clinical trial data. Despite testing with a small synthetic dataset, hardware limitations prevented full execution.
  
- **Solution:** We will demonstrate a prototype using synthetic data to illustrate the potential impact of our system.
2. Other Challenges:
- Unstructured text: Used LLM-based keyword extraction for better structuring.
- Noise & inconsistencies in datasets: Implemented data preprocessing and filtering.
- Complex trial criteria: Improved parsing techniques for better trial segmentation.

## Next Steps
- Improve the accuracy and relevance of information retrieval.
- Enhance user interface for optimal usability.
- Comprehensive system performance evaluation and documentation.
- Finalize report and presentation.

## Acknowledgements
Special thanks to Dr. Xiaowu Dai and our Teaching Assistant Xiang Chen for their guidance and support.

## Contact
- Kathy Hoang –[kathyhoang@g.ucla.edu]
- Kate Pohs – [kpohs@g.ucla.edu]
- Joyce Zhou - [joycezzy803@g.ucla.edu]

## Disclaimer
This project is for educational and research purposes only. The information produced on this website is not intended for direct diagnostic use or medical decision-making without review and oversight by a clinical professional. Individuals should not change their health behavior solely on the basis of information produced on this website. 

