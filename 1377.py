import sys
input = sys.stdin.readline

N = int(input()) #입력받을 총 개수
A =[]  #빈 리스트 초기화
for i in range(N):  #리스트에 index 순서대로 저장
    A.append((int(input()),i))

Max = 0
sorted_A = sorted(A)

for i in range(N):
    if Max < sorted_A[i][1] - i:    #정렬 전 index 정렬 후 index 비교
        Max = sorted_A[i][1] - i    #정렬 후 최대값만 저장

print(Max+1)
