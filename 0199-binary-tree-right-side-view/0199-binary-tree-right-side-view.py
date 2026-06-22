from collections import deque

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:

        #BFS
        if root is None:
            return []
        queue = deque()
        queue.append(root)
        ans=[]

        while queue:
            qLen = len(queue)

            for i in range(qLen):
                node = queue.popleft()
                if i == qLen-1: # if last node of this lvl is visible , basically right node at that level
                    ans.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right) 
            
        return ans
        
        