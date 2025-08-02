import sys
input = sys.stdin.readline

def solution():
    N = int(input())
    height = list(map(int, input().split()))
    
    max_visible = 0
    
    for i in range(N):
        count = 0
        for j in range(N):
            if i == j:
                continue
            
            visible = True
            # 기울기: (height[j] - height[i]) / (j - i)
            dx = j - i
            dy = height[j] - height[i]
            
            for k in range(min(i, j) + 1, max(i, j)):
                # 직선의 높이 예상
                # y = height[i] + dy * (k - i) / dx
                # k위치에서 예상 높이보다 실제 높이가 높으면 못 봄
                if height[k] >= height[i] + dy * (k - i) / dx:
                    visible = False
                    break
            
            if visible:
                count += 1
        
        max_visible = max(max_visible, count)
    
    print(max_visible)

solution()
