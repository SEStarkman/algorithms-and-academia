def max_sub_array(nums):
    max_sum = 0
    current_sum = 0

    for i in nums:
        if current_sum < 0:
            current_sum = 0
        current_sum += i
        max_sum = max(current_sum, max_sum)

    return max_sum

    
if __name__ == '__main__':
    nums = [-2,1,-3,4,-1,2,1,-5,4]
    print(max_sub_array(nums))