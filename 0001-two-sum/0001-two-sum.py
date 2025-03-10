class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
      hmap = {}
      for index, num in enumerate(nums):
        compliment = target - num
        if compliment in hmap:
            return [index, hmap[compliment]]
        hmap[num] = index  