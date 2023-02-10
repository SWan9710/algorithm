import sys
sys.stdin=open('input.txt')

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    # 입력받은 배열의 상하좌우에 [0] 배열을 더해줌
    arr =[[0] * (M+2)] + [[0] +list(map(int, input().split())) + [0] for _ in range(N)] + [[0] * (M+2)]

    count = 0
    for i in range(1,N+1):
        for j in range(1,M+1):
            result = 0
            result += arr[i][j] + arr[i][j+1] + arr[i][j-1] + arr[i+1][j] + arr[i-1][j]
            if result > count:
                count = result
    print(f'#{tc}',count)

    # dx = [0, 1, 0, -1]
    # dy = [1, 0, -1, 0]
    #
    # result = 0
    # for i in range(N):
    #     for j in range(M):
    #
    #         count = 0
    #         for k in range(4):
    #             mi = i + dx[k]
    #             mj = j + dy[k]
    #             if mi >= 0 and mi < N:
    #                 if mj >= 0 and mj < M:
    #                     count += arr[mi][mj]
    #         count += arr[i][j]
    #         if count > result:
    #             result = count
    #
    # print(f'#{tc}',result)
