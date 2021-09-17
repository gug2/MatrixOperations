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
    
def transponse(matrix):
    newMatrix = []
    
    for j in range(len(matrix)):
        newMatrix.append([matrix[i][j] for i in range(len(matrix[0]))])
        
    return newMatrix
    
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
        print(len(matrix[0]))
        printm(matrix)
        
        M = 0
        if len(matrix[0]) == 1:
            M = matrix[0][0]
            print('endless M')
            return M
        else:
            M = det(removeRow(removeColumn(matrix, j), 0))
            print('progressive M')
            A = ((-1)**(1+j+1)) * M
            detA += matrix[0][j] * A
    
    return detA

' MAIN CODE '
print('enter the size of matrix:')

matrix = [
    [ 4, 2, 7, 6, 5, 4, 23 ],
    [ 7, 7, 7, 0, 0, 4, 3 ],
    [ 7, -9, 0, 6, 0, 5, 1 ],
    [ 8, 8, -5, 0, 0, 5, 2 ],
    [ 2, 9, 0, -3, 0, 4, 2 ],
    [ 0, 1, 0, 4, -3, -4, 1 ],
    [ 0, 0, 3, 0, 0, -2, 3 ]
]
'inputm(input().split())'

printm(matrix)

print(det(matrix))
