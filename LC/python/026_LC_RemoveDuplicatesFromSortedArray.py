#!/usr/bin/env python3

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i, j, length = 0, 1, len(nums)
        while(j < length):
            if(nums[i] != nums[j]):
                i+=1
                nums[i] = nums[j]
            j+=1
        return i+1
