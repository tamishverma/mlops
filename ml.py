from sklearn.ensemble import RandomForestClassifier
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import pandas as pd
import pickle

iris = load_iris()
x = iris.data
y = iris.target

x_train, x_test, y_train, y_test = train_test_split(x, y, random_state=42, test_size=0.5)

#Build model
clf = RandomForestClassifier(n_estimators=10)

#Train classifier
clf.fit(x_train, y_train)

predicted = clf.predict(x_test)

#check accuracy

print(accuracy_score(predicted, y_test))


with open(r'C:\Users\tamis\Desktop\MLOPS\rf.pkl','wb') as model_pkl:
    pickle.dump(clf, model_pkl)
