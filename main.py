from flask import Flask ,request

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello this is jenkins piplining"


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=6000)