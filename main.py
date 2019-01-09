from flask import Flask ,request

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello this is jenkins piplining"
@app.route("/amin")
def amin():
    return " Hier ist Amin Jamal , Hallo :)"


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=6000)