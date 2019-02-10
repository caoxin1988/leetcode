class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def maxDepth(self, root):
        return self.depth_of_node(root)

    def depth_of_node(self, node : TreeNode):
        dep_left, dep_right = 0, 0
        
        if not node:
            return 0

        dep_left = 0 if not node.left else self.depth_of_node(node.left)
        dep_right =0 if not node.right else self.depth_of_node(node.right)

        depth = max(dep_left, dep_right) + 1
        
        return depth