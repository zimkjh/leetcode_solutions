import math
class Solution:
    def minDifference(self, nums: List[int]) -> int:
        if len(nums)<= 4:
            return 0
        
        nums.sort()
        
        minVal = math.inf
        for i in range(4):
            leftNum = i
            rightNum = i - 4
            # 0, -4, 
            # 1, -3,
            # 2, -2,
            # 3, -1,
            minVal = min(minVal, nums[rightNum] - nums[leftNum])
            
        return minVal
                
                
            
            
        