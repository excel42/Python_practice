#백준 2751 수 정렬하기 2
#오름차순 정렬
import sys
input=sys.stdin.readline

n = int(input())
list1 = []

for i in range(n):
    list1.append(int(input()))

# print('결과 출력')
for j in sorted(list1):
    print(j)

