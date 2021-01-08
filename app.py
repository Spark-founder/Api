import os
from flask import Flask, flash, request, redirect, url_for, session, jsonify
from werkzeug.utils import secure_filename
from flask_cors import CORS, cross_origin
import logging
import cv2
logging.basicConfig(level=logging.INFO)

logger = logging.getLogger('HELLO WORLD')

PROJECT_HOME = os.path.dirname(os.path.realpath(__file__))
UPLOAD_FOLDER = '{}/uploads/'.format(PROJECT_HOME)
ALLOWED_EXTENSIONS = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'])

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
print(UPLOAD_FOLDER)


@app.route('/upload', methods=['POST'])
def fileUpload():
    target = os.path.join(UPLOAD_FOLDER)
    if not os.path.isdir(target):
        os.mkdir(target)
    file = request.files['file']
    if file:
        filename = secure_filename(file.filename)
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        logger.info("welcome to upload`")
        return jsonify({
            'Sucess': True
        })
    return jsonify({
        'Sucess': False
    })


if __name__ == "__main__":
    app.secret_key = os.urandom(24)
    app.run(debug=True, host="0.0.0.0", use_reloader=False)
