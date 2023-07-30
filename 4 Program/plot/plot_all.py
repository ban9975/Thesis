import matplotlib.pyplot as plt
import pandas as pd
import sys

if len(sys.argv) < 3:
    print('No arguments.')
    sys.exit()
else:
    fileName = sys.argv[1]
    sheetName = sys.argv[2]
xls = pd.read_excel(fileName, sheet_name=sheetName)

while(True):
    _start=list(map(int,input('_start = ').split()))
    _end=list(map(int,input('_end = ').split()))
    _sets, _lines = map(int, input('_sets, _lines = ').split())
    data=[]
    axis_x=[]
    labels=[]
    for k in range(_lines):
        rows = list(range(_start[k]-2, _end[k]-1))
        # rubber sheet, conductive jersey (fixed length, different width)
        # labels.append('W{}'.format(xls[xls.columns[0]][rows[0]-1])) 
        # rubber sheet, conductive jersey (fixed width, different length)
        # labels.append('L{}'.format(xls[xls.columns[1]][rows[0]-1])) 
        # rubber cord
        labels.append('L{}'.format(xls[xls.columns[0]][rows[0]]))
        data.append([0] * len(rows))
        axis_x.append([0] * len(rows))
        for i in range(len(rows)):
            # overall length + stretch, angle
            axis_x[k][i] = xls[xls.columns[0]][rows[i]] 
            # overall stretch
            # axis_x[k][i] = xls[xls.columns[0]][rows[i]]-xls[xls.columns[0]][rows[0]] 
            for j in range(_sets):
                # print(k,i)
                # conductive rubber cord
                data[k][i] += xls[xls.columns[1+j]][rows[i]] 
                # rubber sheet, conductive jersey
                # data[k][i] += xls[xls.columns[3+j]][rows[i]]
            data[k][i]/=_sets
    
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
    plt.savefig('../../5 Result/rubberCord/{}.png'.format(plotName))
    plt.show()
    

    if input('Press y to draw next plot: ') != 'y':
        break