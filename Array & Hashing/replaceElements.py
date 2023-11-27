from typing import List


class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        rightMax = -1
        for i in range(len(arr) - 1, -1, -1):
            newMax = max(arr[i], rightMax)
            arr[i] = rightMax
            rightMax = newMax
        return arr


obj = Solution()
print(obj.replaceElements([17, 18, 5, 4, 6, 1]))
