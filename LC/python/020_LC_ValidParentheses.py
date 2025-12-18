#!/usr/bin/env python3

class Solution:
    def isValid(self, s: str) -> bool:

        stack = []
        pairs = { '{':'}', '[':']', '(':')'}
        for c in s:
            if(c in pairs.keys()):
                stack.append(c)
            elif(stack and pairs[stack[len(stack)-1]] == c):
                stack.pop()
            else:
                return False

        if(len(stack) == 0):
            return True
        return False
