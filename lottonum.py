#로또번호 발생기
from random import *

numlist = []
#1.번호 발생
for i in range(6):
    numlist.append(int(random()*45) +1)
#1.1번호 발생 확인    
#print(numlist)    

result = [] #중복 제거된 값들이 들어갈 리스트

#2.중복제거
for value in numlist:
        if value not in result:
            result.append(value)
#2.1중복제거 확인
#print(result)

#0제거(예외처리)
"""
try:
    result.remove(0)
except ValueError:
    pass
"""
#3. 원소가 부족할경우
for i in range(6):
    if len(result) != 6 :
        result.append(int(random()*45) +1)
result.sort()

#4. 출력
print("이번주 추첨번호는")
print(result)
print("입니다!")