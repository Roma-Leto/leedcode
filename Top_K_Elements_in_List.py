"""
Top K Elements in List

Given an integer array nums and an integer k, return the k most frequent
elements within the array.
The test cases are generated such that the answer is always unique.
You may return the output in any order.

Example 1:
Input: nums = [1,2,2,3,3,3], k = 2
Output: [2,3]

Example 2:
Input: nums = [7,7], k = 1
Output: [7]

Constraints:
    1 <= nums.length <= 10^4.
    -1000 <= nums[i] <= 1000
    1 <= k <= number of distinct elements in nums.
"""
import random
from typing import List


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashlist = dict()
        for item in nums:
            if None == hashlist.get(item):
                hashlist.setdefault(item, 1)
            else:
                hashlist[item] += 1
        print(hashlist)
        dict_max = sorted(hashlist.items(), key=lambda x: x[1], reverse=True)
        print(dict_max)
        return print([x[0] for x in dict_max[:k]])  # Выводит: ['c', 'b']


if __name__ == '__main__':
    nums = []
    k = 5

    for _ in range(1_000_000):
        i = random.randint(1, 100)
        nums.append(i)

    print(nums)

    asd = Solution()
    print(asd.topKFrequent(nums=nums, k=k))
