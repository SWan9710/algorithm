import sys
sys.stdin = open('input.txt')

test_case = int(input())
for tc in range(1,test_case+1):

    N = int(input())
    arr = list(map(int, input().split()))

    # 오름차순 정렬
    for i in range(N-1):                                    # 정렬을 위해 N보다 1작은 값까지 탐색
        min_value = i                                       # 최솟값을 첫째 값으로 설정
        for j in range(i+1, N):                             # j 값은 1부터 시작해서 N까지 1씩 커질때
            if arr[min_value] > arr[j]:                     # 첫번째 값이 j 값보다 클 경우
                min_value = j                               # 최솟값을 j로 바꾸고
        arr[i], arr[min_value] = arr[min_value], arr[i]     # i값에 현재 위치 넣고 최솟값에 바꾼값 넣어주는 형식

    # 낮은값 절반 넣기
    small_arr = []                                          # 오름차순으로 정렬된 값중 절반만 넣어줌
    for i in range(N//2):
        small_arr.append(arr[i])

    # 내림차순 정렬
    for i in range(N-1):
        max_value = i
        for j in range(i+1, N):
            if arr[max_value] < arr[j]:
                max_value = j
        arr[i], arr[max_value] = arr[max_value], arr[i]

    # 높은값 절반 넣기
    big_arr = []                                            # 높은값의 절반만 넣어줌
    for i in range(N//2):
        big_arr.append((arr[i]))

    total_arr = []                                          # 최종결과를 저장하기 위해 빈 배열에
    for i in range(N//2):                                   # 큰값과 작은값을 순서대로 넣어줌
        total_arr.append(big_arr[i])
        total_arr.append(small_arr[i])

    print(f'#{tc}', *total_arr[:10])                        # 10번째 값까지 출력





