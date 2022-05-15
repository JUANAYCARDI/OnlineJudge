from sys import stdin
from heapq import heappush, heappop

def main():
	cases = int(stdin.readline())
	while cases > 0:
		stdin.readline()
		orders = []
		n = int(stdin.readline())
		actTime = 0
		ans = 0
		for i in range(n):
			steel,date = map(int, stdin.readline().split())
			if steel <= date:
				orders.append([date,steel])
		orders.sort(key=lambda x: (x[0], x[1]))
		l = []
		for i in range(0, len(orders)):
			if i == 0:
				ans += 1
				actTime += orders[i][1]
				heappush(l, -orders[i][1])
			else:
				if orders[i][1] + actTime <= abs(orders[i][0]):
					actTime += orders[i][1]
					heappush(l, -orders[i][1])
					ans += 1
				elif orders[i][1] + actTime - abs(l[0]) < actTime:
					actTime -= abs(l[0])
					heappop(l)
					actTime += orders[i][1]
					heappush(l, -orders[i][1])
		print(len(l))
		if cases > 1:
			print()
		cases -= 1
main()