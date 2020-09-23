# iot-app
IOT flask app
HO ciao


## Setup Heroku

```
Procfile: web: gunicorn app:app --log-file=-
Procfile: web: gunicorn --worker-class socketio.sgunicorn.GeventSocketIOWorker --log-file=- websocketApp:app
```