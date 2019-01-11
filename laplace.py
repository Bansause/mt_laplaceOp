import numpy as np

def main():
    #mymatrix = [[1,0,0],[0,1,0],[0,0,1]]
    mymatrix = readFile("input.txt")
    print(mymatrix)
    print(mean3x3(mymatrix,0,0))

def mean3x3(matrix,i,j):
    m = len(matrix)
    n = len(matrix[0])
    val = 0
    for g in range(-1,2):
        for h in range(-1,2):
            if ((i+g) >= 0) and ((i+g) < n) and ((h+j) >= 0) and ((h+j) < m):
                val = val+matrix[i+g][j+h]
    print("n: "+str(n)+" m:"+str(m))
    return val/9

def readFile(path):
    matrix = []
    with open(path,'r') as fileHandle:
        for line in fileHandle:
            values = line.split()
            numbers = []
            for val in values:
                numbers.append(int(val))
            matrix.append(numbers)
    return matrix

main()