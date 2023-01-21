import streamlit as st
import pickle
import string
import nltk
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer

ps = PorterStemmer()

def preprocess_data(text):
    text = text.lower()
    text = nltk.word_tokenize(text)

    li = []
    for i in text:
        if i.isalnum():
            li.append(i)

    text = li[:]  # clonning of list
    li.clear()

    for i in text:
        if i not in stopwords.words('english') and i not in string.punctuation:
            li.append(i)

    text = li[:]
    li.clear()

    for i in text:
        li.append(ps.stem(i))

    return ' '.join(li)

tfidf = pickle.load(open('vectorizer.pkl','rb'))
model = pickle.load(open('model.pkl','rb'))

st.title('Message Classifier')

input_message = st.text_area('Enter the message')

if st.button('Predict'):

    # 1. Preprocess

    transformed_message = preprocess_data(input_message)

    # 2. Vectorize

    vector_input = tfidf.transform([transformed_message])

    # 3. Predict

    result = model.predict(vector_input)[0]

    # 4. Display

    if result == 1:
        st.header('Spam!!')
    else:
        st.header('Not Spam')
