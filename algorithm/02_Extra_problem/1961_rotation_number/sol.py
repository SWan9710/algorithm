import sys
sys.stdin = open('input.txt')

test_case = int(input())
for tc in range(1, test_case+1):

    N = int(input())
    arr =[]

    for i in range(N):
        num_arr = list(map(int, input().split()))
        arr.append(num_arr)

    r1_arr = []
    for i in range(N):
        for j in range(N-1,-1,-1):
            r1_arr += str(arr[j][i])

    r2_arr = []
    for i in range(N-1, -1, -1):
        for j in range(N-1, -1, -1):
            r2_arr += str(arr[i][j])

    r3_arr = []
    for i in range(N-1, -1, -1):
        for j in range(N):
            r3_arr += str(arr[j][i])


    print(f'#{tc}')
    for i in range(N):
        print(*r1_arr[i * N:(i * N) + N],' ' ,*r2_arr[i * N:(i * N) + N], ' ',*r3_arr[i * N:(i * N) + N],sep='')

