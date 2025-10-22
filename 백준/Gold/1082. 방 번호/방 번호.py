n = int(input())
arr = list(map(int,input().split()))
m = int(input())

d = [-10000 for _ in range(m+1)]
# 방 번호 높은 순 조회
for i in range(n-1,-1,-1):
    # 방 가격
    x = arr[i]
    # x원 밑으로는 살 수 없으므로 x원부터 m원까지 조사
    for j in range(x,m+1):
        # d[j] : 현재 방 번호
        # i : 현재 인덱스
        # d[j-x]*10+i :현재 가격에서 x원 만큼 뺀거에 x원만큼 살 수 있는거
        d[j] = max(d[j],i,d[j-x]*10+i)

print(d[m])