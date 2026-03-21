# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        vals = []
        curr = head
        while curr:
            vals.append(curr.val)
            curr = curr.next
        n = len(vals)
        return max(vals[i] + vals[n-1-i] for i in range(n//2))