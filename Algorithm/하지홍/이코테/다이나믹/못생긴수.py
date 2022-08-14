n = int(input())

dp=[0]*1001

dp[0] = 1
i2 = i3 = i5 = 0
num2 = 2
num3 = 3
num5 = 5
for i in range(1, n):
    dp[i] = min(num2, num3, num5)
    
    if dp[i] == num2:
        i2 += 1
        num2 = dp[i2] * 2
        
    if dp[i] == num3:
        i3 += 1
        num3 = dp[i3] * 3
        
    if dp[i] == num5:
        i5 += 1
        num5 = dp[i5] * 5
        
print(dp[n-1])