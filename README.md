# Message-spam-predictor
A classifier that can predict whether or not the provided message or SMS is 'SPAM' or 'NOT SPAM'

The dataset was taken from kaggle named 'spam'

Project workflow
-Data cleaning
-EDA
-Text pre-processing
-Model building
-Evaluation
-Improvements
-Website

## Could not deploy the website due to credit/debit card issues as the details are need to create an account on deployment sites like 'Heroku'
In this project, simple technique is used to remove all the stop words in english language along with the punctuation marks from the text message and keep only the important words

nltk package is used modify the words in terms of verb to focus only on the words and not the different versions of the same word.

Vectorization techniques used for feature extraction were 'Bag of words' and 'TF-IDF'

The best algorithm selected was Multinomial Naive Bayes.

The MnB model was tested against various machine learning classifiers----
- Logistic Regression\
- Decision Tree Classifier
- Support vector classifier
- Random forest classifier
- K nearest neighbours classifier
- AdaBoost Classifier

![not spam](https://user-images.githubusercontent.com/93179217/213878469-58c455df-6bf7-4225-9cdb-58134f1777f0.png)



