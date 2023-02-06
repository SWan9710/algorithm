import sys
sys.stdin = open('input.txt')

test_case = int(input())
for tc in range(1, test_case+1):

    A = [1,2,3,4,5,6,7,8,9,10,11,12]
    N, K = map(int, input().split())
    length = len(A)
    result = 0
    for i in range(1, 1<<length):
        arr = []
        count = 0
        for j in range(length):
            if i & (1<<j):
                arr.append(A[j])
                count += A[j]
        if len(arr) == N and count == K:
            result += 1
    print(f'#{tc} {result}')