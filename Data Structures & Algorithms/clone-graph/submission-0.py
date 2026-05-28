"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        adj_map = {}

        if not node:
            return None

        def helper(node):
            if node.val in adj_map.keys():
                return adj_map[node.val]
            else:
                adj_map[node.val] = Node(node.val)
            

            for i in node.neighbors:
                helper(i)
                adj_map[node.val].neighbors.append(adj_map[i.val])
            return 
        
        helper(node)

        return adj_map[node.val]



        


     


        



        