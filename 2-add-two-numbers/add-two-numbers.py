# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: ListNode | None, l2: ListNode | None) -> ListNode | None:
        start=ListNode(0)
        curr=start
        carry=0

        while l1 is not None or l2 is not None or carry is not 0:
            value1=l1.val if l1 else 0
            value2=l2.val if l2 else 0

            total=value1+value2+carry
            carry=total//10
            curr.next=ListNode(total%10)
            curr=curr.next

            if l1:
                l1=l1.next
            if l2:
                l2=l2.next

        return start.next    
        

        while self is not None:
            sum=l1.self.val+l2.self.val
            new_list.append(sum)
            
            self=self.next
        
        return new_list
        