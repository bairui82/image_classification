from sklearn import preprocessing
lb = preprocessing.LabelBinarizer()
lb.fit([1, 2, 6, 4, 2])
lb.classes_
lb.transform([1, 6])
print(lb.transform([1, 6,5,6,7]))

