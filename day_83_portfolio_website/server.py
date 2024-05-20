'''A Flask web server for a developer portfolio website.'''
from flask import Flask, render_template, redirect

app = Flask(__name__)

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/sendmsg")
def sendmsg():

    return redirect('index.html')

if __name__ == "__main__":
    app.run(debug=True)