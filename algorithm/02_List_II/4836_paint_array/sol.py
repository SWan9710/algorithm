import sys
sys.stdin = open('input.txt')

test_case = int(input())
for tc in range(1, test_case+1):

    N = int(input())
    arr = [[0] * 10 for _ in range(10)]

    for i in range(N):
        r1, r2, c1, c2, color = map(int, input().split())

        for i in range(r1, c1+1):
            for j in range(r2, c2+1):
                arr[i][j] += color

    count = 0
    for i in range(10):
        for j in range(10):
            if arr[i][j] == 3:
                count += 1
    print(f'#{tc} {count}')
    # for i in range(10):
    #     print(arr[i])

