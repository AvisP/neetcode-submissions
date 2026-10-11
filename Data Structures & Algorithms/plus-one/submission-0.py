class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        
        number = 0
        for each_digit in digits:
            number = number*10 + each_digit

        number += 1

        res = []
        while number:
            res.append(number%10)
            number = number // 10

        res = res[::-1]   

        return res