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
def inputm():
    print('enter the size of matrix: (введите размер матрицы)')
    
    matrix = []
    
    inputStr = input().split()
    width = int(inputStr[0])
    height = int(inputStr[1])
    
    print('now enter matrix: (теперь введите матрицу:)')
    for i in range(width):
        rowStr = input().split()
        if(len(rowStr) == height):
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
    
    if len(matrix) != len(matrix[0]):
        print('error! matrix isn\'t square! (матрица не квадратная!)')
        return None
    
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
    
    for j in range(len(matrix[0])):
        newMatrix.append([matrix[i][j] for i in range(len(matrix))])
        
    return newMatrix
    
def inverse(matrix):
    detA = det(matrix)
    if detA == 0:
        print('error! inverse matrix doesn\'t exist! (обратной матрицы не существует, т.к det = 0)')
        return None
    
    newMatrix = []
    
    aMatrix = []
    for i in range(len(matrix)):
        aMatrix.append([((-1)**(i+1+j+1)) * det(removeRow(removeColumn(matrix, j), i)) for j in range(len(matrix[0]))])    
    
    aMatrix = transponse(aMatrix)
    
    for i in range(len(matrix)):
        newMatrix.append([1.0 / detA * aMatrix[i][j] for j in range(len(matrix[0]))])
    
    return newMatrix

def dot(m1, m2):
    newM = []
    
    if len(m1[0]) != len(m2):
        print('error! dot isn\'t possible! (умножение невозможно!)')
        return None
    
    for j2 in range(len(m2[0])):
        newM.append([ sum([ m1[i1][j1] * m2[j1][j2] for j1 in range(len(m1[0])) ]) for i1 in range(len(m1)) ])
    
    newM = transponse(newM)
    
    return newM

' MAIN CODE '
import time

t0 = time.time()

print('Operation codes (коды операций):')
print('Find det and inverse matrix (найти свойства матрицы (определитель, обратная)) -', 0)
print('Find dot of 2 matrices(найти произведение матриц) -', 1)
operationCode = int(input())

if(operationCode == 0):
    matrix = inputm()
    printm(matrix)
    print('Det (детерминант): ', det(matrix))
    print('Inverse (обратная): ')
    printm(inverse(matrix))
elif(operationCode == 1):
    m1 = inputm()
    m2 = inputm()
    print('Dot product (результирующая матрица): ')
    printm(dot(m1, m2))

print('Time elapsed: ', time.time() - t0, 's.')

'задержка'
'input()'
