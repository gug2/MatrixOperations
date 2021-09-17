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

def printPreStr(valStr):
    preMatrixSpace = 10
    valStrSpace = len(valStr)
    
    for i in range((preMatrixSpace - valStrSpace) // 2):
        print(' ', end='')
    
    print(valStr, end='')
        
    for i in range((preMatrixSpace - valStrSpace) // 2 + 1):
        print(' ', end='')

def printm(matrix, *args):
    mHead(matrix)
    
    for i in range(len(matrix)):
        if len(args) == 2:
            if i == len(matrix) // 2 - 1:
                printPreStr(str(args[0]))
            elif i == len(matrix) // 2:
                printPreStr('----')
            elif i == len(matrix) // 2 + 1:
                printPreStr(str(args[1]))
            else:
                printPreStr('')
        
        print('[', end=' ')
        for j in range(len(matrix[0])):
            print(matrix[i][j], end=' ')
        print(']')

def mHead(matrix):
    width = len(matrix[0]) * 2 + 2 - 6
    
    for i in range(width // 2):
        print('-', end='')
    print('matrix', end='')
    for i in range(width // 2 + 1):
        print('-', end='')
    
    print()
    
' OPERATION METHODS '
def inputm(inputStr):
    matrix = []
    
    width = int(inputStr[0])
    height = int(inputStr[1])
    
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
    newMatrix = []
    
    aMatrix = []
    for i in range(len(matrix)):
        aMatrix.append([((-1)**(i+1+j+1)) * det(removeRow(removeColumn(matrix, j), i)) for j in range(len(matrix[0]))])    
    
    aMatrix = transponse(aMatrix)
    
    return [1, det(matrix), aMatrix]
    
' MAIN CODE '
import time

t0 = time.time()
print('enter the size of matrix:')

matrix = [
    [ 3, 2, 0, -1 ],
    [ 6, 1, 0, -1 ],
    [ 0, 6, 4, 0 ],
    [ 4, 5, -2, 1 ]
]
'inputm(input().split())'

printm(matrix)

print('det:', det(matrix))
print('inverse:')
printm(inverse(matrix)[2], inverse(matrix)[0], inverse(matrix)[1])

print('Time elapsed: ', time.time() - t0, 's.')
