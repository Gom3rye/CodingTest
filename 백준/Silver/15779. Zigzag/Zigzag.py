n = int(input())
n_list = list(map(int,input().split()))
max_l = 2
cnt = 2
for i in range(n-2):
	if n_list[i] <= n_list[i+1] and n_list[i+1] <= n_list[i+2]:
		cnt = 2

	elif n_list[i] >= n_list[i+1] and n_list[i+1] >= n_list[i+2]:
		cnt = 2

	else: 
		cnt += 1
	max_l = max(max_l,cnt)
print(max_l)