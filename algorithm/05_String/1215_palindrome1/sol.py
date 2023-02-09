import sys
sys.stdin = open('input.txt')

def count_arr(arr, N):

    reverse_arr = []                                            # 회문인지 비교하기 위해 글자를 뒤집어서 저장할 배열
    array = []                                                  # 회문인지 비교하기 위해 글자를 앞에서부터 저장할 배열

    # 역방향
    for i in range(8):                                          # 배열의 크기가 8로 고정
        for j in range(9 - N):                                  # 자기자신 까지 검사하기 위해 9-N
                                                                # 회문의 크기가 4일때
            if j == 0:                                          # 첫번째 값일때 거꾸로 들고와야 하는데 3부터 -1에 해당하는 자리까지 들고와야 함
                reverse_arr.append(arr[i][N - 1::-1])           # 슬라이싱 할때 -1을 넣으면 빈 배열을 들고와서 0일때는 끝까지 들고오는 경우라 if로 조건 지정
            else:
                reverse_arr.append(arr[i][N - 1 + j:j - 1:-1])  # 1이상일 때는 슬라이싱해도 -1이 아닌 0부터 이므로 5 - > 1 까지는 4 부터 0까지 들고오는거라 j로 지정

    # 정방향
    for i in range(8):                                          # 정방향일때도 마찬가지
        for j in range(8 - N + 1):
            array.append(arr[i][j:j + N])                       # 슬라이싱 할때 j값이 1씩 늘어나고 가져오는 범위는 글자의 갯수만큼 이므로 + N 을 해줌

    count = 0                                                   # 회문의 갯수를 세기위해 count 변수 설정
    for i in range(len(reverse_arr)):                           # 뒤집은 배열과 정방향 배열의 첫번째 값은 같은 위치에 있는 값을 가져온것이기 때문에
        if reverse_arr[i] == array[i]:                          # i값을 1씩 늘려가며 서로 똑같은지 비교
            count += 1                                          # 서로 같다면 count +1 해줌
    return count                                                # 최종 count 값을 리턴해줌

for tc in range(1, 11):
    N = int(input())
    row_arr = []
    col_arr = []

    # 가로배열
    for i in range(8):                                          # 가로배열 만들기
        input_arr = list(input())
        row_arr.append(input_arr)

    # 세로배열
    for i in range(8):                                          # 세로배열 만들기
        new_arr = []                                            # 앞에값만 따와서 임시로 넣을 배열 new_arr[]를 만들어줌
        for j in range(8):                                      # 세로로 값을 들고와서 new_arr에 넣은다음 그 배열을
            new_arr.append(row_arr[j][i])                       # col_arr 배열에 넣어줌
        col_arr.append(new_arr)

    result = count_arr(row_arr, N) + count_arr(col_arr, N)
    print(f'#{tc} {result}')                                    # 함수를 불러오면 회문 여부를 검사한 후 count 를 반환하므로 2개를 더해서 result 에 넣어줌

