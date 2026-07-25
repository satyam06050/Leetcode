class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        def symm(left, right):
            if not left and not right:
                return True
            if not left or not right:
                return False
            if left.val != right.val:
                return False
            return symm(left.left, right.right) and symm(left.right, right.left)

        return symm(root.left, root.right)
