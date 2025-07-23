import sys
input = sys.stdin.readline
from collections import Counter
def solution():
    n, m = map(int, input().split())
    lamps = [input().strip() for _ in range(n)]
    k = int(input())

    # row 별로 같은 패턴이 있는 걸 구하고 하나씩 1로 만들어본다.
    rpattern = Counter(lamps)
    # count 기준으로 내림차순 정렬
    stdrpattern = rpattern.most_common()

    for pattern, count in stdrpattern:
        num_zero = pattern.count('0')
        if k >= num_zero and (k-num_zero)%2==0:
            print(count)
            break
    else:
        print(0)
solution()