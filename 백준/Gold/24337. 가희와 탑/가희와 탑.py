import sys
input = sys.stdin.readline
def solution():
    n, a, b = map(int, input().split()) # #건물 <=100,000, 가희가 볼 수 있는 건물, 단비가 볼 수 있는 건물 <=n
    # 불가능한 경우는 -1 출력, 어떨 때 불가능? -> a+b-1 > n
    if a+b-1 > n: # -1해주는 이유는 가장 높은 빌딩이 겹치니까
        print(-1)
        return
    # [1, 2, ..., a-1] [H] [1, 1, 1...] [b-1, ..., 2, 1]
    # 왼쪽에서 볼 수 있는 빌딩 수: a-1
    # 오른쪽에서 볼 수 있는 빌딩 수: b-1
    # 가운데서 가장 작아서 안 보이는 빌딩 수: n-a-b+1
    # 여기서 중요한 게 [1]들의 위치! 사전 순으로 입력하기 위해 최대한 앞에 놓아야 한다. -> a가 1인지 1이상 인지에 따라 다르다.
    buildings = []
    max_height = max(a, b)
    if a == 1:
        buildings.append(max_height) #1
        buildings.extend([1]*(n-b)) #n-b
        for i in range(b-1, 0, -1): #b-1
            buildings.append(i)
    else: # a>1
        buildings.extend([1]*(n-a-b+1))
        for i in range(1, a):
            buildings.append(i)
        buildings.append(max_height)
        for i in range(b-1, 0, -1):
            buildings.append(i)

    print(*buildings)
solution()