from typing import List


def getFrequencies(nums: List[int]) -> List[int]:
    hashMap = {}
    for i in range(len(nums)):
        hashMap[nums[i]] = 1 + hashMap.get(nums[i], 0)

    max_value = max(hashMap.values())
    min_value = min(hashMap.values())
    max_freq = [key for key, value in hashMap.items() if value == max_value]
    min_freq = [key for key, value in hashMap.items() if value == min_value]
    max_freq_element = min(max_freq)
    min_freq_element = min(min_freq)
    return max_freq_element, min_freq_element


print(getFrequencies(nums=[10, 5, 10, 15, 10, 5]))
print(getFrequencies(nums=[2, 2, 3, 4, 4, 2]))
print(getFrequencies(nums=[10, 10, 10, 3, 3, 3]))
