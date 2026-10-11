class Solution:
    def isHappy(self, n: int) -> bool:
        visit = set()

        # output = self.sumofSquares(n)
        while n not in visit:
            visit.add(n)
            n = self.sumofSquares(n)
            if n == 1:
                return True
        return False
              
        
    def sumofSquares(self, n:int) -> int:
        output = 0
        while n:
            remainder = n % 10
            n = n // 10
            output += remainder*remainder
        print(output)
        return output