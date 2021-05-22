import streamlit as st 
from abc import ABC, abstractmethod
from typing import Any, Dict, List

st.title("The Level Of Communication")

st.markdown("*Please put in __Job Title__ and __Job Description__ to classify the writing skill level you need for the job*")

job_title = st.text_input("Job Title","junior software engineer")
job_description = st.text_input("Job Description","UniSA Centre of Change and Complexity in Learning (C3L) is currently hiring a junior software dev with more than 1 year of experience")


def preprocessing(text: str):
    pass

def modelling(job_title: str, job_description: str):
    return None

def visualize_result(result):
    pass

def checkingTitle(job_title: str):
    return job_title

def checkingJobDescription(job_description):
    return job_description

