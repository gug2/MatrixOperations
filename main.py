'''
Welcome to GDB Online.
GDB online is an online compiler and debugger tool for C, C++, Python, Java, PHP, Ruby, Perl,
C#, VB, Swift, Pascal, Fortran, Haskell, Objective-C, Assembly, HTML, CSS, JS, SQLite, Prolog.
Code, Compile, Run and Debug online from anywhere in world.
'''

' UTIL METHODS '
def E(size):
    matrix = []
    
    k = 0
    for i in range(size):
        matrix.append([int(j == k) for j in range(size)])
        k += 1
    
    return matrix

def printm(matrix):
    mHead(matrix)
    
    for i in range(len(matrix)):
        print('[', end=' ')
        for j in range(len(matrix[0])):
            print(fraction(matrix[i][j]), end=' ')
        print(']')

def mHead(matrix):
    name = 'matrix'
    width = len(matrix[0]) * 2 + 2 - len(name)
    
    for i in range(width // 2):
        print('-', end='')
    print(name, end='')
    for i in range(width // 2 + 1):
        print('-', end='')
    
    print()
    
from fractions import Fraction

def fraction(val):
    return Fraction(val).limit_denominator(1000)
    
' OPERATION METHODS '
def inputm(inputStr):
    matrix = []
    
    width = int(inputStr[0])
    height = int(inputStr[1])
    
    print('now enter matrix: (теперь введите матрицу:)')
    for i in range(height):
        rowStr = input().split()
        if(len(rowStr) == width):
            matrix.append([int(k) for k in rowStr])
        
    return matrix
    
def removeRow(matrix, row):
    newMatrix = []
    
    for i in range(len(matrix)):
        if i != row:
            newMatrix.append([matrix[i][j] for j in range(len(matrix[0]))])
            
    return newMatrix
    
def removeColumn(matrix, column):
    newMatrix = []
    
    for i in range(len(matrix)):
        row = []
        for j in range(len(matrix[0])):
            if j != column:
                row.append(matrix[i][j])
        newMatrix.append(row)
        
    return newMatrix
    
def det(matrix):
    detA = 0
    
    for j in range(len(matrix[0])):
        M = 0
        if len(matrix[0]) == 3:
            M += matrix[0][0] * matrix[1][1] * matrix[2][2]
            M += matrix[0][1] * matrix[1][2] * matrix[2][0]
            M += matrix[1][0] * matrix[2][1] * matrix[0][2]
            M -= matrix[0][2] * matrix[1][1] * matrix[2][0]
            M -= matrix[1][0] * matrix[0][1] * matrix[2][2]
            M -= matrix[1][2] * matrix[2][1] * matrix[0][0]
            return M
        elif len(matrix[0]) == 2:
            M = matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]
            return M
        elif len(matrix[0]) == 1:
            M = matrix[0][0]
            return M
        else:
            M = det(removeRow(removeColumn(matrix, j), 0))
            A = ((-1)**(1+j+1)) * M
            detA += matrix[0][j] * A
    
    return detA
    
def transponse(matrix):
    newMatrix = []
    
    for j in range(len(matrix)):
        newMatrix.append([matrix[i][j] for i in range(len(matrix[0]))])
        
    return newMatrix
    
def inverse(matrix):
    detA = det(matrix)
    if detA == 0:
        print('error! inverse matrix doesn\'t exist! (ошибка! обратной матрицы не существует, т.к det = 0)')
        return matrix
    
    newMatrix = []
    
    aMatrix = []
    for i in range(len(matrix)):
        aMatrix.append([((-1)**(i+1+j+1)) * det(removeRow(removeColumn(matrix, j), i)) for j in range(len(matrix[0]))])    
    
    aMatrix = transponse(aMatrix)
    
    for i in range(len(matrix)):
        newMatrix.append([1.0 / detA * aMatrix[i][j] for j in range(len(matrix[0]))])
    
    return newMatrix

' MAIN CODE '
import time

t0 = time.time()
print('enter the size of matrix: (введите размер матрицы)')

matrix = inputm(input().split())

printm(matrix)

print('det: (детерминант:)', det(matrix))
print('inverse: (обратная:)')
printm(inverse(matrix))

print('Time elapsed: ', time.time() - t0, 's.')

'задержка'
input()
