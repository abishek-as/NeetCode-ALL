from typing import List


class NumArray:

    def __init__(self, nums: List[int]):
        self.prefix = []
        curr_sum = 0
        for i in nums:
            curr_sum += i
            self.prefix.append(curr_sum)

    def sumRange(self, left: int, right: int) -> int:
        rightSum = self.prefix[right]
        leftSum = self.prefix[left - 1] if left > 0 else 0
        return rightSum - leftSum


obj = NumArray([-2, 0, 3, -5, 2, -1])
print(obj.sumRange(0, 2))
