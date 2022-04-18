import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'
from  io import BytesIO
import base64
import numpy as np
from werkzeug.utils import secure_filename
from PIL import Image
from feature_extractor import FeatureExtractor
from flask import Flask, request, render_template
import tensorflow as tf
from tensorflow import keras

from database import select, dictionary
from connection import connect

model = keras.models.load_model("static/model/model_resnet.h5")

def transform_image(pillow_image):
    data = np.asarray(pillow_image)
    data = np.expand_dims(data, axis=0)
    images = np.vstack([data])
    images = tf.image.resize(data, [128, 128])
    return images

def predict(x):
    predictions = model(x)
    pred = predictions[0]
    label = np.argmax(pred)

    sort = np.argsort(pred)
    largest_indices = sort[::-1]
    ranked = largest_indices[:1]

    class_dictionary = dictionary(conn)

    key_list = list(class_dictionary.keys())
    val_list = list(class_dictionary.values())

    prob = []
    for x in ranked:
        position = val_list.index(x)
        prob.append(key_list[position])

    return label, ', '.join(prob), predictions, largest_indices, class_dictionary

def convert_dist(old_value):
    old_min = 1
    old_max = 0
    new_min = 0
    new_max = 100
    return round(((old_value - old_min) / (old_max - old_min) ) * (new_max - new_min) + new_min, 2)

fe = FeatureExtractor()
conn = connect()

app = Flask(__name__)
app.config['UPLOAD_EXTENSIONS'] = ['.jpg', '.png', '.jpeg']

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':

        uploaded_file = request.files["query_img"]

        filename = secure_filename(uploaded_file.filename)
        # check condition submit empty file or not
        if filename != '':
            file_ext = os.path.splitext(filename)[1].lower()
            if file_ext not in app.config['UPLOAD_EXTENSIONS']:
                return render_template("index.html", ext='Uploaded file is not a valid image. Only JPG, JPEG and PNG files are allowed')
            else:
                # open image PIL
                img = Image.open(uploaded_file.stream)
                rgb_pred = img.convert('RGB')
                rgb_blob = img.convert('RGB')

                # image to blob
                buffered = BytesIO()
                rgb_blob.save(buffered, format="JPEG")
                img_encode = base64.b64encode(buffered.getvalue())
                # decode image base64 to load on HTML
                img_decode = img_encode.decode("utf-8")
                
                # Prediction class
                tensor = transform_image(rgb_pred)
                # return id category and probability classes
                category, prob, pred, sort, dictionary = predict(tensor)
                print(pred)
                features, img_binary = select(conn, category)

                # Run search
                query = fe.extract(img)
                # Menghitung jarak euclidean
                dists = np.linalg.norm(features-query, axis=1)
                # indexing 30 hasil teratas
                ids = np.argsort(dists)[:30]  
                scores = [(convert_dist(dists[id]), img_binary[id], query, features[id], dists[id]) for id in ids]

                return render_template("index.html", query_path=img_decode, scores=scores, probability=prob, tensor=tensor, pred=pred, sort=sort, dictionary=dictionary, category=category)
        else: 
            return render_template("index.html", ext = "Please select image file to upload")
    else: 
        return render_template("index.html")

if __name__=="__main__":
    app.run()