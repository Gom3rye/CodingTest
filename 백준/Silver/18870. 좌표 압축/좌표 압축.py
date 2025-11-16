import sys
input = sys.stdin.readline

N = int(input())
arr = list(map(int, input().split()))

# 1. 중복 제거 후 정렬
uniq = sorted(set(arr))

# 2. 각 숫자 → 압축된 번호 매핑
compressed = {value: idx for idx, value in enumerate(uniq)}

# 3. 출력 (원래 순서 유지)
print(' '.join(str(compressed[x]) for x in arr))
