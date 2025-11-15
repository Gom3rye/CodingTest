import sys
import heapq
input = sys.stdin.readline

T = int(input())

for _ in range(T):
    k = int(input())
    min_h = []
    max_h = []
    count = dict()

    for __ in range(k):
        cmd, num = input().split()
        num = int(num)

        if cmd == 'I':
            # insert
            heapq.heappush(min_h, num)
            heapq.heappush(max_h, -num)
            count[num] = count.get(num, 0) + 1

        else:  # cmd == "D"
            if num == -1:
                # delete min
                while min_h and count.get(min_h[0], 0) == 0:
                    heapq.heappop(min_h)

                if min_h:
                    v = heapq.heappop(min_h)
                    count[v] -= 1

            else:
                # delete max
                while max_h and count.get(-max_h[0], 0) == 0:
                    heapq.heappop(max_h)

                if max_h:
                    v = -heapq.heappop(max_h)
                    count[v] -= 1

    # 최종 정리
    # lazy deletion 마무리
    while min_h and count.get(min_h[0], 0) == 0:
        heapq.heappop(min_h)

    while max_h and count.get(-max_h[0], 0) == 0:
        heapq.heappop(max_h)

    if not min_h or not max_h:
        print("EMPTY")
    else:
        print(-max_h[0], min_h[0])
