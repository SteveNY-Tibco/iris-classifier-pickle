# inference.py

import pickle

labels = ["setosa", "versicolor", "virginica"]


class Inference:
    def __init__(self, config):
        self.model = pickle.load(open("/app/artifacts/iris-classifier.pkl", "rb"))

    def evaluate(self, payload):
        measurements = [
            payload["sepal_length"],
            payload["sepal_width"],
            payload["petal_length"],
            payload["petal_width"],
        ]

        label_id = self.model.predict([measurements])[0]
        return labels[label_id]

