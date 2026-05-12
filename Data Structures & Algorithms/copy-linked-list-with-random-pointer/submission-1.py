"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        cp_di = {}
        curr = head
        while curr:
            cp_di[curr] = (Node(curr.val),curr.random)
            curr = curr.next
        nh = Node(0)
        nl = nh
        
        for k,v in cp_di.items():
            v[0].random = cp_di[v[1]][0] if v[1] else None
            nl.next = v[0]
            nl = nl.next
        return nh.next

