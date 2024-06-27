import joblib
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
from tkinter import *
from flask import Flask, render_template

app = Flask(__name__)
swords = stopwords.words('english')
ps = PorterStemmer()

def clean_text(sent):
    tokens1 = word_tokenize(sent)
    tokens2 = [token for token in tokens1 if token.isalnum()]
    tokens3 = [token for token in tokens2 if token.lower() not in swords]
    tokens4 = [ps.stem(token) for token in tokens3]
    return tokens4

classifier=joblib.load('classifier.model')
tfidf= joblib.load('preprocessor.model')

@app.route('/')
def student():
    return render_template('spamfinder.html')
@app.route('/spamfinder',methods=['POST','GET'])
def result():
    if request.method =='POST':
        data= dict(request.form)
        message = tfidf.transform([data['message']])
        data['result'] = classifier.predict(message)[0]    
        return render_template('spamoutput.html',data= data)

if __name__ == '__main__':
    app.run(debug = True)
    