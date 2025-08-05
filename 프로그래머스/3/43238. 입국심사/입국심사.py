def solution(n, times):
    answer = 0
    # 구해야 하는 것: n사람이 모두 심사를 통과하는 최소 시간 => mid로 두기
    left = 1 # 가능한 최소 시간 (심사 시간 범위가 1분 이상 이니까)
    right = max(times)*n # 가능한 최대 시간
    while left <= right:
        mid = (left+right)//2
        count = 0
        
        for t in times:
            count += (mid//t)
            if count >= n:
                break # n사람이 모두 심사를 통과했다는 거니까 빠져나가서 정답 후보 기록
        
        if count >= n:
            answer = mid
            right = mid-1
        else:
            left = mid+1
            
    return answer