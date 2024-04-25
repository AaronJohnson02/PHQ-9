from flask import Flask, render_template, request, redirect, url_for
import csv

app = Flask(__name__)

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
                    return redirect(url_for('form_sheet'))
        
        return "Invalid username or password"
    else:
        # Handle GET request (render the login form)
        return render_template('Login.html')

@app.route('/formsheet')
def form_sheet():
    return render_template('formsheet.html')


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

if __name__ == '__main__':
    app.run(debug=True)
