def double(node):
    if node == None:
        carry = 0
        return carry

    carry = double(node.next)
    node.val *= 2
    node.val += carry
    carry = int(node.val >= 10)
    node.val %= 10
    return carry


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def doubleIt(self, head: Optional[ListNode]) -> Optional[ListNode]:
        carry = double(head)
        if carry:
            new_head = ListNode(carry, head)
            return new_head
        else:
            return head

