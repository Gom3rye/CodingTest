import sys
input = sys.stdin.readline
write = sys.stdout.write

def solution():
    m = int(input())
    mask = 0

    for _ in range(m):
        cmd = input().split()
        op = cmd[0]

        if op == 'add':
            x = int(cmd[1])
            mask |= (1 << x)

        elif op == 'remove':
            x = int(cmd[1])
            mask &= ~(1 << x)

        elif op == 'check':
            x = int(cmd[1])
            if mask & (1 << x):
                write("1\n")
            else:
                write("0\n")

        elif op == 'toggle':
            x = int(cmd[1])
            mask ^= (1 << x)

        elif op == 'all':
            mask = (1 << 21) - 2

        else:  # empty
            mask = 0

solution()