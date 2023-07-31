# matrix1       = [[1, 2], [3, 4]]
# matrix2       = [[5, 6], [7, 8]]
# result_matrix = [[0, 0], [0, 0]]

for i in range(2):
    print(f"i:{i}")
    for j in range(2):
        print(f"i:{i} -- j:{j} ")
        for k in range(2):
            print(f"i:{i} -- j:{j} -- k:{k}")

# matrix1       = [[1, 2], [3, 4]]
# matrix2       = [[5, 6], [7, 8]]
# result_matrix = [[0, 0], [0, 0]]

# for i in range(2):
#     for j in range(2):
#         for k in range(2):
#             print(result_matrix[i], "+="," m1:i",matrix1[i], "->","m2:k", matrix2[k])
#             print(result_matrix[j], "+="," m1:k", matrix1[k], "->","m2:j", matrix2[j])
#             print(result_matrix[i][j], "+=", matrix1[i][k], "->", matrix2[k][j])

#             result_matrix[i][j] += matrix1[i][k] * matrix2[k][j]

# print("Matrix Multiplication Result:")
# for row in result_matrix:
#     print(row)