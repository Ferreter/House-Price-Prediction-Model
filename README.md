
# House Price Prediction Model Documentation

## Table of Contents
1. [Initial Summary](#initial-summary)
2. [Data Cleaning](#data-cleaning)



### Initial Summary<a name="initial-summary"></a>
This project aims to produce a composite index of house price data to explore housing affordability, with a special focus on whether students will be able to afford a house The topic was chosen due to the persistent housing affordability crisis in Ireland, which has significant effects on individuals and society.

### Data Cleaning<a name="data-cleaning"></a>



The data cleaning process was meticulously documented to evaluate the impact of different cleaning techniques on the size of a dataset, which initially contained 4600 entries. Here’s a concise summary of the findings:

- **Uncleaned Data:** Initially, the dataset had 4600 entries, which served as our baseline for comparison.
  
- **Drop Missing Values:** By removing rows with any missing values, the dataset retained 4600 entries, indicating there were no missing values to begin with. This approach would typically reduce dataset size if missing values were present.

- **Fill Missing Values with Mean:** Filling missing values with the mean of their respective columns also resulted in 4600 entries, maintaining the original dataset size. This method ensures that the statistical integrity of numerical features is preserved without reducing the data quantity.

- **Fill and Cleaned:** The most intensive cleaning involved not only filling missing values but also removing duplicates and outliers based on the 'price' column. This step reduced the dataset to 4360 entries, a decrease of about 5.2%. This approach potentially improves model performance by focusing on more typical, representative data points.

  ![image](https://github.com/Ferreter/House-Price-Prediction-Model/assets/31386281/ea5d7e52-8219-4dcd-afa4-d8e15f0eede7)


#### Key Observations:
- The dataset initially did not have any missing values as indicated by the unchanged count after dropping missing data.
- The substantial cleanup (removing duplicates and outliers) resulted in a moderate reduction in dataset size. This suggests the presence of duplicate records and price values that are extreme outliers, which were effectively trimmed to ensure a more normalized dataset for further analysis.

#### Implications:
- **Data Integrity:** Filling missing values (if any were to exist) with the mean is a strategic choice for maintaining the maximum amount of data, crucial for large datasets or when data acquisition is costly or challenging.
- **Quality vs. Quantity:** Removing duplicates and outliers might reduce the dataset size, but it significantly enhances the quality of the data, which can lead to more accurate and reliable predictive models.

This analysis underscores the importance of tailored data cleaning strategies based on the specific requirements and conditions of the dataset to optimize both the quality and usefulness of the data for subsequent analyses.
