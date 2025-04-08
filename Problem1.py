# Problem 1 : Remove Invalid Parentheses
# Time Complexity :
'''
BFS - O(n^n) where n is the length of the string s
DFS - 
'''
# Space Complexity :
'''
BFS - O(n^n) where n is the length of the string s
DFS - 
'''
# Did this code successfully run on Leetcode : Yes
# Any problem you faced while coding this :
'''
None
'''

# Your code here along with comments explaining your approach

# BFS Approach
from collections import deque
from typing import List
class Solution:
    def removeInvalidParentheses(self, s: str) -> List[str]:
        # function to check if the string contain valid parentheses
        def isValid(s:str) -> bool:
            # define count vraible to count valid parentheses
            count = 0
            # loop through string
            for c in s:
                # if the character is alphabet then continue
                if c.isalpha():
                    continue
                # if the character is '(' then increment the count 
                if c == '(':
                    count += 1
                # if the character is ')' then first check if the count is equal to 0 then return False otherwise decrement the count
                elif c == ')':
                    if count == 0: 
                        return False
                    count -= 1
            # return the result of the condition of count == 0
            return count == 0
        # define variables for result, visitedString to keep track of visited string, queue for adding the string for bfs traversal
        result = []
        visitedString = set()
        queue = deque()
        # define found flag and set to False
        found = False
        # append the string to queue and add to the visitedString set
        queue.append(s)
        visitedString.add(s)
        # loop until queue is not empty and flag is False
        while queue and not found:
            # get the length of the current queue
            length = len(queue)
            # loop through all the string at current level
            for i in range(length):
                # pop the string from the queue
                current = queue.popleft()
                # check if the string contains valid parentheses
                if isValid(current):
                    # if it is valid then add the string to result
                    result.append(current)
                    # set flag to True
                    found = True
                # check if the flag is flase then it means the result is not found yet 
                if not found:
                    # loop through the current string
                    for j in range(len(current)):
                        # get the character at jth position
                        c = current[j]
                        # check if the character is alphabet and if it is then continue
                        if c.isalpha():
                            continue
                        # get the string from the current string by removing the jth character from the current string
                        baby = current[:j] + current[j+1:]
                        # check if the created string is not in visitedString set
                        if baby not in visitedString:
                            # if it is not then add to queue and set 
                            queue.append(baby)
                            visitedString.add(baby)
        # return the resut list
        return result


# DFS
from typing import List
class Solution:
    def __init__(self):
        # define variables for maxLength of the string to get the maximum and result
        self.maxLength = 0
        self.result = []

    def removeInvalidParentheses(self, s: str) -> List[str]:
        # define variables for result, visitedString to keep track of visited string
        self.result = []
        visitedNode = set()
        # call dfs function with the string s and set visitedNode
        self.dfs(s, visitedNode)
        # return the resut list
        return self.result
    
    # dfs function
    def dfs(self, s: str, visitedNode: set) -> None:
        # check if the length of string s is less than maxLength and if it is then return
        if(len(s) < self.maxLength):
            return
        # if the string s contains valid parentheses
        if(self.isValid(s)):
            # if it is then if the length of the string s is greater than the maxLength
            if(len(s) > self.maxLength):
                # if the length is greater then set the maxLength with the value of length of string s
                self.maxLength = len(s)
                # reset the result list ie remove the previous answer
                self.result = []
            # append the string s to the result  list
            self.result.append(s)
        # loop through string s
        for i in range(len(s)):
            # get the character at ith position
            c = s[i]
            # check if the character is alphabet and if it is then continue
            if c.isalpha():
                continue
            # get the string from the current string by removing the jth character from the current string
            baby = s[:i] + s[i+1:]
            # check if the created string is not in visitedString set
            if baby not in visitedNode:
                # if it is not then add to queue and set 
                visitedNode.add(baby)
                self.dfs(baby, visitedNode)

    # function to check if the string contain valid parentheses
    def isValid(self, s: str) -> bool:
        # define count vraible to count valid parentheses
        count = 0
        # loop through string
        for i in range(len(s)):
            # get the character at position i
            c = s[i]
            # if the character is alphabet then continue
            if c.isalpha():
                continue
            # if the character is '(' then increment the count
            if c == '(':
                count += 1
            # if the character is ')' then first check if the count is equal to 0 then return False otherwise decrement the count
            else:
                if count == 0:
                    return False
                count -= 1
        # return the result of the condition of count == 0   
        return count == 0