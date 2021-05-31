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

from preprocessing import *
from modelling import Model
    

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


def main():
    st.title("The Level Of Communication")

    st.markdown("*Please put in __Job Title__ and __Job Description__ to classify the writing skill level you need for the job*")

    prep = Preprocessing()
    validate = Validation()

    job_title = st.text_input("Job Title","software engineer")
    job_description = st.text_input("Job Description","UniSA Centre of Change and Complexity in Learning (C3L) is currently hiring a junior software dev with more than 1 year of experience")

    result = st.button("Result")

    if result:
        job_title = prep.deepClean(job_title)
        #job_description = prep.deepClean(job_description)
        st.write(job_title)
        

main()
