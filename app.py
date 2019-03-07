from flask import Flask, request, redirect, flash, url_for , send_from_directory , send_file
import uuid
import os
import json
from flask import jsonify
from werkzeug.utils import secure_filename

UPLOAD_FOLDER = './uploads'
ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'}

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@app.route("/")
def hello():
    hostname = os.uname()[1]
    randomid = uuid.uuid4()
    return 'Container Hostname: ' + hostname + ' , ' + 'UUID: ' + str(randomid) + '\n'
@app.route("/get")
def amin():
    return jsonify({"State":True,"Description":"GET"})
@app.route("/formbody" ,methods=["POST"])
def body():
    return jsonify(request.form)
@app.route("/header")
def header():
    return jsonify({"State":True,"Description":request.headers["Token"]})
@app.route("/jsonbody")
def json_body():
    return jsonify(request.json)

@app.route("/uploadimage",methods=["POST","GET"])
def upload_image():
    try:
        if request.method == 'POST':
            # check if the post request has the file part
            if 'file' not in request.files:
                flash('No file part')
                return redirect(request.url)
            file = request.files['file']
            # if user does not select file, browser also
            # submit an empty part without filename
            if file.filename == '':
                flash('No selected file')
                return Exception("FileNotFound")
            if file and allowed_file(file.filename):
                filename = secure_filename(file.filename)
                file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
                return jsonify({"State":True,"Description":filename})
        return jsonify((os.listdir(app.config["UPLOAD_FOLDER"])))
    except Exception as ex:
        return jsonify({"State":False,"Description":ex.args})

@app.route("/download/<filename>")
def download(filename):
    try:
        print(os.path.join(app.config["UPLOAD_FOLDER"], filename))
        return send_file(os.path.join(app.config["UPLOAD_FOLDER"], filename))

    except Exception as ex:
        return jsonify({"State":False,"Description":ex.args})

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=3007)

