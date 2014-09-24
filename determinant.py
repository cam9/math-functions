import copy


def det(matrix):
    determinant = 0
    for row in matrix:
        if len(row) != len(matrix):
            raise ValueError('Not a square matrix')
    if len(matrix) == 2:
        return matrix[0][0]*matrix[1][1] - matrix[0][1]*matrix[1][0]
    else:
        for i in range(len(n[0])):
            sub_determinant = d(sub_matrix(i,n))
            determinant += ((-1)**i)*(n[0][i]*sub_determinant)
    return determinant


def sub_matrix(index, matrix):
    new_matrix = copy.deepcopy(matrix)
    new_matrix.pop(0)
    for row in new_matrix:
        row.pop(index)
    return new_matrix


