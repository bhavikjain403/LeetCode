class Solution:
    def sumEvenAfterQueries(self, A: List[int], queries: List[List[int]]) -> List[int]:
        evenSum = 0
        res = []
        
        for v in A:
            if v%2==0:
                evenSum += v
                
        for q in queries:
            value, index = q[0], q[1]
            old = A[index]
            A[index] += value
            new = A[index]
        
            if new%2==0: #even
                if old%2==0: #even -> even
                    evenSum += value
                else:  # odd -> even
                    evenSum += new
            else: #odd
                if old%2==0:  # even -> odd
                    evenSum -= old
                
            res.append(evenSum)
                
        return res