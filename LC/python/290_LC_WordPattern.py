#!/usr/bin/env python3

class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:

        mapping = {}
        splitS = s.split()

        if(len(splitS) != len(pattern)):
            return False

        for i in range(len(pattern)):
            if(pattern[i] in mapping.keys()):
                if(mapping[pattern[i]] != splitS[i]):
                    return False
            elif(splitS[i] in mapping.values()):
                return False
            else:
                mapping[pattern[i]] = splitS[i]

        return True
