##조합론_모듈러연산5
n, k=map(int, input().split())
dp = [[0]*1001 for _ in range(1001)] ## 배열 생성

for i in range(1, n+1) :        
    for j in range(0, i+1) : 
        if j ==0:           #k가 0이면 1
            dp[i][j]=1
        elif j==i:      #k 가 n과 같으면 1
            dp[i][j]=1
        else:
            dp[i][j] = (dp[i-1][j-1] + dp[i-1][j])  #나머지 경우 계산 nCk 공식
            
print(dp[n][k])