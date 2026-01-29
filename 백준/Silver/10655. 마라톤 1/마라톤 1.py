import sys

def get_dist(p1, p2):
    # 맨해튼 거리 계산: |x1-x2| + |y1-y2|
    return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])

def solve():
    input = sys.stdin.read().split()
    if not input: return
    
    n = int(input[0])
    points = []
    idx = 1
    for _ in range(n):
        points.append((int(input[idx]), int(input[idx+1])))
        idx += 2
        
    # 1. 건너뛰지 않았을 때의 총 거리 구하기
    total_dist = 0
    for i in range(n - 1):
        total_dist += get_dist(points[i], points[i+1])
        
    # 2. 각 체크포인트를 건너뛸 때 줄어드는 최대 거리(이득) 찾기
    max_save = 0
    for i in range(1, n - 1):
        # i번을 거쳐갈 때의 거리
        original = get_dist(points[i-1], points[i]) + get_dist(points[i], points[i+1])
        # i번을 건너뛰고 직행할 때의 거리
        shortcut = get_dist(points[i-1], points[i+1])
        
        save = original - shortcut
        if save > max_save:
            max_save = save
            
    # 3. 전체 거리에서 가장 큰 이득을 뺌
    print(total_dist - max_save)

if __name__ == "__main__":
    solve()