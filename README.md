# This is just a simple websocket application using python (async)

### Its run socket server locally on port 8765 and listens to all incoming messages.
Note:
- Only server sees all messages
- Clients connecting to separated channels (paths) and see only messages in it.
- There is no delivery status reports/responds (simple websocket app)
- Server doesn't save any data (no DB, files or anything like this)

### Stack:
- Python 3.7 (or above)
- Websockets 11.0.1 (or above)

### Files in repo:
- server.py - websocket server code itself
- spam_sender.py - code for testing of availability and mass message sends to server paths
- Dockerfile - simple docker config for running server locally in container. Use "EXPOSE 8765" option in file, so you can redefine container port to whatever you like


### How to install:
Clone git repo:
```
git clone git@github.com:vafansjev/SimplePythonWebsocketApp.git
```


#### Run locally (without docker): 
install requirements using pip3
```
pip3 install -r requirements.txt
```

run server.py using python3:
```
python3 server.py
```

#### Run dockerized:
Install docker and then build new docker image
```
docker build -t my-websocket-app .
```

Run new container with port configuring (e.g. local port 8766 and docker port 8765)
```
docker run -p 8766:8765 my-websocket-app
```

Server is ready to work "ws://127.0.0.1:8766"

Now you can send some messages to different channels (paths) of your local websocket server.
For example, you can send messages to ws://127.0.0.1:8766/5/
and all clients that use same ws address (with patch "5/") will see your message.


## For testing:
You can use browser extensions (e.g. Simple WebSocket Client in GoogleChrome) or to use template in web folder of current project (HTML + JS).
