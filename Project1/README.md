## Business Understanding
The goal of this project is to use the Boston Airbnb data to answer the following business question: What are the most important features to estimate Airbnb rental price?

## Data Understanding 
The Boston dataset has 3585 rows and 95 columns, containing information about the listings, hosts, reviews, availability, and location.

## Prepare Data
To prepare the data for modeling, I performed the following steps:

### Data cleaning
 I removed outliers, duplicates, and irrelevant columns from the dataset.
### Feature selection
 I picked out the most useful columns to predict the price, such as room type, number of bedrooms, amenities, etc.
### Missing value imputation:
 I filled in the missing values with median or mode based on some other related features2.
### One-hot encoding:
 I converted categorical variables into dummy variables to make them suitable for modeling.
Data Modeling: I used RandomizedSearchCV to find the best parameters for XGBRegressor, a gradient boosting algorithm that can handle complex and nonlinear relationships between features and target variable.

## Evaluate the results: I evaluated the results of the modeling using the following metrics:

### Accuracy: 
I measured how well the model predicted the rental price compared to the actual price. The model achieved an accuracy of 66%, which means it correctly predicted the price for 66% of the listings.
### Feature importance: 
I used correlation analysis to identify the features that had the most influence on the price. The top features were room type, number of bedrooms, cleaning fee, and location.