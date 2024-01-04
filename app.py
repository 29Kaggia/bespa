import sqlite3
from flask import Flask, render_template, request

app = Flask(__name__)

# Create SQLite connection and cursor
conn = sqlite3.connect('bespa.db')
cursor = conn.cursor()

# Create a table for storing emails if it doesn't exist
cursor.execute('''CREATE TABLE IF NOT EXISTS sent_emails (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    sender_email TEXT NOT NULL,
                    message TEXT,
                    sent_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP)'''
               )
conn.commit()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit_form', methods=['POST'])
def submit_form():
    if request.method == 'POST':
        sender_email = request.form['sender_email']
        message = request.form['message']

        # Insert data into the SQLite table
        cursor.execute('INSERT INTO sent_emails (sender_email, message) VALUES (?, ?)', (sender_email, message))
        conn.commit()
        
        return 'Email sent successfully!'

if __name__ == '__main__':
    app.run(debug=True)
