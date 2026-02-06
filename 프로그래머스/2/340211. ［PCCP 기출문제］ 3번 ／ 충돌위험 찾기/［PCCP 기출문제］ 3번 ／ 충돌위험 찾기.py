from collections import Counter
def solution(points, routes):
    nrobot = len(routes) #로봇 <=100
    m = len(routes[0]) # 이동 수
    # point -> coordinates로 보여주는 map 만들기
    point_map = {p+1:(x, y) for p, (x,y) in enumerate(points)} # 1based index
    # 모든 로봇의 이동 경로 추적하기
    all_robots_path = []
    for robot in routes: # robot당
        path = []
        for route in range(m-1): # 1로봇의 경로 당
            (sx, sy), (ex, ey) = point_map[robot[route]], point_map[robot[route+1]]
            if route == 0: # 처음에만 sx, sy 넣어주기
                path.append((sx, sy))
            # r먼저 움직임
            while sx != ex:
                if sx > ex: sx -= 1
                else: sx += 1
                path.append((sx, sy))
            # c후에 움직임
            while sy != ey:
                if sy > ey: sy -= 1
                else: sy += 1
                path.append((sx, sy)) 
        
        all_robots_path.append(path)
        
    # 겹치는 부분이 있는지 시간마다 확인
    answer = 0
    max_time = max(len(path) for path in all_robots_path)
    # 매 시간마다 검사
    for time in range(max_time):
        spots = []
        for path in all_robots_path:
            if time < len(path):
                spots.append(path[time])
        count = Counter(spots)
        for c in count.values():
            if c >= 2:
                answer += 1
    return answer