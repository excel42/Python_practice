# Quiz - 리스트 활용
# 출처 : https://youtu.be/kWiCuklohdY
# 추첨 프로그램 - 치킨1, 커피 3
# 작성자 20명 1~20
# random 모듈의 shuffle과 sample 활용
# 
# 출력 예제
# -- 당첨자 발표 --
# 치킨 당첨자 : 1
# 커피 당첨자 : [2,3,4] 
# -- 축하합니다 --
#
from random import *
list = []
for i in range(1,21): #1~21까지 숫자 생성
    list.append(i)
shuffle(list)

winners = sample(list, 4)
print("-- 당첨자 발표 --")
print("치킨 당첨자 : {0}".format(winners[0]))
print("커피 당첨자 : {0}".format(winners[1:4]))
print("-- 축하합니다 --")