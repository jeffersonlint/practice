#!/usr/bin/env python3

class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if(len(s) != len(t)):
            return False

        mapping = {}

        i = 0
        while(i<len(s)):
            if(s[i] in mapping.keys() or t[i] in mapping.values()):
                if(s[i] not in mapping.keys()):
                    return False
                elif(mapping[s[i]] != t[i]):
                    return False
            else:
                mapping[s[i]] = t[i]
            i+=1
        return True
