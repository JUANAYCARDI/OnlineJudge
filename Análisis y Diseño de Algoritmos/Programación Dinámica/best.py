from sys import stdin, setrecursionlimit

setrecursionlimit(12<<24)

ownership = None
sHolder = None
memo = None

def calculate(total):
	global sHolder
	return (sHolder * 100) / total

def coalition(n, m):
	global ownership, sHolder, memo
	ans = None
	if m in memo:
		ans = memo[m]
	else:
		if m > 5000:
			ans = calculate(m)
		elif n == 0:
			ans = 0
		elif m <= 5000:
			ans = max((coalition(n - 1, m + ownership[n - 1])) , (coalition(n - 1, m)))  
		memo[m] = ans

	return ans

def main():
	global ownership, sHolder, memo
	n, x = map(int, stdin.readline().split())
	while n != 0:
		ownership = []
		memo = dict()
		for i in range(0, n):
			p1, p2 = list(map(int, stdin.readline().split('.')))
			if i != x - 1:
				ownership.append((p1 * 100) + p2)
			else:
				sHolder = (p1 * 100) + p2
		ans = coalition(n - 1, sHolder)
		print("%.2f"%ans)

		n, x = map(int, stdin.readline().split())
	
main()