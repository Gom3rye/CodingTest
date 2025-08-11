def solution(play_time, adv_time, logs):
    # 1. 시간 단위를 초로 통일하는 함수
    def time_to_sec(time_str):
        h, m, s = map(int, time_str.split(':'))
        return h * 3600 + m * 60 + s

    def sec_to_time(sec):
        h = sec // 3600
        sec %= 3600
        m = sec // 60
        s = sec % 60
        return f"{h:02d}:{m:02d}:{s:02d}"

    play_time_sec = time_to_sec(play_time)
    adv_time_sec = time_to_sec(adv_time)
    
    # 2. 각 초(second)별 시청자 수 구하기 (Imos 기법)
    # timeline[i]: i초 시점의 시청자 수 변화량
    timeline = [0] * (play_time_sec + 2)

    for log in logs:
        start_str, end_str = log.split('-')
        start_sec = time_to_sec(start_str)
        end_sec = time_to_sec(end_str)
        timeline[start_sec] += 1
        timeline[end_sec] -= 1
        
    # 첫 번째 누적 합: timeline[i]에 i초 시점의 실제 시청자 수 기록
    for i in range(1, play_time_sec + 1):
        timeline[i] += timeline[i-1]
    
    # 3. 광고 구간의 최대 누적 재생 시간 찾기 (Sliding Window)
    # 두 번째 누적 합: cumulative_sum[i]에 0초부터 i-1초까지의 총 누적 재생 시간 기록
    cumulative_sum = [0] * (play_time_sec + 2)
    for i in range(1, play_time_sec + 2):
        cumulative_sum[i] = cumulative_sum[i-1] + timeline[i-1]
    
    max_view_time = 0
    best_start_time = 0

    # 0초부터 가능한 모든 광고 시작 시간을 순회
    for start_time in range(play_time_sec - adv_time_sec + 1):
        end_time = start_time + adv_time_sec
        
        # O(1) 시간에 구간 합 계산
        current_view_time = cumulative_sum[end_time] - cumulative_sum[start_time]
        
        if current_view_time > max_view_time:
            max_view_time = current_view_time
            best_start_time = start_time
    
    return sec_to_time(best_start_time)