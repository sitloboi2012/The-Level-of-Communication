from curses import nl
from lib2to3.pgen2 import token
from multiprocessing import Pipe
from operator import index
from matplotlib.pyplot import axis
import sklearn
import streamlit as st
import re
import texthero as hero
import nltk
import numpy as np
import pandas as pd
import joblib

from locale import normalize
from tokenize import String
from unicodedata import normalize as unicode_normalize
from abc import ABC, abstractmethod
from typing import Any, Dict, List
from nltk.tokenize import punkt, word_tokenize
from sklearn.pipeline import Pipeline
from sklearn.feature_extraction.text import CountVectorizer, TfidfTransformer
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC

nltk.download("stopwords")
nltk.download("punkt")

st.title("The Level Of Communication")

st.markdown("*Please put in __Job Title__ and __Job Description__ to classify the writing skill level you need for the job*")

job_title = st.text_input("Job Title","software engineer")
job_description = st.text_input("Job Description","UniSA Centre of Change and Complexity in Learning (C3L) is currently hiring a junior software dev with more than 1 year of experience")

validation = True

tempData = pd.DataFrame({"job_title":job_title, "job_description":job_description}, index=[0])
    
def shallowClean(text: str):
    """
    Performs text normalization using regex patterns
    """
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

def deepClean(text: str):
    cleanText = hero.clean(text)
    return cleanText

def visualize_result(result):
    pass

def checkingTitle(job_title) -> bool:
    """Getting an input as a string -> tokenize out -> checking for the specific word ->
    if yes -> pass on and join together
    if no -> ask user to choose a word -> join together and pass on
    """
    return None
            


def model_JobLevel(transformTitle):
    model = joblib.load("SVC_LevelCategory_Model.pkl")
    
    result = model.predict(transformTitle)

    return result

def model_JobCategories(transformDescription):
    model = joblib.load("SVC_JobIndustry_Model.pkl")

    result = model.predict(transformDescription)

    return result

def modelling(job_title, job_description):
    resultLevel = model_JobLevel(job_title)
    if resultLevel[0] == 0:
        st.write("Director")
    elif resultLevel[0] == 1:
        st.write("Junior")
    elif resultLevel[0] == 2:
        st.write("Manager")
    elif resultLevel[0] == 3:
        st.write("Senior")
    else:
        raise("Not regconize level")
    

    resultCategory = model_JobCategories(job_description)
    if resultCategory[0] == 0:
        st.write("Admin")
    elif resultCategory[0] == 1:
        st.write("Educational")
    elif resultCategory[0] == 2:
        st.write("Finance")
    elif resultCategory[0] == 3:
        st.write("Healthcare")
    elif resultCategory[0] == 4:
        st.write("Information Technology")
    else:
        raise("Not regconize level")

def clean_validate(job_title, job_description):
    job_title = deepClean(job_title)
    job_description = deepClean(job_description)

    job_title = checkingTitle(job_title[0])

    return job_title, job_description

def main():
    if st.button("Result"):
        tempData["job_title"], tempData["job_description"] = clean_validate(tempData["job_title"], tempData["job_description"])

    if validation:
        pass
    else:
        modelling(tempData["job_title"], tempData["job_description"])
    

main()
