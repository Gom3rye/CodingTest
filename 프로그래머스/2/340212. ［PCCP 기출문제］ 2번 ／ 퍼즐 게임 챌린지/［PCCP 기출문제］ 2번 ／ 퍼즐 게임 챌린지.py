from math import log2
def solution(diffs, times, limit):
    answer, start, end = -1, 1, max(diffs) # answer: level의 최솟값
    # print(300000*log2(100000)) -> 약 500만으로 가능
    while start <= end:
        mid = (start+end)//2 # level 후보값
        now = 0 # 현재 시간
        time_prev = 0
        for idx, diff in enumerate(diffs):
            time_cur = times[idx]
            if diff <= mid: # 따라서 mid의 최대값은 max(diffs)
                now += time_cur
            else: # diff > mid:
                now += (((diff-mid)*(time_cur+time_prev))+time_cur)
            time_prev = time_cur
        
        if now <= limit:
            answer = mid
            end = mid-1
        else:
            start = mid+1
        
    return answer