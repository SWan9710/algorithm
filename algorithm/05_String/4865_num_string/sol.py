import sys
sys.stdin = open('input.txt')

test_case = int(input())
for tc in range(1, test_case+1):
    str1 = list(input())
    str2 = list(input())

    # 누적합을 구해줄 리스트
    result = [0] * len(str1)

    # 찾을 문자열의 갯수를 i 번째로 고정 후 전체 탐색하며 누적합 진행
    for i in range(len(str1)):
        for j in range(len(str2)):
            if str1[i] == str2[j]:
                result[i] += 1

    # 이후 누적합 리스트를 버블소트를 이용하여 정렬
    for i in range(len(result)-1,-1,-1):
        for j in range(i):
            if result[j] > result[j+1]:
                result[j], result[j+1] = result[j+1], result[j]
    print(f'#{tc}',result[-1])