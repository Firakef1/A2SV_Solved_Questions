# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        if not head:
            return head
        
        arr = []
        cur = head

        while cur:
            arr.append(cur.val)
            cur = cur.next

        count = arr.count(val)
        for _ in range(count):
            arr.remove(val)

        if not arr:
            return None

        cur = head
        i = 0
        while i < len(arr):
            cur.val = arr[i]
            if i == len(arr) - 1:
                cur.next = None
            else:
                if not cur.next:
                    cur.next = ListNode()
                cur = cur.next
            i += 1

        return head