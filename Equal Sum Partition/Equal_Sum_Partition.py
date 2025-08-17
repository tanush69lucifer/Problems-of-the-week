# Technique 1 
def can_partition(nums):
    total = sum(nums)
    if total % 2 != 0:  # odd sum can't be split
        return False

    target = total // 2
    dp = [False] * (target + 1)
    dp[0] = True

    for num in nums:
        for j in range(target, num - 1, -1):
            dp[j] = dp[j] or dp[j - num]

    return dp[target]

# Technique 2 using tricks 
def can_partition(nums):
    s = sum(nums)
    if s % 2: return False
    target, dp = s // 2, {0}
    for n in nums:
        dp |= {x + n for x in dp if x + n <= target}
    return target in dp
  
# Technique 3 golfed version
def can_partition(a):
    s,dp=sum(a),{0}
    return not s%2 and (s//2 in (dp:={*dp}|{x+n for x in dp for n in a}))

# Technique 4 using set
def can_partition(nums):
    s = sum(nums)
    if s % 2:      # odd sum → impossible
        return False
    target = s // 2

    # dp holds all possible subset sums
    dp = {0}
    for n in nums:
        dp |= {x + n for x in dp if x + n <= target}  # add n to all existing sums

    return target in dp


# Test Cases
print(can_partition([15, 5, 20, 10, 35, 15, 10]))  # True
print(can_partition([15, 5, 20, 10, 35]))          # False


