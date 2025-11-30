# 1. Brute Force (Beginner Method — O(n²))
def twoSum(nums, target):
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] + nums[j] == target:
                return [i, j]
print(twoSum([2, 7, 11, 15], 9))

# 2. Hash Map (Optimized Method — O(n))
def twoSum(nums, target):
    num_map = {}
    for i, num in enumerate(nums):
        complement = target - num
        if complement in num_map:
            return [num_map[complement], i]
        num_map[num] = i
print(twoSum([2, 7, 11, 15], 9))