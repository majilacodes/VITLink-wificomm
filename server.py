from flask import Flask, render_template, request, redirect, url_for, session, flash
from flask_socketio import SocketIO, emit
import sqlite3
import datetime

app = Flask(__name__)
app.secret_key = 'cnproject'  # Set a secret key for session management
socketio = SocketIO(app)

# Database setup
def init_db():
    conn = sqlite3.connect('notifications.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS logs
                 (id INTEGER PRIMARY KEY, message TEXT, timestamp TEXT, category TEXT)''')
    conn.commit()
    conn.close()

@app.route('/')
def index():
    return render_template('landing.html')  # Render the landing page

@app.route('/client')
def client():
    # Request notification permission when the client page is accessed
    return render_template('client.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if username == 'admin' and password == 'admin':
            session['logged_in'] = True  # Set the logged_in session variable
            return redirect(url_for('server'))  # Redirect to the server page
        else:
            flash('Invalid username or password. Please try again.')
    return render_template('login.html')

@app.route('/logout')
def logout():
    session.pop('logged_in', None)  # Remove the user from the session
    return redirect(url_for('login'))  # Redirect to login page

@app.route('/server')
def server():
    # Always show the server page, regardless of login status
    return render_template('server.html')

@app.route('/messages')
def messages():
    # Always show the messages page, regardless of login status
    conn = sqlite3.connect('notifications.db')
    c = conn.cursor()
    c.execute("SELECT message, timestamp, category FROM logs ORDER BY timestamp DESC")
    messages = c.fetchall()  # Get all messages
    conn.close()
    
    return render_template('messages.html', messages=messages)  # Pass messages to the template

@app.route('/clear_messages', methods=['POST'])
def clear_messages():
    if not session.get('logged_in'):  # Protect the clear messages route
        flash('You must be logged in to clear messages.')  # Flash message for better UX
        return redirect(url_for('login'))  # Redirect to login if not logged in
    
    # Clear all messages from the database
    conn = sqlite3.connect('notifications.db')
    c = conn.cursor()
    c.execute("DELETE FROM logs")  # Delete all records
    conn.commit()
    conn.close()
    
    flash('All messages have been cleared.')  # Flash message for user feedback
    return redirect(url_for('messages'))  # Redirect to messages page

@socketio.on('send_message')
def handle_message(data):
    if not session.get('logged_in'):  # Check if the user is logged in
        return  # Prevent unauthorized access
    message = data['message']
    category = data['category']
    timestamp = datetime.datetime.now().isoformat()
    
    # Log the message
    conn = sqlite3.connect('notifications.db')
    c = conn.cursor()
    c.execute("INSERT INTO logs (message, timestamp, category) VALUES (?, ?, ?)", 
              (message, timestamp, category))
    conn.commit()
    conn.close()
    
    # Broadcast the message
    emit('receive_message', {'message': message, 'category': category}, broadcast=True)

if __name__ == '__main__':
    init_db()
    socketio.run(app, host='172.20.156.116', port=5002)