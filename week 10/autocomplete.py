class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end = False

class Trie:
    def __init__(self):
        self.root = TrieNode()
    
    def insert(self, word):
        node = self.root
        for ch in word:
            node = node.children.setdefault(ch, TrieNode())
        node.is_end = True
    
    def autocomplete(self, prefix):
        node = self.root
        for ch in prefix:
            if ch not in node.children:
                return []
            node = node.children[ch]
        res = []
        def dfs(n, path):
            if n.is_end:
                res.append(''.join(path))
            for c, child in n.children.items():
                dfs(child, path + [c])
        dfs(node, list(prefix))
        return res
N = int(input())
words = input().split()
prefix = input()
trie = Trie()
for word in words:
    trie.insert(word)
print(' '.join(trie.autocomplete(prefix)))
