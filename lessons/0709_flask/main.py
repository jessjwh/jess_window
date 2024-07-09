from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    return render_template('index.html')

@app.route('/hello')
def hello():
    return '<h1>Hello again.</h1>'

@app.route('/user/<username>')
def show_user_profile(username):
    return f'<h1>Hi {username}!</h1>'

@app.route('/post/<int:post_id>')
def show_post(post_id):
    return f'<h1>Post {post_id}</h1>'

