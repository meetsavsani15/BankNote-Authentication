# -*- coding: utf-8 -*-
"""
Created on Fri May 21 15:23:30 2021

@author: Meet Savsani
"""


# 1. Library imports
import uvicorn
from fastapi import FastAPI


# 2. Create the app object

app = FastAPI()

# 3. Index route, open automatically on https://127.0.0.1:8000

@app.get('/')
def index():
    return {'message': 'Hello, World'}

# 4. Route with a single parameter, returns the parameter within a message located
        # at https:127.0.0.1:8000/Anynamehere
        
@app.get('/Welcome')
def get_name(name: str):
    return {'Welcome to my world': f'{name}'}

# 5. Run the API with uvicorn on https://127.0.0.1:8000

if __name__ == '__main__':
    uvicorn.run(app, host = '127.0.0.1:8000', port = 8000)