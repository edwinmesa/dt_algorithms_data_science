# matrix1       = [[1, 2], [3, 4]]
# matrix2       = [[5, 6], [7, 8]]
# result_matrix = [[0, 0], [0, 0]]
# ic = 0
# jc = 0
# kc = 0
# for i in range(2):
#     ic += 1
#     # print(f"{ic}:i:{i}")
#     for j in range(2):
#         jc += 1
#         # print(f"{ic}:i:{i} --{jc}: j:{j} ")
#         for k in range(2):
#             kc += 1
#             print(f"{ic}:i: {i} --{jc}: j: {j} -- {kc}:k {k}")

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


def selection_sort(arr):
    array_i = []
    array_j = []
    ic    = 0
    jc    = 0
    for i in range(len(arr)): # i = 6
        ic += 1
        # print(f"{ic}:i:{i}")
        min_index = i
        for j in range(i + 1, len(arr)): # (7, 6)
            jc += 1
            array_j.append(j)
            array_i.append(i)
            # print(f"{ic}:i:{i} --{jc}: j:{j} ")
            # print(j)
    return array_j, array_i

# Example usage
array        = [64, 34, 25, 12, 22, 11, 90]
sorted_array = selection_sort(array)


