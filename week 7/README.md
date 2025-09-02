1. Find the Majority Element (MongoDB)
Problem

Given a list of integers, find the majority element, i.e., the element appearing more than ⌊n/2⌋ times.

You can assume such an element always exists.

Approach

Boyer–Moore Majority Vote Algorithm:

Initialize candidate and count = 0.

Traverse the list:

If count == 0, set candidate = current element.

If element == candidate → count += 1; else count -= 1.

Return candidate.

Complexity

Time: O(n)

Space: O(1)

Example

Input: [1, 2, 1, 1, 3, 4, 0] → Output: 1

2. Maximum Removable Edges for Even Tree (Adobe)
Problem

Given a tree with an even number of nodes, remove the maximum number of edges such that every resulting subtree has an even number of nodes.

Approach

Use DFS to compute subtree sizes:

Traverse tree from root.

For each child, compute its subtree size.

If subtree size % 2 == 0, edge can be removed.

Count such removable edges.

Complexity

Time: O(N)

Space: O(N) (adjacency list + recursion stack)

Example

Input:

8
1 2
1 3
3 4
3 5
4 6
4 7
4 8


Output: 2

3. Reverse Words with Delimiters (Facebook)
Problem

Reverse words in a string while keeping delimiters in their original positions.

Words contain lowercase letters; delimiters can be /, :, etc.

Approach

Split + Reconstruct using regex:

Split string into words and delimiters (re.findall).

Reverse the words list.

Reconstruct string by placing reversed words and original delimiters.

Complexity

Time: O(n)

Space: O(n)

Examples

"hello/world:here" → "here/world:hello"

"hello/world:here/" → "here/world:hello/"

"hello//world:here" → "here//world:hello"