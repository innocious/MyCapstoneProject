from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello Innocent Onwukanjo here. You are on the Greeeeeen deployment!!!!"

# @app.route("/healthz")
# def healthz():
#     return "Aive and Kicking!!!!!"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int("9000"), debug=True)