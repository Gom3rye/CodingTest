import sys
input = sys.stdin.readline

# -------------------------------------------------------
# 직사각형 클래스
# -------------------------------------------------------
class Rect:
    def __init__(self, x1, y1, x2, y2):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2

    # 두 직사각형이 "외부 포함 없이" 닿거나 겹치는지 확인
    def intersects(self, other):
        # 1) 한쪽이 다른 쪽 내부에 완전히 포함되면 false
        if (self.x1 < other.x1 and self.y1 < other.y1 and
            self.x2 > other.x2 and self.y2 > other.y2):
            return False

        if (other.x1 < self.x1 and other.y1 < self.y1 and
            other.x2 > self.x2 and other.y2 > self.y2):
            return False

        # 2) 겹치지 않는 경우 false
        if self.x2 < other.x1:  # self가 왼쪽
            return False
        if other.x2 < self.x1:  # other가 왼쪽
            return False
        if self.y2 < other.y1:  # self가 아래
            return False
        if other.y2 < self.y1:  # other가 아래
            return False

        # 3) 나머지는 모두 겹침 또는 접함
        return True


# -------------------------------------------------------
# Union-Find
# -------------------------------------------------------
def find(x):
    if uf[x] != x:
        uf[x] = find(uf[x])
    return uf[x]

def union(a, b):
    ra = find(a)
    rb = find(b)
    if ra != rb:
        uf[rb] = ra


# -------------------------------------------------------
# 입력 처리 / 초기화
# -------------------------------------------------------
N = int(input())
rects = [Rect(0, 0, 0, 0)]  # 인덱스 0 = 시작점(0,0) 가상 직사각형

for _ in range(N):
    x1, y1, x2, y2 = map(int, input().split())
    rects.append(Rect(x1, y1, x2, y2))

uf = [i for i in range(N + 1)]

# -------------------------------------------------------
# 모든 쌍 체크하여 Union
# -------------------------------------------------------
for i in range(N + 1):
    for j in range(i + 1, N + 1):
        if rects[i].intersects(rects[j]):
            union(i, j)

# Find로 부모 갱신
for i in range(N + 1):
    uf[i] = find(uf[i])

# -------------------------------------------------------
# 그룹 개수 세기
# -------------------------------------------------------
# (0,0) 그룹 하나는 제외
answer = len(set(uf)) - 1
print(answer)
