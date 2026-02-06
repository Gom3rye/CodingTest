def solution(video_len, pos, op_start, op_end, commands):
    # 문자 시간 -> 숫자 시간
    def string_to_num(string):
        hour, minute = string.split(':')
        return int(hour)*60+int(minute)
    # 숫자 시간 -> 문자 시간
    def num_to_string(num):
        hour, minute = num//60, num%60
        return str(hour).zfill(2)+":"+str(minute).zfill(2)
    # 필요한 변수들 다 숫자로 변환
    end = string_to_num(video_len)
    now = string_to_num(pos)
    op_s = string_to_num(op_start)
    op_e = string_to_num(op_end)
    
    n = len(commands) # 명령의 개수
    for i in range(n):
        # 오프닝 구간인지 확인
        if op_s<=now<=op_e:
            now = op_e
        if commands[i] == 'next':
            now = min(end, now+10)
        else: # prev
            now = max(0, now-10)
    # 마지막으로 오프닝 구간인지 확인
    if op_s<=now<=op_e:
        now = op_e
    # 정답 시간 문자로 변환
    answer = num_to_string(now)
    return answer