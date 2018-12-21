class Solution(object):
    
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        carry = False
        head = ListNode(0)
        previous = head
        
        while l1 != None and l2 != None:
            if carry:
                previous.next = ListNode((l1.val + l2.val + 1) % 10)
                carry = (l1.val + l2.val + 1) >= 10
            else:
                previous.next = ListNode((l1.val + l2.val) % 10)
                carry = (l1.val + l2.val) >= 10
            l1 = l1.next
            l2 = l2.next
            previous = previous.next
        
        while l1 != None:
            if carry:
                previous.next = ListNode((l1.val + 1) % 10)
                carry = l1.val + 1 >= 10
            else:
                previous.next = ListNode(l1.val)
            previous = previous.next
            l1 = l1.next
            
        while l2 != None:
            if carry:
                previous.next = ListNode((l2.val + 1) % 10)
                carry = l2.val + 1 >= 10
            else:
                previous.next = ListNode(l2.val)
            previous = previous.next
            l2 = l2.next
        
        if carry:
            previous.next = ListNode(1)
            
        return head.next
