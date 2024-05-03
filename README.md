
# House Price Prediction Model Documentation

## Table of Contents
1. [Initial Summary](#initial-summary)
2. [Data Cleaning](#data-cleaning)
3. [Variable Removal](#removed-variables)
3. [Retained Removal](#retained-variables)




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



#### Analysis of Correlation Changes
##### Before Removing Outliers
Strong Correlations: Some variables such as 'sqft_living', 'sqft_above', 'bedrooms', and 'bathrooms' showed strong correlations with 'price', indicating that larger and more accommodating properties tend to have higher prices.
Moderate to Weak Correlations: Variables like 'sqft_lot', 'floors', and 'yr_built' displayed weaker correlations with 'price', suggesting these features have less influence on property pricing or are more variable.
##### After Removing Outliers
General Trends: The correlations generally became slightly weaker, particularly for variables directly associated with property size. This can be attributed to the reduction in extreme price values distorting these relationships.
Reduced Impact of Extreme Cases: The relationship between 'price' and 'sqft_above' or 'sqft_living' lessened slightly, indicating a more normalized and uniform dataset where property size is less variably linked to extreme pricing.

![image](https://github.com/Ferreter/House-Price-Prediction-Model/assets/31386281/da23434d-d839-4dec-af2c-1f20f6e20df3)

Also something interesting to look at is the the values of waterfront 


This analysis underscores the importance of tailored data cleaning strategies based on the specific requirements and conditions of the dataset to optimize both the quality and usefulness of the data for subsequent analyses.

#### Feature Engineering and Correlation Changes 

- House Age: Calculated as the difference between the current year and the year the house was built.
- Years Since Renovation: Represents the number of years since the house was last renovated, providing insight into the property's upkeep and modernity.
- Total Square Footage: Sum of the living area and lot size, offering a composite measure of space.
- Price Per Square Foot: A critical indicator of value, derived by dividing the house price by the living area square footage.
- Bed to Bath Ratio: Gives an idea of the layout efficiency, calculated by dividing the number of bedrooms by the number of bathrooms.

![image](https://github.com/Ferreter/House-Price-Prediction-Model/assets/31386281/179b2728-ff7e-4100-91f9-d775ecef7872)


**Then I saved the cleaned dataset into cleaned_data.csv**

### Variable Removal<a name="removed-variables"></a>


The following variables were removed from the dataset for reasons specified below:

- **Waterfront**: This variable was removed due to its very low correlation with the property prices, indicating that it does not significantly influence the price within the context of our dataset.

- **Condition**: The condition of the property showed minimal correlation with price, suggesting it has little impact on pricing in our dataset, which may be due to the homogeneous nature of property conditions or limited variability captured by this variable.

- **Yr_built**: The year a property was built was found to have a low correlation with its price. The age or historical value is not sufficiently differentiated within the dataset to impact the price significantly.

- **Years_since_renovation** and **Yr_renovated**: Both variables related to renovations showed minimal correlation with property prices. This could be due to the infrequency of significant renovations that substantially affect property value or inconsistencies in how renovation data was reported or captured.

- **View**: The variable measuring the quality of the property’s view had a low correlation with price. This suggests that while intuitively a factor, the view does not play a significant role in price determination within this dataset.

- **Sqft_lot**: The size of the property lot showed an insignificant correlation with price, which could be attributed to the variation in value impact of lot size based on location (urban vs. rural).



### Retained Variables<a name="retained-variables"></a>

The following variables were retained in the dataset due to their significant correlations with property prices or their potential to capture critical aspects of the real estate market:

- **Price**: As the target variable, price is central to our analysis and predictions. It represents the property sale value that we aim to predict.

- **Bedrooms**: The number of bedrooms in a property significantly correlates with price, as it directly influences the utility and potential family size that a property can accommodate.

- **Bathrooms**: Similar to bedrooms, the number of bathrooms is a strong indicator of property size and comfort, which are important factors in determining property prices.

- **Sqft_living**: This variable represents the total living area (excluding the basement), and it is one of the strongest predictors of price due to the direct relationship between living space and property value.

- **Sqft_above**: The square footage above ground level, excluding basements, also shows a strong correlation with property prices. Larger above-ground areas typically denote more spacious and desirable properties.

- **Total Sqft**: If present, this indicates the combined square footage of indoor living areas, which helps in a more nuanced understanding of property size and its impact on price.

- **Price per Sqft**: This is an efficiency metric that represents the price per square foot and helps in understanding value distribution throughout the property.

- **Bed_to_bath_ratio**: The ratio of bedrooms to bathrooms can indicate the balance of accommodations in a property, affecting its appeal and marketability.

- **Floors**: The number of floors in a property can affect its desirability, functionality, and, ultimately, its price. Multi-story homes often cater to different buyer preferences compared to single-story homes.

#### Importance of Structural and Size Variables

Variables related to the size and structure of the property, such as **Sqft_living**, **Sqft_above**, and **Total Sqft**, are crucial because they directly impact the utility and the aesthetic appeal of a property, which are significant determinants of its market value.

#### Functional Variables

**Bedrooms**, **Bathrooms**, and **Floors** are functional variables that influence a buyer's decision-making process based on their needs and preferences. These factors are directly related to the lifestyle that a property can offer, making them critical in predicting property prices.

#### Economic Efficiency

**Price per Sqft** offers insights into the economic value of the property relative to its area, providing a standardized measure to compare properties of different sizes and types.

By retaining these variables, our dataset encapsulates the key elements that reflect a property’s market value, ensuring that our model can effectively predict prices based on these fundamental attributes.

##### Importance of the Date Variable

The **Date** variable has been retained as it is crucial for several reasons:

- **Market Trends**: Capturing the date of the property sale allows us to analyze and model fluctuating market trends over time, which are influenced by broader economic conditions.

- **Seasonality**: The real estate market often shows seasonal fluctuations, with certain times of the year being more active than others. Including the date helps us adjust predictions according to these seasonal variations.

- **Long-term Value Changes**: The date helps capture the inflationary trends in the property market, providing insights into how property values increase over time.

Including the date in the analysis ensures that our model can adjust to these factors, providing more accurate and realistic price predictions.

#### Location-Based Variables

In addition to the structural and functional variables mentioned earlier, location-based variables are crucial for providing context and nuance to our property price predictions:

- **Street**: The street address of a property can influence its price due to specific characteristics of the neighborhood, proximity to desirable amenities, and the overall prestige of the area. Street-level data might also help capture micro-market trends that broader regional variables cannot.

- **City**: The city in which a property is located is a major determinant of its price. Different cities have varying market dynamics, economic conditions, and living standards which significantly affect real estate prices.

- **Zip Code**: Often, zip codes are proxies for socio-economic status, school districts, and local amenities, all of which are important factors in real estate valuation. They can also help in segmenting the market for more localized analysis.

#### Importance of Location Variables

**City**, **Street**, and **Zip Code** are included because they encapsulate several indirect factors influencing property values, such as:

- **Economic Activity**: Areas with higher economic activity or better job markets tend to have higher property prices.
- **School Districts**: Properties in better school districts command premium prices.
- **Local Amenities**: Proximity to amenities like parks, restaurants, and public transport can significantly influence property prices.
- **Urban vs. Suburban**: Typically, urban properties have different price determinants compared to suburban properties, with density playing a key role.

#### Geographical Diversity

By analyzing data across different streets, cities, and zip codes, we can better understand how geographical diversity influences property prices and tailor our predictive models to be more accurate at both a macro and micro level.

#### Integrating Location with Other Variables

Combining location-based variables with structural and functional attributes of properties provides a comprehensive dataset that reflects both the inherent qualities of a property and its contextual value based on location. This holistic approach enables more nuanced insights and predictions in our real estate models.

By retaining these variables, our dataset ensures that all critical elements influencing a property’s market value are considered, enhancing the predictability and reliability of our pricing models.

![image](https://github.com/Ferreter/House-Price-Prediction-Model/assets/31386281/7f04b7b8-3321-476f-8ef2-bed39051f313)
