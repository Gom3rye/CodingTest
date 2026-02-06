import sys
input = sys.stdin.readline
def solution():
    m, n = map(int, input().split()) # m이상 n이하의 정수 <=99
    alpha_dict = {0:'zero', 1:'one', 2:'two', 3:'three', 4:'four', 5:'five', 6:'six', 7:'seven', 8:'eight', 9:'nine'}
    answer = []
    for i in range(m, n+1):
        if i < 10: # 1의 자리인 경우
            answer.append((alpha_dict[i], i))
        else:
            s = alpha_dict[i//10]+alpha_dict[i%10]
            answer.append((s, i))
    answer.sort()
    # 이제 숫자만 10개 단위로 끊어서 출력
    for i, (_, num) in enumerate(answer, start=1): # 인덱스 시작값 1로
        print(num, end=' ')
        if i != 0 and i%10 == 0:
            print()
solution()