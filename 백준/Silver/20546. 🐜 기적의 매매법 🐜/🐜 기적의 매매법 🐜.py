Money = int(input())                                # 초기 현금
MachineDuck = list(map(int, input().split()))       # 1일부터 14일까지의 주가

# 준현이
money_bnp = Money   
count_bnp = 0

# 성민이
money_timing = Money
count_timing = 0

for num, price in enumerate(MachineDuck):

    # 준현
    count_bnp += (money_bnp // price)
    money_bnp %= price

    # 성민
    temp = MachineDuck[num:num+4]

    if len(temp) < 4:
        continue

    if temp[0] < temp[1] < temp[2] < temp[3] and count_timing > 0:         # 매도
        money_timing += (count_timing * temp[3])
        count_timing = 0
    elif temp[0] > temp[1] > temp[2] > temp[3]:                             # 매수
        count_timing += (money_timing // temp[3])
        money_timing %= temp[3]

answer_bnp = money_bnp + count_bnp * MachineDuck[-1]
answer_timing = money_timing + count_timing * MachineDuck[-1] 

if answer_bnp < answer_timing:
    print("TIMING")
elif answer_bnp > answer_timing:
    print("BNP")
else:
    print("SAMESAME")
