import sys
sys.stdin = open('input.txt')

test_case = int(input())
for tc in range(1, test_case+1):


    input_arr = list(map(int, input().split()))
    N = len(input_arr)

    for i in range(1, 1<<N):
        result = 0
        for j in range(N):
            if i & (1<<j):
                result += input_arr[j]
        if result == 0:
            print(f'#{tc}',1)
            break
    else:
        print(f'#{tc}',0)