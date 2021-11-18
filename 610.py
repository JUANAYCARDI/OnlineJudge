from sys import stdin
import sys

sys.setrecursionlimit(10**6)

def bridgesAux(v, ady, visited, low, father, t, result):
	visited[v] = low[v] = t
	t += 1

	for i in range(0, len(ady[v])):
		w = ady[v][i]
		if visited[w] == -1:
			father[w] = v
			bridgesAux(w, ady, visited, low, father, t, result)
			low[v] = min(low[v], low[w])
			result[v].append(w)
			if low[w] > visited[v]:
				result[w].append(v)
							
		elif w != father[v]:
			low[v] = min(low[v], visited[w])
			if visited[v] > visited[w]:
				result[v].append(w)

def bridgesTarjan(n, ady, visited, low, father, t, result):
	for i in range(0, n):
		low[i] = visited[i] = father[i] = -1
	for i in range(0, n):
		if visited[i] == -1:
			bridgesAux(i, ady, visited, low, father, t, result)

def main():
	n, m = list(map(int, stdin.readline().strip().split()))
	ady = [[] for i in range(1001)]
	result = [[] for i in range(1001)]
	visited = [-1 for i in range(1001)]
	low = [-1 for i in range(1001)]
	father = [-1 for i in range(1001)]
	case = 1
	while n != 0:
		for i in range(0, m):
			a, b = list(map(int, stdin.readline().strip().split()))
			ady[a - 1].append(b - 1) 
			ady[b - 1].append(a - 1)
		t = 1
		if m > 0:
			bridgesTarjan(n, ady, visited, low, father, t, result);

		print(case)
		print()
		for i in range(0, n):
			if len(result[i]) > 0:
				for j in range(0, len(result[i])):
					print(i + 1, result[i][j] + 1)
		print('#')
		for i in range(0, n):
			ady[i] = []
			result[i] = []
			
		n, m = list(map(int, stdin.readline().strip().split()))

		case += 1

main()