import numpy as np
#from flask_ngrok import run_with_ngrok
from flask import Flask,render_template,request
from utils import *

app = Flask(__name__)
#run_with_ngrok(app)  # Start ngrok when app is run


def load_data():
    df = pd.read_csv("https://raw.githubusercontent.com/pcm-dpc/COVID-19/master/dati-andamento-nazionale/dpc-covid19-ita-andamento-nazionale.csv")
    df["data"] = [el[0:10] for el in df["data"].values.tolist()]
    return df 

# https://iot-app-course.herokuapp.com/
@app.route('/')
def index():
    df = load_data()
    select = ["deceduti","totale_casi","dimessi_guariti","variazione_totale_positivi"]
    fig = plot_plotly(dfplot,x ="data", y=["deceduti","dimessi_guariti","totale_positivi"],title="Andamento Nazionale")    
    
    return render_template('index.html', 
                            name="Manuel",
                            surname="Rucci",
                            eta="26",
                            sesso="Maschio",
							collaboratore = "Sono Ugo e collaboro all'app")
                            fig= convert_plotly_fig_to_json(fig))

if __name__ == "__main__":
    app.run()
