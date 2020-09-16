import numpy as np

'''
virtualen env
MAC: source env/bin/activate 
WINDOWS: source env/Scripts/activate
pip install numpy
pip install pandas scikit-learn 
pip install flask
pip install pylint
pip 
192.168.1.224
'''

from flask import Flask,render_template
app = Flask(__name__)

'''
@app.route('/')
def hello_world():
    return 'Hello, ,dsd!'
'''

@app.route('/')
def index():
    name = "Mi Chiamo Manuel Rucci FINE DI OGGI"
    return render_template('index.html', name=name)

'''
if __name__ == "__main__":
    app.run(host='0.0.0.0',port=6600,debug=True)
'''
