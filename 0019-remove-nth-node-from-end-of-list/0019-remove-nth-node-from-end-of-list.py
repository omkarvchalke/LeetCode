# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        ans=[]
        curr = head
        while curr:
            ans.append(curr.val)
            curr = curr.next
        ans.pop(len(ans)-n)
        
        dummy = ListNode()
        curr = dummy

        for a in ans:
            curr.next = ListNode(a)
            curr = curr.next

        return dummy.next