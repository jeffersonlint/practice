#!/usr/bin/env python3

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        i, length = 0, len(nums)
        while(i<length):
            if(nums[i] == val):
                del nums[i]
                i-=1
                length-=1
            i+=1
        return len(nums)
