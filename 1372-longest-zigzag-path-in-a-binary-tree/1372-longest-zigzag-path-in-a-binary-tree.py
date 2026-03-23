# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestZigZag(self, root: Optional[TreeNode]) -> int:
        self.max_len = 0
        def dfs(node, left_len, right_len):
            if not node:
                return
            self.max_len = max(self.max_len, left_len, right_len)
            dfs(node.left, 0, left_len + 1 )
            dfs(node.right, right_len + 1, 0)
        dfs(root,0,0)
        return self.max_len