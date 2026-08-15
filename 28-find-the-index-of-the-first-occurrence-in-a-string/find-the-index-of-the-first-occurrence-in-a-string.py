class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        found = 0
        for i in range(len(haystack)-len(needle)+1):
            if needle == haystack[i:i+len(needle)]:
              found += 1
              return i
              break
        if found == 0:
            return -1