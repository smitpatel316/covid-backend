from flask import Flask

from app.controllers.canada import canada

app = Flask(__name__)


@app.after_request
def after_request(response):
    header = response.headers
    header["Access-Control-Allow-Origin"] = "*"
    header["Access-Control-Allow-Headers"] = "*"
    return response


@app.route("/")
def home():
    return "On Home"


app.register_blueprint(canada)


if __name__ == "__main__":
    app.run()
