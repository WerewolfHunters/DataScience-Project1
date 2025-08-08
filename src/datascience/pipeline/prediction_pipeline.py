import joblib
import os
import pandas as pd
import numpy as np
from pathlib import Path


class ModelPredictionPipeline:
    def __init__(self):
        self.model = joblib.load('artifacts/model_trainer/model.joblib')

    def predict(self, data):
        prediction = self.model.predict(data)

        return prediction