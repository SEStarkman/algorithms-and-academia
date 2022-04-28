from operator import index


def find_median_sorted_array(nums1, nums2):
    i = j = k = 0

    combined_array = []

    while i < len(nums1) and j < len(nums2):
        if nums1[i] < nums2[j]:
            combined_array.insert(k, nums1[i])
            i += 1
        else:
            combined_array.insert(k, nums2[j])
            j += 1
        k += 1

    while i < len(nums1):
        combined_array.insert(k, nums1[i])
        i += 1
        k += 1

    while j < len(nums2):
        combined_array.insert(k, nums2[j])
        j += 1
        k += 1

    print(combined_array)

    # if odd, //2 and that is index of median, if even, //2 - 1 is index

    if len(combined_array)//2 == len(combined_array)/2: # even
        median_index = len(combined_array) // 2
        med = (combined_array[median_index - 1] + combined_array[median_index]) / 2
    else: # odd
        median_index = len(combined_array) // 2
        med = combined_array[median_index]


    return med


if __name__ == '__main__':
    nums1 = [1, 3, 7, 8]
    nums2 = [2, 4, 5, 8]

    print(find_median_sorted_array(nums1, nums2))