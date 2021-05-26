from flask import Flask, request
from flasgger import Swagger
import pickle5 as pickle
import pandas as pd

# load model from PKL file 
model_file = 'model.pkl'

with open(model_file,'rb') as file:
  prediction_model = pickle.load(file)

app = Flask(__name__)

# enable this app for swagger and it will auto generate UI
swagger = Swagger(app)


@app.route('/nn_model_file', methods=['POST'])
def detection_file():
    # BELOW docstring lines are required to support swagger documentation
    """ Endpoint returning Breast Cancer Detection prediction
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

    data_df = pd.read_csv(request.files["input_file"])
    data_df = data_df[columns]
    print('~~~~~~~~~~ DataFrame for Prediction: ~~~~~~~~~~\n\n', data_df)
    print('\n')

    prediction = prediction_model.predict(data_df)
    
    if prediction[0] == 1:
        result = "M"

    else:
        result = "B"
    
    print(f'Prediction: {result}')
    print('\n')
    return result
    #return str(list(result))

if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0', port=5000)
