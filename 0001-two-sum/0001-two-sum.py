class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        Seen = {}
        for i in range (len(nums)):
            required = target - nums[i]
            if required in Seen:
                return [Seen[required],i]
            Seen [nums[i]] = i        