from typing import (
    List,
)

class Solution:

    def three_sum_smaller(self, nums: List[int], target: int) -> int:
        """
        sort the array:
        -3      -2      -1      0       1      3     ................       
        a       b                               c       
        
        we fix the position of 
        a and b
        if a + b + c <target then c can go till all number before b
        else shift c to right
        
        """

        ans = 0
        n = len(nums)
        nums.sort()
        for i in range(n - 2):
            
            left = i + 1
            right = n - 1

            while(left<right):
                if nums[i] + nums[left] + nums[right] < target:
                    ans += right - left 
                    left +=1
                else:
                    right -= 1
        return ans
