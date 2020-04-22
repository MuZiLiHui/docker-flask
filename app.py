
from flask import Flask,render_template
from flask_restful import reqparse, abort, Api, Resource

app = Flask(__name__, static_url_path='')
##
## Actually setup the Api resource routing here
##

@app.route('/')
def visualData():
    return app.send_static_file('index.html')

if __name__ == '__main__':
    app.run(host="0.0.0.0",debug=True)

'''
import socket
import os
from redis import Redis, RedisError

# Connect to Redis
redis = Redis(host="redis", db=0, socket_connect_timeout=2, socket_timeout=2)
@app.route("/")
def hello():
    try:
        visits = redis.incr("counter")
    except RedisError:
        visits = "<i>cannot connect to Redis, counter disabled</i>"

    html = "<h3>Hello {name}!</h3>" \
           "<b>Hostname:</b> {hostname}<br/>" \
           "<b>Visits:</b> {visits}"
    return html.format(name=os.getenv("NAME", "world"), hostname=socket.gethostname(), visits=visits)
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80)
'''

