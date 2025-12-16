#!/usr/bin/env python3

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        index1 = 0
        index2 = 0
        mergedList = []
        while(not (index1 == m and index2 == n)):
            if(index1 == m):
                mergedList.append(nums2[index2])
                index2+=1
            elif(index2 == n):
                mergedList.append(nums1[index1])
                index1+=1
            elif(nums1[index1] <= nums2[index2]):
                mergedList.append(nums1[index1])
                index1+=1
            else:
                mergedList.append(nums2[index2])
                index2+=1

        index3 = 0
        while(index3 != m+n):
            nums1[index3] = mergedList[index3]
            index3+=1
