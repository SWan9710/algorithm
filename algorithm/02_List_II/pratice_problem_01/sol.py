import sys
sys.stdin = open('input.txt')

test_case = int(input())
for tc in range(1, test_case+1):
    N = int(input())

    arr = []
    for i in range(N):
        input_arr = list(map(int, input().split()))
        arr.append((input_arr))

    move_x = [0, 1, 0, -1]
    move_y = [1, 0, -1, 0]

    result = 0
    for i in range(N):
        for j in range(N):

            for k in range(4):
                ni = i + move_x[k]
                nj = j + move_y[k]
                if ni >= 0 and ni < N:
                    if nj >= 0 and nj < N:
                        result += abs(arr[ni][nj] - arr[i][j])
    print(f'#{tc} {result}')


