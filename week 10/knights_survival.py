from functools import lru_cache
moves = [(-2, -1), (-1, -2), (1, -2), (2, -1),
         (2, 1), (1, 2), (-1, 2), (-2, 1)]
def knight_probability(r, c, k):
    @lru_cache(None)
    def dp(i, j, moves_left):
        if not (0 <= i < 8 and 0 <= j < 8): 
            return 0.0
        if moves_left == 0: 
            return 1.0
        return sum(dp(i+dx, j+dy, moves_left-1) for dx, dy in moves) / 8
    return dp(r, c, k)
r, c, k = map(int, input().split())
print(knight_probability(r, c, k))
