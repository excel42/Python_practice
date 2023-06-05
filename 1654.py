#백준 1654 랜선 자르기
import sys

k, n = map(int, sys.stdin.readline().split()) #가지고 있는 랜선수, 목표 개수
arr = []

for i in range(k):
    arr.append(int(input()))

start = 1 #최솟값 1
end = max(arr) #최대길이

#이분탐색
while(start <= end):
    mid = (start + end) //2 # 최대값의 반
    cnt = 0
    for i in range(k):
        cnt += arr[i] // mid
    if cnt >= n:
        start = mid +1 #최대값이 개수를 만들때 +1하고 끝냄
    else:
        end = mid -1 #최대값이 개수를 못만들때 -1

print(end)