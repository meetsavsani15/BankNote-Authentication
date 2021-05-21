# -*- coding: utf-8 -*-
"""
Created on Fri May 21 16:12:11 2021

@author: Meet Savsani
"""
import uvicorn
from fastapi import FastAPI
from BankNotes import BankNote

import pickle

#creating a app object

app = FastAPI()
pickle_in = open("classifier_rf.pkl", "rb")
classifier = pickle.load(pickle_in)

# 3. Index route, open on https://127.0.0.1:8000

@app.get('/')
def index():
    return {'message': 'Hello, World'}

@app.get('/name')
def get_name(name: str):
    return {'Welcome to the world': f'{name}'}


#Making a prediction passed on JSON data and return the predicted bank note with probablity
@app.post('/predict')
def predict_banknotes(data:BankNote):
    data = data.dict()
    variance = data['variance']
    skewness = data['skewness']
    curtosis = data['curtosis']
    entropy = data['entropy']
    
    print(classifier.predict([[variance, skewness, curtosis, entropy]]))
    prediction = classifier.predict([[variance, skewness, curtosis, entropy]])
    
    if (prediction[0] > 0.5):
        prediction = "Fake note"
    else:
        prediction = "It is a bank note"
    return {
        'prediction': prediction
    }
        
        
# 5. Run the app on Uvicorn

if __name__ == '__main__':
    uvicorn.run(app, host = '127.0.0.1', port = 8000)
