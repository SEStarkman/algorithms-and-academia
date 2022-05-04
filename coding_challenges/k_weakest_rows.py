def k_weakest_rows(mat, k):

    weakest_indicies = []
    traversing_index = 0
    while k > 0:
        for index, row in enumerate(mat):
            if (row[traversing_index] == 0 and index not in weakest_indicies):
                weakest_indicies.append(index)
                # mat.pop(index)
                k -= 1
                break
        traversing_index += 1


    return weakest_indicies


if __name__ == '__main__':
    k = 5
    mat = [[1,1,0,0,0],
        [1,1,1,1,0],
        [1,0,0,0,0],
        [1,1,0,0,0],
        [1,1,1,1,1]]

    print(k_weakest_rows(mat, k))

    mat2 = [[1,0,0,0],
        [1,1,1,1],
        [1,0,0,0],
        [1,0,0,0]]
    k2 = 2

    print(k_weakest_rows(mat2, k2))