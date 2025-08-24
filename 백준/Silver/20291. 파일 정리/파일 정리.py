import sys
from collections import defaultdict

input = sys.stdin.readline

n = int(input())
ext_count = defaultdict(int)

for _ in range(n):
    filename = input().strip()
    ext = filename.split('.')[-1]
    ext_count[ext] += 1

for ext in sorted(ext_count):
    print(f"{ext} {ext_count[ext]}")