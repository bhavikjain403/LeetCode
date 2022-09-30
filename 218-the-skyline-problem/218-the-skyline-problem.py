class Solution:
    def getSkyline(self, buildings):
        points = []
        for Li, Ri, Hi in buildings:
            points.append((Li, -Hi, 1))
            points.append((Ri, Hi, -1))
        points.sort()
        pq, max_height = [0], 0
        key_points = []
        for x, h, s in points:
            if s == 1: # start point
                if -h > max_height:
                    max_height = -h
                    key_points.append([x, -h])
                bisect.insort_right(pq, -h)
            else: # end point
                pq.pop(bisect.bisect_left(pq, h))
                pq_max = pq[-1]
                if pq_max < max_height:
                    max_height = pq_max
                    key_points.append([x, max_height])
        return key_points