# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:

        ans = TreeNode()

        def compare(root, p, q):

            if (root.val < p.val and root.val > q.val) or (root.val > p.val and root.val < q.val) or (root is q) or (root is p):
                return root
            elif(root.val > p.val and root.val > q.val):
                root = root.left
                print(root.val)
                return compare(root,p,q)
            else:
                root = root.right
                print(root.val)
                return compare(root,p,q)
        



        return compare(root,p,q)
            
        