import copy

def d(n):
    determinant = 0
    for i in n:
        if len(i) != len(n):
            return False
    if len(n) == 2:
        return n[0][0]*n[1][1] - n[0][1]*n[1][0]
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

print d([
    [1,2,3,4,5,6,7],
    [1,2,3,4,5,6,7],
    [1,2,3,4,5,6,7],
    [1,2,3,4,5,6,7],
    [1,2,3,4,5,6,7],
    [1,2,3,4,5,6,7],
    [1,2,3,4,5,6,7],
])