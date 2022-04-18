import mysql.connector as mc
import pickle
import numpy as np

def insert(id_cat, array, image,  db):
    # Memasukan data fitur ke dataset
    try:
        if db.is_connected():
            cursor = db.cursor()
            # Insert data id_cat, fitur, image 
            sql = "INSERT INTO feature (id_cat, array, image) VALUES (%s, %s, %s)"
            val = (id_cat, pickle.dumps(array), image)
            cursor.execute(sql, val)

            db.commit()

    except mc.Error as e:
        print("Gagal saat menghubungkan ke MySQL", e)     

def select(db, category):
    # Menampilkan dataset
    try:
        if db.is_connected():
            cursor = db.cursor()
            # Menampilkan semua data sesuai id kategori
            sql = f"SELECT array, image FROM feature WHERE id_cat = {category}"
            cursor.execute(sql)
            result = cursor.fetchall()

            features = []
            img = []
            for index in range(len(result)):
                # [index] adalah list dan didalamnya ada tuple [(array, image), (array, image)]
                # [0] di dalam list terdapat kumpulan tuple yang isinya (array, image)

                # melakukan decode data gambar
                decode = result[index][1].decode("utf-8")
                img.append(decode)

                # Me-load binary image
                features.append(pickle.loads(result[index][0]))
                
            return np.array(features), img

    except mc.Error as e:
        print("Gagal saat menghubungkan ke MySQL", e)

def dictionary(db):
    # membuat dictionary
    try:
        if db.is_connected():
            cursor = db.cursor()

            sql = f"SELECT id_cat, label FROM category"
            cursor.execute(sql)
            result = cursor.fetchall()
            
            d = {}
            for index in range(len(result)):
                d[f'{result[index][1]}'] = result[index][0]
                
            return d

    except mc.Error as e:
        print("Gagal saat menghubungkan ke MySQL", e)


def check(label, db):
    # Check ketersediaan kategori 
    try:
        if db.is_connected():
            cursor = db.cursor()
            sql = f"SELECT id_cat FROM category WHERE label = '{label}'"
            cursor.execute(sql)

            result = cursor.fetchone()

            return result

    except mc.Error as e:
        print("Gagal saat menghubungkan ke MySQL", e)