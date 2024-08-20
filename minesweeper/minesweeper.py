import numpy as np

def get_neighbors_higher(matrix, row, col):
    rows, cols = matrix.shape

    for i in range(max(0, row - 1), min(rows, row + 2)):
        for j in range(max(0, col - 1), min(cols, col + 2)):
            if i == row and j == col:
                continue
            matrix[i][j]+=1
    
    return matrix

def annotate(minefield):
    temp=[]
    res=[]
    for row in minefield:
        temp.append(list(row))

    temp_matrix=np.array(temp)

    matrix_shape=temp_matrix.shape
    integer_matrix=np.zeros(matrix_shape)
            
    for i in range(matrix_shape[0]):
        for y in range(matrix_shape[1]):
            if temp_matrix[i][y]=="*":
                get_neighbors_higher(integer_matrix,i,y)

    return integer_matrix

print(annotate(["   ","** "]))