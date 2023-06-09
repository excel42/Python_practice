#백준 1929 소수 구하기
#소수 : 자기 자신보다 작은 수로 나눴을때 나머지가 0이 아닌 수
import math
M, N = map(int, input().split())
A = [0] * (N+1) #소수 리스트 생성

for i in range(2, N+1): #리스트 초기화
    A[i] = i

for i in range(2, int(math.sqrt(N)) + 1): #제곱근까지 반복
    if A[i] == 0:
        continue
    for j in range(i+i, N+1, i): #배수 지우기
        A[j] = 0

for i in range(M, N+1):
    if A[i] != 0:
        print(A[i])