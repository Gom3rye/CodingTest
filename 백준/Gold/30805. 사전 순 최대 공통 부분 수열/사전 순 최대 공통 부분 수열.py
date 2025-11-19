import sys
input = sys.stdin.readline

# 입력 받기
n = int(input())
arrA = list(map(int, input().split()))
m = int(input())
arrB = list(map(int, input().split()))

# 두 수열의 공통되는 숫자 집합 구하기
common_elements = set(arrA) & set(arrB)

# 공통되는 숫자가 없으면 0 출력 후 종료
if not common_elements:
    print(0)
    exit()

result = []
while common_elements:
    # 공통 숫자들 중 최대값 찾기
    max_val = max(common_elements)
    result.append(max_val)

    # 각각의 A와 B 수열에서 최대값 이후의 부분 수열로 업데이트
    idx1 = arrA.index(max_val)
    idx2 = arrB.index(max_val)
    arrA = arrA[idx1 + 1:]
    arrB = arrB[idx2 + 1:]

    # 새로운 공통 숫자 집합 구하기
    common_elements = set(arrA) & set(arrB)

# 결과 출력
print(len(result))
print(*result)