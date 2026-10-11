class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        table = {}

        for each in nums:
            table[each] = 1 + table.get(each, 0)
            if table[each] > 1:
                return True

        return False
        