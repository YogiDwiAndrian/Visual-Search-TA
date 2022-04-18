<h1 align="center">Hello Buddy😎</h1>

![Pencarian Hats](https://user-images.githubusercontent.com/56554261/163801334-4d85ebf1-c405-4068-9950-99d529905319.png)
![Hasil Proses Pencarian Hats](https://user-images.githubusercontent.com/56554261/163801360-b4424ba6-41c1-47be-8dd8-37f5e6bdc80d.png)

## **Table of Contents**
1. [Introduction](#introduction)
2. [Dataset](#dataset) 
3. [Implementation](#implementation)
4. [How to launch](#how-to-launch)
5. [Note](#note)

## **Introduction**
This repository is the result of the implementation of my Final Project (Thesis) at the Yogyakarta Technological University in pursuing a bachelor's program in the department of Informatics. The title of my thesis is "IMPLEMENTATION OF DEEP LEARNING FOR PRODUCT IMAGE SEARCH SYSTEMS USING CONVOLUTIONAL NEURAL NETWORK (CNN) ALGORITHM".

## **Dataset**
The dataset used is the Real Fashion dataset from the kaggle website. The Real Fashion dataset contains 30,276 image data and consists of 7 categories with a total of 42 sub-categories in it. The 42 sub-categories in the dataset consist of objects commonly found in the marketplace in the fashion category.

![Sampul Dataset](https://user-images.githubusercontent.com/56554261/138807261-1ef8414e-9e38-40d5-8200-4e03d5ccbb8c.PNG)

Informasi Dataset :

Type | Information
--- | ---
Source | [Kaggle Dataset : Real Fashion](https://www.kaggle.com/hammaadali/real-fashion)
License | Unknown
Category | clothing and accessories
Rating | 4.4
File Type and Size | Folder (2 GB)

## **Implementation**
### **Installation**
* Clone this repo
* Install Python dependencies

```console
$ git clone https://github.com/YogiDwiAndrian/Visual-Search-TA.git
$ cd Visual-Search-TA
$ pip install -r requirements.txt
```

### **Materials**
------------
#### **Models**
The model is used to classify categories in the search process and is also used for image feature extraction which will then be added to the database. The model can be obtained from downloading the model that I have trained ([Model Resnet](https://drive.google.com/drive/folders/1teIMRvnbGMeyP7SQoOgXcvl-V4cr4Hyg?usp=sharing)) or you can train yourself by running the `Tugas_Akhir.ipynb` program on Google Collaboratory. put the model in `static/model/your_model.h5`
```
Visual-Search-TA/
                |->static/
                |        |->data/
                |        |->dataset/
                |        |->model/
                |        |       |->model_resnet.h5
                |->templates/
                |            |->index.html
                |->connection.py
                |->data2dataset.py
                |->...
```
------------
#### **Datasets**
1. Download [`Kaggle Dataset : Real Fashion`](https://www.kaggle.com/hammaadali/real-fashion) and extract it into the `static/data/` folder
```
Visual-Search-TA/
                |->static/
                |        |->data/
                |        |       |->(Extracted data)
                |        |->dataset/
                |        |->model/
                |->templates/
                |->connection.py
                |->data2dataset.py
                |->...
```
2. After that, changing the structure of the data that originally contained a main-category, then each main-category containing sub-categories was changed to only sub-categories. Run the script `data2dataset.py`
```console
$ python data2dataset.py
```
```
Visual-Search-TA/
                |->static/
                |         |->data/
                |         |      |->dress/
                |         |      |        |->mini
                |         |      |        |->midi
                |         |      |        |->...
                |         |      |->...
                |         |->dataset/
                |         |       |->mini
                |         |       |->midi
                |         |       |->...
                |         |->model/
                |->templates/
                |->connection.py
                |->data2dataset.py
                |->...
```
3. Adding feature extraction data and images to the database. Run the script `image2db.py`
```console
$ python image2db.py
```
<p align="center">
  <strong>OR</strong>
</p>

You can skip steps 1, 2, and 3 by downloading the sql data from the export data that I did [`ta.sql`](https://drive.google.com/drive/folders/1phxIxTExRzizjwf--f81Ra_rlzSVhPPk?usp=sharing). After successfully downloading it then just import it into your database.

## **How to launch**
The program is run using the Flask web framework, to run it by running the `main.py` script.
```console
$ python main.py
```
Then we just open it in our favorite browser, [http://localhost:5000/](http://localhost:5000/) or [http://localhost:5000/index](http://localhost:5000/index), it will display the program page that is run. To stop the running Flask program, just type `Ctrl+C` at the terminal/command prompt

## **Note**
- How to get the kaggle.json used to download [Kaggle Dataset : Real Fashion](https://www.kaggle.com/hammaadali/real-fashion) is to go to https://www.kaggle.com. Then go to the [Account tab of your user profile](https://www.kaggle.com/me/account) and select Create API Token. This will trigger the download of kaggle.json, a file containing your API credentials.
- If the program doesn't work properly, you can contact me via instagram or linkedin

------------

<h3>📞📬 Stay in touch</h3>
<p>
  <a href="https://www.linkedin.com/in/yogidwiandrian/"><img alt="LinkedIn" src="https://img.shields.io/badge/linkedin-%230077B5.svg?style=for-the-badge&logo=linkedin&logoColor=white"/></a>
  <a href="https://www.instagram.com/yogidwi11/"><img alt="Instagram" src="https://img.shields.io/badge/instagram-%23E4405F.svg?style=for-the-badge&logo=Instagram&logoColor=white"/></a>
</p>
