#Longest common subsequence
# LCW of two strings eg secretary and persecution
# sec is common so ans will be 3
def LCW(u, v):
    m = len(u)
    n = len(v)
    LCS = [[0] * (n + 1) for _ in range(m + 1)]
    
    maxLCW = 0
    
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if u[i - 1] == v[j - 1]:
                LCS[i][j] = 1 + LCS[i - 1][j - 1]
                maxLCW = max(maxLCW, LCS[i][j])  
            else:
                LCS[i][j] = 0  
    
    return maxLCW

s = "secretary"
t = "gensecrr"
print(LCW(s, t))  
