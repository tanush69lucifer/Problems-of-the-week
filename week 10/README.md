WEEK 10

 1. Knight’s Survival Probability
A knight moves randomly on an 8×8 chessboard for k moves. Compute the probability that it stays on the board after exactly k moves.  
Example: Starting at (0,0) with k=1 → probability = 0.25.


2. Autocomplete System 
Given a query prefix and a set of dictionary strings, return all words that begin with the prefix.  
Efficient approach uses a Trie (prefix tree) for fast lookup.  
Example: Dictionary = `[dog, deer, deal]`, prefix = `de` → Output = `[deer, deal]`.


3. First Missing Positive Integer 
Given an unsorted array, find the smallest positive integer missing from it.  
Optimal approach uses in-place rearrangement to place each number x at index x-1.  
Example: `[3,4,-1,1]` → 2; `[1,2,0]` → 3.
