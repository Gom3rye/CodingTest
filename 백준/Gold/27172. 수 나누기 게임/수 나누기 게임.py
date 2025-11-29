import sys
from collections import deque

input = sys.stdin.readline

n = int(input())

l = []

# 정답을 저장할 딕셔너리 자료구조.
answer = dict()

# 입력받은 숫자의 최대값
maxNum = 0

# 입력
for i,num in enumerate([*map(int,input().strip().split())]):
    maxNum = max(maxNum, num)
    l.append((i,num))
    answer[num] = 0


# 입력받은 숫자를 작은 수대로 정렬함.
l.sort(key=lambda x : x[1])
   

# 입력 받은 숫자에 대해 하나하나 진행 시작.
for li in range(n):

	# 값을 num으로 받음.
    originPos, num = l[li]
    
    # 에라토스테네스의 체와 유사하게 운용
    # target은 num의 배수
    for target in range(num*2,maxNum+1, num):
    	
        # target이 만약 num에 등장한 값이라면 비교 시작.
        # target은 num의 배수이므로 무조건 target % num == 0 임.
        # 따라서 num이 무조건 이김.
        if target in answer :
            answer[num] += 1
            answer[target] -= 1
        
        
# answer를 순회하여 결과 출력
# dictionary 자료구조가 파이썬 3.6 이상에선 입력받은 순서를 기억한다고 함. 따라서 이 방식으로도 순서가 꼬이지 않음.
for key, item in answer.items():
    print(item,end=" ")