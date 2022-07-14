#QUIZ
#택시기
#50명의 승객과 매칭 기회가 있을때, 총 탑승 승객 수를 구하는 프로그램을 작성하시오

#조건 1 : 승객별 운행 소요 시간을 5~ 50분 사이의 난수로 정해집니다.
#조건 2 : 당신은 소요 시간 5분 ~ 10분 사이의 승객만 매칭해야 합니다.

#출력예제
#[0] 1번째 손님 (소요시간 : 15분)
#[ ] 2번째 손님 (소요시간 : 50분)
# ...
#[ ] 2번째 손님 (소요시간 : 50분)

#총 탑승 승객 : 2분
from random import *
count = 0

for waiting_no in range(1,51):
    waiting_time = int(random()*45) +1
    if waiting_time <= 15:
        count += 1
        print("[O] {0}번째 손님(소요시간 : {1}분)".format(waiting_no, waiting_time))
    else:
        print("[X] {0}번째 손님(소요시간 : {1}분)".format(waiting_no, waiting_time))

print("총 탑승 승객 : " + str(count) + "명")