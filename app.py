from flask import Flask, render_template, redirect, url_for

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/register')
def register():
    return render_template('register.html')

@app.route('/character')
def character():
    return render_template('character.html')

if __name__ == '__main__':
    app.run(debug=True)
