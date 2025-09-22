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
    
# Execution
# arr = [6, 4, 5, 3, 1, 12, 8, 9, 2, 14]
arr = [5, 2, 8]

root = TreeNode(arr[0])
for val in arr[1:]:
    insertNode(root, val)
    
inOrder(root)