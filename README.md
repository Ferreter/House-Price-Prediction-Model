# House Price Prediction Model Documentation

## Initial Summary<a name="initial-summary"></a>
This project aims to produce a composite index of house price data to explore housing affordability, with a special focus on whether students will be able to afford a house The topic was chosen due to the persistent housing affordability crisis in Ireland, which has significant effects on individuals and society.

## Project Cleaning Documentation

### Introduction

This document outlines the cleaning process for a dataset in the context of a project. The goal of this cleaning process is to prepare the dataset for further analysis and modeling tasks.

### Initial Setup and Exploration

The cleaning process begins by importing necessary libraries and loading the dataset. The first few rows of the dataset are displayed to confirm its loading and structure, and a summary of the dataset's structure and missing values is obtained.

### Handling Missing Values

Missing values are identified and counted for each column. They are then addressed by either dropping them or filling them with appropriate values.

![image](https://github.com/Ferreter/House-Price-Prediction-Model/assets/31386281/f8688bd1-0258-4421-bd52-3402d3a61781)

### Feature Engineering

New features are derived from existing ones to potentially improve model performance. For instance:
- **House Age**: Calculated as the difference between the current year (assumed as 2023) and the year the house was built. This feature provides insight into the age of the property.
- **Years Since Renovation**: Calculated as the difference between the current year (assumed as 2023) and the year of renovation, if applicable. This feature helps to assess the recency of renovations.
- **Total Square Footage**: Sum of the living area and the lot size, providing a comprehensive measure of the property's size.
- **Price per Square Foot**: Calculated as the ratio of price to square footage of living area. This feature standardizes price relative to the size of the property.
- **Bedroom to Bathroom Ratio**: Ratio of bedrooms to bathrooms, offering insights into the property's layout and functionality.

### Removing Duplicates and Outliers

Duplicate entries are removed to ensure data integrity. Outliers, identified based on the 'price' column, are removed to prevent them from skewing analysis and model performance.


![image](https://github.com/Ferreter/House-Price-Prediction-Model/assets/31386281/d62489be-032e-47ac-9a59-e68aaf8a4f35)

### Removing Columns

Columns deemed unnecessary for analysis are dropped. For example:
- **Waterfront**: Since it may not significantly affect house prices in the dataset.
- **Year Built and Year Renovated**: These are replaced by derived features like 'House Age' and 'Years Since Renovation'.
- **View**: As it may not be a strong predictor of house prices in this context.
- **Square Footage of Lot**: Since 'Total Square Footage' encompasses both living area and lot size.
- **Country**: Assuming it's not relevant for this dataset.

![image](https://github.com/Ferreter/House-Price-Prediction-Model/assets/31386281/fa28abd6-7792-4390-b795-3d1434a63dbe)
![image](https://github.com/Ferreter/House-Price-Prediction-Model/assets/31386281/bb2fa760-37b8-4f9b-ac20-838fbc8f0efb)

## Visualization

### Pairplot:
The pairplot shows pairwise relationships between numerical variables (price, bedrooms, bathrooms, sqft_living, price_per_sqft, condition) in the dataset. Each scatterplot in the pairplot represents the relationship between two variables. The diagonal of the pairplot displays histograms of each variable.
![image](https://github.com/Ferreter/House-Price-Prediction-Model/assets/31386281/cd7f6226-d42b-4b9a-85bc-bb44040da67c)

### Boxplots:
The boxplot for price distribution across different numbers of bedrooms shows the distribution of price for each category of bedrooms. It helps in understanding how the price varies with the number of bedrooms. Similarly, the boxplot for price distribution across different numbers of bathrooms shows the distribution of price for each category of bathrooms.

![image](https://github.com/Ferreter/House-Price-Prediction-Model/assets/31386281/1d340f17-7688-4e16-abe0-ae452e2ae4a4)

![image](https://github.com/Ferreter/House-Price-Prediction-Model/assets/31386281/27b38fd5-3bb0-4185-a895-74a95c193c81)
### Scatter Plots:
The scatter plot of price vs. square footage of living area shows how the price varies with the sqft_living. It helps in understanding the relationship between the size of the living area and the price. The scatter plot of price vs. condition shows how the price varies with the condition of the property. It helps in understanding whether the condition of the property influences its price. The scatter plot of price vs. bedrooms shows how the price varies with the number of bedrooms. It helps in understanding whether the number of bedrooms has an impact on the price.

![image](https://github.com/Ferreter/House-Price-Prediction-Model/assets/31386281/265d3130-96e1-43f7-aead-5efd28a4ffb5)

![image](https://github.com/Ferreter/House-Price-Prediction-Model/assets/31386281/7380b13e-504e-4632-ada0-667db72b880d)

![image](https://github.com/Ferreter/House-Price-Prediction-Model/assets/31386281/abe85d96-4908-4368-bd29-0cc9ccf6f239)


### Histogram:
The histogram of price distribution shows the frequency distribution of price. It helps in understanding the overall distribution of prices in the dataset, including any skewness or outliers.

![image](https://github.com/Ferreter/House-Price-Prediction-Model/assets/31386281/132c855a-f01e-4c42-8a94-7556b6dc26ea)


### Correlation Matrix Heatmap:
The heatmap of the correlation matrix visualizes the correlation coefficients between numerical variables. It helps in understanding the strength and direction of linear relationships between variables. Warmer colors (e.g., red) indicate stronger positive correlations, while cooler colors (e.g., blue) indicate stronger negative correlations.

![image](https://github.com/Ferreter/House-Price-Prediction-Model/assets/31386281/536024d6-d57c-4aca-94f0-311a109bb202)


### City-wise Barplot:
The barplot shows the average price for each city. It helps in comparing the average prices across different cities, providing insights into the variation of prices based on location.

![image](https://github.com/Ferreter/House-Price-Prediction-Model/assets/31386281/0bea3f57-e6d8-4045-9e31-fd84fc75cf67)
