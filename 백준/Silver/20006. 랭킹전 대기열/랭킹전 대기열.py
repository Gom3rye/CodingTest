import sys
input = sys.stdin.readline
def solution():
    p, m = map(int, input().split()) # #player <=300, 방의 정원 <=300
    # 한 방의 레벨 차이는 처음 입장한 레벨 기준으로 쁠마 10까지 가능
    # 방에 있는 플레이어들은 닉네임 사전순으로 출력
    # 모든 플레이어 매칭이 끝난 후 방 단위로 한 번만 출력 이때, 
    # 인원 == m → Started!
    # 인원 < m → Waiting!

    # 방의 개수는 미리 정할 수 없고 방마다 관리해야 할 정보가 여러 개라서 []+dict로 선언!
    rooms = []
    for _ in range(p):
        level, nickname = input().split()
        level = int(level)

        # 기존 방에 넣을 수 있는지 확인
        for room in rooms: # room: dict
            if len(room['player']) < m and abs(room['start']-level) <= 10:
                room['player'].append((level, nickname))
                break
        # 못 넣는 다면    
        else:
            rooms.append({
                'start': level,
                'player': [(level, nickname)]
            })
    
    for room in rooms:
        if len(room['player']) == m:
            print('Started!')
        else:
            print('Waiting!')
        room['player'].sort(key=lambda x: x[1])
        for lv, nic in room['player']:
            print(lv, nic)
        
solution()