# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def balanceBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        inorder = []

        def dfs(node):
            if not node:
                return
            dfs(node.left)
            inorder.append(node)
            dfs(node.right)

        def build(l, r):
            if l > r:
                return None
            mid = (l + r) // 2
            node = inorder[mid]
            node.left = build(l, mid - 1)
            node.right = build(mid + 1, r)
            return node

        dfs(root)
        return build(0, len(inorder) - 1)
