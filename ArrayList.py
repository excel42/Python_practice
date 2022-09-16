n = int(input()) #정수 개수 입력
array_list = list(map(int, input().split())) # n개의 정수 입력

max_num = array_list[0] #최댓값
min_num = array_list[0] #최솟값

for num in array_list:
    
    if num > max_num:
        max_num = num
    if num < min_num:
        min_num = num

print(min_num, max_num)
