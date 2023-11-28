from typing import List


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        # Optimal Approach: Moore’s Voting Algorithm:
        res, count = 0, 0
        for i in nums:
            if count == 0:
                res = i
            count += (1 if i == res else -1)
        return res

        # # O(n) Solution:
        # hashMap = {}
        # res, maxCount = 0, 0
        # for i in nums:
        #     hashMap[i] = 1 + hashMap.get(i, 0)
        #     res = i if hashMap[i] > maxCount else res
        #     maxCount = max(hashMap[i], maxCount)
        # return res


obj = Solution()
print(obj.majorityElement([2, 2, 1, 1, 1, 2, 2]))
