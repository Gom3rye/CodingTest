import sys

def is_cyclic(s):
    n = len(s)
    num = int(s)
    double_s = s + s
    
    # 1부터 n까지 곱하며 확인
    for i in range(1, n + 1):
        res = str(num * i).zfill(n)
        
        # 곱셈 결과의 자릿수가 n을 넘어가면 cyclic이 될 수 없음
        if len(res) > n:
            return False
            
        # 결과가 s + s 안에 부분 문자열로 존재하지 않으면 False
        if res not in double_s:
            return False
            
    return True

def solution():
    # 모든 입력을 한꺼번에 읽어들임
    lines = sys.stdin.read().splitlines()
    
    for line in lines:
        s = line.strip()
        if not s:
            continue
            
        if is_cyclic(s):
            print(f"{s} is cyclic")
        else:
            print(f"{s} is not cyclic")

if __name__ == "__main__":
    solution()