str1 = "knowledge"
str2 = "acknowledgement"

dp = [[0]*(len(str1)+1) for _ in range(len(str2)+1)]
direction = [['hi']*(len(str1)+1) for _ in range(len(str2)+1)]

## init the first row
for first_row in range(len(dp[0])):
    dp[0][first_row] = first_row
    direction[0][first_row] = ''
## init the first column
for first_column in range(len(dp)):
    dp[first_column][0] = first_column
print(dp)

for i in range(1,len(str2)+1):
    for j in range(1,len(str1)+1):
        if(str1[j-1] == str2[i-1]):
            dp[i][j] = min(min(dp[i-1][j]+1,dp[i][j-1]+1),dp[i-1][j-1])
        else:
            dp[i][j] = min(min(dp[i-1][j]+1,dp[i][j-1]+1),dp[i-1][j-1]+2)

for i in range(1,len(str2)):
    print(dp[i])
print(dp[len(str2)][len(str1)])