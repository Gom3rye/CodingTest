import sys
from collections import deque
input = sys.stdin.readline

def solution():
    a, b = map(int, input().split())  # A → B
    def bfs():
        q = deque([b])
        distance = {b: 1}  # 시작 거리 1
        while q:
            num = q.popleft()
            if num == a:
                return distance[num]

            # 연산 1: 끝이 1이면 (x - 1) // 10
            if num % 10 == 1:
                next_num = (num - 1) // 10
                if next_num >= a and next_num not in distance:
                    distance[next_num] = distance[num] + 1
                    q.append(next_num)
            # 연산 2: 짝수이면 //2
            if num % 2 == 0:
                next_num = num // 2
                if next_num >= a and next_num not in distance:
                    distance[next_num] = distance[num] + 1
                    q.append(next_num)
        return -1
    print(bfs())

solution()