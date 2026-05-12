# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        nl = ListNode()
        nh = nl

        curr_1 = l1
        curr_2 = l2
        carry = 0

        while curr_1 and curr_2:
            new_num = curr_1.val + curr_2.val + carry
            remainder = new_num % 10
            carry = new_num // 10
            nh.next = ListNode(val=remainder)
            nh = nh.next
            curr_1 = curr_1.next
            curr_2 = curr_2.next
        
        while curr_1:
            new_num = curr_1.val + carry
            remainder = new_num % 10
            carry = new_num // 10
            nh.next = ListNode(val=remainder)
            nh = nh.next
            curr_1 = curr_1.next
        
        while curr_2:
            new_num = curr_2.val + carry
            remainder = new_num % 10
            carry = new_num // 10
            nh.next = ListNode(val=remainder)
            nh = nh.next
            curr_2 = curr_2.next
        
        if carry:
            nh.next = ListNode(val=carry)
        
        # curr = nl.next
        # prev = None

        # while curr:
        #     temp = curr.next
        #     curr.next = prev
        #     prev = curr
        #     curr = temp
        
        return nl.next


            

