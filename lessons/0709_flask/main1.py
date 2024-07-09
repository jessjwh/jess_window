from flask import Flask, url_for

app = Flask(__name__)

@app.route("/")
def index():
    return "<h1>Welcome to Index!</h1>\n<h2>It's Jess.</h2>"

@app.route('/login')
def login():
    return '<h1>Hello again! Please log in.</h1>'

@app.route('/user/<username>')
def profile(username):
    return f"<h1>This is {username}'s profile.</h1>"

with app.test_request_context():
    print(url_for('index'))
    print(url_for('login'))
    print(url_for('login', name='Jess', password='555'))
    print(url_for('profile', username='Jess'))

