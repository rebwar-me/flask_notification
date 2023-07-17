1-sudo apt update
2-sudo apt install redis-server
3-create python env:
	python3 -m venv env

4-activate env:
	source env/bin/activate

5-install :
	pip install flask
	pip install redis
	pip install rq
	pip install Flask-SocketIO
	pip install eventlet
	pip install cryptography