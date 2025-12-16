#!/usr/bin/env python3

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        i = 0
        diffs = {}

        while(i<len(nums)):
            if(nums[i] in diffs.keys()):
                return [i, diffs[nums[i]]]
            else:
                diffs[target-nums[i]] = i
            i+=1
