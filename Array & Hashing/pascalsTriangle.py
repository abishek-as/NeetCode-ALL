from typing import List


class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        ans = [[1]]
        for _ in range(numRows - 1):
            temp = [0] + ans[-1] + [0]
            row = []
            for j in range(len(ans[-1]) + 1):
                row.append(temp[j] + temp[j+1])
            ans.append(row)
        return ans


obj = Solution()
print(obj.generate(numRows=5))
