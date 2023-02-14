import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):

    words = input()
    bracket = []
    result = 1

    for i in words:
        if i =='(' or i == '{':
            bracket.append(i)
        else:
            if i == ')':
                if bracket and bracket[-1] == '(':
                    bracket.pop()
                elif not bracket:
                    result = 0
                    break
                elif bracket[-1] != '(':
                    result = 0
                    break

            if i == '}':
                if not bracket or bracket[-1] != '{':
                    result = 0
                    break
                else:
                    bracket.pop()
    if bracket:
        result = 0
    print(f'#{tc}',result)