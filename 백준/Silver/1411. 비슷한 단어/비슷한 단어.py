import sys
import math
replace_word = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

n = int(sys.stdin.readline())

s_dict = {}
for _ in range(n):
    count = 0
    s = sys.stdin.readline().rstrip()

    for i in range(len(s)):
        if s[i].isupper():
            continue
        s = s.replace(s[i],replace_word[count])
        count+=1

    if s not in s_dict:
        s_dict[s] = 1
    else:
        s_dict[s] +=1

result = 0
for v in s_dict.values():
    result += math.comb(v,2)

print(result)