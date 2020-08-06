import os

import numpy as np
import pandas as pd

print(os.getcwd())
bc_data = pd.read_csv('bc_data.csv', header=0)  # 数据集中没有列名信息，所以header设置为0
bc_data.head()
print(bc_data.shape)  # 查看形状
print(bc_data.columns)  # 查看列名
print(bc_data.describe())  # 查看描述性统计信息
data = bc_data.drop(['id'], axis=1)
print(data.head())
x_data = data.drop(['diagnosis'], axis=1)
x_data.head()
y_data = np.ravel(data[['diagnosis']])  # np.ravel()
y_data[0:6]
from sklearn.model_selection import train_test_split

x_trainingSet, x_testSet = train_test_split(x_data)
y_trainingSet, y_testSet = train_test_split(y_data)
print(x_trainingSet.shape)
print(x_testSet.shape)
from sklearn.neighbors import KNeighborsClassifier

myModel = KNeighborsClassifier(algorithm='kd_tree')
myModel.fit(x_trainingSet, y_trainingSet)
y_predictSet = myModel.predict(x_testSet)
print(y_predictSet)
print(y_testSet)
from sklearn.metrics import accuracy_score

print(accuracy_score(y_testSet, y_predictSet))
