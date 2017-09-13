import os
from flask import Flask, request, redirect, url_for,flash
from werkzeug.utils import secure_filename

UPLOAD_FOLDER = 'D:/'
ALLOWED_EXTENSIONS = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'])

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/upload', methods=['GET', 'POST'])
def upload():
    if request.method == 'POST':
        file = request.files['file']
        f_name = file.filename
        extension = os.path.splitext(file.filename)[1]
        print('file name', extension)
        #f_name = str(uuid.uuid4()) + extension
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], f_name))
        return json.dumps({'filename':f_name})
    

if __name__ == '__main__':
    app.run()
