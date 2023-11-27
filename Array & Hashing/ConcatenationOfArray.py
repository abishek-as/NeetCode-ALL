from typing import List


class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        ans, n = [0] * 2 * len(nums), len(nums)
        for i in range(0, 2 * n):
            if i < n:
                ans[i] = nums[i]
            else:
                ans[i] = nums[i - n]
        return ans


obj = Solution()
print(obj.getConcatenation([1, 3, 2, 1]))
