N = int(input()) # 입력받을 숫자의 수
A = [0]*N #입력받을 리스트 초기화

for i in range(N): #숫자 입력
    A[i] = int(input()) 

for i in range(N-1): # 버블정렬
    for j in range(N-1-i): 
        if A[j]>A[j+1]: 
            temp=A[j] 
            A[j]=A[j+1] 
            A[j+1]=temp 

for i in range(N): #결과 출력
    print(A[i]) 