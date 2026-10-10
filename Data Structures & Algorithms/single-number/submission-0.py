class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        hash_table = {}

        for each_num in nums:
            hash_table[each_num] = 1 + hash_table.get(each_num, 0)

        for key in hash_table:
            if hash_table[key] == 1:
                return key
