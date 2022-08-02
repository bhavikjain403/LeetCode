class Solution:
    def romanToInt(self, s: str) -> int:
        s=s[::-1]
        ans=0
        data=[]
        for i in s:
            if i=="I":
                data.append(1)
            elif i=="V":
                data.append(5)
            elif i=="X":
                data.append(10)
            elif i=="L":
                data.append(50)
            elif i=="C":
                data.append(100)
            elif i=="D":
                data.append(500)
            elif i=="M":
                data.append(1000)
        for i in range(len(data)):
            if data[i]<ans and data[i-1]!=data[i]:
                ans-=data[i]
            else:
                ans+=data[i]
        return ans