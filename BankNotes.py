# -*- coding: utf-8 -*-
"""
Created on Fri May 21 16:16:39 2021

@author: Meet Savsani
"""
from pydantic import BaseModel

class BankNote(BaseModel):
    variance: float
    skewness: float
    curtosis: float
    entropy: float