# Problem 2 : Clone Graph
# Time Complexity :
'''
BFS - O(N+E) where N is the number of nodes and E is the number of edges in the graph
DFS - O(N+E) where N is the number of nodes and E is the number of edges in the graph
'''
# Space Complexity :
'''
BFS - O(N) where N is the number of nodes
DFS - O(N) where N is the number of nodes
'''
# Did this code successfully run on Leetcode : Yes
# Any problem you faced while coding this :
'''
None
'''

# Your code here along with comments explaining your approach

# BFS Approach

from collections import deque
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        # edge case if the node is None then return None
        if node is None:
            return None

        # define nodeMap hashmap where key is the original node and value is the copy node ie node mapping
        nodeMap = {}
        # create a new node of the original head node
        newNode = Node(node.val)
        # add the node mapping to the hash map
        nodeMap[node] = newNode
        # add the original node to the queue
        queue = deque([node])

        # loop through the queue is not empty
        while queue:
            # pop the element from the queue
            current = queue.popleft()
            # loop through neighbours of the poped node
            for neighbor in current.neighbors:
                # check if there is mapping of the neighbour node in hashmap
                if neighbor not in nodeMap:
                    # if the mapping is not present then create a copy of the node
                    copyNode = Node(neighbor.val)
                    # add the mapping of the node to hashmap
                    nodeMap[neighbor] = copyNode
                    # add the original node to the queue
                    queue.append(neighbor)
                # update the neighbour of the copy node 
                # first get the copy node of the original node from hash map
                # update the neighbours list of the copy node with the values for the key as neighbour in hash map
                nodeMap[current].neighbors.append(nodeMap[neighbor])
        # return the value of key node in hash map
        return nodeMap[node]


# DFS Approach

# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        # edge case if the node is None then return None
        if node is None:
            return None

        # define nodeMap hashmap where key is the original node and value is the copy node ie node mapping
        nodeMap = {}
        # dfs function to traverse in dfs way
        def dfs(node: Optional['Node'], nodeMap) -> None:
            # base case
            # if node has a mapping in the hash map then return
            if node in nodeMap:
                return
            # create a copy of the node
            copyNode = Node(node.val)
            # add the mapping of the node to hashmap
            nodeMap[node] = copyNode
            # loop through neighbours of the node
            for neighbor in node.neighbors:
                # call dfs function with neighbor node and nodeMap hash map
                dfs(neighbor, nodeMap)
                # update the neighbour of the copy node 
                # first get the copy node of the original node from hash map
                # update the neighbours list of the copy node with the values for the key as neighbour in hash map
                nodeMap[node].neighbors.append(nodeMap[neighbor])

        # call dfs function with head node and nodeMap hash map
        dfs(node, nodeMap)
        # return the value of key node in hash map
        return nodeMap[node]
        
        