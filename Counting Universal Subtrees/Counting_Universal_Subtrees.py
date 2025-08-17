# Technique 1
class Node:
    def __init__(self, val, left=None, right=None):
        self.val, self.left, self.right = val, left, right

def count_unival_subtrees(root):
    count = 0

    def dfs(node):
        nonlocal count
        if not node: 
            return True   # empty is unival

        left_uni = dfs(node.left)
        right_uni = dfs(node.right)

        if not (left_uni and right_uni): 
            return False
        if node.left and node.left.val != node.val: 
            return False
        if node.right and node.right.val != node.val: 
            return False

        count += 1
        return True

    dfs(root)
    return count


# Technique 2 
def count_unival_subtrees(root):
    def dfs(n):
        if not n: return True
        L, R = dfs(n.left), dfs(n.right)
        if not(L and R) or (n.left and n.left.val!=n.val) or (n.right and n.right.val!=n.val): return False
        nonlocal count; count+=1; return True
    count=0; dfs(root); return count

# Test 
class Node:
    def __init__(self,v,l=None,r=None): self.val,self.left,self.right=v,l,r

root = Node(0, Node(1), Node(0, Node(1, Node(1), Node(1)), Node(0)))
print(count_unival_subtrees(root))  # 5
