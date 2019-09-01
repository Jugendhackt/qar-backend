from flask import Flask, request, render_template, redirect, send_file
from werkzeug import secure_filename
import time
import json
import pyqrcode
from PIL import Image
app = Flask(__name__)

#print(app.config['UPLOAD_FOLDER'])

@app.route("/")
@app.route("/welcome")
def welcome():
    return render_template("welcome.html")

@app.route("/file/<path>")
def Download(path = None):
    print("hi",path)
    if path is None:
        #app.Error(400)
        return "Error 400, no path"
    try:
        print(path)
        return send_file(path, as_attachment = True)
    except Exception as e:
        #app.log.exception(e)
        return "Error 400, wrong file?" #app.Error(400)

@app.route('/uploaded', methods = ['POST','GET'])
def upload_file():
   if request.method == 'POST':
      f = request.files['file']
      f.save(secure_filename(f.filename))
      urli = "http://nifanta.ch:8080/display/"+str(f.filename)
      print(urli)
      url = pyqrcode.create(urli)
      url.png("test.png",scale=10)
      im = Image.open('test.png')
      im = im.convert("RGBA")
      for k in range(2,5):
      	logo = Image.open('static/pic/bucket_empty.png')
      	box = (200,200,300,300)
      	im.crop(box)
      	region = logo
      	region = region.resize((box[2] - box[0], box[3] - box[1]))
      	im.paste(region,box)
      	im.save(f'static/pic/qr-code{k}.png')
      	del im
      return render_template("uploaded.html",time = time.time())
   else:
        return "Just Post"
@app.route("/display/<path>")
def display(path = None):
   print("display",path)
   if path is None:
       return "errorrr"
   x = request.args.get('app', default = False, type = bool)

   if x:
       print("hi")
       return redirect("/file/"+str(path))
   print(path)
   return render_template("display.html",file="/file/"+path)

if __name__ == "__main__":
    app.run(debug=True,port = 8080, host="0.0.0.0")
