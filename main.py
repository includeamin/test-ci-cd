from flask import Flask ,request

app = Flask(__name__)

@app.route("/")
def hello():
    return "warum bist du hier? was machst du? sag mir!"
@app.route("/amin")
def amin():
    return "Hallo liebe Sheyda :)"


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=3007)