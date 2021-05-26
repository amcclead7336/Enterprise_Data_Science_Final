# -*- coding: utf-8 -*-
"""

@author: Narges
"""

from flask import Flask, request
#TO generate UI for sending request via browser
from flasgger import Swagger 
import pickle
import pandas as pd

# Load the pickled CA Houseprice regression model
model_filename = 'C:\\Users\\nargesBassir\\Desktop\\final project\\deployments\\RandomForestClassifier\\model.pkl'

# Load model from file - read mode
with open(model_filename,'rb') as file:
  model = pickle.load(file)

print(model)
app = Flask(__name__)

#Enable this app for swagger and it will auto generate UI
swagger = Swagger(app)

@app.route('/cahouseprice', methods=['POST'])
def predict_houseprice():
    #BELOW docstring lines are required to support swagger documentation
    """ Endpoint returning CA Houseprice prediction
    ---
    parameters:
        - name: Clump_Thickness
          in: formData
          type: number
          required: true
        - name: Uniformity_Cell_Size
          in: formData
          type: number
          required: true
        - name: Uniformity_Cell_shape
          in: formData
          type: number
          required: true
        - name: Marginal_Adhesion
          in: formData
          type: number
          required: true
        - name: Normal_Nucleoli
          in: formData
          type: number
          required: true        
         
    """

    Clump_Thickness = request.form["Clump_Thickness"]
    Uniformity_Cell_Size= request.form["Uniformity_Cell_Size"]
    Uniformity_Cell_shape= request.form["Uniformity_Cell_shape"]
    Marginal_Adhesion= request.form["Marginal_Adhesion"]
    Normal_Nucleoli=request.form["Normal_Nucleoli"]
    

    # Create a test dataframe to use for prediction - Column name has to be SAME as training set
    data = {'Clump_Thickness': [Clump_Thickness], 'Uniformity_Cell_Size': [Uniformity_Cell_Size],
    'Uniformity_Cell_shape': [Uniformity_Cell_shape],'Marginal_Adhesion': [Marginal_Adhesion],'Normal_Nucleoli': [Normal_Nucleoli]}

    df = pd.DataFrame(data)
    # print("-------- PD Dataframe for prediction: -------\n", df)
    
    # Make prediction using the input data
    prediction = model.predict(df)
    # print("Debug: Prediction: ", prediction[0])

    if prediction[0]==0:
      prediction="B"
      print ("Benign")
    else:
      prediction="M"
      print ("Malignant")

    # Send the prediction as response - will need to convert number to string
    return str(prediction)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5010)
    