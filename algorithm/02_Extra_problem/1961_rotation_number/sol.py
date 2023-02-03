import sys
sys.stdin = open('input.txt')

test_case = int(input())
for tc in range(1, test_case+1):

    N = int(input())
    arr =[]

    for i in range(N):
        num_arr = list(map(int, input().split()))
        arr.append(num_arr)

    print(arr)
    print('#' * 30)
    r1_arr = []
    for i in range(N):
        for j in range(N-1,-1,-1):
            r1_arr.append(arr[j][i])
    print(r1_arr)
    print('#' * 30)

    for i in range(N)


