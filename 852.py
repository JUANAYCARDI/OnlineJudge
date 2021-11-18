from sys import stdin

def dfsAux(i,j,visited,board,check,token,result,count):
  
    visited[i][j] = 1  
    rows = (0,1,0,-1)
    columns = (-1,0,1,0)
    
    for u in range(0,4):
    	if count == 1:
    	   	check = []
    	newI = i + rows[u] 
    	newJ = j + columns[u]
    	if newI >= 0 and newI < 9 and newJ >= 0 and newJ < 9 and visited[newI][newJ] == 0 and board[newI][newJ] == '.':
    		board[newI][newJ] = token
    		check.append((newI,newJ))
    		if result != 0:
    			result = dfsAux(newI, newJ, visited, board, check, token, result, count + 1)
    		else:
    			dfsAux(newI, newJ, visited, board, check, token, result, count + 1)
    		
	    	for x in range(0,4):
	    		checkI = newI + rows[x]
	    		checkJ = newJ + columns[x] 		
	    		if checkI >= 0 and checkI < 9 and checkJ >= 0 and checkJ < 9 and board[checkI][checkJ] != '.':	    		
	    			if board[checkI][checkJ] != board[newI][newJ]:
	    				result = 0
	    					    				
    	if result == 0 and count == 1:
	        for l in check:
	            board[l[0]][l[1]] = '.' 
	        result = 1
	        check = []

    return result

def dfs(board):
    visited = [[0 for i in range(0,9)] for j in range(0,9)]
    check = []
    for i in range(0,9):
    	for j in range(0,9):
        	if visited[i][j] == 0 and board[i][j] != '.':
        		result = dfsAux(i,j,visited,board,check, board[i][j], 1, 1)
        		if result == 0:
        			for l in check:
        				board[l[0]][l[1]] = '.'
        		check = []


def main():
	boards = int(stdin.readline())
	board = [[0 for i in range(0,9)] for j in range(0,9)]
	
	while boards > 0:
		for i in range(0,9):
			line = stdin.readline()
			for j in range(0,9):
				board[i][j] = line[j]

		dfs(board)
		X = 0
		O = 0
		for i in range(0,9):
			for j  in range(0,9):
				if board[i][j] == 'X':
					X += 1
				elif board[i][j] == 'O':
					O += 1	

		print("Black",X,"White",O)

		boards -= 1

main()