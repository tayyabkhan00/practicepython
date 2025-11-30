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

# 3. Two-Pointer Technique (Requires Sorted Array — O(n log n) due to sorting)
def twoSum(nums, target):
    nums_with_indices = list(enumerate(nums))
    nums_with_indices.sort(key=lambda x: x[1])
    
    left, right = 0, len(nums) - 1
    while left < right:
        current_sum = nums_with_indices[left][1] + nums_with_indices[right][1]
        if current_sum == target:
            return [nums_with_indices[left][0], nums_with_indices[right][0]]
        elif current_sum < target:
            left += 1
        else:
            right -= 1
print(twoSum([2, 7, 11, 15], 9))

# 4. Using Set for Lookup (Alternative Optimized Method — O(n))
def twoSum(nums, target):
    seen = set()
    for i, num in enumerate(nums):
        complement = target - num
        if complement in seen:
            return [nums.index(complement), i]
        seen.add(num)
print(twoSum([2, 7, 11, 15], 9))

# 5. Using List Comprehension (Concise but Less Efficient — O(n²))
def twoSum(nums, target):
    return next(([i, j] for i in range(len(nums)) for j in range(i + 1, len(nums)) if nums[i] + nums[j] == target), None)
print(twoSum([2, 7, 11, 15], 9))

# 6. Using itertools.combinations (Functional Approach — O(n²)) 
import itertools
def twoSum(nums, target):
    for i, j in itertools.combinations(range(len(nums)), 2):
        if nums[i] + nums[j] == target:
            return [i, j]
print(twoSum([2, 7, 11, 15], 9))

# 7. beginner_methods to take input from user and print output
arr = list(map(int, input("Enter numbers: ").split()))
target = int(input("Enter target: "))

for i in range(len(arr)):
    for j in range(i + 1, len(arr)):
        if arr[i] + arr[j] == target:
            print(i, j)

