class Solution:
    def hash(self, word):
        result = 0
        base = 27  # Using a constant for the base

        for i, ch in enumerate(word):
            result += (ord(ch) - ord('a') + 1) * (base ** (len(word) - i - 1))
        
        return result

    def strStr(self, haystack: str, needle: str) -> int:
        if len(needle) > len(haystack):
            return -1

        hashed_subStr = self.hash(needle)
        haystack_hash = self.hash(haystack[:len(needle)])

        if haystack_hash == hashed_subStr:
            return 0

        for i in range(1, len(haystack) - len(needle) + 1):
            haystack_hash = (haystack_hash - (ord(haystack[i - 1]) - ord('a') + 1) *
                             (27 ** (len(needle) - 1))) * 27 + ord(haystack[i + len(needle) - 1]) - ord('a') + 1

            if haystack_hash == hashed_subStr:
                return i

        return -1
