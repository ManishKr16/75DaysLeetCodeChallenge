class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        left, right = 0, len(nums) - 1
        
        while left <= right:
            # Calculate the middle index safely to prevent potential overflow
            mid = left + (right - left) // 2
            
            # Found the target, return its index
            if nums[mid] == target:
                return mid
            # Target is larger, discard the left half
            elif nums[mid] < target:
                left = mid + 1
            # Target is smaller, discard the right half
            else:
                right = mid - 1
                
        # Target does not exist in the array
        return -1
        