from preprocessing import Preprocessing
from joblib import load
from sklearn.pipeline import Pipeline

class Model:
    def __init__(self):
        pass
    
    def jobCategory(self, transformDescription):
        model = load("SVC_JobIndustry_Model.pkl")

        predict = model.predict(transformDescription)

        return predict
    
    def jobLevel(self, transformTitle):
        model = load("SVC_LevelCategory_Model")

        predict = model.predict(transformTitle)

        return predict