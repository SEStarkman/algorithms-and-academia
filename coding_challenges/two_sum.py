def two_sum_brute_force(nums, target):
    for i in range(0, len(nums)):
        val1 = nums[i]
        for j in range(i + 1, len(nums)):
            val2 = nums[j]
            if val1 + val2 == target:
                return [i, j]
    
    return "NO SOLUTION"

def two_sum_hash_map(nums, target):
    seen = {}
    for i in range(0, len(nums)):
        remaining = target - nums[i]
        if remaining in seen:  
            return [seen[remaining], i]
        else:
            seen[nums[i]] = i


if __name__ == '__main__':
    nums = [2, 7, 11, 15]
    target = 22
    print(two_sum_hash_map(nums, target))