from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn import metrics
import matplotlib.pyplot as plt
import numpy as np
from mlxtend.plotting import plot_confusion_matrix

import importDataRaw

modes=['gesture','length', 'raw']
mode = int(input("0: gesture, 1: length, 2: raw: "))
version = 'v4'
trainFile = 'wristband/'+ version + '_train.xlsx'
testFile = 'wristband/'+ version + '_test.xlsx'
# print('\nimport train')
train = importDataRaw.importData(trainFile,mode)
# print('\nimport test')
test = importDataRaw.importData(testFile,mode)

# train.data.to_excel('wristband/cal/'+ version + '_train_' +  modes[mode] + '.xlsx')
# test.data.to_excel('wristband/cal/'+ version + '_test_' +  modes[mode] + '.xlsx')
print(trainFile)

x_train, x_test, y_train, y_test = train_test_split(train.features,train.labels,train_size=0.7, random_state=9999)
model = RandomForestClassifier()
model.fit(x_train, y_train)


print('\ncalibration with',modes[mode])
predictions = model.predict(x_train)
acc = metrics.accuracy_score(y_train, predictions)
print('acc: ', acc)

gestures = ['down', 'up', 'thumb', 'little finger', 'stretch', 'fist', 'rest']
predictions = model.predict(x_test)
val = metrics.accuracy_score(y_test, predictions)
print('val: ', val)
mat = metrics.confusion_matrix(y_test, predictions)
fig, ax = plot_confusion_matrix(conf_mat=mat,
                                colorbar=True,
                                show_absolute=True,
                                show_normed=True,
                                class_names=gestures,
                                figsize=(7, 6))
plt.title('Validation Confusion Matrix '+modes[mode])
plt.tight_layout()
# plt.savefig('wristband/conMat/{}_val.png'.format(modes[mode]))
# plt.show()

predictionsTest = model.predict(test.features)
accTest = metrics.accuracy_score(test.labels, predictionsTest)
print('test: ', accTest)
mat = metrics.confusion_matrix(test.labels, predictionsTest)
fig, ax = plot_confusion_matrix(conf_mat=mat,
                                colorbar=True,
                                show_absolute=True,
                                show_normed=True,
                                class_names=gestures,
                                figsize=(7, 6))
plt.title('Testing Confusion Matrix '+modes[mode])
plt.tight_layout()
# plt.savefig('wristband/conMat/{}_test.png'.format(modes[mode]))
# plt.show()


