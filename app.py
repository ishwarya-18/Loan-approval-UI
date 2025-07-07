from flask import Flask, request, jsonify, render_template
import joblib
import pandas as pd
from flask_cors import CORS
import os 

app = Flask(__name__)
CORS(app)

# Load the trained model
model = joblib.load("loan_model.pkl")

@app.route('/')
def home():
    return render_template("index.html")  # Ensure index.html is inside 'templates' folder

@app.route('/predict', methods=['POST'])
def predict():
    data = request.json

    # Same encoding logic from earlier
    gender = 1 if data['Gender'] == 'Male' else 0
    married = 1 if data['Married'] == 'Yes' else 0
    education = 1 if data['Education'] == 'Graduate' else 0
    self_employed = 1 if data['Self_Employed'] == 'Yes' else 0

    dependents = 0
    if data['Dependents'] == '1':
        dependents = 1
    elif data['Dependents'] == '2':
        dependents = 2
    elif data['Dependents'] == '3+':
        dependents = 3

    property_area = {'Rural': 0, 'Semiurban': 1, 'Urban': 2}.get(data['Property_Area'], 0)

    input_data = [[
        gender,
        married,
        dependents,
        education,
        self_employed,
        data['ApplicantIncome'],
        data['CoapplicantIncome'],
        data['LoanAmount'],
        data['Loan_Amount_Term'],
        data['Credit_History'],
        property_area
    ]]

    prediction = model.predict(input_data)[0]
    result = "Approved" if prediction == 1 else "Rejected (Try with better credit history or lower loan)"
    return jsonify({"loan_status": result})

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))  # Use Render's PORT env variable
    app.run(host='0.0.0.0', port=port)