def majority_element(nums):
    # Boyer-Moore Voting Algorithm
    candidate = None
    count = 0
    for num in nums:
        if count == 0:
            candidate = num
        count += (1 if num == candidate else -1)
    return candidate

# Example usage
nums = [1, 2, 1, 1, 3, 4, 0]
print(majority_element(nums))  # Output: 1
