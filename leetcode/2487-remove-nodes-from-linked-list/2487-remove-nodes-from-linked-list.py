# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        stack = deque()

        temp = head

        while temp:
            while stack and stack[-1].val < temp.val:
                stack.pop()
            if stack:
                stack[-1].next = temp
            else:
                head = temp
            stack.append(temp)
            temp = temp.next
        
        return head