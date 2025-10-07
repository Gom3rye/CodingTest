import sys

h, w = map(int,input().split())
n = int(input())
sticker = []
for _ in range(n):
	r,c = map(int,sys.stdin.readline().split())
	sticker.append([r,c])
max_n = 0
for i in range(n):
	r1 = sticker[i][0]
	c1 = sticker[i][1]
	for j in range(i+1,n):
		r2 = sticker[j][0]
		c2 = sticker[j][1]

		if (r1+r2 <= h and max(c1,c2) <= w) or (max(r1,r2) <= h and c1+c2 <= w):
			max_n = max(max_n, r1*c1+r2*c2)
		elif (r1+c2 <= h and max(c1,r2) <= w) or (max(r1,c2) <= h and c1+r2 <= w):
			max_n = max(max_n, r1*c1+r2*c2)
		elif (c1+r2 <= h and max(r1,c2) <= w) or (max(c1,r2) <= h and r1+c2 <= w):
			max_n = max(max_n, r1*c1+r2*c2)
		elif (c1+c2 <= h and max(r1,r2) <= w) or (max(c1,c2) <= h and r1+r2 <= w):
			max_n = max(max_n, r1*c1+r2*c2)
			
print(max_n)