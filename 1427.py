#백준 1427 내림차순 정렬(선택정렬)
import sys
print = sys.stdout.write()    #줄바꿈 없이 바로 이어서 출력
A = list(input())   #list 자료형 입력

for i in range(len(A)):
    Max = i
    for j in range(i+1, len(A)):
        if A[j] > A[Max]:   #최댓값 찾기
            Max = j
    
    if A[i] < A[Max]: #현재 i값과 최대값을 비교해 switch 연산
        temp = A[i]
        A[i] = A[Max]
        A[Max] = temp

for i in range(len(A)):
    print(A[i])