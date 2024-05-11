from flask import Flask, render_template, request, redirect, url_for
import csv
from datetime import datetime
import jsonify

app = Flask(__name__)

@app.route('/get_data/<patient_name>')
def get_data(patient_name):
    data = []

    # Read the score data from the CSV file
    with open('Code/Data/score.csv', 'r') as f:
        reader = csv.reader(f)
        for row in reader:
            if row[0] == patient_name:
                # Convert the date string to a datetime object for better handling
                date_obj = datetime.strptime(row[1], '%Y-%m-%d %H:%M:%S')
                data.append({'date': date_obj.strftime('%Y-%m-%d'), 'score': int(row[2])})

    return jsonify(data)  # Use jsonify function provided by Flask

@app.route('/visualization')
def visualization():
    patients = read_patient_data()  # Read patient data from CSV
    return render_template('visualization.html', patients=patients)  # Pass patients data to the template
    
# Function to check if user exists in the CSV file
def user_exists(username):
    with open('Code/Data/user.csv', 'r') as f:
        reader = csv.reader(f)
        for row in reader:
            if len(row) >= 2 and row[0] == username:
                return True
    return False

@app.route('/')
def index():
    return render_template('register.html')

@app.route('/login', methods=['POST', 'GET'])
def login():
    if request.method == 'POST':
        username = request.form['name']
        password = request.form['password']

        with open('Code/Data/user.csv', 'r') as f:
            reader = csv.reader(f)
            for row in reader:
                if len(row) >= 2 and row[0] == username and row[1] == password:
                    return redirect(url_for('form_sheet'))  # Corrected endpoint name
        
        return "Invalid username or password"
    else:
        # Handle GET request (render the login form)
        return render_template('Login.html')


@app.route('/formsheet')
def form_sheet():
    patients = read_patient_data()  # Read patient data from CSV
    return render_template('formsheet.html', patients=patients)  # Pass patients data to the template

# Function to read patient data from CSV
def read_patient_data():
    patients = []
    with open('Code/Data/patient.csv', 'r') as f:
        reader = csv.reader(f)
        for row in reader:
            patients.append(row[1])  # Assuming patient name is in the second column
    return patients

# This is to allow users to register 
@app.route('/register', methods=['POST'])
def register():
    username = request.form['name']
    password = request.form['password']

    # if user_exists(username):
    #     return "User already exists!"

    with open('Code/Data/user.csv', 'a', newline='') as f:
        writer = csv.writer(f)
        writer.writerow([username, password])
    return redirect(url_for('index'))

@app.route('/logged_in')
def logged_in():
    return "You are logged in!"

@app.route('/patients', methods=['POST'])
def patient_register():
    name = request.form['pname']
    age = request.form['page']
    pid = request.form['pid']

    with open('Code/Data/patient.csv', 'a', newline='') as f:
        writer = csv.writer(f)
        writer.writerow([pid, name, age])
        return redirect(url_for('patients'))

@app.route('/save_score', methods=['POST'])
def save_score():
    if request.method == 'POST':
        # Get the patient name from the form
        patient_name = request.form['patient_name']
        
        # Get the scores for each question from the form
        scores = [int(request.form[f'q{i}']) for i in range(1, 10)]
        
        # Calculate total score
        total_score = sum(scores)
        
        # Get current date and time
        current_date = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        
        # Save the data to score.csv
        print(f"YOLAOAOJAOM")
        with open('Code/Data/score.csv', 'a', newline='') as f:
            writer = csv.writer(f)
            writer.writerow([patient_name, current_date, total_score])
        
        return redirect(url_for('form_sheet'))




@app.route('/patients')
def patients():
    # Logic to fetch and render patients goes here
    return render_template('patients.html')

if __name__ == '__main__':
    app.run(debug=True)
