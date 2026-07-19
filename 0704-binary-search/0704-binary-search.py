class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        
        left, right = 0, len(nums) - 1
        
        while left <= right:
            mid = (left + right) // 2
            
            # Found the target, return its index
            if nums[mid] == target:
                return mid
            # Target is smaller, ignore the right half
            elif nums[mid] > target:
                right = mid - 1
            # Target is larger, ignore the left half
            else:
                left = mid + 1
                
        # Target does not exist in the array
        return -1