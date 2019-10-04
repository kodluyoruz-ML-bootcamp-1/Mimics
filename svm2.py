import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
def warn(*args, **kwargs):
    pass
import warnings
warnings.warn = warn

data = pd.read_csv("ds.csv")
df = pd.DataFrame(data)

x,y = data.loc[:,data.columns != 'emotion'], data.loc[:,'emotion']
def splitTestTrain():
    return train_test_split(x, y, test_size = 0.2, random_state = 42)

model = SVC()
x_train, x_test, y_train, y_test = splitTestTrain()
model.fit(x_train, y_train)
model.score(x_test, y_test)

#Tune_Parameters

#Regularization (C)
model_C = SVC(C=1)
model_C.fit(x_train, y_train)
model_C.score(x_test, y_test)
print(model_C.score(x_test, y_test))

model_C = SVC(C=10)
model_C.fit(x_train, y_train)
model_C.score(x_test, y_test)
print(model_C.score(x_test, y_test))

#Gamma
model_g = SVC(gamma=10)
model_g.fit(x_train, y_train)
model_g.score(x_test, y_test)
print(model_g.score(x_test, y_test))

#Kernel
model_linear_kernal = SVC(kernel='linear')
model_linear_kernal.fit(x_train, y_train)
model_linear_kernal.score(x_test, y_test)
print(model_linear_kernal.score(x_test, y_test))