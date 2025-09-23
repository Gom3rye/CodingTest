import sys
from itertools import product # 가능한 숫자 조합 생성
input = sys.stdin.readline
def solution():
    n = int(input())
    s = list(map(int, input().split()))
    s1 = s[0] # A자리수
    s2 = s[1] # B자리수
    partial = s[2:-1] # 부분곱 자리수
    result = s[-1] # 결과 자리수
    k = int(input())
    available_num = set(map(int, input().split()))
    count = 0
    # A와 B의 모든 조합 시도
    for a in product(available_num, repeat=s1):
        if a[0] == 0: # 앞자리는 0이면 안됨
            continue
        a = int("".join(map(str, a))) # a 숫자로 만들기
        for b in product(available_num, repeat=s2):
            if b[0] == 0:
                continue
            for i in range(s2): # s2길이만큼
                part = a*b[i]
                part_str = str(part)
                if len(part_str) != partial[-(i+1)] or not (set(int(ch) for ch in part_str).issubset(available_num)):
                    break
            # 부분 곱들의 결과의 합이 result인지 확인
            else:
                # 결과 부분 확인
                b = int("".join(map(str, b))) # b 숫자로 만들기 (a*b로 결과 비교 위해서)
                cal_result = a*b
                cal_result_str = str(cal_result)
                if len(cal_result_str) == result and set(int(ch) for ch in cal_result_str).issubset(available_num):
                    count += 1

    print(count)
solution()