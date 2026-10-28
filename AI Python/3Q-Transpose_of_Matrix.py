# Transpose of a Matrix in Python

# Function to transpose a matrix

def transpose_matrix(matrix):
    rows = len(matrix)
    cols = len(matrix[0])
    result = [[0 for _ in range(rows)] for _ in range(cols)]

    for i in range(rows):
        for j in range(cols):
            result[j][i] = matrix[i][j]

    return result


# Example matrix
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

transposed = transpose_matrix(matrix)

print("Original Matrix:")
for row in matrix:
    print(row)

print("\nTranspose Matrix:")
for row in transposed:
    print(row)
