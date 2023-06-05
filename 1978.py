#백준 1978 소수 찾기

n = int(input()) #입력받을 숫자의 개수
data = list(map(int, input().split())) #소수 판별 숫자 입력 
count = 0 #결과값 변수

for x in data:  #data 값 전체 조회
    for i in range(2, x+1): # 최소 소수 2부터 최대값까지 조회
        if x % i == 0: #소수 인 경우
            if x == i:
                count += 1

            break
print(count)