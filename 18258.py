#큐 구현
import sys
from collections import deque #deque 라이브러리 사용
n = int(sys.stdin.readline()) #명령 수 작성
queue = deque([]) 

for i in range(n): #명령 수만큼
    command = sys.stdin.readline().split() #명령어 입력
    if command[0] == 'push': #push 명령을 받으면 큐에 숫자를 넣는다.
        queue.append(command[1])
    elif command[0] == 'pop': #pop 명령을 받으면 
        if not queue: #queue의 크기가 0이면 -1을 출력
            print(-1) 
        else:
            print(queue.popleft()) #queue의 크기가 0이 아니면 큐의 전단을 출력하고 삭제
    elif command[0] == 'size': #명령어가 size라면 큐의 크기 출력
            print(len(queue))
    elif command[0] == 'empty': #empty명령일 경우
            if not queue: #queue의 크기가 0이면 1을 출력
                print(1)
            else: #queue의 크기가 0이 아니면 0을 출력
                print(0)
    elif command[0] == 'front': #front 명령일경우
            if not queue: #큐의 크기가 0이라면 -1을 출력
                print(-1)
            else: #큐의 크기가 0이 아니라면 큐의 전단을 출력
                print(queue[0])
    elif command[0] == 'back': #명령어가 back일경우
            if not queue: # 큐의 크기가 0이라면 -1을 출력
                print(-1)
            else: # 큐의 크기가 0이 아니라면 queue의 후단을 출력
                print(queue[-1])