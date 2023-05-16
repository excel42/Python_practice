# 사용자로부터 문자열 입력받기
words = input().upper()

# 입력받은 문자열에서 중복값 제거
unique_words = list(set(words))

# 각 문자의 개수를 세서 리스트에 저장
cnt_list = []
for x in unique_words :
    cnt = words.count(x)
    cnt_list.append(cnt)

# count 숫자 최대값 중복시 '?' 출력
if cnt_list.count(max(cnt_list)) > 1:
    print('?')
else : 
    # count 숫자 최대값의 인덱스를 찾아 해당 문자 출력
    max_index = cnt_list.index(max(cnt_list))
    print(unique_words[max_index])
