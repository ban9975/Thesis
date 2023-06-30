import matplotlib.pyplot as plt
import pandas as pd
import sys

if len(sys.argv) < 3:
    print('No arguments.')
    sys.exit()
else:
    fileName = sys.argv[1]
    sheetName = sys.argv[2]
    print(fileName)
    print(sheetName)
xls = pd.read_excel(fileName, sheet_name=sheetName)

while(True):
    _start=list(map(int,input('_start=').split()))
    _end=list(map(int,input('_end=').split()))
    _sets, _lines = map(int, input('_sets , _lines= ').split())
    data=[]
    axis_x=[]
    labels=[]
    for k in range(_lines):
        rows = list(range(_start[k]-2, _end[k]-1))
        # labels.append('W{}'.format(xls[xls.columns[0]][rows[0]-1]))
        labels.append('L{}'.format(xls[xls.columns[0]][rows[0]]))
        print(labels[k])
        # print(rows)
        data.append([0] * len(rows))
        axis_x.append([0] * len(rows))
        for i in range(len(rows)):
            axis_x[k][i] = xls[xls.columns[0]][rows[i]] #overall length + stretch
            # axis_x[k][i] = xls[xls.columns[0]][rows[i]]-xls[xls.columns[0]][rows[0]] #overall stretch
            # print(axis_x[k][i])
            for j in range(_sets):
                # print(k,i)
                data[k][i] += xls[xls.columns[1+j]][rows[i]]
                # print(xls[xls.columns[3+j]][rows[i]], end = ' ')
            data[k][i]/=_sets
            # print('')
    
    # plotting
    plotName = input('plotName = ')
    for i in range(_lines):
        plt.plot(axis_x[i], data[i], marker = '.', label=labels[i])
    plt.title(plotName)
    plt.ylabel('Resistance (Ohm)')
    # plt.xlabel('Stretch (cm)')
    plt.xlabel('Length + Stretch (cm)')
    # plt.xlabel('Aangle (deg)')
    plt.legend()
    plt.grid(True)
    plt.savefig('rubberCord/plot/{}.png'.format(plotName))
    plt.show()
    

    if input('Press y to draw next plot: ') != 'y':
        break