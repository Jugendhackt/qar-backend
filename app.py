from flask import Flask, request, render_template, redirect, send_file
from werkzeug import secure_filename
import json
app = Flask(__name__)

#print(app.config['UPLOAD_FOLDER'])

@app.route("/")
@app.route("/welcome")
def welcome():
    return render_template("welcome.html")


@app.route('/<path>')
def my_form(path = None):
    if path is None:
         return "Not yet here"
    return json.dumps({"File":"nifanta.ch:8080/file/"+str(path),"virtual":True})

@app.route("/file/<path>")
def Download(path = None):
    if path is None:
        #app.Error(400)
        return "Error 400, no path"
    try:
        print(path)
        return send_file(path, as_attachment = True)
    except Exception as e:
        #app.log.exception(e)
        return "Error 400, wrong file?" #app.Error(400)

@app.route('/assets/<path>')
def get_file(path = None):
    if path is None:
        return "Error"
    try:
        print(path)
        return send_file("assets/"+path, as_attachment = True)
    except Exception as e:
        return "Errrrrrrrrrrror"
@app.route('/uploaded', methods = ['POST','GET'])
def upload_file():
   if request.method == 'POST':
      f = request.files['file']
      f.save(secure_filename(f.filename))
      return render_template("uploaded.html")

@app.route("/display")
def display():
   return render_template("display.html")

if __name__ == "__main__":
    app.run(debug=True,host='0.0.0.0',port = 8080)
