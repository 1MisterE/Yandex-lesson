from flask import Flask, url_for

app = Flask(__name__)


@app.route("/")
def home():
    return f"Миссия Колонизация Марса"


@app.route("/index")
def index():
    return "И на Марсе будут яблони цвести!"


@app.route("/promote")
def promote():
    s = [
        "Человечество вырастает из детства.",
        "Человечеству мала одна планета.",
        "Мы сделаем обитаемыми безжизненные пока планеты.",
        "И начнем с Марса!",
        "Присоединяйся!",
    ]
    return "</br>".join(s)


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5252)
