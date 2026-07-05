class Solution(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        nums.sort()
        n = len(nums)
        quadruplets = []
        
        for i in range(n - 3):
            # Skip duplicate values for the first element
            if i > 0 and nums[i] == nums[i - 1]:
                continue
                
            # Quick Pruning Optimizations
            # 1. Minimum possible sum from here is too large
            if nums[i] + nums[i + 1] + nums[i + 2] + nums[i + 3] > target:
                break
            # 2. Maximum possible sum with nums[i] is too small
            if nums[i] + nums[n - 3] + nums[n - 2] + nums[n - 1] < target:
                continue
                
            for j in range(i + 1, n - 2):
                # Skip duplicate values for the second element
                if j > i + 1 and nums[j] == nums[j - 1]:
                    continue
                    
                # More Pruning Optimizations
                if nums[i] + nums[j] + nums[j + 1] + nums[j + 2] > target:
                    break
                if nums[i] + nums[j] + nums[n - 2] + nums[n - 1] < target:
                    continue
                
                # Two-pointer approach for the remaining two elements
                left = j + 1
                right = n - 1
                
                while left < right:
                    current_sum = nums[i] + nums[j] + nums[left] + nums[right]
                    
                    if current_sum == target:
                        quadruplets.append([nums[i], nums[j], nums[left], nums[right]])
                        
                        # Skip duplicate values for the third element
                        while left < right and nums[left] == nums[left + 1]:
                            left += 1
                        # Skip duplicate values for the fourth element
                        while left < right and nums[right] == nums[right - 1]:
                            right -= 1
                            
                        left += 1
                        right -= 1
                    elif current_sum < target:
                        left += 1
                    else:
                        right -= 1
                        
        return quadruplets