class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        
        # Initialize the global max, and the running max/min with the first element
        global_max = nums[0]
        current_max = nums[0]
        current_min = nums[0]
        
        for i in range(1, len(nums)):
            num = nums[i]
            
            # If the current number is negative, swapping max and min 
            # accounts for the sign flip when multiplied
            if num < 0:
                current_max, current_min = current_min, current_max
            
            # The choice is either starting a new subarray at the current element,
            # or continuing the existing subarray product
            current_max = max(num, current_max * num)
            current_min = min(num, current_min * num)
            
            # Update our overall answer
            global_max = max(global_max, current_max)
            
        return global_max
        