from collections import Counter


class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        ransomNoteCounter = Counter(ransomNote)
        magazineCounter = Counter(magazine)
        for k in ransomNoteCounter:
            magazineCounter[k] = magazineCounter.get(k, 0) - ransomNoteCounter[k]
            if magazineCounter[k] < 0:
                return False
        return True


if __name__ == "__main__":
    ransomNote = "aab"
    magazine = "baa"
    print(Solution().canConstruct(ransomNote, magazine))


#
#
# https://leetcode.com/problems/ransom-note/
