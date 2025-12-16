#!/usr/bin/env python3

class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        for character in ransomNote:
            if(character in magazine):
                magazine = magazine.replace(str(character), "", 1)
            else:
                return False
        return True
