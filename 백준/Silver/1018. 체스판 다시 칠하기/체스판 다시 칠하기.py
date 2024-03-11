import sys


if __name__ == '__main__':
    N, M = map(int, sys.stdin.readline().split())
    board = [list(sys.stdin.readline()) for _ in range(N)]
    save = []

    for g in range(N - 8 + 1):  # 전체 행
        for h in range(M - 8 + 1):  # 전체 열
            white = 0 #체스 첫 칸이 흰색일 경우
            black = 0 # 체스 첫 칸이 검은색일 경우
            
            for i in range(g, g+8):
                for j in range(h, h+8):
                    if (i+j)%2 == 0: 
                        if board[i][j]!='W':
                            white += 1
                        else:
                            black += 1
                    else:
                        if board[i][j]=='W':
                            white += 1
                        else:
                            black += 1

            save.append(min(white, black))

    print(min(save))