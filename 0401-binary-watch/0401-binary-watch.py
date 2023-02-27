class Solution:
    def readBinaryWatch(self, turnedOn: int) -> List[str]:
        ans=[]
        for i in range(12):
            for j in range(60):
                if (bin(i)+bin(j)).count("1")==turnedOn:
                    if j<10:
                        j="0"+str(j)
                    ans.append(f"{i}:{j}")
        return ans