def contains_duplicates(nums) -> bool:
    return len(set(nums)) != len(nums)


if __name__ == '__main__':
    nums = [1, 4, 2, 3]
    print(contains_duplicates(nums))