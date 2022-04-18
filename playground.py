from database import insert, check, select, dictionary
from connection import connect
from tensorflow.keras.preprocessing import image
from tensorflow.keras.applications.vgg16 import VGG16, preprocess_input
from tensorflow.keras.models import Model, load_model
import numpy as np
from PIL import Image
from pathlib import Path
from feature_extractor import FeatureExtractor

# fe = FeatureExtractor()
# conn = connect()

# ## Check layer model
# base_model = load_model('static/model/model_resnet.h5')
# print(base_model.summary())

# Check CRUD Database

# Get dictionary
# dictionary = dictionary(conn)
# print(dictionary)

# Select
# features, img_binary = select(conn, 0)
# print(features[0])
# print(img_binary[0])

# Check
# id = check("gloves", conn)
# print(id)


# Feature Extractor
# img = Image.open('static/dataset/blazers/P_0.jpg') # PIL image
# feature = fe.extract(img)
# print(feature)

# old_value = 0.2
# old_min = 1
# old_max = 0
# new_min = 0
# new_max = 100

# new_value = ( (old_value - old_min) / (old_max - old_min) ) * (new_max - new_min) + new_min

# print(new_value)


