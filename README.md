# 📊 Job Market Trends Analysis & Career Recommendation System

This project explores the dynamic nature of the job market and provides predictive insights using machine learning and natural language processing techniques. It includes advanced modeling, clustering, correlation analysis, and a Retrieval-Augmented Generation (RAG) based assistant for career guidance.

---

##  Project Overview

The job market is continuously evolving due to factors such as technological advancement, demographic changes, economic shifts, and political influences. Understanding these changes is crucial for governments, organizations, academic institutions, and individuals making career decisions.

This project focuses on:
- Analyzing job market growth and decline
- Predicting future employment trends
- Identifying skill gaps and potential mismatches
- Offering career guidance using a custom-built LLM-based assistant (RAG)

---

##  Challenges Addressed

-  Rapid market shifts due to crises (e.g., COVID-19)
-  Incomplete and biased datasets
-  Geographical and demographic variability
-  Uncertainty in emerging technologies
-  Poorly defined new job roles

---

##  Solutions Implemented

- **Diverse data sources**: Including job boards, government surveys, and career websites
- **Dynamic models**: Flexible ML models updated with new labor trends
- **Regional and demographic segmentation**
- **Bias detection and mitigation**
- **Clustering**: Grouping professions by similarity in skillsets, demand, or pay
- **Forecasting**: Future job demand using supervised models

---

##  About the Dataset

The primary dataset used is from the **Current Population Survey (CPS)**, conducted by the **U.S. Bureau of Labor Statistics (BLS)** and the **U.S. Census Bureau**. It provides monthly statistics on employment, wages, occupations, and demographics.

Sources:
- [BLS.gov](https://www.bls.gov/)
- [Data.gov](https://catalog.data.gov/dataset)
- [Kaggle - US Jobs on Monster](https://www.kaggle.com/datasets/PromptCloudHQ/us-jobs-on-monstercom)
- [BLS CPS Tables](https://www.bls.gov/cps/tables.htm)

---

##  RAG-Based Career Assistant

We developed a Retrieval-Augmented Generation (RAG) system that serves as a **career recommendation assistant**. It integrates scraped career path data with an LLM to provide personalized guidance.

###  RAG Pipeline Includes:
1. **Data loading**
2. **Chunking and embedding**
3. **Vector storage (FAISS/Chroma)**
4. **Retriever with dynamic prompts**
5. **Answer generation via LLM**

Capabilities:
- Recommends study paths for target professions
- Matches job seekers with career directions based on background and interests
- Explains required qualifications for specific roles

---

##  Tools & Technologies

- Python (Pandas, NumPy, Scikit-learn, Matplotlib, Seaborn)
- Jupyter Notebook
- Clustering (KMeans, Hierarchical)
- Forecasting models
- RAG architecture (LLM + vector database)
- LangChain, HuggingFace Transformers

---

##  Project Goals

-  Help governments plan economic strategy and retraining programs
-  Enable citizens to make better career decisions
-  Equip institutions to align education with market demand
-  Provide a modular ML pipeline for career-related insights

---

##  Getting Started

This project is computationally heavy and intended to run on systems with sufficient memory and CPU/GPU support.

Clone and open in Jupyter:
```bash
git clone https://github.com/edenTamari/job-market-analysis-data-science-project.git
cd job-market-analysis
jupyter notebook
