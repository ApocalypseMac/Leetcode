class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if needle == "":
            return 0
        m = len(needle)
        for i in range(len(haystack) - m + 1):
            j = 0
            while j < m:
                if haystack[i+j] == needle[j]:
                    j += 1
                else:
                    break
            if j == m:
                return i
        return -1