import sys
input = sys.stdin.readline
def solution():
    origin = input().strip()
    ip = origin.split(':') # 자동으로 list됨
    answer = ''
    def fill(string):
        answer = ''
        for s in string:
            answer += s.zfill(4)+':' # 4자리수 맞춰서
        return answer

    if len(ip) == 8:
        answer = fill(ip)
    else:
        # ::를 기준으로 왼쪽 그룹, 오른쪽 그룹을 나누기
        left, right = origin.split('::')
        left = left.split(':')
        right = right.split(':')
        nl = 0 if left == [''] else len(left)
        nr = 0 if right == [''] else len(right)
        zero_needed = 8-(nl+nr)
        if nl == 0 and nr == 0:
            answer = '0000:'*8
        elif nl == 0:
            answer = '0000:'*zero_needed+fill(right)
        elif nr == 0:
            answer = fill(left)+'0000:'*zero_needed
        else:
            answer = fill(left)+'0000:'*zero_needed+fill(right)
    print(answer[:-1])
solution()