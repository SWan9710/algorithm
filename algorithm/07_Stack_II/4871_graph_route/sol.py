import sys
sys.stdin = open('input.txt')

def DFS(start):
    # 첫 시작위치 방문정보 표기
    visited[start] = 1
    stack = [start]
    while stack:
        start = stack.pop()
        # print(start, end=' ')
        # 현재 조사 대상이 도착지점인지 아닌지 물어보는 조건문
        if start == G:
            # 만약 현재가 도착지점이면 더이상 반복하지 않고 함수 종료
            return 1

        # 아직 도착하지 않았다면 반복문을 돌면서 start 정보를 계속 들고옴
        for next in range(1, V+1):
            if data[start][next] and not visited[next]:
                visited[start] = 1
                stack.append(next)
    # 반복문을 다돌았는데 도착지점에 도착하지 못했다면 0 반환
    return 0

T = int(input())
for tc in range(1,T+1):

    V, E = map(int, input().split())
    # 인접 행렬
    data = [[0] * (V+1) for i in range(V+1)]
    # print(data)
    # 방문 표시용 리스트
    visited = [0] * (V+1)

    # 간선정보를 토대로 매트릭스에 추가하기
    for _ in range(E):
        x, y = map(int, input().split())
        # print(x, y)
        data[x][y] = 1

    # 시작지점 S, 도착지점 E
    S, G = map(int, input().split())
    # print(S, E)

    print(f'#{tc}',DFS(S))

