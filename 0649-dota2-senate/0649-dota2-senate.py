class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        n = len(senate)
        r_arr = [i for i in range(len(senate)) if senate[i]=='R']
        d_arr = [j for j in range(len(senate)) if senate[j]=='D']
        while r_arr and d_arr:
            r = r_arr.pop(0)
            d = d_arr.pop(0)
            if r < d:
                r_arr.append(n + r)
            else:
                d_arr.append(n + d)
        return 'Radiant' if r_arr else 'Dire'