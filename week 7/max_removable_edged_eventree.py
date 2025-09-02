from collections import defaultdict

def max_removable_edges(n, edges):
    adj = defaultdict(list)
    for u, v in edges:
        adj[u].append(v)
        adj[v].append(u)

    removable = 0

    def dfs(node, parent):
        nonlocal removable
        size = 1
        for child in adj[node]:
            if child != parent:
                child_size = dfs(child, node)
                if child_size % 2 == 0:
                    removable += 1
                else:
                    size += child_size
        return size

    dfs(1, -1)
    return removable

# Example usage
n = 8
edges = [
    (1,2),(1,3),(3,4),(3,5),(4,6),(4,7),(4,8)
]
print(max_removable_edges(n, edges))  # Output: 2
