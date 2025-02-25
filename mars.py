from flask import Flask, url_for

app = Flask(__name__)

@app.route('/')
def qls():
	return f"Миссия Колонизация Марса"

@app.route('/index')
def index():
    return "И на Марсе будут яблони цвести!"



if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5252)
