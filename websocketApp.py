
from flask import Flask, render_template
from flask_socketio import SocketIO
import threading
import pandas as pd
import time
from utils import *
import json

app = Flask(__name__)
app.config['SECRET_KEY'] = 'vnkdjnfjknfl1232#'
socketio = SocketIO(app)

def load_data():
    df = pd.read_csv("https://raw.githubusercontent.com/pcm-dpc/COVID-19/master/dati-andamento-nazionale/dpc-covid19-ita-andamento-nazionale.csv")
    df["data"] = [el[0:10] for el in df["data"].values.tolist()]
    return df 

def update_func():
    dfplot = []
    ii = 3
    df = load_data()
    print(df.keys())
    start=True
    while(start):
        if (df.values.shape[0]-1)==ii:
            ii=3
            #start=False
            time.sleep(2)
        else:
            ii =ii+1
        time.sleep(0.1)
        dfplot = df.iloc[0:ii]
        fig1 = plot_plotly(dfplot,x ="data", y=["deceduti","totale_casi","dimessi_guariti"],title="Andamento Nazionale")    
        fig2 = plot_plotly(dfplot,x ="data", y=["variazione_totale_positivi"],title="Variazione totale positivi")
        fig3 = plot_plotly(dfplot,x ="data", y=["terapia_intensiva"],title="Terapia Intensiva")
        fig4 = plot_plotly(dfplot,x ="data", y=["tamponi"],title="Tamponi")
        
        fig1_json = json.loads(convert_plotly_fig_to_json(fig1))
        fig2_json = json.loads(convert_plotly_fig_to_json(fig2))
        fig3_json = json.loads(convert_plotly_fig_to_json(fig3))
        fig4_json = json.loads(convert_plotly_fig_to_json(fig4))
        
        # Trovami anomalie
        socketio.emit("stream", {   "date": df.iloc[ii]["data"] ,
                                    "fig1_data": fig1_json["data"] , 
                                    "fig1_layout": fig1_json["layout"],
                                    "fig2_data": fig2_json["data"] , 
                                    "fig2_layout": fig2_json["layout"],
                                    "fig3_data": fig3_json["data"] ,    
                                    "fig3_layout": fig3_json["layout"],
                                    "fig4_data": fig4_json["data"] , 
                                    "fig4_layout": fig4_json["layout"],


                                })
def timer():
    i=0
    while(True):
        time.sleep(0.5)
        socketio.emit("stream", "Clock: " + str(i))
        i = i + 1


x = threading.Thread(target=update_func)
x.start()
time.sleep(2)

@app.route('/')
def sessions():
    return render_template('websocket.html')

@app.route('/test')
def sessions_test():
    return render_template('index.html')

@socketio.on('connected')
def handle_my_custom_event(json, methods=['GET', 'POST']):
    print('received my event: ' + str(json))


if __name__ == '__main__':
    socketio.run(app) #, host="0.0.0.0") #, debug=True)