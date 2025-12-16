#!/usr/bin/env python

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        anagrams = {}

        for word in strs:
            alphaWord = ''.join(sorted(word))
            if(alphaWord in anagrams):
                anagrams[alphaWord].append(word)
            else:
                anagrams[alphaWord] = [word]

        return list(anagrams.values())
