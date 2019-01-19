from flask import Flask ,request
from flask_prometheus import monitor 
import uuid
import os

app = Flask(__name__)

@app.route("/")
def hello():
    hostname = os.uname()[1]
    randomid = uuid.uuid4()
    return 'Container Hostname: ' + hostname + ' , ' + 'UUID: ' + str(randomid) + '\n'
@app.route("/amin")
def amin():
    return "check mail"
@app.route("/body" ,methods=["POST"])
def body():
    return request.form["Token"]
@app.route("/header")
def header():
    return request.headers["Token"]
if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=3007)

