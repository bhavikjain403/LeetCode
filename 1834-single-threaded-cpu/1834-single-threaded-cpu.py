class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        newTask=[]
        ans=[]
        sortTask=[(e,p,i) for i,(e,p) in enumerate(tasks)]
        sortTask.sort()
        time,idx=0,0
        while idx<len(tasks) or newTask:
            if not newTask and time<sortTask[idx][0]:
                time=sortTask[idx][0]
            while idx<len(sortTask) and time>=sortTask[idx][0]:
                e,p,i=sortTask[idx]
                heapq.heappush(newTask,(p,i))
                idx+=1
            p,i=heapq.heappop(newTask)
            time+=p
            ans.append(i)
        return ans