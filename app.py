import numpy as np
from flask_ngrok import run_with_ngrok
from flask import Flask,render_template,request
app = Flask(__name__)
#run_with_ngrok(app)  # Start ngrok when app is run

@app.route('/')
def index():
    name = "Mi Chiamo Manuel Rucci FINE Lezione di Lunedi"
    return render_template('index.html', name=name)

if __name__ == "__main__":
    app.run()
