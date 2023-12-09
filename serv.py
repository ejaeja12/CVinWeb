from flask import Flask, render_template, request, flash,Response
from werkzeug.utils import secure_filename
from parkingSpacePicker import picker
from pathlib import Path
import tempfile
import os

UPLOAD = os.path.join('static', 'uploads')
ALLOWED_EXTENSIONS = {'mp4'}

app = Flask(__name__)
app.secret_key = 'super secret key'
app.config['UPLOAD'] = UPLOAD


def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/", methods=["GET","POST"])
def video():
    if request.method == "POST": 
        # check if the post request has the file part
        if 'file' not in request.files:
            flash('No file part')
            return "error"
        file = request.files['file']
        # If the user does not select a file, the browser submits an
        # empty file without a filename.
        if file.filename == '':
            flash('No selected file')
            return "error no selected file"
        if file and allowed_file(file.filename):
            file.save('static/uploads/' + file.filename)
            
            # return Response(picker.tes('uploads/'+file.filename),mimetype='multipart/x-mixed-replace; boundary=frame')
            # return render_template("index.html",video=picker.tes('uploads/'+file.filename))
            # file_a = picker.tes('uploads/' + file.filename)
            picker.tes('static/uploads/'+file.filename,str(file.filename))
            img = os.path.join(app.config['UPLOAD'], file.filename + ".jpg")
            return render_template("index.html",img =  img)

    return render_template("index.html")


@app.route("/", methods=["GET","POST"])
def submit_xy():
    formData = request.values if request.method == "GET" else request.values
    response = "Form Contents <pre>%s</pre>" % "<br/>\n".join(["%s:%s" % item for item in formData.items()] )
    return response

if __name__ == '__main__':
    app.run(debug=True, port=8001)