# Analysis of Real Estate Sales Data

 
## 1. Title and Author

<!-- - Analysis of Real Estate Sales Data -->
- Prepared for UMBC Data Science Master Degree Capstone by *Dr Chaojie (Jay) Wang*
- Author : *Office of Policy and Management*
<!-- - Link to the author's GitHub profile
- Link to the author's LinkedIn progile
- Link to your PowerPoint presentation file
- Link to your  YouTube video  -->
    
## 2. Background

The project aims to analyze real estate sales data in Connecticut from 2001 to 2020 to gain insights into the real estate market trends, property types, and sales prices over the years.
Understanding the patterns and trends in real estate sales is essential for various stakeholders, including homebuyers, investors, and policymakers. It can help in making informed decisions regarding property investments, policy adjustments, and market predictions.

#### Research Questions:
1. How has the sales volume of different property types (residential, apartment, commercial, industrial, vacant land) evolved over the years?
2. What is the trend in the average sales price for each property type during this period?
3. Can we identify any seasonal patterns in real estate sales?
4. Is there a correlation between property assessments and actual sales prices?

## 3. Data 

Describe the datasets you are using to answer your research questions.

- Data sources - https://portal.ct.gov/OPM/IGPP/Publications/Real-Estate-Sales-Listing
- Data size - 110.4 MB
- Data shape (997213 of rows and 14 columns)

- Data dictionary


|   Column Name      | Data Type  | Definition                                                                                                                                      | Potential Values                                                                                                                                                             |
|-------------------|------------|--------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Serial Number     | int64      | Unique identifier for each sale.                                                                                                                | [2020348, 20002, 200212, 200243, 200377]                                                                                                                                    |
| List Year         | int64      | The year of the real estate listing (grand list year).                                                                                         | [2020, 2001, 2002, 2003, 2004]                                                                                                                                              |
| Date Recorded     | object     | The date when the sale was recorded.                                                                                                            | [09/13/2021, 10/02/2020, 03/09/2021, 04/13/2021, 07/02/2021]                                                                                                                |
| Town              | object     | The town where the property is located.                                                                                                         | [Ansonia, Ashford, Avon, Berlin, Bethany]                                                                                                                                    |
| Address           | object     | The address of the property.                                                                                                                    | [230 WAKELEE AVE, 390 TURNPIKE RD, 5 CHESTNUT DRIVE, 111 NORTHINGTON DRIVE, 70 FAR HILLS DRIVE]                                                                             |
| Assessed Value    | float64    | The assessed value of the property.                                                                                                             | [150500.0, 253000.0, 130400.0, 619290.0, 862330.0]                                                                                                                           |
| Sale Amount       | float64    | The sales price of the property.                                                                                                                | [325000.0, 430000.0, 179900.0, 890000.0, 1447500.0]                                                                                                                          |
| Sales Ratio       | float64    | A ratio related to the assessed value and sale amount.                                                                                         | [0.463, 0.5883, 0.7248, 0.6958, 0.5957]                                                                                                                                     |
| Property Type     | object     | The type of property (residential, apartment, commercial, industrial, vacant land).                                                            | [Commercial, Residential, Vacant Land, nan, Apartments]                                                                                                                      |
| Residential Type  | object     | Specific type within residential properties (if applicable).                                                                                    | [nan, Single Family, Condo, Two Family, Three Family]                                                                                                                         |
| Non Use Code      | object     | Code related to the use of the property.                                                                                                        | [nan, 08 - Part Interest, 14 - Foreclosure, 25 - Other, 01 - Family]                                                                                                          |
| Assessor Remarks  | object     | Remarks from the assessor (if available).                                                                                                       | [nan, WATERFRONT/COTTAGE ONLY/LAND IS ASSOCIATION OWNED, FORECLOSURE SALE OUT OF BANK, DEFERRED MAINTENANCE, H16095]                                                        |
| OPM Remarks       | object     | Remarks from the Office of Policy and Management (if available).                                                                                 | [nan, GAS STATION, GOOD SALE PER MLS, RENOVATED ONE UNIT PER MLS - SEE PREVIOUS SALE #201127, PER MLS SALE IS FOR LAND - ASSESSMENT INCLUDES BUILDING]                 |
| Location          | object     | Additional location-related information (if available).                                                                                         | [nan, POINT (-73.18197 41.64672), POINT (-72.22025 41.3942), POINT (-72.24486 41.32183), POINT (-72.07229 41.32148)]                                                        |


- Which variable/column will be your target/label in your ML model? - <span style="color:green;">*The "Sale Amount" will be the target/label variable for machine learning models. We may aim to predict this variable based on other features.*</span>
- Which variables/columns may selected as features/predictors for your ML models? -
<span style="color:green;">*Potential predictor variables could include "List Year," "Assessed Value," "Property Type," and other relevant columns that could influence property sales prices.*</span>

<!-- ## 4. Exploratory Data Analysis (EDA)

- Perform data exploration using Jupyter Notebook
- You would focus on the target variable and the selected features and drop all other columns.
- produce summary statistics of key variables
- Create visualizations (I recommend using Plotly)
- Find out if the data require cleansing:
  - missing values?
  - duplicate rows? 
- Find out if the data require splitting, merging, pivoting, etc.
- Find out if you need to bring in other data sources to augment your data.
  - For example, population, socioeconomic data from Census may be helpful.
- For textual data, you will pre-process (normalize, remove stopwords, tokenize) them before you can analyze them in predictive analysis/machine learning.
- Make sure the resulting dataset need to be "tidy":
  - each row represent one observation (ideally one unique entity/subject).
  - each columm represents one unique property of that entity. 

## 5. Model Training 

- What models you will be using for predictive analytics?
- How will you train the models?
  - Train vs test split (80/20, 70/30, etc.)
  - Python packages to be used (scikit-learn, NLTK, spaCy, etc.)
  - The development environments (your laptop, Google CoLab, GitHub CodeSpaces, etc.)
- How will you measure and compare the performance of the models?

## 6. Application of the Trained Models

Develop a web app for people to interact with your trained models. Potential tools for web app development:

- Streamlit (recommended)
- Dash
- Flask

## 7. Conclusion

- Summarize your work and its potetial application
- Point out the limitations of your work
- Lessons learned 
- Talk about future research direction -->

## 8. References 

- Real Estate Sales 2001-2020 GL | Connecticut Data. (2022, October 20). https://data.ct.gov/Housing-and-Development/Real-Estate-Sales-2001-2020-GL/5mzw-sjtu

<!-- List articles, blogs, and websites that you have referenced or used in your project. -->