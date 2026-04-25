# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:

        i = 1
        arr = []
        temp = head

        while temp:

            if i in range(left, right+1):
                arr.append(temp.val)
            
            i+=1
            temp = temp.next
        
        arr.reverse()

        i = 1
        j = 0
        temp = head

        while temp:

            if i in range(left, right+1):
                temp.val = arr[j]
                j += 1
            
            i+= 1
            temp = temp.next

        return head