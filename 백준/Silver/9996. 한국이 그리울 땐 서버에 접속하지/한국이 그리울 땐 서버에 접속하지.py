def solution():
    n = int(input())
    pattern = input().strip()
    prefix, suffix = pattern.split("*")

    result = []
    for _ in range(n):
        filename = input().strip()
        # 길이가 패턴보다 짧으면 절대 안 맞음
        if len(filename) < len(prefix) + len(suffix):
            result.append("NE")
        elif filename.startswith(prefix) and filename.endswith(suffix):
            result.append("DA")
        else:
            result.append("NE")
    
    print('\n'.join(result))

solution()