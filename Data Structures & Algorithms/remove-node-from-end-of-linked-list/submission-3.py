# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if head.next is None:
            return None

        temp = ListNode(0,head) 
        prevOne = temp
        nextOne = temp

        for _ in range(n + 1):
            nextOne = nextOne.next

        while nextOne is not None:
            nextOne = nextOne.next
            prevOne = prevOne.next
        
        prevOne.next = prevOne.next.next

        return temp.next