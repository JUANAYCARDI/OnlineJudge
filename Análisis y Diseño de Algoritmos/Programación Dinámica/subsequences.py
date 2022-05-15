from sys import stdin, setrecursionlimit

setrecursionlimit(12<<24)

x , z = None, None

def distinct(n, m, memo):
	ans,key = None,(n,m)
	if key in memo:
		ans = memo[key]
	else:
		if m == 0:
			ans = 1
		elif m > n:
			ans = 0
		else:
			ans = distinct(n - 1, m, memo)
			if x[n - 1] == z[m - 1]:
				ans += distinct(n - 1, m - 1, memo)
		memo[key] = ans
	return ans				
	
def main():
	global x, z
	n = int(stdin.readline())
	while n > 0:
		memo = dict()
		x = stdin.readline().strip()
		z = stdin.readline().strip()
		print(distinct(len(x),len(z),memo))
		n -= 1

main()