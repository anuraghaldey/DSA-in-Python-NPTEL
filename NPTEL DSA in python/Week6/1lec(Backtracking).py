#Backtracking
#N-Queen Problem
def placequeen(i,board):
    n=len(board['queen'].keys())
    for j in range(n):
        if(isfree(i,j,board)):
            addqueen(i,j,board)
            if(i==n-1):
                return True
            else:
                extendedsol=placequeen(i+1,board)
            if(extendedsol):
                return True
            else:
                undoqueen(i,j,board)
    
    return 0

def initialize(board,n):
    for key in ['queen','row','col','nwtose','swtone']:
        board[key]={}
    for i in range(n):
        board['queen'][i]=-1
        board['row'][i]=0
        board['col'][i]=0
    for i in range(-(n-1),n):
        board['nwtose'][i]=0
    for i in range(2*(n-1)):
        board['swtone'][i]=0
        
def printboard(board):
    for row in sorted(board['queen'].keys()):
        print((row,board['queen'][row]))

def isfree(i,j,board):
    return(board['row'][i]==0 and board['col'][j]==0 and board['nwtose'][j-i]==0 and board['swtone'][j+i]==0)
def addqueen(i,j,board): 
    board['queen'][i]=j
    board['row'][i]=1
    board['col'][j]=1
    board['nwtose'][j-i]=1
    board['swtone'][j+i]=1
def undoqueen(i,j,board):
    board['queen'][i]=-1
    board['row'][i]=0
    board['col'][j]=0
    board['nwtose'][j-i]=0
    board['swtone'][j+i]=0
    
board={}
n=int(input("Enter the number of queens to place: "))
initialize(board,n)
if(placequeen(0,board)):
    printboard(board)
else:
    print("Sorry,Queens cant be placed")