import sys, heapq
def solution(jobs):
    # 관리해야 하는 것: 아직 들어오지 못한 job, 아직 대기 큐에 들어오지 못한 job
    jobs.sort() # 시간대별로 들어오도록 정렬
    q = []
    n = len(jobs) # 작업의 개수
    idx, now = 0, 0 # 현재 작업 번호, 현재 시간
    avg = 0
    while idx < n or q: # 도착할 작업도 없고 대기 중인 작업도 없을 때까지 반복
        
        # 언제 heapq에 넣을 수 있나? job의 시작시점보다 현재 시간이 크거나 같을 때!
        while idx < n and jobs[idx][0] <= now:
            heapq.heappush(q, (jobs[idx][1], jobs[idx][0]))
            idx += 1
            
        # heapq에 작업이 있다면 (job 시작 가능)
        if q:
            length, start = heapq.heappop(q)
            now += length
            avg += (now-start)
        else: # 없다면 job의 시작 시간으로 점프
            now = jobs[idx][0]
            
    return avg//n