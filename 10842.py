from sys import stdin
from heapq import heappop, heappush

INF = float('inf')

def prim(ady, s, n, d, p, visited):

	for i in range(0, n):
		d[i] = INF
		p[i] = -1
		visited[i] = False
	d[s] = 0
	heap = [(0, s)]
	while len(heap) != 0:
		weight, u = heappop(heap)	
		weight *= -1
		visited[u] = True	
		if weight == d[u]:
			for v, w in ady[u]:
				if (visited[v] == False and w > d[v]) or d[v] == INF:
					d[v], p[v] = w, u	
					heappush(heap, (-1 * d[v], v))

def main():
	cases = int(stdin.readline())
	ady = [[] for i in range(101)]
	d, p = [INF for i in range(101)], [-1 for i in range(101)]
	visited = [False for i in range(101)]
	case = 1
	while cases > 0:
		n, m = list(map(int, stdin.readline().strip().split()))
		for i in range(m):
			u, v, c = list(map(int, stdin.readline().strip().split()))
			ady[u].append((v, c))
			ady[v].append((u, c))

		prim(ady, 0, n, d, p, visited)
			
		result = d[1]
		for i in range(2, n):
			if d[i] < result:
				result = d[i]
		print("Case #" + str(case) + ": " + str(result))
		for i in range(n):
			ady[i] = []
		case += 1
		cases -= 1

main()