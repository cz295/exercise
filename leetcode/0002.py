# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:

        if l1 is None or l2 is None:
            return l1 if l2 is None else l2
        start_node = ListNode(0)
        curr_node = start_node
        addition = 0
        while l1 or l2:
            val = addition
            val += l1.val if l1 else 0
            val += l2.val if l2 else 0
            curr_node.val = val % 10
            addition = val // 10
            l1 = l1.next if l1 else l1
            l2 = l2.next if l2 else l2
            if (l1 or l2):
                curr_node.next = ListNode(0)
                curr_node = curr_node.next
            else:
                if l1 is None and l2 is None and addition != 0:
                    curr_node.next = ListNode(addition)
        return start_node
            
