#!/usr/bin/env python3

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i, j, length, twoFlag = 0, 1, len(nums), False
        suspect = nums[0]

        while(j<length):
            if(nums[j] != suspect):
                if(twoFlag):
                    nums[i] = suspect
                    nums[i+1] = suspect
                    i+=2
                else:
                    nums[i] = suspect
                    i+=1
                twoFlag = False
                suspect = nums[j]
            else:
                twoFlag = True
            j+=1

        if(twoFlag):
            nums[i] = suspect
            nums[i+1] = suspect
            i+=2
        else:
            nums[i] = suspect
            i+=1

        return i
