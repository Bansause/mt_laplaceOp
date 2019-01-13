import numpy as np

def main():
    #mymatrix = [[1,0,0],[0,1,0],[0,0,1]]
    mymatrix = readFile("input.txt")
    print(mymatrix)
    print(meanFilter(mymatrix))
    print(laplaceFilter(mymatrix))

def laplaceFilter(matrix):
    resmatrix = matrix.copy()
    for i in range(0,len(matrix)):
        for j in range(0,len(matrix[0])):
            resmatrix[i,j] = laplace3x3(matrix,i,j)
    return resmatrix

def laplace3x3(matrix,i,j):
    val = 0
    for g in range(len(laplaceOp())):
        if ((i+g-1) >= 0) and ((i+g-1) < len(matrix)):
            for h in range(len(laplaceOp())):
                if ((h+j-1) >= 0) and ((h+j-1) < len(matrix[0])):
                    val = val+(matrix[i+g-1][j+h-1]*laplaceOp()[g,h])
    return int(val)


def scaleableLaplaceOp(eps):
    return np.array([[0,0,0],[0,1,0],[0,0,0]])-(eps*laplaceOp())

def laplaceOp():
    return np.array([[0,1,0],[1,-4,1],[0,1,0]])
   
def meanFilter(matrix):
    resmatrix = matrix.copy()
    for i in range(0,len(matrix)):
        for j in range(0,len(matrix[0])):
            resmatrix[i,j] = mean3x3(matrix,i,j)
    return resmatrix

def mean3x3(matrix,i,j):
    val = 0
    for g in range(-1,2):
        if ((i+g) >= 0) and ((i+g) < len(matrix)):
            for h in range(-1,2):
                if ((h+j) >= 0) and ((h+j) < len(matrix[0])):
                    val = val+matrix[i+g][j+h]
    return int(val/9)

def set_template(template,matrix,i,j):
    if (len(template) != 3) or (len(template) != 3):
        print('Input Error, template is not of format 3x3')
        return matrix
    for g in range(len(template)): #range(-1,2):
        if ((i+g-1) >= 0) and ((i+g-1) < len(matrix)):
            for h in range(len(template[g])): #range(-1,2):
                if ((h+j-1) >= 0) and ((h+j-1) < len(matrix[0])):
                    matrix[i+g-1,j+h-1] = template[g,h]


def readFile(path):
    matrix = np.loadtxt(path, dtype='i', delimiter=' ')
    return matrix

main()