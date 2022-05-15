from sys import stdin
import math

n, b = None, None
a, ans = None, None

def solve(mid):
	global b
	boxes = 0
	for i in a:
		boxes += math.ceil(i/mid)
	return boxes <= b

def divideConquer():
	global a,ans
	hi = max(a)
	low = 0
	while low + 1 != hi:
		mid = low + ((hi - low) >> 1)
		if solve(mid):
			hi = mid
		else:
			low = mid
	ans = hi


def main():
	global a,n,b,ans
	n, b = map(int, stdin.readline().strip().split())
	a = [int(stdin.readline().strip()) for _ in range(n)]
	while n != -1:
		divideConquer()
		print(ans)
		stdin.readline()
		n, b = map(int, stdin.readline().strip().split())
		a = [int(stdin.readline().strip()) for _ in range(n)]

main()
