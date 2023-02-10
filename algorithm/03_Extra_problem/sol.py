import sys
sys.stdin = open('input.txt')

# 행우선 탐색
def search(arr,N, M):
    for i in range(N):
        treasure = 0
        for j in range(M-1):
            if arr[i][j] == 1:
                treasure += 1
                if arr[i][j+1] == 1:
                    treasure += 1
            eles:








T = int(input())
for tc in range(1,T+1):

    N, M = input().split()
    N, M = int(N), int(M)
    # 가로배열
    row_arr = [list(map(int, input().split())) for _ in range(M)]
    # 세로배열
    col_arr = [[0]*N for _ in range(M)]

    for i in range(N):
        for j in range(M):
            col_arr[i][j] = row_arr[j][i]

    # 행우선 탐색 실시



