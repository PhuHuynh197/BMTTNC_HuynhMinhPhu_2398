input_str = input("Nhap X, Y: ")
dimension = [int (X) for X in input_str.split(",")]
rowNum = dimension[0]
colNum = dimension[1]
multilist = [[0 for col in range(colNum)] for row in range(rowNum)]
for row in range(rowNum):
    for col in range(colNum):
        multilist[row][col] = row * col
print(multilist)