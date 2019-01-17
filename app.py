from flask import Flask ,request
from flask_prometheus import monitor 

app = Flask(__name__)

@app.route("/")
def hello():
    return "testing swarm mode"
@app.route("/amin")
def amin():
    return "check mail"


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=3007)

