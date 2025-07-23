import sys
input = sys.stdin.readline
from collections import Counter
def solution():
    n, m = map(int, input().split())
    lamps = [input().strip() for _ in range(n)]
    k = int(input())

    # row 별로 같은 패턴이 있는 걸 구하고 하나씩 1로 만들어본다.
    rpattern = Counter(lamps[i] for i in range(n)) # == Counter(lamps)
    stdrpattern = rpattern.most_common()
    for i in range(len(rpattern)):
        num_zero = stdrpattern[i][0].count('0')
        if k >= num_zero and (k-num_zero)%2==0:
            print(stdrpattern[i][1])
            break
    else:
        print(0)
solution()