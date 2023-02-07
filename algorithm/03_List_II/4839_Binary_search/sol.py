'''
예를 들어 책이 총 400쪽이면,
검색 구간의 왼쪽 l=1, 오른쪽 r=400이 되고,
중간 페이지 c= int((l+r)/2)로 계산한다.

찾는 쪽 번호가 c와 같아지면 탐색을 끝낸다.
'''

import sys
sys.stdin = open('input.txt')

test_case = int(input())
for tc in range(1,test_case+1):
    total_page, p1_search_page, p2_search_page = map(int, input().split())

    start = 1                                           # 시작값
    end = total_page                                    # 끝 값
    p1_count = 0                                        # P1 이 페이지를 찾는데 걸린 횟수

    while start <= end:                     # 시작값이 끝값보다 커지거나 같아지는 경우 종료
        middle = ((start + end) // 2)       # 중간값을 계속 바꿔주기 위해 while문 안에 middle값 설정
        if middle == p1_search_page:        # 원하는 페이지를 한번에 찾거나 찾았을 경우 count = 0 출력
            break
        elif middle > p1_search_page:       # 찾는값보다 중간값이 클경우
            p1_count += 1                   # 횟수를 1번 추가
            end = middle                    # 종료 시점을 중간값으로 설정
        else:
            p1_count += 1                   # 찾는값이 중간값보다 작을경우
            start = middle                  # 횟수를 1번 추가 후 시작지점을 중간값으로 설정

    if middle != p1_search_page:
        p1_count = 0

    start = 1
    end = total_page
    p2_count = 0

    while start <= end:
        middle = ((start + end) // 2)
        if middle == p2_search_page:
            break
        elif middle > p2_search_page:
            p2_count += 1
            end = middle
        else:
            p2_count += 1
            start = middle
    if middle != p2_search_page:
        p2_count = 0

    if p1_count < p2_count:             # 횟수비교
        print(f'#{tc} A')               # P1이 더 적게 걸렸을 경우
    elif p2_count < p1_count:           # P2가 더 적게 걸렸을 경우
        print(f'#{tc} B')
    else:                               # 비긴경우
        print(f'#{tc} 0')

