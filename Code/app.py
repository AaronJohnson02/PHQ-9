from flask import Flask, render_template, request, redirect, url_for
import csv
from datetime import datetime
import jsonify

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

# @app.route('/formsheet')
# def form_sheet():
#     patients = read_patient_data() 
#     return render_template('formsheet.html', patients=patients)

# # Function to read patient data from CSV
# def read_patient_data():
#     patients = []
#     with open('Code/Data/patient.csv', 'r') as f:
#         reader = csv.reader(f)
#         for row in reader:
#             patients.append(row[1])  # Assuming patient name is in the second column
#     return patients


if __name__ == '__main__':
    app.run(debug=True)
