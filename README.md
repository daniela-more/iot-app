# iot-app

* [APP LINK](https://iot-app-course.herokuapp.com/)
* https://iot-app-course.herokuapp.com/

## Setup Locally

```
virtualenv env
Windows: source env/Scripts/activate
MAC: source env/bin/activate
pip install -r requirements.txt

# python
App HTTP: python app.py
App WEBSOCKET: python websocketApp.py

# guinicorn
App HTTP: gunicorn app:app --log-file=- --bind=0.0.0.0:4500
App WEBSOCKET: gunicorn -k eventlet  -w 1 --log-file=- websocketApp:app --bind=0.0.0.0:4500
```


## Setup Heroku

```
Procfile: web: gunicorn app:app --log-file=-
Procfile: web: web: gunicorn -k eventlet  -w 1 --log-file=- websocketApp:app
```

* [Flas-SocketIO ](https://flask-socketio.readthedocs.io/en/latest/)
* [Flask Quick Start](https://flask.palletsprojects.com/en/1.1.x/quickstart/)
* [Plotly figure reference](https://plotly.com/python/reference/)
