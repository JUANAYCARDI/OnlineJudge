from sys import stdin
from heapq import heappop, heappush
import math

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
		visited[u] = True	
		if weight == d[u]:
			for v, w in ady[u]:
				if visited[v] == False and w < d[v]:
					d[v], p[v] = w, u						
					heappush(heap, (d[v], v))

def distance(a, b, d):
	result = math.sqrt(pow(d[a][0] - d[b][0], 2) + pow(d[a][1] - d[b][1], 2))
	return result

def main():
	ady = [[] for i in range(500)]
	d, p = [INF for i in range(500)], [-1 for i in range(500)]
	visited = [False for i in range(500)]
	cases = int(stdin.readline())
	outposts = dict()
	while cases > 0:
		s, o = list(map(int, stdin.readline().strip().split()))
		for i in range(0, o):
			x, y = list(map(int, stdin.readline().strip().split()))
			outposts[i] = (x, y) 

		for i in range(0, o):
			for j in range(i + 1, o):
				dis = distance(i, j, outposts)
				ady[i].append((j, dis))
				ady[j].append((i, dis))
		
		prim(ady, 0, o, d, p, visited)
		r = []
		for i in range(0, o):
			r.append(d[i])
		r.sort(reverse = True)

		s -= 1
		for i in range(0, o):
			if s == 0:
				print("%.2f" % r[i])
				break
			s -= 1

		for i in range(0, o):
			ady[i] = []

		cases -= 1

main()