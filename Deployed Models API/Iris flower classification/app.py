# Exposing the model via an API
from sklearn.externals import joblib
from flask import Flask, request
import numpy as np
import pandas as pd
from flasgger import Swagger


# Load the model
model = joblib.load('clf.pkl')


# Initiate the Flask App
app = Flask(__name__)
swagger = Swagger(app)


@app.route('/predict')
def predicti_iris():
    # Grab all the input features that is needed for the prediction
    s_length = request.args.get("s_length")
    s_width = request.args.get("s_width")
    p_length = request.args.get("p_length")
    p_width = request.args.get("p_width")

    # Convrt to numpy array and ensure the other of the input features
    prediction = model.predict(
        np.array([[s_length, s_width, p_length, p_width]]))

    return str(prediction)


@app.route('/predict_file', methods=['POST'])
def predict_file():
    input_data = pd.read_csv(request.files.get('input_file'), header=None)
    prediction = model.predict(input_data)
    return str(list(prediction))


if __name__ == '__main__':
    app.run(port=3000)
