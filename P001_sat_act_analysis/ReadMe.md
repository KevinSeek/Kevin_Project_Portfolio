### Name of Project

Trend in SAT & ACT in year 2017 - 2018

### Overview and background behind the project
The new format for the SAT was released in March 2016. As an employee of the College Board - the organization that administers the SAT - you are a part of a team that tracks statewide participation and recommends where money is best spent to improve SAT participation rates. Your presentation and report should be geared toward non-technical executives with the College Board and you will use the provided data and outside research to make recommendations about how the College Board might work to increase the participation rate in states of interests - states with less than 80% participation rate.

### Executive summary
SAT & ACT are the 2 standardized test used by many colleges in US as part of their admission decision process. Juniors and seniors in high school usually take these tests to demonstrate their readiness for college level work. Both tests are designed to different way to measure college readiness and predict future academic success.

After a new format of SAT was released, we would like to see how it perform against it's competitor - ACT in term of popularity (measured by participation rate) among high school students as the standardized test for their college admission.

We shall limit the scope of our analysis to states that have SAT participation rate in 2018 that are more than 50%. Other factors may be in play for states which have less 50% participation rate, eg. strong political affiliation to ACT and more data will be necessary which is beyond the scope of this project.

#### Key Observation
- SAT & ACT participation rates in each states are mostly inversely related. An increase in one often mean a decrease in another.
- Negative correlation between participation rate and respective test scores for both SAT & ACT
- Year-on-year participation in both states tends to remain the same. Exception for Illinois & Colorado where there are policy changes.
- Preference for one test over the other maybe geographically driven - coastal states preferring SAT over ACT.

#### Additional observation
- We discover states such as Illinois & Colorado have almost a 90% jump in participation rate in 2018 compared to 2017. This may be due to the new format of SAT and various new initiatives such as SAT 'school day' event and educational investment by state;

- States which do not have specific preferred test (states that have more than 50% participation rate in both SAT & ACT) also see a marginal increase in SAT participation rate in 2018.

Based on analysis of the data & additional research, I choose Florida as the next state we can invest in. The reason for choosing the state are as follow:

1. Florida is the 3rd largest state in term of population which means that there are likely to have more students participating in college admission test.

2. As an investment risk mitigation option, we may not be able to replicate the success case of Illinois & Colorado, low SAT to high SAT participation rate. Using Florida, which already have close to 50% participation rate in both SAT and ACT, it is likely to have less 'barrier to entry' for students to switch from ACT to SAT since they may be familiar with the structure of both exam.

3. Florida is committed to make big investment into education, hence it is highly likely to win political favor in expanding into Florida, given that our part of our current initiatives (free online review/classes) can contribute to more students being admitted to college.<a herf="https://www.politifact.com/factchecks/2017/may/15/richard-corcoran/corcoran-touts-level-education-spending-there/"> Florida make big investment in education</a>

In addition, I believe that we should continue & expand current initiatives to other states which still show weakness in SAT participation rate (>50% but below 75%) based on previous year (2018). This way, we are likely to see improvement in participation rate year-on-year across all states going forward.

### Contents:
- Problem Statement
- Executive Summary
- 2017 Data Import & Cleaning
- 2018 Data Import and Cleaning
- Exploratory Data Analysis
- Data Visualization
- Descriptive and Inferential Statistics
- Outside Research
- Conclusions and Recommendations

### Datasets

#### Main Datasets
- [2017 SAT Scores](./data/sat_2017.csv)
- [2017 ACT Scores](./data/act_2017.csv)
- [2018 SAT Scores](./data/sat_2018.csv)
- [2018 ACT Scores](./data/act_2018_updated.csv)

These data give average SAT and ACT scores by state, as well as participation rates, for the graduating class of 2017 & 2018

#### Sources of datasets
You can see the source for the SAT data [here](https://blog.collegevine.com/here-are-the-average-sat-scores-by-state/), and the source for the ACT data [here](https://blog.prepscholar.com/act-scores-by-state-averages-highs-and-lows). The 2018 data for ACT can be found [here](http://www.act.org/content/dam/act/unsecured/documents/cccr2018/Average-Scores-by-State.pdf)

As SAT website has refreshed the 2018 data to 2019. We are unable to provide the link to the dataset and take the acquired data as accurate.

#### Secondary Datasets
- [Combined_2017](./data/combined_2017.csv)
- [final](./data/final.csv)

The combined_2017 is a compilation of the 2017 SAT Scores & 2017 ACT Score by state. Data are join across columns - keyword = state.

The final dataset is similar to combined_2017 which include 2018 data.

#### Additional Resources
- [Understanding ACT & SAT](https://blog.collegevine.com/here-are-the-average-sat-scores-by-state/)


### Python Libraries used
  * Pandas
  * Numpy
  * Scipy - Stats
  * Matplotlib.pyplot
  * Seaborn

#### Data Dictionary
|Feature|Type|Dataset|Description|
|---|---|---|---|
|state|object|SAT|show state in USA|
|sat_part_rate|float|SAT|Display the SAT participation rate in percentage for each state|
|sat_ebrw|int|SAT|The raw score against a maximum score of 800|
|sat_math|int|SAT|The raw score against a maximum score of 800|
|sat_total|int|SAT|The sum of 'ebrw' & 'math' raw score against a maximum score of 1600|
|state|object|ACT|show state in USA|
|act_part_rate|float|ACT|Display the ACT participation rate in percentage for each state|
|act_eng|float|ACT|Scaled score for english against population; maximum score of 36|
|act_math|float|ACT|scaled score for math against population; maximum score of 36|
|act_reading|float|ACT|scaled score for reading against population; maximum score of 36|
|act_sci|float|ACT|scaled score for science against population; maximum score of 36|
|act_composite|float|ACT|Average of the sum of scaled score against population; maximum score of 36|


### Author & Contributors
Author: Kevin Seek
