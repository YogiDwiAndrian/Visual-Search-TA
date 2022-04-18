import os
import base64
from PIL import Image
from pathlib import Path
from feature_extractor import FeatureExtractor
from database import insert, check
from connection import connect

if __name__ == "__main__":
    fe = FeatureExtractor()
    conn = connect()

    path = "static/dataset/"

    for cat in os.listdir(path):
        # Check name folder is same category name on db
        id = check(cat, conn)
        if id == None:
            pass
        else:
            print(f"Proses ekstraksi fitur pada kategori {cat}")
            for img_path in sorted(Path(f"./static/dataset/{cat}").glob("*jpg")):
                feature = fe.extract(img=Image.open(img_path))
                file = open(img_path,'rb').read()
                file = base64.b64encode(file)
                insert(id[0], feature, file,  conn)
                    
    print("Proses ekstraksi fitur selesai")

    conn.close()
            

