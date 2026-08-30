class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_sum = nums[0]
        current_sum = nums[0]
        
        for num in nums[1:]:
            # Either extend the existing subarray or start a new one from num
            current_sum = max(num, current_sum + num)
            # Track the maximum sum found so far
            max_sum = max(max_sum, current_sum)
            
        return max_sum
        