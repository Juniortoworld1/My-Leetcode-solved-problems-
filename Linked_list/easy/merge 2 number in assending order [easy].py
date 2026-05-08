# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        # Create a dummy node to hold the start of the merged list
        dummy = ListNode(-1)
        current = dummy

        # While both lists have nodes remaining
        while list1 and list2:
            if list1.val <= list2.val:
                current.next = list1
                list1 = list1.next
            else:
                current.next = list2
                list2 = list2.next
            
            # Move the pointer in the merged list forward
            current = current.next

        # If one list is longer than the other, attach the remainder
        # Since the lists are already sorted, we just point to the rest of the list
        current.next = list1 if list1 is not None else list2

        # The merged list starts after the dummy node
        return dummy.next
