Coding Problems Collection
1. Validate Number in a String (LinkedIn)
Problem

Check if a given string is a valid number.
Valid inputs: integers, decimals, scientific notation.
Invalid inputs: ".", "1e", "e9", "a", "1 2".

Approach

Trim spaces.

Use flags: seen_digit, seen_dot, seen_exp, digit_after_exp.

Apply parsing rules in one pass.

Complexity

Time: O(n)

Space: O(1)

Edge Cases

✅ "10", "-10.1", "1e5", "3.", " .1", " -90e3 "
❌ ".", "1e", "e9", "+", "1 2"

2. Maximum Path Sum Between Any Two Nodes in a Binary Tree (Google)
Problem

Given a binary tree, find the maximum path sum between any two nodes.
The path must include at least one node but doesn’t need to pass through the root.

Approach

Use post-order DFS traversal.

For each node:

Compute max path from left and right (ignore negatives).

Update global max using node.val + left + right.

Return node.val + max(left, right) for recursion.

Complexity

Time: O(N) (visit each node once)

Space: O(H) (recursion stack, H = tree height)

Example

Tree:

    -10
    /  \
   9   20
      /  \
     15   7


Output: 42 (path 15 → 20 → 7)

3. Prime Numbers with Multiple Occurrences (KPIT)
Problem

From an array, find all prime numbers that occur more than once.
Return them in the order of first appearance. If none, return -1.

Approach

Check primality (O(√n)).

Use frequency map to count primes.

Collect primes with frequency > 1 in order.

Complexity

Time: O(N√M) where M = max value in array.

Space: O(N) for frequency map.

Examples

Input: 10 → [2, 3, 5, 7, 11, 3, 2, 15, 17, 5]
Output: 2 3 5

Input: 6 → [4, 6, 8, 9, 10, 12]
Output: -1