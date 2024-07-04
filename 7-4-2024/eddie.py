# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        zero = head
        node = zero.next
        sum = 0
        while True:
            if node.val == 0 and node.next == None:
                zero.val = sum
                zero.next = None
                break

            if node.val == 0:
                zero.val = sum
                zero.next = node
                zero = node
                sum = 0
                node = node.next
                continue

            sum += node.val
            node = node.next

        return head
