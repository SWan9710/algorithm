import sys
sys.stdin = open('input.txt')

test_case = int(input())
for tc in range(1, test_case+1):
    N = int(input())
    arr = []
    for i in range(N):
        alphabet, num = input().split()
        arr.append(alphabet*int(num))
    result = ''
    for i in range(len(arr)):
        result += arr[i]

    print(f'#{tc}')
    for i in range((len(result)//10)+1):
        for j in range(i*10, (i+1)*10):
            print(result[j], end='')
            if j == len(result)-1:
                break
        print()