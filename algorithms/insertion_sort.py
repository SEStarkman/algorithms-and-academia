def insertion_sort(arr):
    for i in range(1, len(arr)):

        key = arr[i]

        j = i - 1

        while key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        
        arr[j + 1] = key

    print(arr)


if __name__ == '__main__':
    arr = [2, 5, 3, 10, 11, 7]

    insertion_sort(arr)