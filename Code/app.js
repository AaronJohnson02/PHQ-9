const express = require('express');
const bodyParser = require('body-parser');
const sqlite3 = require('sqlite3').verbose();
const cookieSession = require('cookie-session');

const crypto = require('crypto');
const sessionSecret = crypto.randomBytes(64).toString('hex');

const app = express();
const port = 3000;

app.use(bodyParser.urlencoded({ extended: false }));

app.use(cookieSession({
  keys: [sessionSecret]
}));

const db = new sqlite3.Database(':memory:', (err) => {
  if (err) {
    console.error(err.message);
  }
  console.log('Connected to the in-memory SQLite database.');
});

app.get('/', (req, res) => {
    res.sendFile(__dirname + '\\Index.html'); // Updated file path with backslashes
});

app.post('/login', (req, res) => {
  const email = req.body.email;
  const password = req.body.password;

  db.get('SELECT * FROM user_details WHERE Email = ? AND Password = ?', [email, password], (err, row) => {
    if (err) {
      console.error(err.message);
      return res.status(500).send('Internal Server Error');
    }

    
    if (row) {
      req.session.userId = row.Email;
      res.redirect('Patients.html');
    } else {
      res.send('Invalid email or password');
    }
  });
});

app.get('/Form_Sheet.html', (req, res) => {
  if (req.session.userId) {
    res.sendFile(__dirname + '\\Form_Sheet.html'); // Updated file path with backslashes
  } else {
    res.redirect('Login.html');
  }
});

app.get('/Login.html', (req, res) => {
  res.sendFile(__dirname + '\\Login.html'); // Updated file path with backslashes
});

// Start the server
app.listen(port, () => {
  console.log(`Server listening on port ${port}`);
});
