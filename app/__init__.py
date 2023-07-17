# author : @rebwar_ai :: __init__.py
import eventlet
from flask import Flask,render_template
from rq import Queue
from flask_socketio import SocketIO
import redis

app = Flask(__name__)

app.config["SECRET_KEY"] = "sd5d56s56d6sd56sd6s5d"

r = redis.Redis()
q=Queue(connection=r)

eventlet.monkey_patch()

socketio = SocketIO(
	app,
	async_mode = "eventlet",
	logger = True,
	engineio_logger = True,
	allow_upgrades = True,
	cors_allowed_origins = "*",
	ping_timeout = 5,
	ping_interval = 5,
	message_queue = "redis://"
	)

@socketio.on("connect")
def connect():
	print('@socketio.on("connect")')



def push_notification_job(data):
	socketio.emit("notification_js",data)

@app.route("/",methods=["GET"])
def index():
	return "<h1> Index Page </h1>"


@app.route("/push_notification",methods=["GET"])
def push_notification():
	data = {"new_notification": 1}
	push = q.enqueue(push_notification_job,data)
	return "<h1> push notification Page </h1>"


@app.route("/notification",methods=["GET"])
def notification():
	return render_template("notification.html")