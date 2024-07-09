from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    return render_template('index.html.jinja')

@app.route('/gallery')
def gallery():
    return render_template('gallery.html.jinja')

@app.route('/instagram')
def instagram():
    return render_template('instagram.html.jinja')

@app.route('/contact')
def contact():
    return render_template('contact.html.jinja')

