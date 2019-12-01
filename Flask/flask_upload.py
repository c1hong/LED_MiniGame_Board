from flask import Flask, render_template, request, redirect, url_for, send_from_directory
from werkzeug.utils import secure_filename
import os

app = Flask(__name__)

ROOT_APP = os.path.dirname(os.path.abspath(__file__))
UPLOAD_FOLDER = os.path.join(ROOT_APP, 'uploads')
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route('/upload')
def render_file() :
    return render_template('upload.html')

@app.route('/fileUpload', methods = ['GET', 'POST'])
def upload_file() :
    if request.method == 'POST' :
        f = request.files['file']
        filename = secure_filename(f.filename)
        f.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        return redirect(url_for('render_file')) 

@app.route('/GetUserPhoto/<path:filename>')
def download(filename) :
    try :
        return send_from_directory(app.config['UPLOAD_FOLDER'], filename=filename, mimetype='image/jpeg', as_attachment=True)
    except FileNotFoundError :
        abort(404)

# --------- main ---------- #

if __name__ == '__main__' :
    app.run(debug = True)
