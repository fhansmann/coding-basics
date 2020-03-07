
tableData = [['apples', 'oranges', 'cherries', 'banana'],
             ['Alice', 'Bob', 'Carol', 'David'],
             ['dogs', 'cats', 'moose', 'goose']]


def printTable(listOfLists):
    # the widest words of each column
    colWidths = [0] * len(tableData[0])
    for i in colWidths:
        i = 0

    # calculate width for each column
    for i in range(len(tableData[0])):
        for listt in tableData:
            if len(listt[i]) > colWidths[i]:
                colWidths[i] = len(listt[i]) + 1

    for i in colWidths:
        print(i)

    for i in range(len(tableData)):
        for j in range(len(tableData[0])):
            print(tableData[i][j].rjust(colWidths[j]), end='')
        print('')

    print(''* 5)

    # list by list columns
    colWidths2 = [0] * len(tableData[0])

    for i in range(len(tableData)):
        for j in range(len(tableData[0])):
            if len(tableData[i][j]) > colWidths2[i]:
                colWidths2[i] = len(tableData[i][j])+1

    for i in range(len(tableData[0])):
        for j in range(len(tableData)):
            print(tableData[j][i].rjust(colWidths2[j]), end='')
        print('')


printTable(tableData)
