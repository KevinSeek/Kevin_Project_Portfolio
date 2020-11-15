# Project 2 - Ames Housing Data and Kaggle Challenge

## Background
----
The Iowa State City Assessor's Office has complied historical data of all real estates brought and sold between 2006 & 2010. This compilation provide a treasure trove of insights for both buyers - how much they should pay for their dream house and to developer - what features they should include to increase the value and sale of their project. The initial compilation comes as a data dump and a team was brought in to simplify the data which resulted in 80 variables and sale prices. There are 20 continuous variables, 14 discrete variables and 46 categorical variables (23 nominal & 23 ordinal).

The Assessor's office is looking into creating a model that can serve both residents & developers:
- For residents - An avenue to make informed choice about their real estate.
- For developers - An estimate of the sale price of their development project and to identify important features they need to include in their designs.

As the model is being used by external parties and people who may not have in-dept knowledge about real estate, one key criterion is that the model need to  be simple to use and able to predict house price as accurately as possible.

## Problem Statement
To create a real estate sale price prediction model that can provide sufficently accurate target sale price, low RMSE value, based on as few variables as possible - around 20-30 variables.

## Executive Summary

The Iowa State City Assessor's Office has complied historical data of all real estate sold and purchased from 2006 to 2010. With this complied data, the Assessor's Office wants to publicise this data and help both Iowa's residents and real estate developers better understand the real estate trend in the state via a real estate sale price prediction model. There are 3 objective that need to be achieved:
1. Allowing residents who may not be expert in real estate to make informed choice about their purchase.
2. Allowing developers to manage their project profit expectation and provide information that can help them design houses which have higher demand.
3. Model need to be simple (contains as few variable as possible) and sufficiently accurate to predict sale price (accuracy based on model's prediction against historical sale price and against newly unseen compiled data after 2010 (kaggle test)

From the intial compilation, there are 80 variables include target variable - saleprice. The 80 variables are a combination of 20 continuous variables, 14 discrete variable and 64 categorical variables (23 nominal & 23 ordinal).

Out of the 80 variables, I have chosen 33 features which have work well against historical saleprice and new unseen saleprice. The acuracy of the model is measured by how close root mean square error (RMSE) is to 0. when RMSE is 0, it means the predicted sale equate to the actual sale price for all observation. As RMSE can only be known when we know the actual sale price, we cannot tell how good our model is against unseen, new saleprice. We need a base model based on the mean saleprice of our dataset to give us a gauage of how well our model can predict saleprice.

### Key Observations
1. There is high collinearity between given variables - some variable are subset/superset of other variable - eg gr_liv_area is a superset of 1st_flr_sf, 2nd_flr_sf, low_qual_fin_sf
2. There are redundant variables - variables which have single element dominating the entire set of observations.
3. Data Errors or data which doesnt make sense eg. there is an input error where the garage_yr_blt was 2207.

### Conclusion, Recommendation & Further Research
- The model provided 33 features which stakeholders can input to predict saleprice. Although the model contains more interaction terms from basement & garage variables, it does contains other variables which do make business sense to both developers & resident when looking for a house - such as total bathroom, kitchen quality, fireplace, living area, etc.
- I conclude that the model is robust in predicting saleprice in Iowa or cities which have similar real estate pattern. It may not work well with cities that have other residential patterns.
- Due to the variables used in the model, it is impossible to draw a strong conclusion which combination of variables can best predict saleprice. Due to the time scope of the project, the selected 33 variables are considered the best based on our evaluation criteria - low Root Mean Square Errors.

- However, it does hint on further research topic to find relationship of certain combination of variables that likely affect saleprice eg. bsmt_qual, bsmt_cond, bsmt_fin_type_1.
- The next step in improvement to the model can be to understand other dropped variables such as neighborhood, saletype, utilities in detail. This way, it can improve the model predictability.

### Contents

#### P2_EDA.ipynb
1. Background
2. Problem Statement
3. Executive Summary
4. Data cleaning & EDA (Chart plots are in P2_EDA Plots.ipynb)
5. Encoding of Variables - mapping & dummy variables
5. Application of changes to Kaggle Test data set

#### P2_Modeling.ipynb
1. 1st Set of Model - Train, fit & predict
2. 1st Set of Model - Evaluation of model
3. Features Engineering
4. 2nd Set of Model - Train, fit & predict
5. 2nd Set of Model - Evaluation of model
6. Application of changes to Kaggle Test data set
7. Submission of predictions to Kaggle

### Source of Data
The source data can be taken from https://www.kaggle.com/c/dsi-us-6-project-2-regression-challenge/data

### Python Libraries used
  * Pandas
  * Numpy
  * Scipy - Stats
  * Matplotlib.pyplot
  * Seaborn
  * From sklearn.linear_model: LinearRegression, Ridge, Lasso, ElasticNet, RidgeCV, LassoCV, ElasticNetCV
  * From sklearn.preprocessing: StandardScaler, PolynomialFeatures
  * From sklearn.model_selection: train_test_split, cross_val_score, GridSearchCV
  * From sklearn.metrics: mean_squared_error, r2_score
  * From sklearn: metrics


#### Data Dictionary
|No.|Feature|Data Type|Category|Description|
|---|---|---|---|---|
|01|ms_subclass|int64|nomial|The building class|
|02|ms_zoning|object|nomial|Identifies the general zoning classification of the sale.|
|03|lot_frontage|float64|continuous|Linear feet of street connected to property|
|04|lot_area|int64|continuous|Lot size in square feet|
|05|street|object|nomial|Type of road access to property|
|06|alley|object|nomial|Type of alley access to property|
|07|lot_shape|object|nomial|General shape of property|
|08|land_contour|object|nomial|Flatness of the property|
|09|utilities|object|nomial|Type of utilities available|
|10|lot_config|object|nomial|Lot configuration|
|11|land_slope|object|nomial|Slope of property|
|12|neighborhood|object|nomial|Physical locations within Ames city limits|
|13|condition_1|object|nomial|Proximity to main road or railroad|
|14|condition_2|object|nomial|Proximity to main road or railroad (if a second is present)|
|15|bldg_type|object|nomial|Type of dwelling|
|16|house_style|object|nomial|Style of dwelling|
|17|overall_qual|int64|ordinal|Overall material and finish quality|
|18|overall_cond|int64|ordinal|Overall condition rating|
|19|year_built|int64|continuous|Original construction date|
|20|year_remod/add|int64|continuous|Remodel date (same as construction date if no remodeling or additions)|
|21|roof_style|object|nomial|Type of roof|
|22|roof_matl|object|nomial|Roof material|
|23|exterior_1st|object|nomial|Exterior covering on house|
|24|exterior_2nd|object|nomial|Exterior covering on house (if more than one material)|
|25|mas_vnr_type|object|nomial|Masonry veneer type|
|26|mas_vnr_area|float64|continuous|Masonry veneer area in square feet|
|27|exter_qual|object|ordinal|Exterior material quality|
|28|exter_cond|object|ordinal|Present condition of the material on the exterior|
|29|foundation|object|nomial|Type of foundation|
|30|bsmt_qual|object|ordinal|Height of the basement|
|31|bsmt_cond|object|ordinal|General condition of the basement|
|32|bsmt_exposure|object|ordinal|Walkout or garden level basement walls|
|33|bsmtfin_type_1|object|ordinal|Quality of basement finished area|
|34|bsmtfin_sf_1|float64|continuous|Type 1 finished square feet|
|35|bsmtfin_type_2|object|ordinal|Quality of second finished area (if present)|
|36|bsmtfin_sf_2|float64|continuous|Type 2 finished square feet|
|37|bsmt_unf_sf|float64|continuous|Unfinished square feet of basement area|
|38|total_bsmt_sf|float64|continuous|Total square feet of basement area|
|39|heating|object|nomial|Type of heating|
|40|heating_qc|object|ordinal|Heating quality and condition|
|41|central_air|object|ordinal|Central air conditioning|
|42|electrical|object|nomial|Electrical System|
|43|1st_flr_sf|int64|continuous|First Floor square feet|
|44|2nd_flr_sf|int64|continuous|Second floor square feet|
|45|low_qual_fin_sf|int64|continuous|Low quality finished square feet (all floors)|
|46|gr_liv_area|int64|continuous|Above grade (ground) living area square feet|
|47|bsmt_full_bath|float64|discrete|Basement full bathrooms|
|48|bsmt_half_bath|float64|discrete|Basement half bathrooms|
|49|full_bath|int64|discrete|Full bathrooms above grade|
|50|half_bath|int64|discrete|Half baths above grade|
|51|bedroom_abvgr|int64|discrete|Number of bedrooms above basement level|
|52|kitchen_abvgr|int64|discrete|Number of kitchens|
|53|kitchen_qual|object|ordinal|Kitchen quality|
|54|totrms_abvgrd|in64|discrete|Total rooms above grade (does not include bathrooms)|
|55|functional|object|ordinal|Home functionality rating|
|56|fireplaces|int64|discrete|Number of fireplaces|
|57|fireplace_qu|object|ordinal|Fireplace quality|
|58|garage_type|object|nomial|Garage location|
|59|garage_yr_blt|int64|continuous|Year garage was built|
|60|garage_finish|object|nomial|Interior finish of the garage|
|61|garage_cars|float64|discrete|Size of garage in car capacity|
|62|garage_area|float64|continuous|Size of garage in square feet|
|63|garage_qual|object|ordinal|Garage quality|
|64|garage_cond|object|ordinal|Garage condition|
|65|paved_drive|object|ordinal|Paved driveway|
|66|wood_deck_sf|int64|continuous|Wood deck area in square feet|
|67|open_porch_sf|int64|continuous|Open porch area in square feet|
|68|enclosed_porch|int64|continuous|Enclosed porch area in square feet|
|69|3ssn_porch|int64|continuous|Three season porch area in square feet|
|70|screen_porch|int64|continuous|Screen porch area in square feet|
|71|pool_area|int64|continuous|Pool area in square feet|
|72|pool_qc|object|ordinal|Pool quality|
|73|fence|object|ordinal|Fence quality|
|74|misc_feature|object|nomial|Miscellaneous feature not covered in other categories|
|75|misc_val|int64|continuous|Dollar Value of miscellaneous feature|
|76|mo_sold|int64|discrete|Month Sold|
|77|yr_sold|int64|continuous|Year Sold|
|78|sale_type|object|nomial|Type of sale|
|---|---|---|---|---|---|
|79|id|int64|id|||
|80|pid|int64|id|||
|81|saleprice|int64|continuous|Target Variable|


### Author & Contributors
Author: Kevin Seek
