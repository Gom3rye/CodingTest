def solution(schedules, timelogs, startday):
    answer = 0
    for i in range(len(schedules)):
        # deadline 형식에 맞게 구하기
        setting = schedules[i]
        setting +=10
        if setting%100 >= 60:
            hour = setting//100+1
            minute = (setting%100)%60
            deadline = hour*100+minute
        else:
            deadline = setting
        # 일주일간 잘 도착했는지 검사
        original_startday = startday
        for time in timelogs[i]:
            day=startday%7
            if day==6 or day==0:
                startday += 1
                continue
            if time > deadline:
                break
            startday += 1
        else:
            answer += 1
        startday = original_startday
    return answer