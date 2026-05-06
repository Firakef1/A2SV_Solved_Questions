# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[Optional[ListNode]]
        :rtype: Optional[ListNode]
        """

        node_list = []
        #take the values
        for i in lists:

            while i:

                node_list.append(i.val)
                i = i.next
        node_list.sort()

        if len(node_list) == 0:

            return  None

        head = ListNode(node_list[0])
        curr = head
        for i in range(1, len(node_list)):

            curr.next = ListNode(node_list[i])

            curr = curr.next
        return head