import sklearn
import streamlit as st
import re
#import texthero as hero
import nltk
import numpy as np
import pandas as pd
import joblib

from preprocessing import *
from modelling import *
    

def main():
    st.title("The Level Of Communication")

    st.markdown("*Please put in __Job Title__ and __Job Description__ to classify the writing skill level you need for the job*")

    prep = Preprocessing()
    validate = Validation()
    model = Model()

    job_title = st.text_input("Job Title","junior teacher")
    job_description = st.text_input("Job Description","UniSA Centre of Change and Complexity in Learning (C3L) is currently hiring a junior software dev with more than 1 year of experience")

    result = st.button("Result")

    if result:
        job_title = prep.shallowClean(job_title)
        job_description = prep.shallowClean(job_description)

        #transformText = prep.transformer(job_description)
        
        job_predict = model.jobCategory([job_description])
        title_predict = model.jobLevel([job_title])

        model.communicationLevel(title_predict, job_predict)

        

main()
