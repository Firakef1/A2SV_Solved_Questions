# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: Optional[ListNode]
        :type l2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        
        first = ""
        second = ""

        current = l1
        while current:

            first = str(current.val) + first
            current = current.next

        current = l2
        while current:

            second = str(current.val) + second
            current = current.next

        new_number = str(int(first)+int(second))

        new_node = ListNode(int(new_number[-1]))
        current = new_node

        for i in range(len(new_number)-2 ,-1 , -1):

            current.next =  ListNode(int(new_number[i]))
            current = current.next

        return new_node