class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        existsDict = {}
        for i in range(len(nums)):
            result = target - nums[i]
            if result in existsDict:
                return[existsDict[result],i]
            existsDict[nums[i]] = i
