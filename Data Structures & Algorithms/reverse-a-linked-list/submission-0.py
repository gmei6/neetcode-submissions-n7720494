from collections import deque

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None

        newHead = head
        if head.next:
            print("we are passing in this into the reverseList: ", head.val)
            newHead = self.reverseList(head.next)
            if head.next.next: 
                print("We have set ", head.next.next.val, " to ", head.val)

            head.next.next = head
            print("")
        head.next = None

        return newHead