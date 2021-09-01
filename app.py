import numpy as np
from flask import Flask, request, jsonify, render_template
import pickle

app = Flask(__name__) #This is the app name we will be using in the Procfile invoke execution during Heroku deployment & execution
model = pickle.load(open('model.pkl', 'rb')) #Opening the trained model we saved earlier in model.py file.

@app.route('/') #This tells to execute the home() function defined below
def home():
    #This function renders the i/p webpage as per the index.html file
    return render_template('index.html')

@app.route('/predict',methods=['POST']) #This tells to execute the predict() method below and use the POST method that we have defined in index.html for data transfer via API
def predict():
    '''
    For rendering results on HTML GUI
    '''
    int_features = [int(x) for x in request.form.values()] #extracts values from the different fields defined inside the form block in index.html.
    final_features = [np.array(int_features)] #converts these field values into a single array
    prediction = model.predict(final_features) #sends these values to the trained model that we loaded earlier for prediction

    output = round(prediction[0], 2)

    return render_template('index.html', prediction_text='Employee Salary should be $ {}'.format(output))
    #In this line we once again render the webpage, based on index.html, but this time we add the model predictions to the field 'prediction_text' defined in the same index.html


if __name__ == "__main__":
    app.run(host='0.0.0.0',port=8080)
