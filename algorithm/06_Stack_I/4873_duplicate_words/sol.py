import sys
sys.stdin = open('input.txt')

# def search(words):
#     # 조사 대상 문자와 조사 대상 다음 문자가
#     # 같은지를 알아 보고,
#     # 같아면 다음 조사 대상에서 두 글자 모두 제외
#     # 다르면, 현재 조사대상인 문자는 다음 조사 대상에 포함
#     # 그리고, 조사 대상을 다음칸으로 이동
#     # 다음 조사 대상이 될 문자열을 내가 만들어 나갈거
#     temp = ''
#     i = 0
#     while i < len(words)-1:
#         if words[i] == words[i+1]:  # 현재 문자와 다음문자를 비교했는데 같다면
#             temp += words[i+2:]    # i, i+1 번째 빼고 전부 추가
#             words = temp            # words를 temp에 추가한 단어로 초기화
#             i = 0                   # i 값을 0으로 초기화
#             temp = ''               # temp 값도 초기화
#
#         else:                   # 현재 문자와 다음문자가 같지 않다면
#             temp += words[i]    # 빈 문자열에 현재 문자 추가
#             i += 1              # i 값을 증가시켜 조사할 위치를 계속 증가
#     return words
#
T = int(input())
for tc in range(1, T+1):

    words = input()
    stack = []

    # for i in words:
    #     if not stack:                   # stack에 값이 없다면 i값을 stack에 추가
    #         stack.append(i)
    #     elif stack and stack[-1] != i:  # stack에 값이 있고 마지막값이 i값이랑 다르면
    #         stack.append(i)
    #     elif stack and stack[-1] == i:  # stack에 값이 있고 마지막 값이 i값과 같다면
    #         stack.pop()                 # stack의 마지막 값을 제거

    for i in words:
        if stack and stack[-1] == i:      # stack에 값이 있고 마지막값이 i값과 같다면
            stack.pop()                   # stack의 마지막 값을 제거
        else:                             # 제거조건이 1개 뿐이니 나머지는 다 추가해줄거
            stack.append(i)               # 그래서 다 추가해줌
    print(f'#{tc} {len(stack)}')


