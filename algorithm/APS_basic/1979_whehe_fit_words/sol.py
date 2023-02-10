import sys
sys.stdin = open('input.txt')

def count(arr):
    result = 0
    for lst in arr:
        cnt = 0
        for n in lst:
            if n == 1:      # 단어를 넣을 수 있는 공백
                cnt += 1
            else:           # 칸 없음
                if cnt == K:
                    result += 1
                cnt = 0
    return result

test_case = int(input())
for tc in range(1,test_case+1):
    N, K = map(int, input().split()) # 배열의 수, 단어의 길이
    arr = [list(map(int, input().split())) + [0] for _ in range(N)] + [[0]*(N+1)]

    # row arr와 arr_t로 각각 개수를 계산
    arr_t = list(map(list, zip(*arr)))  # arr을 언패킹 한다음 zip으로 묶은걸 map으로 list로 형변환 한걸 다시 list?
    result = count(arr) + count(arr_t)

    print(f'#{tc} {result}')