import sys
sys.stdin = open('input.txt')

def DFS(start):
    visited[start] = 1
    # print(start, end=' ')
    if start == E:
        # print()
        return
    for next in range(1, V+1):
        if data[start][next] and not visited[next]:
            DFS(next)


T = int(input())
for tc in range(1,T+1):

    V, E = map(int, input().split())
    # 인접 행렬
    data = [[0] * (V+1) for i in range(V+1)]
    # 방문 표시용 리스트
    visited = [0] * (V+1)

    # 간선정보 만들기
    for _ in range(E):
        x, y = map(int, input().split())
        # print(x, y)
        data[x][y] = 1

    # 시작지점 S, 도착지점 E
    S, E = map(int, input().split())
    print(DFS(S))
    print(visited[E])