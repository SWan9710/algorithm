import sys
sys.stdin = open('input.txt')

test_case = int(input())
for tc in range(1, test_case+1):
    D, A, B, F = map(int, input().split())

    for i in range(test_case):
        result = D / (A+B)
        time = result * F

    print(f'#{tc} {time}')