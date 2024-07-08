import pandas as pd
import numpy as np
from sklearn.naive_bayes import MultinomialNB
from sklearn.feature_extraction.text import CountVectorizer
from flask import Flask, request, render_template
import pickle
app = Flask(__name__)

f1=open('cv.pkl','rb')
cv=pickle.load(f1)
f2=open('rest_model.pkl','rb')
model=pickle.load(f2)
f1.close()
f2.close()

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    text = request.form['Review']
    a_cv=cv.transform([text]).toarray()
    result=model.predict(a_cv)
    if ("not" in text) or ("n't" in text):
        result[0] = abs(result[0] - 1)
    if result[0] == 1:
        return render_template('index.html', prediction_text='The review is Postive')
    else:
        return render_template('index.html', prediction_text='The review is Negative.')




if __name__ == "__main__":
    app.run(debug=True)