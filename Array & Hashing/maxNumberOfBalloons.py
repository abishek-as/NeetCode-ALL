from typing import List


class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        mapText, balloon = {}, {}

        for i in text:
            mapText[i] = 1 + mapText.get(i, 0)
        for i in "balloon":
            balloon[i] = 1 + balloon.get(i, 0)

        res = len(text)  # or float("inf")
        for c in balloon:
            res = min(res, mapText[c] // balloon[c]) if c in mapText else 0
        return res


obj = Solution()
print(obj.maxNumberOfBalloons(text="nlaebolko"))
print(obj.maxNumberOfBalloons(text="loonbalxballpoon"))
print(obj.maxNumberOfBalloons(text="leetcode"))
