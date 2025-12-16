#!/usr/bin/env python3

class Solution:
    def isHappy(self, n: int) -> bool:
        seen = []

        num = n
        while(num != 1):
            nStr = str(num)
            newNum = 0
            for i in range(len(nStr)):
                newNum += int(nStr[i])*int(nStr[i])
            num = newNum

            if(num in seen):
                return False
            else:
                seen.append(num)

        return True
