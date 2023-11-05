#!/usr/bin/env python
# -*- coding: utf-8 -*-
from typing import List


class Solution:

    def containsDuplicate(self, nums: List[int]) -> bool:
        hashset = set()
        for i in nums:
            if i in hashset:
                return True
            hashset.add(i)
        return False


obj = Solution()
nums = [int(i) for i in input().split()]
print(obj.containsDuplicate(nums))
