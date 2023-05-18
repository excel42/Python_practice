#백준 1753 최단거리 구하기(다익스트라)
import sys
input = sys.stdin.readline
from queue import PriorityQueue

V,E = map(int, input().split()) #노드 개수, 에지 개수
K = int(input())
distance = [sys.maxsize] * (V+1)
visited = [False] * (V+1) 
myList = [[] for _ in range(V+1)]
q = PriorityQueue()

for _ in range(E):
    u, v, w = map(int, input().split()) #가중치가 있는 인접 리스트 저장
    myList[u].append((v, w))

q.put((0, K))   #K를 시작점 설정
distance[K] = 0

while q.qsize() > 0:
    current = q.get()
    c_v = current[1]
    if visited[c_v]:
        continue
    visited[c_v] = True
    for tmp in myList[c_v]:
        next = tmp[0]
        value = tmp[1]
        if distance[next] > distance[c_v] + value:  #다익스트라 (최소거리로 업데이트)
            distance[next] = distance[c_v] + value
            #가중치가 정렬 기준이므로 순서를 가중치, 목표 노드 순으로 우선순위 큐 설정  
            q.put((distance[next], next)) 

for i in range(1, V+1):
    if visited[i]:
        print(distance[i])
    else:
        print("INF")    #경로 없을때 INF 출력

