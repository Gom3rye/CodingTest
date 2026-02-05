import sys
input = sys.stdin.readline
def solution(word):
    # 단어 개수는 최대 5(한자리수)+5^2(두자리수)+5^3(3자리수)+5^4(4자리수)+5^5(다섯자리수)=3905
    # 자리 별 가중치를 통해 풀면 된다!
    # 1자리수 뒤에 올 수 있는 경우의 수(최대 4자리수까지 붙을 수 있음), 2자리수 뒤에 올 수 있는 경우의 수(최대 3자리수까지 붙을 수 있음), 3자리수 뒤에 올 수 있는 경우의 수(최대 2자리수까지 붙을 수 있음)...
    weights = [1+5+25+125+625, 1+5+25+125, 1+5+25, 1+5, 1]
    alpha_dict = {'A':0, 'E':1, 'I':2, 'O':3, 'U':4}
    answer = 0
    for i, w in enumerate(word):
        answer += alpha_dict[w]*weights[i]+1
    return answer