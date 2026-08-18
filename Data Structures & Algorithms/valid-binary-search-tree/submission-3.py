# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        lowerBound = -float("inf")
        upperBound = float("inf")

        def check(root, lowerBound, upperBound):
            if not root:
                return True

            if not (lowerBound < root.val < upperBound):
                return False
            else:
                return (check(root.right, root.val, upperBound) and check(root.left, lowerBound, root.val))

        return check(root, lowerBound, upperBound)