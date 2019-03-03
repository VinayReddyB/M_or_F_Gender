from sklearn import tree
X=[[38,24,38],[34,26,40],[32,24,36],[30,32,32]]
Y=['female','female','female','male']
clf=tree.DecisionTreeClassifier()
clf=clf.fit(X,Y)
prediction=clf.predict([[34,35.5,36.5]])
print(prediction)



