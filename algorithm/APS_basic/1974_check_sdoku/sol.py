import sys
sys.stdin = open('input.txt')

def solve(arr):
    # 행을 체크
    for lst in arr:
        if len(set(lst)) != 9:  # 스도쿠의 중복을 제거한 길이가 9가 아닐때
            return 0

    # 열을 체크 하기 위해 돌려주기
    arr_t = list(zip(*arr))
    for lst in arr_t:
        if len(set(lst)) != 9:  # 스도쿠의 중복을 제거한 길이가 9가 아닐때
            return 0

    # 격자형태 체크하기
    for i in (0, 3, 6):         # 스도쿠 가로행의 시작위치
        for j in (0, 3, 6):     # 스도쿠 세로열의 시작위치
            # 격자형태를 체크 할때도 스도쿠의 범위는 지정되어 있기 때문에
            # i값에 +1, +2등을 해줘도 되는거
            # j값 역시 슬라이싱의 범위가 고정되어 있기때문에 +3을 해주는거
            lst = arr[i][j:j+3] + arr[i+1][j:j+3] + arr[i+2][j:j+3]
            if len(set(lst)) != 9:
                return 0
    return 1


test_case = int(input())
for tc in range(1,test_case+1):
    sdoku_arr = []
    # 스도쿠 가져오기
    for i in range((tc * 9) - 9, tc * 9):
        sdoku = list(map(int, input().split()))
        sdoku_arr.append((sdoku))

    ans = solve(sdoku_arr)
    print(f'#{tc} {ans}')
