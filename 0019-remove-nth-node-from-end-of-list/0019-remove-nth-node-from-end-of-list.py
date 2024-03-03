# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if head.next == None:
            return None
        count = 0
        cur = head
        while cur:
            count += 1
            cur =cur.next
        if count == 2 and n == 1:
            head.next = None
            return head
        elif count == 2 and n == 2:
            head = head.next
            return head
        cur1 = head
        if count-n == 0:
            return head.next
        for i in range(count - n):
            if i == (count - n - 1):
                cur1.next = cur1.next.next
            cur1 = cur1.next
        return head  