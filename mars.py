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
@app.route("/image_mars")
def image_draw():
	return f"""<!doctype html>
                <html lang="en">
                  <head>
                    <meta charset="utf-8">
                    <title>Привет, Марс!</title>
                  </head>
                  <body>
                    <h1>Жди нас, Марс!</h1>
                    <img src="{url_for('static', filename='img/image_mars.jpg')}"
           alt="здесь должна была быть картинка, но не нашлась">
                    <h2>Вот она какая, красная конфета</h2>
                  </body>
                </html>"""


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5252)
