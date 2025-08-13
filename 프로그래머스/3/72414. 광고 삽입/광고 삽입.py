def solution(play_time, adv_time, logs):
    answer = ''
    # 시간을 모두 초로 바꾸기
    def time_to_sec(time):
        h, m, s = map(int, time.split(":"))
        return h*3600+m*60+s
    # 계산 결과는 시간으로 나타내줘야 하니까
    def sec_to_time(second):
        h = second//3600
        m = (second%3600)//60
        s = (second%3600)%60
        return f"{h:02d}:{m:02d}:{s:02d}"
    play_time = time_to_sec(play_time)
    timeline = [0]*(play_time+2)
    for log in logs:
        start, end = log.split("-")
        start, end = time_to_sec(start), time_to_sec(end)
        timeline[start] += 1
        timeline[end] -= 1
    # 1차 누적합 (해당 timeline에 몇 명이 재생하고 있는지 기록)
    for i in range(1, play_time+1):
        timeline[i] += timeline[i-1]
    # 2차 누적합 (제일 많은 사람들이 재생하고 있는 "구간"이 필요한 거니까)
    cumulative_sum = [0]*(play_time+2)
    for i in range(1, play_time+1):
        # i초까지 총 누적 재생 시간 구하기
        cumulative_sum[i] = cumulative_sum[i-1]+timeline[i-1]
        
    # 가장 많은 사람들이 재생하고 있는 구간의 start 지점 구하기
    max_ppl = 0
    adv_start = 0
    adv_time = time_to_sec(adv_time)
    for start in range(play_time-adv_time+1):
        end = start+adv_time
        ppl = cumulative_sum[end] - cumulative_sum[start]
        if ppl > max_ppl:
            max_ppl = ppl
            adv_start = start
    answer = sec_to_time(adv_start)
    return answer