import sys
sys.stdin = open('input.txt')

test_case = int(input())
for tc in range(1, test_case+1):

    N = int(input())
    arr = [input().split() for _ in range(N)]

    r1_arr = [[0]*N for _ in range(N)]
    r2_arr = [[0] * N for _ in range(N)]
    r3_arr = [[0] * N for _ in range(N)]

    # 회전각도에 따른 위치값을 저장
    for i in range(N):
        for j in range(N):
            r1_arr[i][j] = arr[N-1-j][i]
            r2_arr[i][j] = arr[N-1-i][N-1-j]
            r3_arr[i][j] = arr[j][N-1-i]

    print(f'#{tc}')
    # zip함수는 각 배열의 첫번째 값을 묶어서 해당하는 변수들에 각각 할당
    for a,b,c in zip(r1_arr,r2_arr,r3_arr):
        print(*a,' ',*b,' ',*c,sep='')