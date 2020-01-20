def add(*matrices):
    rows, cols = len(matrices[0]), len(matrices[0][0])

    # Check all matrices have the same number of rows
    if not all(len(matrix) == rows for matrix in matrices):
        raise ValueError("Given matrices are not the same size.")

    # Check all rows have the same number of columns
    if not all(len(row) == cols for matrix in matrices for row in matrix):
        raise ValueError("Given matrices are not the same size.")

    return [[sum(x) for x in zip(*pair)] for pair in zip(*matrices)]
