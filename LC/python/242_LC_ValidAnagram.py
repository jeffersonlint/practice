#!/usr/bin/env python3

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if(len(s) != len(t)):
            return False

        alphaCount = {}
        for character in s:
            if(character in alphaCount.keys()):
                alphaCount[character] = alphaCount[character]+1
            else:
                alphaCount[character] = 1

        for character in t:
            if(character in alphaCount.keys()):
                if(alphaCount[character] == 0):
                    return False
                alphaCount[character] = alphaCount[character]-1
            else:
                return False

        return True
