class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        
        missing = 0
        for i in range(len(nums)):
            # print(i)
            if i not in nums:
                missing = i
                return missing

        return len(nums)