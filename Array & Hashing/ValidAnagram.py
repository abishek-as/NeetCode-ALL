class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        # define hashmaps
        countS, countT = {}, {}

        # store values in hashmap
        for i in range(len(s)):
            countS[s[i]] = 1 + countS.get(s[i], 0)
            countT[t[i]] = 1 + countT.get(t[i], 0)

        for key in countS:
            if countS[key] != countT.get(key, 0):
                return False

        return True


obj = Solution()
print(obj.isAnagram("anagram", "nagaram"))
