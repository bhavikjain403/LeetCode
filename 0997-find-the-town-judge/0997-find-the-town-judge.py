class Solution:
    def findJudge(self, N: int, trust: List[List[int]]) -> int:
        if not trust:
            if N==1:
                return 1
            return -1
        trustingPeople = set([group[0] for group in trust])
        total = (N*(N+1))//2
        townJudge = total - sum(trustingPeople)
        if townJudge:
            peopleTrustingTownJudge = [group[0] for group in trust if group[1] ==  townJudge]
            if total - sum(peopleTrustingTownJudge) == townJudge:
                return townJudge
        return -1