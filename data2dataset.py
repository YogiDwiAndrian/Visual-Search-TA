import os
import shutil

# Inisiasi data yang akan dipindah
sources = ['dress', 'accessories', 'bag', 'bottom', 'shoes', 'outerwear', 'swimwear']
source = "static/data"
destination = "static/dataset"

# Melakukan pemindahan sub-kategori dataset ke satu folder
for category in sources:
  cur_cat = os.path.join(source, category)
  for sub in os.listdir(category):
    cur_sub = os.path.join(cur_cat, sub)
    shutil.move(cur_sub, destination, copy_function = shutil.copytree)
  os.rmdir(cur_cat)