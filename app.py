import numpy as np
#from flask_ngrok import run_with_ngrok
from flask import Flask,render_template,request
app = Flask(__name__)
#run_with_ngrok(app)  # Start ngrok when app is run

# https://iot-app-course.herokuapp.com/
@app.route('/')
def index():
    return render_template('index.html', 
                            name="Manuel",
                            surname="Rucci",
                            eta="26",
                            sesso="Maschio")

if __name__ == "__main__":
    app.run()
