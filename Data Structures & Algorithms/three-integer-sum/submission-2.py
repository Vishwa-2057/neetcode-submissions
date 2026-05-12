class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        for i, a in enumerate(nums):
            a = nums[i]
            if a > 0:
                break
            
            if i > 0 and a == nums[i - 1]:
                continue
            l = i + 1
            r = len(nums) - 1

            while l < r:
                sums3 = a + nums[l] + nums[r]
                if sums3 > 0:
                    r-=1
                elif sums3 < 0:
                    l+=1
                else:
                    res.append([a, nums[l], nums[r]])
                    l+=1
                    r-=1
                    while nums[l] == nums[l - 1] and l < r:
                        l += 1
        return res

            