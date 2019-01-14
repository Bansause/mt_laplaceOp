import matplotlib.pyplot as plt
from matplotlib import colors
from matplotlib.colors import NoNorm
import numpy as np

def main():
    mymatrix = readFile("input.txt")
    plot(mymatrix,'raw')
    plot(meanFilter(mymatrix),'mean')
    laplace_mat = laplaceFilter(mymatrix)
    plot(laplace_mat,'laplace')
    print(getGrayDistance(mymatrix,laplace_mat))
    plot(laplace_mat,'laplace')
    plot(scalebleLaplaceFilter(mymatrix,2),'laplace2')

def scalebleLaplaceFilter(matrix,eps):
    resmatrix = matrix.copy()
    for i in range(0,len(matrix)):
        for j in range(0,len(matrix[0])):
            resmatrix[i,j] = scaleableLaplace3x3(matrix,i,j,eps)
    return normalize(resmatrix)

def scaleableLaplace3x3(matrix,i,j,eps):
    val = 0
    for g in range(len(laplaceOp())):
        if ((i+g-1) >= 0) and ((i+g-1) < len(matrix)):
            for h in range(len(laplaceOp())):
                if ((h+j-1) >= 0) and ((h+j-1) < len(matrix[0])):
                    val = val+(matrix[i+g-1][j+h-1]*scaleableLaplaceOp(eps)[g,h])
    #Negative Werte nullen?
    #Werte über 100 auf 100 begrenzen?
    #return limit(val,0,100)
    return val

def scaleableLaplaceOp(eps):
    return np.array([[0,0,0],[0,1,0],[0,0,0]])-(eps*laplaceOp())

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
    #return limit(val,0,100)
    return int(val)

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

def getGrayDistance(A,B):
    x = 0
    y = 0
    dist = 0
    C = abs(A-B)
    dist = C.max()
    idx = np.argmax(C)
    x = (idx % 10) + 1
    y = int(idx / 10) + 1
    return (dist,x,y)


def plot(matrix,name):
    writeFile(matrix,name)
    plt.matshow(np.transpose(matrix), cmap="gray")
    plt.savefig(name+'.pdf')


def normalize(matrix):
    max = matrix.max()
    min = matrix.min()
    for i in range(len(matrix)):
        for j in range(len(matrix)):
            matrix[i,j] = int(np.interp(matrix[i,j],[min,max],[0,100]))
    return matrix


def limit(val,min,max):
    result = int(val)
    if result <= min:
        return min
    if result >= max:
        return max
    return result

def writeFile(matrix,path):
    np.savetxt(path+'.mat',matrix, delimiter=' ', fmt='%i')

def readFile(path):
    matrix = np.loadtxt(path, dtype='i', delimiter=' ')
    return matrix

main()