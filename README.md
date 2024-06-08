##Insurance Premium Prediction


Overview

This project aims to develop a predictive model to accurately estimate insurance premiums based on individual risk factors and market trends. The model is built using linear regression, a basic yet effective method for capturing relationships between predictors and the target variable (insurance premiums). The project includes data preprocessing, exploratory data analysis, model training, evaluation, and prescriptive insights for optimizing insurance pricing strategies.

Table of Contents

Introduction
Dataset
Data Preprocessing
Exploratory Data Analysis
Modeling
Model Evaluation
Prescriptive Analysis
Conclusion
Installation
Usage
Contributing
License


Introduction

Insurance companies often face challenges in pricing policies accurately, leading to potential losses or customer dissatisfaction. This project leverages linear regression to estimate insurance premiums, improving pricing precision and risk management. The approach focuses on handling complex relationships in the data, ensuring fair and competitive premiums.

Dataset

The dataset used in this project is sourced from Kaggle and includes the following columns:

Numerical: age, bmi, blood pressure, children, claim
Categorical: gender, diabetic, smoker, region
Mixed: Patient ID (identifier)
Data Preprocessing
Missing values in age and region columns were imputed with the mean and mode, respectively.
Categorical variables were encoded using LabelEncoder.
Unnecessary columns (index and PatientID) were dropped.


Exploratory Data Analysis

Key findings from EDA:

Age Distribution: Normal distribution with peaks at 32-35 and 43-46 age groups.
BMI Variation: Right-skewed distribution with a high count around BMI of 30.
Blood Pressure Profile: Majority in the 80-100 range, few in 110-140.
Children Count Impact: Most individuals have 0 children, decreasing counts as the number of children increases.
Diabetic and Smoker Analysis: Significant differences in claims between diabetic/non-diabetic and smoker/non-smoker groups.
Gender and Region Representation: Balanced gender distribution, varied region distribution.
Claims Amount Distribution: Majority of claims between 5000-20000.


Modeling

Linear Regression
Linear regression was chosen for its simplicity and effectiveness in predicting continuous target variables.

Model Training

Data was split into 80% training and 20% testing sets.
Model trained using scikit-learn.


Model Evaluation
Metrics: R-squared and Adjusted R-squared


Performance Comparison:

Linear Regression: R2 Score: 0.7271, Adjusted R2 Score: 0.7216
Lasso Regression: R2 Score: 0.7271, Adjusted R2 Score: 0.7215
Ridge Regression: R2 Score: 0.7263, Adjusted R2 Score: 0.7207
Polynomial Regression: R2 Score: 0.7071, Adjusted R2 Score: 0.6701
Elastic Net Regression: R2 Score: 0.4285, Adjusted R2 Score: 0.4169


Prescriptive Analysis

Marketing Campaigns: Target the South East region with tailored products and benefits.
Specialized Policies: Offer policies for individuals with diabetes, high blood pressure, and smokers.
Promotions: Create promotions for individuals with 0 children and BMI between 20-40.
Wellness Programs: Implement programs to promote preventive care and healthier lifestyles.
Transparency and Personalized Recommendations: Enhance policy transparency and offer personalized coverage recommendations.
Customer Support: Provide efficient claims processing and responsive support.
Continuous Improvement: Analyze feedback to refine product offerings and pricing strategies.


Conclusion

Linear regression effectively estimates insurance premiums, aiding insurance companies in pricing policies accurately and managing risks. This project demonstrates the benefits of predictive modeling in the insurance industry, contributing to improved profitability and customer satisfaction.


Contributing

Contributions are welcome! Please submit a pull request or open an issue for any suggestions or improvements.
