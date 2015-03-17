import copy


def det(matrix):
    determinant = 0
    if not(is_square(matrix)):
            raise ValueError('Not a square matrix')

    if len(matrix) == 2:
        return matrix[0][0]*matrix[1][1] - matrix[0][1]*matrix[1][0]
    else:
        for i in range(len(matrix[0])):
            sub_determinant = det(sub_matrix(i,matrix))
            determinant += ((-1)**i)*(matrix[0][i]*sub_determinant)
    return determinant


def sub_matrix(index, matrix):
    new_matrix = copy.deepcopy(matrix)
    new_matrix.pop(0)
    for row in new_matrix:
        row.pop(index)
    return new_matrix


def is_square(matrix):
    for row in matrix:
        if len(row) != len(matrix):
            return False
    return True


print det([
    [1,5,-3],[3,-3,3],[2,13,-7]
])

