nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
def maxSubArray(nums):
    current_sum = nums[0]     # 1
    max_sum = nums[0]         # 2

    for num in nums[1:]:      # 3
        current_sum = max(num, current_sum + num)  # 4
        max_sum = max(max_sum, current_sum)        # 5
    
    return max_sum            # 6

print(maxSubArray(nums))  # Output: 6)
# complexity O(n)


# ---------------- EXTENDED FUNCTIONALITY ---------------- #

def maxSubArray(nums):
    current_sum = nums[0]
    max_sum = nums[0]

    start = 0        # temp start index
    end = 0          # final end index of best subarray
    best_start = 0   # final start index

    for i in range(1, len(nums)):
        if nums[i] > current_sum + nums[i]:
            current_sum = nums[i]
            start = i
        else:
            current_sum = current_sum + nums[i]

        if current_sum > max_sum:
            max_sum = current_sum
            best_start = start
            end = i

    return max_sum, nums[best_start:end+1]   # return sum and the actual subarray
# complexity O(n)


# ---------------- USER INPUT SECTION ---------------- #

# Take input from user (space-separated integers)
nums = list(map(int, input("Enter numbers separated by space: ").split()))

max_sum, subarray = maxSubArray(nums)

print("Maximum Subarray Sum:", max_sum)
print("Maximum Subarray:", subarray)


# brute force approach
arr = [1, -3, 2, 1, -1]

max_sum = float('-inf')

for i in range(len(arr)):                 # start of subarray
    for j in range(i, len(arr)):          # end of subarray
        sub_sum = sum(arr[i:j+1])         # sum of arr[i..j]
        
        if sub_sum > max_sum:             # update max
            max_sum = sub_sum

print(max_sum)
# complexity O(n^3)