from sys import stdin, setrecursionlimit

setrecursionlimit(12<<24)

values = None
memo = None
first = None

def compareMax(b1, b2):
	ans = None
	if b1[0] > b2[0]:
		ans = b1
	elif b1[0] < b2[0]:
		ans = b2
	else:
		if b1[1] < b2[1]:
			ans = b1
		else:
			ans = b2
	return ans

def sumP(b1, b2):
	return (b1[0] + b2[0], b1[1] + b2[1])

def recursion(i, j):
	global memo, first, values
	ans = None
	c = -1
	if first == "Petra":
		c = i // 2 
	else:
		if i % 2 != 0:
			c = (i // 2) + 1
		else:
			c = i // 2
	key = (i, j)
	if key in memo:
		ans = memo[key]
	else:
		if i == 0 or j == 0 or c < j:
			ans = (0, 0)
		else:
			ans = compareMax(sumP(recursion(i - 1, j - 1), (values[i-1][1], values[i-1][0])), recursion(i - 1, j))
		memo[key] = ans

	return ans

def main():
	global values, memo, first
	cases = int(stdin.readline())
	while cases > 0:
		goodies = int(stdin.readline())
		first = stdin.readline().strip()
		values = []
		memo = dict()
		petra = 0
		for i in range(0, goodies):
			p, j = map(int, stdin.readline().split())
			values.append((p,j))
			petra += p
		values.sort(key=lambda x : (-x[0], x[1]))
		c = -1
		if first == "Petra":
			c = goodies // 2 
		else:
			if goodies % 2 != 0:
				c = (goodies // 2) + 1
			else:
				c = goodies // 2
		ans = recursion(goodies, c)
		print(petra-ans[1], ans[0])
		cases -= 1

main()