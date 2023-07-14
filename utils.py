import numpy as np
import json
import pickle
import os
import config


class HeartPrediction:
    def __init__(self):
        self.load_raw()

    def load_raw(self):
        with open(config.model, "rb") as file:
            self.model = pickle.load(file)

        with open(config.json, "r") as json_file:
            self.columns = json.load(json_file)

    def predict_result(self, data):
        self.data = data

        user_input = np.zeros([1, self.model.n_features_in_])
        self.model.feature_names = self.columns

        age = self.data["age"]
        gender = self.data["gender"]
        cp = self.data["cp"]
        trestbps = self.data["trestbps"]
        chol = self.data["chol"]
        fbs = self.data["fbs"]
        restecg = self.data["restecg"]
        thalach = self.data["thalach"]
        exang = self.data["exang"]
        oldpeak = self.data["oldpeak"]
        slope = self.data["slope"]
        ca = self.data["ca"]
        thal = self.data["thal"]

        user_input[0, 0] = float(age)
        user_input[0, 1] = float(gender)
        user_input[0, 2] = float(cp)
        user_input[0, 3] = float(trestbps)
        user_input[0, 4] = float(chol)
        user_input[0, 5] = float(fbs)
        user_input[0, 6] = float(restecg)
        user_input[0, 7] = float(thalach)
        user_input[0, 8] = float(exang)
        user_input[0, 9] = float(oldpeak)
        user_input[0, 10] = float(slope)
        user_input[0, 11] = float(ca)
        user_input[0, 12] = float(thal)

        pred = self.model.predict(user_input)[0]

        if pred == 0:
            return "No, You Don't have Heart Disease"
        elif pred == 1:
            return "Yes, You have Heart Disease"
