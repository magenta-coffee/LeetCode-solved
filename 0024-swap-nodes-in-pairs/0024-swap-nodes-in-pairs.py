# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
class Solution:
    def swapPairs(self, head):
        nod = prev = ListNode(0)
        nod.next = head
        
        while (head) and (head.next):
            a = head
            b = head.next
            
            prev.next = b
            a.next = b.next
            b.next = a
            
            prev = a
            head = a.next
        return nod.next