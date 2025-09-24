class TreeNode:
    def __init__(self, val=None, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def insertNode(root, val):
    if not root:
        root = TreeNode(val)
        return root
    if val < root.val:
        if not root.left:
            root.left = TreeNode(val)
            return root
        else:
            insertNode(root.left, val)
    else:
        if not root.right:
            root.right = TreeNode(val)
            return root
        else:
            insertNode(root.right, val)

def inOrder(root):
    if root:
        inOrder(root.left)
        print(root.val)
        inOrder(root.right)
    
def searchTree(root, key):
    if not root: return False
    if root.val == key: return True
 
    findLeft = searchTree(root.left, key)
    findRight = searchTree(root.right, key)
    return findLeft or findRight


# Execution
# arr = [6, 4, 5, 3, 1, 12, 8, 9, 2, 14]
arr = [5, 2, 8]

# Create a tree from the given array
root = TreeNode(arr[0])
for val in arr[1:]:
    insertNode(root, val)
    
inOrder(root)

# Search operations
print(searchTree(root, 17))
print(searchTree(root, 5))
print(searchTree(root, 2))