# Project 3 - Evian (Web APIs & Classification)

## Background
----
Seeking Alpha site is trying to understand the American consumer's interests in investing and to find the latest buzz words to provide more targeted portfolio offers to them. However, they realized that consumers/users to their sites have mixed interested in pure investment-related posts to anything and everything related to personal finance. This makes it hard for them to identify new customer bases of which they can offer their services too. Due to this problem, they have hired ML company to help them to address this issue.  

Upon taking up this project, ML company have assigned me, a junior data analyst, to help Seeking Alpha to solve this problem.


## Problem Statement

- Help-Seeking Alpha to build a classification model that help to classify their users' posts based on the words they use and where possible, help to identify consumer's lifestyle habits eg. Buzz words, the time where users are most active in generating posts related to investment.


- The model must be simple enough for non-technical executives to understand and must have at least an 80% success rate of correctly classifying the posts.  
    - The client, Seeking Alpha, understand that in the eyes of consumers, personal finance and investing are closely related and they accept and tolerate some misclassification errors - posts that are wrongly tagged as either personal finance or investing.

## Executive Summary

Seeking Alpha is looking for a tool/model which can help them to accurately (~80%) identify users, based on their posts, to market to them their financial (investment) products. This marketing campaign is targeted to American netizen only and hence a suitable social news aggregator website, Reddit, is used to gather data. 2 subreddits - Investing and personal finance was chosen to train the model for the following reasons:  

1. Topics are similar; this can be a test to see if the model is robust enough to identify investing posts correctly against the contrasting topic - personal finance


2. Reduced loss - There is a minimum loss to the client if they target their financial products to the wrong groups, personal finance given the similar concerns the users might be facing; they may even convert them as buyers. This may not be the case if the contrasting topic is eg. baking. Users from that groups might complain against them for spam marketing.

**Key Observations**  
- Although selection criteria is that text-based posts where posts are longer than 255 characters are used. There is a sizable number of posts gathered suggesting that there are many users who are concerns about investing and/or personal finance - good business opportunity.


- Users are generally more active from Monday to Thursday, from 9 pm to midnight. This information may help the client to strategize their marketing efforts to ensure maximum reach.


- 2 text-processing techniques are used
    - Counter Vectorizer which simply ranks the importance of words based on the occurrence frequency
    - TF-IDF is a score that tells us which words are important to one document, relative to all other documents. Words that occur often in one document but don't occur in many documents contain more predictive power.


- 2 type of model are chosen:
    - logistic regression classifier
    - Naive Bayes Model are trained & test.  


All four models' performance exceeds the minimum accuracy of 80% agreed with clients. TF-IDF Text processing technique and Naive Bayes Modeling were recommended based on business concerns.


### Contents

#### P3_Web Scraping.ipynb
1. Introduction
2. Libraries Used
3. User Defined Functions
4. Extraction of 1st URL - Investing
5. Extraction of 2nd URL - Personal finance


#### P2_Modeling.ipynb
1.  Scenario
2.  Problem Statement
3.  Executive Summary
4.  Web Scraping
5.  Libraries Used
6.  User Defined Functions
7.  Extraction & Transforming Users' posts
8.  Modeling of Lem text
9.  Baseline Modeling
10. Log Regression Using Count CountVectorizer
11. Log Regression Using TF-IDF
12. Naive Bayes with Count Vectorizer
13. Naive Bayes with TF-IDF
14. Conclusion & Recommendations

### Source of Data
Main Source: https://www.reddit.com/

Investing Sub-reddit:
https://www.reddit.com/r/investing.json

Personal Finance:
https://www.reddit.com/r/personalfinance.json


### Python Libraries used
  * Pandas
  * Numpy
  * Scipy - Stats
  * Matplotlib.pyplot
  * Seaborn
  * from nltk.stem import WordNetLemmatizer, PorterStemmer
  * from nltk.tokenize import RegexpTokenizer
  * from nltk.corpus import stopwords
  * from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer
  * from sklearn.naive_bayes import MultinomialNB
  * from sklearn.metrics import confusion_matrix, roc_auc_score
  * from wordcloud import WordCloud, STOPWORDS

### Author & Contributors
Author: Kevin Seek
