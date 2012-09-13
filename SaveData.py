import sklearn

import cPickle as pickle

train = open('train.csv','rb')
y_train = []
X_train = []
i = 0
for line in train:
    if i == 0:
        i += 1
        continue
    lineSplit = line.split(',')
    y_train.append(lineSplit[0])
    X_train.append(lineSplit[1:])
    
print X_train[0]
print y_train[0]
pickle.dump(y_train,open('y_train.p','wb'))
pickle.dump(X_train,open('X_train.p','wb'))

train = open('test.csv','rb')
X_test = []
i = 0
for line in train:
    if i == 0:
        i += 1
        continue
    lineSplit = line.split(',')
    X_test.append(lineSplit)
    
print X_test[0]
pickle.dump(X_test,open('X_test.p','wb'))