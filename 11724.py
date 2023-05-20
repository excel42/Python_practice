#백준 11724 연결요소의 개수
import sys
sys.setrecursionlimit(10000) #재귀함수 최대 깊이 설정
input = sys.stdin.readline
N,M = map(int,input().split())
A = [[] for _ in range(N+1)]
visited = [False] * (N+1)
result = 0

def DFS(v): #DFS 탐색 실행
    visited[v] = True
    for i in A[v]:
        if not visited[i]:
            DFS(i)

for _ in range(M): #에지 입력
    s, e = map(int, input().split())
    #양방향 에지이므로 양쪽에 에지 더함
    A[s].append(e)
    A[e].append(s)


for i in range(1, N+1): #연결 노드 중 방문x 노드만 탐색
    if not visited[i]:
        result += 1
        DFS(i)

print(result)