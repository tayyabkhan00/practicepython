def productExceptSelf(nums):
    n = len(nums)
    result = [1] * n                # 1

    prefix = 1                      # 2
    for i in range(n):              # 3
        result[i] = prefix          # 4
        prefix *= nums[i]           # 5

    suffix = 1                      # 6
    for i in range(n - 1, -1, -1):  # 7
        result[i] *= suffix         # 8
        suffix *= nums[i]           # 9

    return result                   # 10
# optimized approach (O(n) time complexity and O(1) space complexity)


# brute-force approach (O(n^2) time complexity)

def productExceptSelf(nums):
    result = []

    for i in range(len(nums)):         # choose the index to skip
        product = 1

        for j in range(len(nums)):     # multiply all other numbers
            if j != i:                 # skip the current index
                product *= nums[j]

        result.append(product)         # store the answer

    return result

