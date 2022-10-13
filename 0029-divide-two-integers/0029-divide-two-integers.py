class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        if (divisor<0 and dividend<0) or (divisor>0 and dividend>0):
            return min(dividend//divisor,2147483647)
        return -((abs(dividend))//abs(divisor))