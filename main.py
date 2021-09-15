'''

Welcome to GDB Online.
GDB online is an online compiler and debugger tool for C, C++, Python, Java, PHP, Ruby, Perl,
C#, VB, Swift, Pascal, Fortran, Haskell, Objective-C, Assembly, HTML, CSS, JS, SQLite, Prolog.
Code, Compile, Run and Debug online from anywhere in world.

'''
def E(size):
    e = []
    k = 0
    for i in range(size):
        e.append([int(j == k) for j in range(size)])
        k += 1
        
    return e

def removeRow(matrix, iR):
    newMatrix = []
    
    for i in range(len(matrix)):
        if(i != iR):
            newMatrix.append([matrix[i][j] for j in range(len(matrix[0]))])
    
    return newMatrix
    
def removeColumn(matrix, jR):
    newMatrix = []
    
    for i in range(len(matrix)):
        row = []
        for j in range(len(matrix[0])):
            if j != jR:
                row.append(matrix[i][j])
        newMatrix.append(row)
    
    return newMatrix

def minor(matrix):
    minor = 0
    
    if len(matrix) != len(matrix[0]):
        print('error! matrix isn\'t square!')
        return matrix
        
    if(len(matrix) == 1):
        minor = matrix[0][0]
    if(len(matrix) == 2):
        minor = matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]
    if(len(matrix) == 3):
        minor += matrix[0][0] * matrix[1][1] * matrix[2][2]
        minor += matrix[1][0] * matrix[2][1] * matrix[0][2]
        minor += matrix[0][1] * matrix[1][2] * matrix[2][0]
        minor -= matrix[0][2] * matrix[1][1] * matrix[2][0]
        minor -= matrix[0][1] * matrix[1][0] * matrix[2][2]
        minor -= matrix[1][2] * matrix[2][1] * matrix[0][0]
    else:
        print('error! size > 3!', 'len matrix:', len(matrix))
        
    return minor

def det(matrix):
    detA = 0
    if len(matrix) != len(matrix[0]):
        print('error! matrix isn\'t square!')
        return matrix
        
    for j in range(len(matrix[0])):
        A0j = -1**(1+j+1) * minor(removeRow(removeColumn(matrix, j), 0))
        detA += matrix[0][j] * A0j
        
    return detA

def transponse(matrix):
    newMatrix = []
    for j in range(len(matrix[0])):
        newMatrix.append([matrix[i][j] for i in range(len(matrix))])
            
    return newMatrix

def printm(matrix):
    print('--matrix', len(matrix), 'x', len(matrix[0]), '--')
    for i in range(len(matrix)):
        print('[', end=' ')
        for j in range(len(matrix[0])):
            print(matrix[i][j], end=' ')
        print(']')

print('enter size of matrix in format \'m x n\'')
m, n = [int(a) for a in input().split()]

matrix = []

for i in range(m):
    print('print ', i, ' line: ', end='')
    matrix.append([int(a) for a in input().split()])

printm(matrix)
print(det(matrix))
