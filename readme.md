# Job Market Analysis for Data Roles in Germany

This repository contains tools for collecting and analyzing job vacancy data in the fields of Data Science, Data Engineering, and Data Analytics on the German labor market as of May 2025. The project is composed of three main components:

## 🗂 Repository Structure

. 
├── data/ # Sample CSV files with job vacancies 
├── userfunctions.py # Helper functions for data processing 
├── parser.ipynb # Vacancy parser using Stepstone.de 
├── analisys.ipynb # Data analysis and visualization 
└── README.md


## 📋 Requirements

- Python 3.9+
- Libraries: `pandas`, `numpy`, `matplotlib`, `seaborn`, `selenium`, `beautifulsoup4`
- ChromeDriver for Selenium

## 🛠 Installation

```bash
git clone https://github.com/yourusername/job-market-analysis-de.git
cd job-market-analysis-de
pip install -r requirements.txt


🧩 Main Components
1. userfunctions.py Key Functions:

    extract_keywords_job(): Classifies vacancies into 6 categories: ["Data scientist", "Data analyst", "Data engineer", ...]

    extract_seniority(): Determines the experience level (Junior, Senior, Lead)

    count_locations(): Analyzes the geographical distribution of vacancies

    extract_location_remote(): Identifies remote vacancies

2. parser.ipynb Parser Features:

    Extraction of key data fields

    Export to CSV with UTF-8 encoding

3. analisys.ipynb Key Analyses:

    Salary Distribution:

        Boxplot with outlier handling (5th-95th percentiles)

        Histograms with KDE density estimation

    City Analysis:

        Salary comparison by experience level (Violin Plot)

    Geographic analytics:

        Stacked bar chart by city and specialization

        Comparison of average salaries in the top-10 cities

Author: Sergej Kurtasch 
Contact: sergej.kurtasch@gmail.com 
LastUpdated: May 5, 2025