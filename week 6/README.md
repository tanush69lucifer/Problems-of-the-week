Coding Problems Collection 
1. Misère Nim — Determine if First Player Has a Forced Win (Google)
Problem

Game of Nim on several heaps.

Misère variant: player who takes last stone loses.

Given three non-zero heaps [a, b, c], decide if the first player has a forced win assuming optimal play.

Approach

If all heaps are 1 → first player wins iff number of heaps is even.

Otherwise → compute XOR (nim-sum) of heap sizes:

nim-sum != 0 → first player can win

nim-sum == 0 → first player loses

Complexity

Time: O(n) for n heaps (here n=3 → O(1))

Space: O(1)

Examples

[3, 4, 5] → True

[1, 1, 1] → False

[1, 1, 2] → True

2. Minimum Number of Perfect Squares to Sum to N (Facebook)
Problem

Find smallest number of perfect squares that sum exactly to n.

Perfect squares: 1, 4, 9, 16...

Same square can be used multiple times.

Approach

Use dynamic programming:

dp[i] = minimum number of perfect squares to sum to i.

For each i, iterate over all perfect squares ≤ i and update dp[i].

Complexity

Time: O(n * √n)

Space: O(n)

Examples

Input: 13 → Output: 2 (9 + 4)

Input: 27 → Output: 3 (9 + 9 + 9)

Input: 1 → Output: 1 (1)

3. Alternating Add and Subtract (Curried Function) (Squarespace)
Problem

Implement a curried function add_subtract that alternately adds and subtracts numbers.

First number is added, second subtracted, third added, fourth subtracted, etc.

Approach

Use closure to track total and sign.

Each call updates total += sign * next_number and flips sign.

Return the inner function for chaining.

Call with empty () to get final result.

Complexity

Time: O(n) for n numbers

Space: O(1) extra space (closure)

Examples

add_subtract(7)() → 7

add_subtract(1)(2)(3)() → 0 (1 + 2 - 3)

add_subtract(-5)(10)(3)(9)() → 11 (-5 + 10 - 3 + 9)

add_subtract(5)(6)(7)() → 4 (5 + 6 - 7)