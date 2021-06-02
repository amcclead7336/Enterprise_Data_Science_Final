from flask import Flask, request
# TO generate UI for sending request via browser
from flasgger import Swagger
import pickle5 as pickle
import pandas as pd


# Load model from file - read mode
with open("../LogisticRegression-model/model.pkl", 'rb') as file:

    bca_model = pickle.load(file)

app = Flask(__name__)

# Enable this app for swagger and it will auto generate UI
swagger = Swagger(app)


@app.route('/bca_model_file', methods=['POST'])
def predict_mal_file():
    # BELOW docstring lines are required to support swagger documentation
    """ Endpoint returning Breast Cancer prediction
    ---
    parameters:
        - name: input_file
          in: formData
          type: file
          required: true
    """
    columns = ['radius_mean',
     'perimeter_mean',
     'area_mean',
     'concave points_mean',
     'radius_worst',
     'perimeter_worst',
     'area_worst',
     'concave points_worst']

    # Create a test dataframe to use for prediction - Column name has to be SAME as training set
    df_bca = pd.read_csv(request.files["input_file"])
    df_bca = df_bca[columns]
    print("-------- PD Dataframe for prediction: -------\n", df_bca)

    # Make prediction using the input data
    prediction = bca_model.predict(df_bca)
    if prediction[0] == 1:
        re = "M"

    else:
        re = "B"
    print("Debug: Prediction: ", re)

    # Send the prediction as response - will need to convert number to string
    return re


@app.route('/bca_model_itemized', methods=['POST'])
def predict_mal_itemized():
    # BELOW docstring lines are required to support swagger documentation
    """ Endpoint returning Breast Cancer prediction
    ---
    parameters:
        - name: radius_mean
          in: formData
          type: number
          required: true
        - name: perimeter_mean
          in: formData
          type: number
          required: true
        - name: area_mean
          in: formData
          type: number
          required: true
        - name: concave points_mean
          in: formData
          type: number
          required: true
        - name: radius_worst
          in: formData
          type: number
          required: true
        - name: perimeter_worst
          in: formData
          type: number
          required: true
        - name: area_worst
          in: formData
          type: number
          required: true
        - name: concave points_worst
          in: formData
          type: number
          required: true
    """
    radius_mean = request.form["radius_mean"]
    perimeter_mean = request.form["perimeter_mean"]
    area_mean = request.form["area_mean"]
    concave_points_mean = request.form["concave points_mean"]
    radius_worst = request.form["radius_worst"]
    perimeter_worst = request.form["perimeter_worst"]
    area_worst = request.form["area_worst"]
    concave_points_worst = request.form["concave points_worst"]

    # Create a test dataframe to use for prediction - Column name has to be SAME as training set
    data = {'radius_mean': [radius_mean],
            'perimeter_mean': [perimeter_mean],
            'area_mean': [area_mean],
            'concave points_mean': [concave_points_mean],
            'radius_worst': [radius_worst],
            'perimeter_worst': [perimeter_worst],
            'area_worst': [area_worst],
            'concave points_worst': [concave_points_worst]
            }
    df_bca = pd.DataFrame(data)
    print("-------- PD Dataframe for prediction: -------\n", df_bca)

    # Make prediction using the input data
    prediction = bca_model.predict(df_bca)
    if prediction[0] == 1:
        re = "M"

    else:
        re = "B"
    print("Debug: Prediction: ", re)

    # Send the prediction as response - will need to convert number to string
    return re


if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0', port=5010)
