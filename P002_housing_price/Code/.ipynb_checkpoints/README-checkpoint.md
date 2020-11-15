# Project 2 - Ames Housing Data and Kaggle Challenge






#### Data Dictionary
|No.|Feature|Original d.Type|New d.Type|Description|Remarks|
|---|---|---|---|---|---|
|1|SalePrice|int64|---|Property's sale price in dollars| Target Variable|
|2|Id|int64|---|Serial Number| Can remove|
|3|PID|int64|---|Serial Number| Can remove|
|4|MS Subclass|int64|Categorical|The building class|---|
|5|MS Zoning| object|Categorical|Identifies the general zoning classification of the sale.|---|
|6|Lot Frontage|float64|---|Linear feet of street connected to property| Missing Data|
|7|Lot Area|int64|---|Lot size in square feet||
|8|Street|object|Categorical|Type of road access to property|---|
|9|Alley|object|Categorical|Type of alley access to property| NA = No Alley Access|
|10|Lot Shape| object|Categorical|General shape of property|---|
|11|Land Contour| object|Categorical|Flatness of the property|---|
|12|Utilities| object|Categorical|Type of utilities available|---|
|13|Lot Config| object|Categorical|Lot configuration|---|
|14|Land Slope| object|Categorical|Slope of property|---|
|15|Neighborhood| object|Categorical|Physical locations within Ames city limits|---|
|16|Condition 1| object|Categorical|Proximity to main road or railroad|---|
|17|Condition 2| object|Categorical|Proximity to main road or railroad (if a second is present)|---|
|18|Bldg Type| object|Categorical|Type of dwelling|---|
|19|House Style| object|Categorical|Style of dwelling|---|
|20|Overall Qual| int64|Categorical|Overall material and finish quality|---|
|21|Overall Cond| int64|Categorical|Overall condition rating|---|
|22|Year Built| int64|---|Original construction date|---|
|23|Year Remod/Add| int64|---|Remodel date (same as construction date if no remodeling or additions)|---|
|24|Roof Style| object|Categorical|Type of roof|---|
|25|Roof Matl| object|Categorical|Roof material|---|
|26|Exterior 1st| object|Categorical|Exterior covering on house|---|
|27|Exterior 2nd| object|Categorical|Exterior covering on house (if more than one material)|---|
|28|Mas Vnr Type| object|Categorical|Masonry veneer type|---|
|29|Mas Vnr Area| object|Categorical|Masonry veneer area in square feet|---|
|30|Exter Qual| object|Categorical|Exterior material quality|---|
|31|Exter Cond| object|Categorical|Present condition of the material on the exterior|---|
|32|Foundation| object|Categorical|Type of foundation|---|
|33|Bsmt Qual| object|Categorical|Height of the basement|---|
|34|Bsmt Cond| object|Categorical|General condition of the basement|---|
|35|Bsmt Exposure| object|Categorical|Walkout or garden level basement walls|---|
|36|BsmtFin Type 1| object|Categorical|Quality of basement finished area|---|
|37|BsmtFin SF 1| float64|---|Type 1 finished square feet|---|
|38|BsmtFin Type 2| object|Categorical|Quality of second finished area (if present)|---|
|39|BsmtFin SF 2| float64|---|Type 2 finished square feet|---|
|40|Bsmt Unf SF| float64|---|Unfinished square feet of basement area|---|
|41|Total Bsmt SF| float64|---|Total square feet of basement area|---|
|42|Heating| object|Categorical|Type of heating|---|
|43|Heating QC| object|Categorical|Heating quality and condition|---|
|44|Central Air| object|Categorical|Central air conditioning|---|
|45|Electrical| object|Categorical|Electrical System|---|
|46|1st Flr SF| int64|---|First Floor square feet|---|
|47|2nd Flr SF| int64|---|Second floor square feet|---|
|48|Low Qual Fin SF| int64|---|Low quality finished square feet (all floors)|---|
|49|Gr Liv Area| int64|---|Above grade (ground) living area square feet|---|
|50|Bsmt Full Bath| float64|---|Basement full bathrooms|---|
|51|Bsmt Half Bath| float64|---|Basement half bathrooms|---|
|52|Full Bath| int64|---|Full bathrooms above grade|---|
|53|Half Bath| int64|---|Half baths above grade|---|
|54|Bedroom AbvGr| int64|---|Number of bedrooms above basement level|---|
|55|Kitchen AbvGr| int64|---|Number of kitchens|---|
|56|Kitchen Qual| object|Categorical|Kitchen quality|---|
|57|TotRms AbvGrd| int64|---|Total rooms above grade (does not include bathrooms)|---|
|58|Functional| object|Categorical|Home functionality rating|---|
|59|Fireplaces| int64|---|Number of fireplaces|---|
|60|Fireplace Qu| object|Categorical|Fireplace quality|---|
|61|Garage Type| object|Categorical|Garage location|---|
|62|Garage Yr Blt| float64|---|Year garage was built|---|
|63|Garage Finish| object|Categorical|Interior finish of the garage|---|
|64|Garage Cars| float64|---|Size of garage in car capacity|---|
|65|Garage Area| float64|---|Size of garage in square feet|---|
|66|Garage Qual| object|Categorical|Garage quality|---|
|67|Garage Cond| object|Categorical|Garage condition|---|
|68|Paved Drive| object|Categorical|Paved driveway|---|
|69|Wood Deck SF| int64|---|Wood deck area in square feet|---|
|70|Open Porch SF| int64|---|Open porch area in square feet|---|
|71|Enclosed Porch| int64|---|Enclosed porch area in square feet|---|
|72|3Ssn Porch| int64|---|Three season porch area in square feet|---|
|73|Screen Porch| int64|---|Screen porch area in square feet|---|
|74|Pool Area| int64|---|Pool area in square feet|---|
|75|Pool QC| object|Categorical|Pool quality|---|
|76|Fence| object|Categorical|Fence quality|---|
|77|Misc Feature| object|Categorical|Miscellaneous feature not covered in other categories|---|
|78|Misc Val| int64|---|$Value of miscellaneous feature|---|
|79|Mo Sold| int64|---|Month Sold|---|
|80|Yr Sold| int64|---|Year Sold|---|
|81|Sale Type| object|Categorical|Type of sale|---|
