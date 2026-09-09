class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:

        count = Counter(tasks)
        maxHeap = [-cnt for cnt in count.values()]
        heapq.heapify(maxHeap)

        time = 0 
        q = deque() # pairs of [-cnt, idleTime]

        while maxHeap or q:
            # each operation we count the time
            time += 1

            # if the maxHeap is not empty
            if maxHeap: 
                cnt = 1 + heapq.heappop(maxHeap) #count for each letter, place it in the operation, and -1
                if cnt:
                    q.append([cnt, time + n]) # the queue then add the (current count, time to be ready)
            
            if q and q[0][1] == time: # if it's ready, then we push the count into maxHeap 
                heapq.heappush(maxHeap, q.popleft()[0])
        return time 


