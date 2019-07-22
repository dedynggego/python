# -*- coding: utf-8 -*-
"""
Created on Mon Jul 22 16:29:36 2019
@author: deding
"""

from os import listdir
from PIL import Image as PImage
import numpy as np
import matplotlib.pyplot as plt
from sklearn import datasets
from sklearn import metrics
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.naive_bayes import GaussianNB
from sklearn.linear_model import LogisticRegression
from sklearn.svm import SVC
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.neural_network import MLPClassifier
from sklearn.preprocessing import LabelEncoder

def extract_color_stats(image):
    (nR, nG, nB) = image.split()
    nfeatures=[np.mean(nR),np.mean(nG), np.mean(nB), np.std(nR), np.std(nG), np.std(nB)]
    return nfeatures

le=LabelEncoder()
data_all_label= le.fit_transform(data_all_label)

(trainX, testX, trainY, testY)= train_test_split(data_all_features, data_all_label, test_size=0.25)

path = "E:/DIGITALENT SCHOLARSHIP 2019/dataset/planecar/train/"
models_name = "knn"
model= models[models_name]
model.fit(trainX, trainY)

imageList = listdir(path)
data_all_features=[]
data_all_label = []
loadedImages=[]

for image in imageList:
    img= PImage.open(path + image)
    loadedImages.append(img)
    
    label = image.split()[0]
    data_all_label.append(label)
    
    data_feature = extract_color_stats(img)
    data_all_features.append(data_feature)

models ={
"knn":KNeighborsClassifier(n_neighbors=1),
"naive_bayes":GaussianNB(),
"logistic_regresion":LogisticRegression(solver="lbfgs", multi_class="auto"),
"support_vector_machine":SVC(kernel="rbf", gamma="auto"),
"decision_tree":DecisionTreeClassifier(),
"random_forest":RandomForestClassifier(n_estimators=100),
"neural_network":MLPClassifier()      
}

#make prediction
expected = testY
predicted = model.predict(testX)

print("metrics klasifikasi report")
print(metrics.classification_report(expected, predicted, target_names = le.classes_))
print("metrics konfunsion")
print(metrics.confusion_matrix(expected, predicted))
print("metrics akurasi skor")
print(metrics.accuracy_score(expected, predicted))
