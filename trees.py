class TreeNode:
    def __init__(self, val=None, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

root = TreeNode(17)
root.left = TreeNode(5)
root.right = TreeNode(25)
root.left.left = TreeNode(1)
root.right.left = TreeNode(20)