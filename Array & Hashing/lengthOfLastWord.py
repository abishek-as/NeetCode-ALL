class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        # return len(s.split()[-1])  # one shortcut
        c = 0
        for i in s[::-1]:
            if i == " ":
                if c >= 1:
                    return c
            else:
                c += 1
        return c


obj = Solution()
print(obj.lengthOfLastWord("Hello World"))
