import sys
sys.setrecursionlimit(10**9)
input = sys.stdin.readline

preorder = []
while True:
    line = input().rstrip()
    if not line:
        break
    preorder.append(int(line))

def solve(start, end):
    if start > end:
        return
    
    root = preorder[start]
    idx = start + 1

    # 오른쪽 서브트리가 시작하는 지점 찾기
    while idx <= end and preorder[idx] < root:
        idx += 1

    # 왼쪽 서브트리
    solve(start + 1, idx - 1)

    # 오른쪽 서브트리
    solve(idx, end)

    # 후위 순회: root 출력
    print(root)

solve(0, len(preorder) - 1)
