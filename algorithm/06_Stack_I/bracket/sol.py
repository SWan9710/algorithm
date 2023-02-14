import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    bracket = input()
    # print(bracket)

    stack = []
    result = 1
    for i in bracket:
        if i == '(':
            stack.append(i)
        else:
            if stack:
                stack.pop()
            else:
                result = -1
                break
    else:
        if stack:
            result = -1
    print(result)
