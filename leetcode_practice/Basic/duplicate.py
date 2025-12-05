# hash map approach
nums = [1, 2, 3, 1]
def containsDuplicate(nums):
    seen = set()              # 1
    
    for num in nums:          # 2
        if num in seen:       # 3
            return True       # 4
        
        seen.add(num)         # 5
    
    return False              # 6
print(containsDuplicate(nums))  # Output: True
# complexity O(n)


# brute force approach
def containsDuplicate(nums):
    for i in range(len(nums)):              # pick one number
        for j in range(i + 1, len(nums)):   # compare with all numbers after it
            if nums[i] == nums[j]:          # if any match found
                return True                 # duplicate exists
    return False                             # no duplicates found
# complexity O(n^2)
