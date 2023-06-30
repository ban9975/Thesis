import matplotlib.pyplot as plt
import pandas as pd
import sys
import math
mode=int(input('mode: '))
modes=['gesture','length','raw']
version = 'v4'
trainName = 'wristband/cal/'+version+'_train_'+modes[mode]+'.xlsx'
testName = 'wristband/cal/'+version+'_test_'+modes[mode]+'.xlsx'
sheetName = "Sheet1"
plotName = version+'_'+modes[mode]
train = pd.read_excel(trainName, sheet_name=sheetName)
test = pd.read_excel(testName, sheet_name=sheetName)

# plotting
for i in range(4):
    plt.figure()
    if mode==0:
        plt.xlim(-150,150)
    elif mode==1:
        plt.xlim(-0.02,0.02)
    elif mode==2:
        plt.xlim(200,500)
    elif mode==3:
        plt.xlim(-130,130)
    elif mode==4:
        plt.xlim(-100,100)
    plt.scatter(train[i],train['gesture'], marker='.',label='train')
    plt.scatter(test[i],test['gesture'], marker='.',label='test')
    plt.title(plotName+'_{}'.format(i))
    plt.legend()
    plt.ylabel('gesture')
    plt.xlabel('calibration with '+modes[mode]+' data')
    plt.grid(True)
    plt.savefig('wristband/cal/plot/'+plotName+'_{}'.format(i)+'.png')
