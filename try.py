import numpy as np

a = np.array([(1,2,3),(4,5,6)])


def twoMaxes(L):
    row = []
    for i in range(len(a[0])):
        row.append(max(a[:,i]))

    column = []
    for j in range(len(a[:,0])):
        column.append(max(a[j]))
    print(row)
    print(column)

twoMaxes(a)