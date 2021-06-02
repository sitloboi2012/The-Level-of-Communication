from preprocessing import Preprocessing
import joblib
from sklearn.pipeline import Pipeline
import streamlit as st

class Model:
    def __init__(self):
        pass
    
    def jobCategory(self, transformDescription):
        model = joblib.load("SVC_JobIndustry_Model.pkl")

        resultCategory = model.predict(transformDescription)

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

        return resultCategory
    
    def jobLevel(self, transformTitle):
        model = joblib.load("SVC_LevelCategory_Model.pkl")

        predict = model.predict(transformTitle)

        if predict[0] == 0:
            st.write("Director")
        elif predict[0] == 1:
            st.write("Junior")
        elif predict[0] == 2:
            st.write("Manager")
        elif [0] == 3:
            st.write("Senior")
        else:
            raise("Not regconize level")

        return predict

    def communicationLevel(self, job_title, job_predict):
        if job_title == 1:
            if job_predict == 0:
                st.write("Good Communication Skill")
                st.write("Assessment Score: 6.5")
            
            elif job_predict == 1:
                st.write("Good Communication Skill")
                st.write("Assessment Score: 6.5")
            
            elif job_predict in [2,3,4]:
                st.write("Normal Communication Skill")
                st.write("Assessment Score: 6.5")
            
            
        
        elif job_title == 3:
            if job_predict == 0:
                st.write("Excellent Communication Skill")
                st.write("Assessment Score: 7.5 - 8.0")

            elif job_predict == 1:
                st.write("Excellent Communication Skill")
                st.write("Assessment Score: 7.0 - 7.5")

            elif job_predict in [2,3,4]:
                st.write("Normal Communication Skill")
                st.write("Assessment Score: 6.5")
            

        elif job_title == 2:
            if job_predict == 0:
                st.write("Exceptional Communication Skill")
                st.write("Assessment Score: 8.0 - 8.5")

            elif job_predict == 1:
                st.write("Excellent Communication Skill")
                st.write("Assessment Score: 7.5 - 8.0")

            elif job_predict in [2,3,4]:
                st.write("Good Communication Skill")
                st.write("Assessment Score: 7.0 - 7.5")
        
        elif job_title == 0:
            if job_predict == 0:
                st.write("Exceptional Communication Skill")
                st.write("Assessment Score: 8.5 - 9.0")

            elif job_predict == 1:
                st.write("Exceptional Communication Skill")
                st.write("Assessment Score: 8.5 - 9.0")

            elif job_predict in [2,3,4]:
                st.write("Excellent Communication Skill")
                st.write("Assessment Score: 8.0")
