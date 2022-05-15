from sys import stdin

board = None
memo = None
rows = None

def nextColumn(r, c):
	global board
	if r > (len(board) - 1) / 2:
		columns = [c, c + 1]
	else:
		if c == 0:
			columns = [c]
		elif c < len(board[r]) - 1:
			columns = [c - 1, c]
		else:
			columns = [c - 1]
	return columns

def solveAux(r, c, x, memo):
	global board
	ans, key = None, (r,c,x)
	if key in memo:
		ans = memo[key]
	else:
		if r == 0:
			ans = abs(board[r][0]) == abs(x)
		else:
			ans, n, columns = False, 0, nextColumn(r, c)
			while ans == False and n != len(columns):
				c1 = columns[n]
				b1 = board[r][c]
				ans = solveAux(r - 1, c1, x + b1, memo) or solveAux(r - 1, c1, x - b1, memo)
				n += 1
		memo[key] = ans
	return ans

def solve():
	ans, n, found, memo = None, 0, False, dict()
	while found == False:
		found = solveAux(rows-1, 0, n, memo) or solveAux(rows - 1, 0, -n, memo)
		if found:
			ans = n
		n += 1
	return ans

def main():
	global board, rows
	n = int(stdin.readline())
	while n != 0:
		board = []
		rows = (2*n) - 1
		for i in range(0, rows):
			board.append(list(map(int, stdin.readline().split())))
		print(solve())
		n = int(stdin.readline())

main()