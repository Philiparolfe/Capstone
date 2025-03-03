from flask import Flask, render_template
import sqlite3

app = Flask(__name__)

# Function to retrieve logs from the database
def get_logs():
    conn = sqlite3.connect('syslogs.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM logs ORDER BY id DESC')  # Fetch all logs ordered by ID (latest first)
    logs = cursor.fetchall()
    conn.close()
    return logs

@app.route('/')
def home():
    # Get logs from the database
    logs = get_logs()
    
    # Render the logs in the frontend
    return render_template('logs.html', logs=logs)

if __name__ == '__main__':
    app.run(debug=True)
