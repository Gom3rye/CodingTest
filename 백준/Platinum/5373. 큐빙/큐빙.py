import sys
input = sys.stdin.readline
def solution():
    t = int(input()) # <=100
    # 시계방향으로 돌림
    def rotate(b, cw):
        # 시계방향으로 돌림
        if cw:
            return [list(row) for row in zip(*b[::-1])] # list(zip(*b[::-1]))
        # 반시게방향으로 돌림
        else:
            return [list(row) for row in zip(*b)][::-1] # list(zip(*b))[::-1]
    def simulate(ops):
        for op in ops:
            face, dir = op # 면, 방향
            # 면 회전 (rotate는 새 객체를 반환하는 거라 cube[face]를 갱신하는데 인자로 cube[face]를 넣어도 괜춘)
            # ex) 읽기 -> 새 객체 생성 -> 참조 교체
            cw = (dir == '+')
            cube[face] = rotate(cube[face], cw)
            
            # 띠 회전 (기준: U면을 위에서 내려다 본 상황)
            # 각 면 회전 시 영향을 받는 띠(Belt) 처리
            if face == 'U':
                # B(0행) -> R(0행) -> F(0행) -> L(0행)
                t = [*cube['B'][0],
                     *cube['R'][0],
                     *cube['F'][0],
                     *cube['L'][0]] # 12개의 원소를 1열로 linearize
                if cw: t = t[9:] + t[:9]
                else: t = t[3:] + t[:3]
                cube['B'][0][0], cube['B'][0][1], cube['B'][0][2] = t[0:3]
                cube['R'][0][0], cube['R'][0][1], cube['R'][0][2] = t[3:6]
                cube['F'][0][0], cube['F'][0][1], cube['F'][0][2] = t[6:9]
                cube['L'][0][0], cube['L'][0][1], cube['L'][0][2] = t[9:12]

            elif face == 'D':
                # F(2행) -> R(2행) -> B(2행) -> L(2행)
                t = [cube['F'][2][0], cube['F'][2][1], cube['F'][2][2],
                     cube['R'][2][0], cube['R'][2][1], cube['R'][2][2],
                     cube['B'][2][0], cube['B'][2][1], cube['B'][2][2],
                     cube['L'][2][0], cube['L'][2][1], cube['L'][2][2]]
                if cw: t = t[9:] + t[:9]
                else: t = t[3:] + t[:3]
                cube['F'][2][0], cube['F'][2][1], cube['F'][2][2] = t[0:3]
                cube['R'][2][0], cube['R'][2][1], cube['R'][2][2] = t[3:6]
                cube['B'][2][0], cube['B'][2][1], cube['B'][2][2] = t[6:9]
                cube['L'][2][0], cube['L'][2][1], cube['L'][2][2] = t[9:12]

            elif face == 'F':
                # U(2행) -> R(열) -> D(0행 역순) -> L(열 역순)
                t = [cube['U'][2][0], cube['U'][2][1], cube['U'][2][2],
                     cube['R'][0][0], cube['R'][1][0], cube['R'][2][0],
                     cube['D'][0][2], cube['D'][0][1], cube['D'][0][0],
                     cube['L'][2][2], cube['L'][1][2], cube['L'][0][2]]
                if cw: t = t[9:] + t[:9]
                else: t = t[3:] + t[:3]
                cube['U'][2][0], cube['U'][2][1], cube['U'][2][2] = t[0:3]
                cube['R'][0][0], cube['R'][1][0], cube['R'][2][0] = t[3:6]
                cube['D'][0][2], cube['D'][0][1], cube['D'][0][0] = t[6:9]
                cube['L'][2][2], cube['L'][1][2], cube['L'][0][2] = t[9:12]

            elif face == 'B':
                # U(0행 역순) -> L(열) -> D(2행) -> R(열 역순)
                t = [cube['U'][0][2], cube['U'][0][1], cube['U'][0][0],
                     cube['L'][0][0], cube['L'][1][0], cube['L'][2][0],
                     cube['D'][2][0], cube['D'][2][1], cube['D'][2][2],
                     cube['R'][2][2], cube['R'][1][2], cube['R'][0][2]]
                if cw: t = t[9:] + t[:9]
                else: t = t[3:] + t[:3]
                cube['U'][0][2], cube['U'][0][1], cube['U'][0][0] = t[0:3]
                cube['L'][0][0], cube['L'][1][0], cube['L'][2][0] = t[3:6]
                cube['D'][2][0], cube['D'][2][1], cube['D'][2][2] = t[6:9]
                cube['R'][2][2], cube['R'][1][2], cube['R'][0][2] = t[9:12]

            elif face == 'L':
                # U(열) -> F(열) -> D(열) -> B(열 역순)
                t = [cube['U'][0][0], cube['U'][1][0], cube['U'][2][0],
                     cube['F'][0][0], cube['F'][1][0], cube['F'][2][0],
                     cube['D'][0][0], cube['D'][1][0], cube['D'][2][0],
                     cube['B'][2][2], cube['B'][1][2], cube['B'][0][2]]
                if cw: t = t[9:] + t[:9]
                else: t = t[3:] + t[:3]
                cube['U'][0][0], cube['U'][1][0], cube['U'][2][0] = t[0:3]
                cube['F'][0][0], cube['F'][1][0], cube['F'][2][0] = t[3:6]
                cube['D'][0][0], cube['D'][1][0], cube['D'][2][0] = t[6:9]
                cube['B'][2][2], cube['B'][1][2], cube['B'][0][2] = t[9:12]

            elif face == 'R':
                # U(열 역순) -> B(열) -> D(열 역순) -> F(열 역순)
                t = [cube['U'][2][2], cube['U'][1][2], cube['U'][0][2],
                     cube['B'][0][0], cube['B'][1][0], cube['B'][2][0],
                     cube['D'][2][2], cube['D'][1][2], cube['D'][0][2],
                     cube['F'][2][2], cube['F'][1][2], cube['F'][0][2]]
                if cw: t = t[9:] + t[:9]
                else: t = t[3:] + t[:3]
                cube['U'][2][2], cube['U'][1][2], cube['U'][0][2] = t[0:3]
                cube['B'][0][0], cube['B'][1][0], cube['B'][2][0] = t[3:6]
                cube['D'][2][2], cube['D'][1][2], cube['D'][0][2] = t[6:9]
                cube['F'][2][2], cube['F'][1][2], cube['F'][0][2] = t[9:12]
            
    for _ in range(t):
        n = int(input()) # 큐브를 돌린 횟수 <=1000
        # 면마다 색이 다르니 딕셔너리로 정리
        cube = {
            'U':[['w']*3 for _ in range(3)],
            'D':[['y']*3 for _ in range(3)],
            'F':[['r']*3 for _ in range(3)],
            'B':[['o']*3 for _ in range(3)],
            'L':[['g']*3 for _ in range(3)],
            'R':[['b']*3 for _ in range(3)],
        }
        ops = input().split() # 자동으로 list 붙여서 나온다.
        simulate(ops)
        for row in cube['U']:
            print("".join(row))
solution()