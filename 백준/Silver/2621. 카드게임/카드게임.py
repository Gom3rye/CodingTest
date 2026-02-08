# 첫 번째 리스트는 색깔의 개수를 저장
# 두 번째 리스트는 숫자의 개수를 저장 (0~9까지, 인덱스 0은 사용되지 않음)
# 세 번째 리스트는 입력된 숫자를 저장 (스트레이트 계산에 활용)
card = [[0]*4, [0]*10, []]

# 5개의 카드 입력을 처리
for _ in range(5):
    color, idx = input().split()

    # 색깔별로 개수 증가
    if color == 'R':
        card[0][0] += 1  # 빨간색 카운트 증가
    elif color == 'B':
        card[0][1] += 1  # 파란색 카운트 증가
    elif color == 'Y':
        card[0][2] += 1  # 노란색 카운트 증가
    elif color == 'G':
        card[0][3] += 1  # 초록색 카운트 증가

    # 숫자별로 개수 증가
    card[1][int(idx)] += 1

    # 입력된 숫자 저장
    card[2].append(int(idx))

# 같은 색깔 카드가 5장인 경우
if 5 in card[0]:
    # 연속된 숫자인 경우 (스트레이트 플러시)
    if max(card[2]) - min(card[2]) == 4:
        print(max(card[2]) + 900)
    # 연속된 숫자가 아닌 경우 (플러시)
    else:
        print(max(card[2]) + 600)

# 같은 숫자 카드가 4장인 경우 (포카드)
elif 4 in card[1]:
    print(800 + card[1].index(4))

# 같은 숫자 카드가 3장인 경우
elif 3 in card[1]:
    # 추가로 같은 숫자 카드가 2장인 경우 (풀하우스)
    if 2 in card[1]:
        print(card[1].index(3)*10 + card[1].index(2) + 700)
    # 풀하우스가 아닌 경우 (트리플)
    else:
        print(card[1].index(3) + 400)

# 같은 숫자 카드가 2장인 경우
elif 2 in card[1]:
    # 두 개의 페어인 경우 (투 페어)
    if card[1].count(2) == 2:
        nums = []
        for i in range(1, 10):
            if card[1][i] == 2:
                nums.append(i)
        print(min(nums) + max(nums)*10 + 300)
    # 하나의 페어인 경우 (원 페어)
    else:
        print(card[1].index(2) + 200)

# 위의 모든 조건에 해당하지 않는 경우 (높은 카드)
else:
    # 연속된 숫자인 경우 (스트레이트)
    if max(card[2]) - min(card[2]) == 4:
        print(max(card[2]) + 500)
    # 그 외의 경우 (하이 카드)
    else:
        print(max(card[2]) + 100)