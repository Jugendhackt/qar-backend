from flask import Flask, request, render_template, redirect, send_file
import json
app = Flask(__name__)

@app.route('/')
@app.route('/first_3d')
def my_form():
    return json.dumps({"File":"nifanta.ch:8080/file/some3dfile.3d","virtual":True})

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


if __name__ == "__main__":
    app.run(debug=True,host='0.0.0.0',port = 8080)
