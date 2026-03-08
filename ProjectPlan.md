# Project Plan: USD vs Exports

## Overview: 
The goal of this project is to analyze the relationship between the strength of the United States Dollar (USD) and the competitiveness of U.S. exports. We will utilize the Real Trade Weighted U.S. Dollar Index (RTWEXBGS) and Real Exports of Goods and Services (EXPGS) from the Federal Reserve Economic Data (FRED) repository. We aim to analyze how changes in currency value impact the volume of U.S. goods sold internationally. Our hypothesis is that a stronger dollar creates a price disadvantage for U.S. businesses, leading to a decline in exports due to decreased international purchasing power. 

To execute this project, we’ll follow an end-to-end data lifecycle. First, we’ll acquire both datasets using the FRED API. Next, we’ll clean and match the data by using Python Pandas to resample the currency index into quarterly averages because the Dollar Index is reported weekly and the Export data is reported quarterly. We’ll also adjust for seasonal changes and missing observations. Then, we’ll integrate the datasets by performing a merge of the two datasets on their date indexes. Through our approach, we’ll analyze the merged dataset to determine if currency shifts serve as a leading indicator of export trends. Finally, we’ll document our work to ensure full reproducibility through a GitHub repository that includes the interim status report and final report visualized through Markdown. 

## Team:

Member 1: Prajeeta Dahal
Focused on Data Acquisition, Integration, and Workflow Automation. This team member will conduct data sourcing, so will be responsible for setting up the FRED API connection and writing the scripts to pull RTWEXBGS and EXPGS datasets. This team member will also conduct database integration by developing Python to resample the weekly currency index into quarterly averages and merging the data. Next, this team member will conduct automation by creating the automated workflow script to ensure the analysis can be re-run with a single command. This team member will also be in charge of overall Git Management and manage the repository structure and ensure clean merges.

Member 2: Shannon Choi 
Focused on Data Cleaning, Quality Assessment, and Documentation. This member will initially inspect the FRED data to identify missing values, outliers, or inconsistencies. Responsible for writing the documentation and ensuring the project meets the Metadata standards. Leading the drafting of the Interim and Final reports in Markdown, ensuring all visualizations are correctly interpreted.

## Business Question:
"To what degree does a 5% increase in the Real Trade Weighted U.S. Dollar Index correlates with a decline in Real Exports over the following two fiscal quarters, and has this relationship shifted in the post-2020 economy?"
Rationale: This project researches the "Exchange Rate Pass-Through" effect to determine how a stronger U.S. Dollar increases the price of American goods for international buyers. By analyzing a two-quarter lag and comparing pre- and post-2020 data, we will evaluate if modern supply chain shifts have  changed how sensitive U.S. trade is to currency volatility.

## Datasets: 
We selected two primary datasets from Federal Reserve Economic Data (FRED). These datasets are ideal for this project because they provide high-quality and verified macro-economic data.

1. Real Trade Weighted U.S. Dollar Index (RTWEXBGS): Real Trade Weighted U.S. Dollar Index (RTWEXBGS)
* Source: The data is retrieved from FRED (Federal Reserve Economic Data), a premier database maintained by the Federal Reserve Bank of St. Louis. FRED aggregates data from dozens of national and international sources, providing a trustworthy, central repository for high-fidelity economic time-series data used globally by auditors, economists, and researchers. Originally though, the data was produced by the Board of Governors of the Federal Reserve System (US), which is the central bank of the United States, responsible for conducting monetary policy, supervising banking institutions, and maintaining the stability of the financial system.
* Format: Time-series (Weekly)
* Description: This index measures the foreign exchange value of the U.S. Dollar against a weighted average of the currencies of a broad group of major U.S. trading partners. It is "Real" because it is adjusted for inflation, making it the most accurate measure of purchasing power
* Access Method: Programmatic extraction via the FRED API using the fredapi Python library

2. Real Exports of Goods and Services (EXPGS): Real Exports of Goods and Services (EXPGS)
* Source: This dataset is also retrieved from FRED (Federal Reserve Economic Data),  but is originally produced by the U.S. Bureau of Economic Analysis (BEA). The BEA is the primary federal agency responsible for calculating the Gross Domestic Product (GDP) and other National Income and Product Accounts (NIPA), ensuring the data meets rigorous federal standards for statistical accuracy and provenance.
Format: Time-series (Quarterly)
* Description: This represents the total inflation-adjusted value of all goods and services produced in the U.S. and sold to the rest of the world. It is a key component of GDP
* Access Method: Programmatic extraction via the FRED API

## Data Integration: 
The primary challenge in integrating these datasets is the difference in reporting frequency. The Dollar Index is updated weekly, while Export data is updated quarterly. To resolve this, we’ll use a downsampling transformation in Python Pandas. We’ll calculate the mean value of the weekly Dollar Index for each quarter, creating a new "Quarterly Average" series. We’ll create a lagged version of the Export dataset by shifting it by two quarters to test our hypothesis that currency fluctuations have a delayed impact on trade volume.

## Timeline:

| Phase | Task | Description | Deadline | Responsibility |
| :--- | :--- | :--- | :--- | :--- |
| **I. Acquisition** | API Infrastructure | Develop Python script using `fredapi` to pull RTWEXBGS and EXPGS. | March 15 | Member 1 |
| **II. Integration** | Temporal Alignment | Resample weekly Index to quarterly averages and perform inner join. | March 20 | Member 1 |
| **III. Quality** | Data Audit | Conduct formal Quality Assessment (Module 10) for nulls and outliers. | March 25 | Member 2 |
| **IV. Reporting** | Interim Status | Draft 1000–1500 word status report (Milestone 3). | **March 31** | Both |
| **V. Analysis** | Correlation Study | Calculate Pearson r coefficients and visualize the two-quarter lag. | April 15 | Member 1 |
| **VI. Provenance** | Metadata | Create Data Dictionary and JSON metadata (Module 15). | April 25 | Member 2 |
| **VII. Delivery** | Final Release | Final code review and create the `final-project` tag on GitHub. | **May 03** | Both |

## Constraints: 
Despite the high quality of FRED data, our project faces several constraints:
* Temporal Mismatch: The most significant technical challenge is the difference in reporting frequencies. While the Dollar Index is provided weekly, Real Export data is only available quarterly. This requires a downsampling strategy that could smooth out small spikes that could actually have significant short-term business impacts
* Data Latency: Economic indicators like "Real Exports" are subject to time lags in reporting. The most recent data points may be subject to future revisions by the Bureau of Economic Analysis (BEA), which could impact our post-2020 analysis
* Aggregation Bias: Because we are using national-level data, we can’t account for how different industries react to currency shifts. Some sectors may be more resilient due to global demand, but our dataset treats all exports as a single "Real Exports"
* Legal Constraints: While the data is public domain, we must ensure our scripts include proper API Rate Limiting to avoid overwhelming FRED’s servers, which is a key ethical consideration in automated data collection

## Gaps:
We have identified the following gaps where further refinement or external input may be required as the project evolves:
* Confounding Variables: Our current model only looks at the USD strength. However, global exports are also affected by foreign GDP growth, trade tariffs, and shipping costs. We currently have a gap in accounting for these "confounding variables," which might explain drops in exports better than USD strength alone.
* Statistical Methodology: As we move into the analysis phase, we need to determine the most robust way to handle non-stationary time-series data. We may need additional input on whether to use "First-Difference" (calculating the change from the previous quarter) or "Percentage Change" to ensure our correlation results aren't just showing two lines that both happen to trend upward over time.
* Course Content Gap: We currently have a gap in our details for Module 10 and onward topics, but we anticipate to fill in the gaps as we learn. Especially for related the later modules, we need to research tools like r specific Python workflow managers to ensure our end-to-end process is fully automated and reproducible for the final submission.
