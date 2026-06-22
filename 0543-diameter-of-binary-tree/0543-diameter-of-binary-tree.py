# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        max_dia = [0]

        def height(node):
            if node is None:
                return 0

            left_height = height(node.left)
            right_height = height(node.right)

            # diameter through current node
            dia = left_height + right_height

            max_dia[0] = max(max_dia[0], dia)

            # return height, not node
            return 1 + max(left_height, right_height)

        height(root)
        return max_dia[0]