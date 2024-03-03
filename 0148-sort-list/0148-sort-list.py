# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        lst = []
        if head is None:
            return None
        cur = head
        while cur != None:
            lst.append(cur.val)
            cur = cur.next
        return self.ll(sorted(lst))

    def ll(self, lst):
        head = ListNode(lst[0])   
        cur = head
        for i in range(1, len(lst)):
            cur.next = ListNode(lst[i])
            cur = cur.next
        return head