# House Price Prediction Model Documentation

# Table of Contents

1. [Initial Summary](#initial-summary)
2. [Theoretical Analysis of the Data Cleaning Process](#theoretical-analysis-of-the-data-cleaning-process)
   - [Understanding Date Transformations and Price Filtering](#date-transformations-and-price-filtering)
   - [Handling Missing Values](#handling-missing-values)
   - [Feature Engineering](#feature-engineering)
   - [Outliers and Duplicates Removal](#outliers-and-duplicates-removal)
   - [Multicollinearity and Feature Selection](#multicollinearity-and-feature-selection)
3. [Plotting Data](#plotting-data)
   - [Correlation Analysis Visualization](#correlation-analysis-visualization)
   - [Pair Plot for Key Features](#pair-plot-for-key-features)
   - [Box Plot Analysis for Distribution Insights](#box-plot-analysis-for-distribution-insights)
   - [Price Analysis by Specific Features](#price-analysis-by-specific-features)
4. [Multivariate Analysis and Visualization](#multivariate-analysis-and-visualization)
   - [Principal Component Analysis (PCA)](#principal-component-analysis-pca)
   - [Regression Analysis](#regression-analysis)
5. [Normalization and Data Transformation](#normalization-and-data-transformation)
   - [Data Preparation](#data-preparation)
   - [Normalization Techniques](#normalization-techniques)
   - [Outputs and Review](#outputs-and-review)
6. [Modeling Steps](#modeling-steps)
   - [Clustering with K-Means](#clustering-with-k-means)
   - [Regression Analysis with Cluster Labels](#regression-analysis-with-cluster-labels)
   - [Advanced Cluster Analysis by City](#advanced-cluster-analysis-by-city)
7. [Learning Outcomes and Reflections](#learning-outcomes-and-reflections)
   - [Multivariate Analysis and Regression Techniques](#multivariate-analysis-and-regression-techniques)
   - [Clustering](#clustering)
   - [Visualization](#visualization)
   - [Challenges and Lessons Learned](#challenges-and-lessons-learned)
   - [Broader Impacts and Continuous Learning](#broader-impacts-and-continuous-learning)


## Initial Summary<a name="initial-summary"></a>
This project aims to produce a composite index of house price data to explore housing affordability, with a special focus on whether students will be able to afford a house The topic was chosen due to the persistent housing affordability crisis in Ireland, which has significant effects on individuals and society.

# Theoretical Analysis of the Data Cleaning Process

## Understanding Date Transformations and Price Filtering:

- **Date Conversion:** Converting 'date' fields to datetime objects is crucial because it allows for more sophisticated time-series analysis, potentially enabling trend analysis over time, which is vital in real estate market fluctuations.

  

- **Price Filtering:** Removing entries with a price of zero is essential because these are likely to be data entry errors or special cases that do not represent typical market transactions. This step ensures the integrity of the dataset, focusing on genuine sales data.

![image](https://github.com/Ferreter/House-Price-Prediction-Model/assets/31386281/45544106-ab2f-4857-9c60-f31b2febc63e)


## Handling Missing Values:

- **Strategy Choice:** The decision between dropping missing values and filling them can drastically affect the dataset's size and the robustness of subsequent analyses. Dropping missing data simplifies the dataset but at the risk of losing valuable information, especially in smaller datasets. Filling missing values with the mean maintains data integrity but introduces potential biases if the missingness is not random.

- **Feature-Specific Implications:** Filling missing values in features like 'sqft_living' and 'bathrooms' with the mean preserves relationships in the data that are crucial for understanding property values. However, this approach assumes that the data is missing at random, which might not always be the case.

## Feature Engineering:

- **Creating New Variables:** Derived features such as 'house_age', 'years_since_renovation', and 'price_per_sqft' are theoretically significant because they directly relate to a property's appeal and market value. For instance, newer houses or recently renovated properties might attract higher prices.

- **Ratios and Combined Metrics:** Features like 'bed_to_bath_ratio' and 'total_sqft' provide additional dimensions of analysis that capture more nuanced aspects of what might affect property prices, like functionality and living space.

  ![image](https://github.com/Ferreter/House-Price-Prediction-Model/assets/31386281/eff3a842-0e4a-4e31-8753-6cb403475da7)


## Outliers and Duplicates Removal:

- **Outlier Detection:** The use of IQR to identify and remove outliers helps in stabilizing model predictions by eliminating extreme values that could skew results. This is particularly pertinent in real estate, where exceptionally high or low prices might reflect unique properties or erroneous data rather than typical market conditions.

- **Redundancy and Influence on Modeling:** Reducing the influence of outliers and duplicates enhances the model's generalizability and prevents overfitting.

## Multicollinearity and Feature Selection:

- **VIF Analysis:** Assessing multicollinearity through VIF helps in identifying features that do not add unique information. This is crucial in modeling scenarios where independent predictors should ideally influence the outcome variable without interdependencies, which might distort the effect of individual predictors on the response variable.

![image](https://github.com/Ferreter/House-Price-Prediction-Model/assets/31386281/2c8226da-77f2-4622-b72e-d2e9172c4199)


- **Decisions on Feature Dropping:** Dropping features with high VIF, like 'sqft_above' when 'sqft_living' is present, is based on the redundancy that can impair model accuracy and interpretability.

  ![image](https://github.com/Ferreter/House-Price-Prediction-Model/assets/31386281/488dc9c0-2d77-4cb9-bedf-1c5f3e6d8a99)

  ![image](https://github.com/Ferreter/House-Price-Prediction-Model/assets/31386281/211a39e1-0ae6-4898-9c19-1ab1224a05a6)



# Plotting Data

## Correlation Analysis Visualization:

- **Heatmaps:** The use of heatmaps to visualize the correlation matrix is a powerful tool for quickly identifying relationships between variables. It provides insights into which features are closely related, which can influence decisions on feature selection and model complexity in regression or classification tasks.

## Pair Plot for Key Features:

- **Pair Plot:** This plot provides scatter plots and histograms for combinations of selected variables ('sqft_living', 'bedrooms', 'bathrooms', and 'price'). It is used to visually assess the relationships between square footage, number of bedrooms, and bathrooms against price, and to check for linearity, clustering, and distribution shapes. It can guide the type of regression analysis or transformations needed for better model fit.
![image](https://github.com/Ferreter/House-Price-Prediction-Model/assets/31386281/fb2ae079-075a-413a-9a59-5f9200b65c6f)




## Box Plot Analysis for Distribution Insights:

- **Box Plots:** Creating box plots for key variables like 'sqft_living', 'bedrooms', and 'bathrooms' helps in understanding the distribution, detecting outliers, and observing central tendencies and spread. This is crucial in real estate analysis to evaluate property attributes that most influence pricing or market desirability.

![image](https://github.com/Ferreter/House-Price-Prediction-Model/assets/31386281/281a1382-b4e3-4bd5-bed3-cdbc625af75a)




## Price Analysis by Specific Features:

- **Box Plots by Categories:** Examining how categorical features such as 'waterfront' and 'view' influence price via box plots allows for an evaluation of premium factors in property pricing. These plots help in assessing whether features like a waterfront location or a particular view have a significant premium on property prices and are useful in constructing feature interactions for more complex models.


![image](https://github.com/Ferreter/House-Price-Prediction-Model/assets/31386281/f0701f18-bda4-4d7e-a801-9ac7622c0e5a)



# Multivariate Analysis and Visualization

## Principal Component Analysis (PCA):

![image](https://github.com/Ferreter/House-Price-Prediction-Model/assets/31386281/89a5c832-7b9c-4132-97d1-33d39d9337f9)


- **Data Standardization and PCA:** The dataset's numerical columns are standardized, which is crucial for PCA because it is sensitive to variances in data scale. PCA is then applied to reduce dimensionality, aiming to capture most of the variance with fewer components.

- **PCA Output Review:** The first two principal components are extracted, and their contribution to explaining the variance in the dataset is displayed. This is crucial to understand how much information is retained in the reduced dimensions.

![image](https://github.com/Ferreter/House-Price-Prediction-Model/assets/31386281/f5e69173-f2cc-48f4-9c40-44ec01a774a2)


- **PCA Scatter Plot:** A scatter plot of the two principal components helps visualize any inherent clustering or patterns in the data. This can indicate groupings or relationships that are not obvious in the higher-dimensional space.

- **Component Loadings:** The loadings for each principal component are examined to determine which variables most influence each component. This helps interpret the components in terms of the original variables.

## Regression Analysis:

![image](https://github.com/Ferreter/House-Price-Prediction-Model/assets/31386281/37806d26-5e96-4bc3-995b-f26040d3aa35)


- **Model Fitting:** An Ordinary Least Squares (OLS) regression is performed with 'price' as the dependent variable and features like 'sqft_living', 'bathrooms', etc., as independent variables. This model aims to quantify the relationships between house attributes and their prices.

- **Regression Summary:** The output summary provides coefficients, significance levels, and diagnostic statistics such as R-squared and F-statistic. This summary is crucial for understanding which variables significantly impact house prices and how well the model fits the data.

- **Diagnostic Plots:**
  - **Residual Plot:** A plot of the residuals (differences between observed and predicted values) against the predicted values is used to check for non-random patterns that might suggest poor model fit or non-linear relationships.
 
    ![image](https://github.com/Ferreter/House-Price-Prediction-Model/assets/31386281/b19c1886-9d3e-4e82-9c09-4b5a6e62f49c)

  
  - **Q-Q Plot:** This plot compares the quantiles of residuals to a normal distribution. It's essential for checking the assumption of normality in the residuals, which underpins many regression model inferences.
 
    ![image](https://github.com/Ferreter/House-Price-Prediction-Model/assets/31386281/dbcbe815-33e9-4720-96e8-346c57ae9fdf)


# Normalization and Data Transformation

## Data Preparation:

- **Date Handling:** The notebook processes a 'date' column, converting it to a datetime format and extracting the year, month, and day into separate columns. This step is typically useful for time-series analysis or models where trends over time are relevant. The original 'date' column is then dropped, simplifying the dataset.

## Normalization Techniques:

![image](https://github.com/Ferreter/House-Price-Prediction-Model/assets/31386281/427083c2-08a2-4f33-81ba-74990f0da263)


- **Min-Max Scaling:** This technique scales numerical features to a specified range (usually 0 to 1). This is particularly useful for algorithms that assume data is on the same scale, like many machine learning models. The scaled data is then stored in a new DataFrame, ensuring the structure is maintained.

- **Standardization (Z-score Normalization):** This method transforms data to have zero mean and a variance of one. It's effective in handling outliers and is used in situations where data needs to be normalized without being bounded to a specific range.

## Outputs and Review

![image](https://github.com/Ferreter/House-Price-Prediction-Model/assets/31386281/86b0ca17-bc45-43d0-b815-539f652682dc)

![image](https://github.com/Ferreter/House-Price-Prediction-Model/assets/31386281/83f77c6e-8caa-4b01-bc96-18f82627cfdd)



- **Transformed Data Snapshots:** The notebook outputs the first few rows of both the min-max scaled and standardized data, allowing for a quick verification of the transformations. These snapshots are essential for confirming that the scaling has been applied correctly across the dataset.

- **Visualization and Usage:** Although not explicitly shown in the extracted code, these normalization steps typically precede further analysis or modeling. For example, normalized data might be used in clustering algorithms, principal component analysis, or regression models, where scale and distribution could significantly impact performance.

- **Dataframe Reconstitution:** Post-normalization, the data is reconstituted into new DataFrames matching the original structure but with transformed values. This practice is important for maintaining compatibility with downstream analytical processes that might rely on the DataFrame's structure.

## Practical Implications

- **Impact on Analysis:** Normalized data reduces bias that could be introduced by varying scales, especially when combining features like square footage and number of bedrooms, which typically operate on different scales.

- **Compatibility with Machine Learning:** Both scaling techniques ensure the data is appropriately conditioned for machine learning algorithms, which might otherwise perform poorly or converge slowly due to scale discrepancies.

# Modeling Steps

## Clustering with K-Means:

![image](https://github.com/Ferreter/House-Price-Prediction-Model/assets/31386281/7f1e6033-f1f8-45fc-99ab-3e4f683a341c)


- **Feature Selection for Clustering:** Features like 'sqft_living', 'bathrooms', 'bedrooms', and additional attributes such as 'floors', 'view', and 'waterfront' are selected for clustering. This selection suggests an aim to group properties based on their physical characteristics and premium features.

- **Elbow Method for Optimal k:** The elbow method is used to determine the optimal number of clusters. This involves plotting the sum of squared distances within clusters for different values of k and looking for a 'knee' in the curve.


![image](https://github.com/Ferreter/House-Price-Prediction-Model/assets/31386281/513ddce2-8d40-4631-ae3b-0e014bafb5b5)

![image](https://github.com/Ferreter/House-Price-Prediction-Model/assets/31386281/03caca81-6be5-49d5-b746-56249bc2f239)


- **Clustering Execution and Output:** K-Means clustering is performed with an optimal k found (assumed as 3 based on the plot). Cluster assignments are added as a new column in the dataset.

## Regression Analysis with Cluster Labels:

![image](https://github.com/Ferreter/House-Price-Prediction-Model/assets/31386281/0d69619f-4bc0-4efa-8f45-766c10dd05ba)

![image](https://github.com/Ferreter/House-Price-Prediction-Model/assets/31386281/a10c87c2-99ce-4275-8f10-06d41895df55)





- **Incorporating Cluster Labels into Features:** Cluster labels from the K-Means clustering are included as a feature in the regression model, indicating an exploration of how cluster categorization based on property attributes correlates with pricing.

- **Model Training and Evaluation:** A linear regression model is trained using features including cluster labels, and the model's performance is evaluated using the Mean Squared Error (MSE) metric on a test set.

![image](https://github.com/Ferreter/House-Price-Prediction-Model/assets/31386281/024ec4c4-533c-41b3-a3f9-4a8857b0961e)


## Advanced Cluster Analysis by City:

- **City-specific Clustering:** Clustering is applied within each city in the dataset to explore local patterns. This detailed analysis helps understand how property features cluster differently across cities.

- **Visualization of Clusters:** Pair plots are used to visualize the clustering within each city, using hue to differentiate clusters. This visualization helps in understanding the characteristics that define each cluster in different urban contexts.

  ![image](https://github.com/Ferreter/House-Price-Prediction-Model/assets/31386281/652396fe-c56c-4ea0-a031-98bcbf362ae2)


## Outputs and Insights

- **Elbow Plot:** This plot indicated the sum of squared distances for each k, with an assumed elbow at k=3. The choice of k significantly affects clustering outcomes and subsequent analysis, making this a critical step.

- **Cluster Distribution and Centroids:** After assigning cluster labels, the distribution of data points across clusters and the centroids for each cluster are examined. This provides insight into the commonalities within each cluster.

- **Regression Output:** The inclusion of cluster labels as predictors in the regression model and the resulting MSE provides insights into the effectiveness of using clustering as a feature engineering technique.

- **City-specific Analysis:** Detailed cluster analysis for each city could reveal unique local market dynamics, which are crucial for tailored real estate strategies.

# Learning Outcomes and Reflections

## Multivariate Analysis and Regression Techniques

Initially, the project aimed to implement various regression techniques to understand how different variables influence house prices. The process involved setting up a linear regression model to assess relationships within the data, but not without its trials. As a novice in ML, selecting the appropriate variables and correctly setting up the model required several attempts. Missteps in initial analyses included incorrect data cleaning where properties with a price of zero were not removed and some unnecessary features were retained, like 'Country'. Moreover, some newly engineered features proved to be redundant, adding complexity without value. After recognizing these issues, a decision was made to restart the analysis, highlighting a crucial lesson in data science: the importance of meticulous data preparation.

## Clustering

The clustering component introduced the K-Means algorithm to explore how properties grouped based on attributes such as living area square footage and number of bathrooms. This step was instrumental in visualizing and understanding the data's structure beyond surface-level relationships. Clustering helped identify patterns that weren't immediately obvious, though it also highlighted challenges in choosing the number of clusters and interpreting cluster centers meaningfully.

## Visualization

Visualization played a pivotal role in each stage of the project. From using the elbow method to determine the optimal number of clusters to employing pair plots and heatmaps for exploratory data analysis, these techniques were crucial in making informed decisions about the data. Visualization not only facilitated a better understanding of the underlying distributions and relationships but also helped in communicating findings effectively.

## Challenges and Lessons Learned

The project was not without its challenges. The initial approach to data cleaning and feature engineering was flawed, leading to hours of troubleshooting and reworking. Recognizing these errors was disheartening yet educational, emphasizing the iterative nature of ML projects. The documentation style evolved from these experiences, with earlier attempts marked as "old-" to reflect the progression and changes in approach.

The analysis was performed multiple times with varying main variables due to unsatisfactory initial outcomes, such as high mean squared errors and root mean squared errors. This iterative process was crucial in improving the model's accuracy and understanding the impact of different variables on house prices.

## Broader Impacts and Continuous Learning

The dataset itself, sourced from a common repository, initially seemed adequate. However, further exploration revealed its limitations in depth and variability, impacting the potential for achieving high accuracy. This realization underscores the importance of dataset selection in ML projects and the need to critically evaluate data sources for their suitability and completeness.

In conclusion, this first foray into machine learning was rich with learning opportunities, despite the initial setbacks. Each challenge encountered and overcome not only improved the technical understanding of ML techniques but also highlighted the importance of resilience and adaptability in data science. Through this project, the foundational skills in regression analysis, clustering, and visualization were developed, setting the stage for more advanced explorations in the future. The experience has been a testament to the power of learning through doing, particularly in a field as complex and dynamic as machine learning.

Also, for the record a lot of this project wouldnt have been possible without the help of generative AI, it helped in logical thinking aspects. Generating documentation and data visualization.
Also, As i have been listening to a lot of kendrick recently I wanted to share a meme I made (it works better after you listen to the last part of the song as it helps u visualise the beat)

You lied about your models and your test sets, all is perjury

You lied about your algorithms, you lied about your parameters

They all faulty, you lied on 'em, I know they all got bias in 'em

You lied about your data, you lied about your plots, huh

You lied about those other models that's out there hoping that you run

You lied about the only coder that can offer you some help



This is based on his latest song called "meet the grahams" https://genius.com/Kendrick-lamar-meet-the-grahams-lyrics
