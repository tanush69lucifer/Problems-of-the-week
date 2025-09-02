def min_perfect_squares(n):
    # DP array: dp[i] = min number of squares to sum i
    dp = [float('inf')] * (n + 1)
    dp[0] = 0

    # Precompute perfect squares ≤ n
    squares = [i*i for i in range(1, int(n**0.5)+1)]

    for i in range(1, n + 1):
        for sq in squares:
            if sq <= i:
                dp[i] = min(dp[i], dp[i - sq] + 1)
            else:
                break
    return dp[n]

# Examples
print(min_perfect_squares(13))  # 2
print(min_perfect_squares(27))  # 3
print(min_perfect_squares(1))   # 1
