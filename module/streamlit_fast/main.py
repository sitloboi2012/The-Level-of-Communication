from lib2to3.pgen2 import token
from operator import index
from xmlrpc.client import boolean
import streamlit as st 
from abc import ABC, abstractmethod
from typing import Any, Dict, List
from nltk.tokenize import word_tokenize
import nltk

nltk.download("punkt")

st.title("The Level Of Communication")

st.markdown("*Please put in __Job Title__ and __Job Description__ to classify the writing skill level you need for the job*")

job_title = st.text_input("Job Title","software engineer")
job_description = st.text_input("Job Description","UniSA Centre of Change and Complexity in Learning (C3L) is currently hiring a junior software dev with more than 1 year of experience")


def preprocessing(text: str):
    pass

def modelling(job_title: str, job_description: str):
    return None

def visualize_result(result):
    pass

def checkingTitle(job_title: str) -> bool:
    tokenizer = word_tokenize(job_title)
    compulsoryWord = ["junior","graduate","entry","senior","experienced","manager","director","executive","chief","supervisor"]
    for i in tokenizer:
        if i in compulsoryWord:
            job_title = " ".join(tokenizer)
            return job_title
            break
        elif i not in compulsoryWord:
            st.warning("Missing Job Level")
            title = st.radio("Job Level Categories:", ("Junior","Senior","Director"))
            tokenizer.insert(0,title)
            job_title = " ".join(tokenizer)
            return job_title
            break
        else:
            pass

checkingTitle(job_title)