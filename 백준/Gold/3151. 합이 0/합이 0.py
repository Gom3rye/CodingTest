import sys
from collections import Counter
input = sys.stdin.readline
def solution():
    n = int(input())
    a = sorted(map(int, input().split()))
    # n<=10000으로 매우 크기 때문에 3중 for문은 안되고 0~n-3까지의 수를 고정시켜 놓고 그 안에서 투포인터로 2개 고르기 -> O(n^2)
    counter = Counter(a)
    cnt = 0
    for i in range(n-2):
        one = a[i] # 고정시켜놓고
        two, three = i+1, n-1
        while two < three:
            result = one + a[two] + a[three]
            if result < 0:
                two += 1
            elif result > 0:
                three -= 1
            else: # result == 0:
                if a[two] == a[three]:
                    # 정렬되어 있는 상태니까 two인덱스 이후 a[three]의 개수는
                    cnt += three-two
                else: 
                    cnt += counter[a[three]]
                two += 1
    print(cnt)      
solution()