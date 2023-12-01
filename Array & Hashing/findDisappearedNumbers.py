from typing import List


class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        # mark existing
        for i in nums:
            idx = abs(i) - 1
            nums[idx] = - 1 * abs(nums[idx])

        res = []
        for i, ele in enumerate(nums):
            if ele > 0:
                res.append(i + 1)
        return res


obj = Solution()
print(obj.findDisappearedNumbers(nums=[4, 3, 2, 7, 8, 2, 3, 1]))
print(obj.findDisappearedNumbers(nums=[1, 1]))
