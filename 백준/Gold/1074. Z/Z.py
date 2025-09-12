def z(n, r, c):
    result = 0
    size = 2 ** n

    while n > 0:
        half = size // 2
        quadrant_size = half * half

        if r < half and c < half:  # 1사분면 (왼쪽 위)
            pass  # result += 0
        elif r < half and c >= half:  # 2사분면 (오른쪽 위)
            result += quadrant_size
            c -= half
        elif r >= half and c < half:  # 3사분면 (왼쪽 아래)
            result += 2 * quadrant_size
            r -= half
        else:  # 4사분면 (오른쪽 아래)
            result += 3 * quadrant_size
            r -= half
            c -= half

        size = half
        n -= 1

    return result

# 입력 처리
N, r, c = map(int, input().split())
print(z(N, r, c))
