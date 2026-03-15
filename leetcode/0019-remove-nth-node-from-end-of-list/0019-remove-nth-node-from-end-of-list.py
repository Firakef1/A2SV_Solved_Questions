# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        _list = head
        length = 0

        while _list:
            length += 1
            _list = _list.next


        amount = length - n


        if amount == 0:
            return head.next


        _list = head
        for i in range(amount - 1):
            _list = _list.next


        _list.next = _list.next.next

        return head