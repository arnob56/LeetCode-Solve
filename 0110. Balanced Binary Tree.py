class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
    
        def check_balance(node):
            if not node:
                return 0  
            left = check_balance(node.left)
            right = check_balance(node.right)

  
            if left == -1 or right == -1 or abs(left - right) > 1:
                return -1

            return 1 + max(left, right)

        return check_balance(root) != -1
