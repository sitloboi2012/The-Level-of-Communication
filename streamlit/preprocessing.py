import nltk
import numpy as np
import pandas as pd
#import texthero as hero
import streamlit as st
import re

from nltk.tokenize import punkt, word_tokenize
from sklearn.feature_extraction.text import CountVectorizer, TfidfTransformer
from sklearn.model_selection import train_test_split, KFold
from unicodedata import normalize as unicode_normalize
from sklearn.pipeline import Pipeline


class Preprocessing:
    def __init__(self):
        pass
    
    def shallowClean(self,text):
        text = unicode_normalize("NFC", text)
        text = text.lower()
        text = re.sub("```(.|\n|\r)*?```", "", text)
        text = re.sub(r"\s+", " ", text)
        text = re.sub("[-_:/]", " ", text)

        text = re.sub(r"http\S+", "", text)
        text = re.sub(r"\.+", ".", text)
        text = re.sub("[?!;…]", ".", text)
        text = text.replace("\n", ".")
        return text
    
    def deepClean(self,text):
        nltk.download("stopwords")
        nltk.download("punkt")
        temp_df = pd.Series(text)
        cleanText = hero.clean(temp_df)
        print(cleanText[0])
        cleanText = cleanText[0]
        cleanText = Validation().checkValidTitle(cleanText)
        return str(cleanText)
    
    def split_dataset(self,x,y):
        for train, test in KFold().split(x):
            x_train, x_test = x[train], x[test]
            y_train, y_test = y[train], y[test]

        return x_train, x_test, y_train, y_test

class Validation:
    def __init__(self):
        pass
    
    def fixTitle(self, title):
        st.warning("Job Title is missing level")
        value = st.radio("Please choose one",("Junior","Senior","Executive"))
        if value:
            return value + " " + title
        else:
            pass
    

    def checkValidTitle(self, title):
        title_split = list(title.split(" "))
        compulsoryWord = [
            "graduate",
            "entry",
            "junior",
            "senior",
            "director",
            "executive",
            "manager",
            "chief",
            "supervisor"
        ]

        print(title_split)
        for i in title_split:
            if i in compulsoryWord:
                return title
        else:
            title = Validation().fixTitle(title)
            return title        
                