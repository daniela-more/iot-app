
# ------- Plotly 
import plotly
import plotly.graph_objects as go
import plotly.figure_factory as ff
from kaleido.scopes.plotly import PlotlyScope
import json
scope = PlotlyScope()

def plot_plotly(df,x, y,title):
    n = df[x].values.tolist()
    fig = go.Figure()
    for name in y:
        m = df[name]
        fig.add_trace(go.Scatter(x=n, y=m,
                      mode='lines',#mode='lines+markers',
                      name=name))
    fig.update_layout(
        hovermode = "x",
        #paper_bgcolor = "rgb(0,0,0)" ,
        #plot_bgcolor = "rgb(10,10,10)" , 
        dragmode="pan",
        title=dict(
            x = 0.5,
            text = title,
            font=dict(
                size = 20,
                color = "rgb(0,0,0)"
            )
        )
    )
    return fig

def convert_plotly_fig_to_json(fig):
    fig_json = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)
    return fig_json

def export_plotly_fig(fig,name,ext="png",width=1280,height=720):
    #ext = "png" #"png" #pdf, svg, jpeg, png
    img_bytes = scope.transform(fig,format=ext,width=width,height=height,scale=1)
    #display(IPython.display.Image(img_bytes))
    with open(name+"."+ext, "wb") as f:
        f.write(img_bytes) 

# ------ Pandas dataframe
import pandas as pd

def convert_dataframe_to_plotly_fig(df):
    fig =  ff.create_table(df)
    fig.update_layout(
        width=450,
        height=60,
        font_size=20
    )
    return fig
      
def convert_dataframe_to_html(df,class_name="mytable",index=False):
    return df.to_html(index=index,classes=class_name)

def convert_dataframe_to_json(df):
    return df.to_json(index=False) #orient='split', index=False)

# ------ Datetime
import datetime

def convert_datetime_to_string(dt, formatting='%Y_%m_%d.%H_%M_%S'):
    return datetime.datetime.strptime(dt, formatting)

def convert_numpy_datetime64_to_string(dt, formatting='%Y_%m_%d.%H_%M_%S'):
    return datetime.datetime.utcfromtimestamp(dt/1e9).strftime('%d-%m-%Y %H:%M:%S')

# ----- Matplotlib
import io
import base64
import matplotlib.pyplot as plt

def plot_matplotlib(df,select,title):
    with plt.style.context("seaborn"):
        #print(plt.style.available)
        fig, ax = plt.subplots(1, 1, figsize=(15, 8))
        df.set_index("data").plot(y=select, kind="line", stacked=False,title=title,ax=ax)
        #el = ax.get_figure()
        return fig

def convert_image_to_base64(fig,ext="png"):
    f = io.BytesIO()
    fig.savefig(f, format=ext, bbox_inches="tight")
    f.seek(0)
    s = base64.b64encode(f.getvalue()).decode("utf-8").replace("\n", "")
    string  = "data:image/"+ext+";base64,"+ s
    return string

def export_matplotlib_image(fig,name, ext="png"):
    path = name + "." + ext
    fig.savefig(path,dpi=300, transparent=False)
     