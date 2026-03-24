# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def sortList(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        lis = []

        node = head

        while node:

            lis.append(node.val)
            node = node.next
        

        lis.sort()

        node = head

        for i in range(len(lis)):

            node.val = lis[i]
            node = node.next

        return head