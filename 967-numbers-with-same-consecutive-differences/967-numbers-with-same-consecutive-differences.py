class Solution:
    def numsSameConsecDiff(self, N: int, K: int) -> List[int]:
        def dfs( N, K, cur_num):
            if N == 0:
                result.append( cur_num )
                return
            last_digit = cur_num % 10
            if last_digit + K < 10:
                next_num = 10 * cur_num + last_digit + K
                dfs( N-1, K, next_num)
            if last_digit - K >= 0 and K != 0:
                next_num = 10 * cur_num + last_digit - K
                dfs( N-1, K, next_num)
                
        result = []
        if N == 1:
            result.append( 0 )
        for digit in range(1, 10):
            dfs( N-1, K, cur_num=digit)
        return result