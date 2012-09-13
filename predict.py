import cPickle as pickle
import csv
import collections
from sklearn import svm
import time

def predict(filename):
    print 'Opening Files'
    prediction = pickle.load(open(filename,'rb'))
    X_test = pickle.load(open('X_test.p','rb'))
    print 'Loaded'
    file = open(filename.replace('.p','Results.csv'),'wb')
    for line in X_test:
        print>>file, int(prediction.predict([line])[0])
    print 'Complete'

def predictOne(filename, row = 0):
    print 'Opening Files'
    prediction = pickle.load(open(filename,'rb'))
    X_test = pickle.load(open('X_test.p','rb'))
    print 'Loaded'
    line = X_test[0]
    currentTime = time.clock()
    pred = prediction.predict([line])[0]
    print time.clock() - currentTime
    return pred
    
    
def predictMultiple(files):
    results = open('CombinedResults.csv','wb')
    predictions = []
    print 'Loading Files'
    for row in files:
        file = csv.reader(open(row))
        predictions.append(file)
        print 'Opened ' + row
    print 'Predicting Now'
    c = 0
    for i in range(28000):
        diffPredictions = []
        for predict in predictions:
            diffPredictions.append(int(predict.next()[0]))


        counted = [x for x in collections.Counter(diffPredictions).items()]
        sorty = sorted(counted, key=lambda x: x[1], reverse=True)
        if sorty[0][1] == 1:
            c += 1
        print>>results, sorty[0][0]
    print c
        
        
    
    
    
#Examples
predict('SVM.p')
predictMultiple(['SVMResults.csv','RandomForestResults.csv','NNResults.csv'])