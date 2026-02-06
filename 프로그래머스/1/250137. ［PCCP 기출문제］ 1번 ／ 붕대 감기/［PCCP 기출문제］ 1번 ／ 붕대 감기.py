def solution(bandage, health, attacks):
    continuous = 0 # 연속 성공 시간
    n = len(attacks)
    hp = health # 현재 체력 hp = min(health, hp+heal), max(0, hp-attack)
    i, time = 0, 0 # 공격 인덱스, 현재 시간
    c, heal, additional = bandage # 연속t, 초당+, 추가+
    while i < n:
        if hp == 0:
            break
        time += 1
        attack_time, attack = attacks[i]
        if attack_time == time:
            hp = max(0, hp-attack)
            continuous = 0
            i += 1
        else:
            continuous += 1
            if continuous == c:
                continuous = 0
                hp = min(health, hp+heal+additional)
            else:
                hp = min(health, hp+heal)
        
    return hp if hp != 0 else -1