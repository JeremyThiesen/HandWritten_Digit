import sklearn
import cPickle as pickle
from sklearn.linear_model import SGDClassifier
from sklearn import neighbors
from sklearn.ensemble import RandomForestClassifier
from sklearn.multiclass import OneVsRestClassifier
from sklearn.multiclass import OutputCodeClassifier
from sklearn.svm import LinearSVC
import numpy as np
print 'Loading Files'
X_train = pickle.load(open('X_train.p','rb'))
y_train = pickle.load(open('y_train.p','rb'))

X = X_train
y = y_train

def SGD():
    prediction = SGDClassifier(loss="hinge", penalty="l2").fit(X,y)
    print 'Now Saving'
    pickle.dump(prediction,open('SGD.p','wb'))


def nearestNeighbors():
    prediction = neighbors.KNeighborsClassifier(10, weights='distance').fit(X,y)
    print 'Now Saving'
    pickle.dump(prediction,open('NN.p','wb'))
    
def RandomForest():
    clf = RandomForestClassifier(n_estimators=1000)
    print 'Now Fitting'
    clf = clf.fit(X,y)
    pickle.dump(clf,open('RandomForest.p','wb'))
    
def OneVsTheRest():
    prediction = OneVsRestClassifier(LinearSVC()).fit(X,y)
    print 'Now Saving'
    pickle.dump(prediction,open('OVR.p','wb'))  
    
def OCC():
    prediction = OutputCodeClassifier(LinearSVC(),code_size=2).fit(np.array(X),np.array(y))
    print 'Now Saving'
    pickle.dump(prediction,open('OCC.p','wb')) 
    
def SVM():
    prediction = svm.SVC(kernel='poly').fit(X, y)
    print 'Now Saving'
    pickle.dump(prediction,open('SVM.p','wb'))
    

print 'Calculating'
RandomForest()