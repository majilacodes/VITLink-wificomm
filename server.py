from flask import Flask, render_template
from flask_socketio import SocketIO, emit
import sqlite3
import datetime

app = Flask(__name__)
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
    return render_template('index.html')

@app.route('/client')
def client():
    return render_template('client.html')

@socketio.on('send_message')
def handle_message(data):
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
    socketio.run(app, host='192.168.102.81', port=5002)
