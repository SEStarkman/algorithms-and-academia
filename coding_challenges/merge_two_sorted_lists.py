# Pseudocode
# take list1
# for each element i in list2
# if list2[i] <= 

def merge_two_lists(list1, list2):
    sorted_list = list1

    for i, val in enumerate(list1):
        for j, val in enumerate(list2):
            if list2[j] <= list1[i]:
                sorted_list.insert(i, list2[j])

    return sorted_list


if __name__ == '__main__':
    list1 = [1, 2, 4]
    list2 = [1, 3, 4]

    print(merge_two_lists(list1, list2))