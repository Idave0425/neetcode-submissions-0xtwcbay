# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        N = 0
        curr = head

        while curr:
            curr = curr.next
            N += 1
        
        idx = N - n
        if idx == 0:
            return head.next
            
        curr = head
        for i in range(idx):
            if i == idx - 1:
                curr.next = curr.next.next
                break
            curr = curr.next
        
        return head