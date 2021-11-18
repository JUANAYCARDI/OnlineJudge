from sys import stdin
from collections import deque
import sys

sys.setrecursionlimit(10**6)

def kosarajuAux(v, ady, order, visited, flag):
	if visited[v] == False:
		visited[v] = True

		for i in ady[v]:
			kosarajuAux(i, ady, order, visited, flag)
		if flag ==  True:
			order.appendleft(v)

def kosaraju(nodes, visited, ady, order):
	total = 0
	flag = True
	for i in range(0, nodes):
		kosarajuAux(i, ady, order, visited, flag)
	for i in range(0, nodes):
		visited[i] = False
	flag = False
	for i in order:
		if visited[i] == False:
			kosarajuAux(i, ady, order, visited, flag)
			total += 1

	return total

def main():
	cases = int(stdin.readline())
	ady = [[] for i in range(100000)]
	visited = [False for i in range(100000)]
	while cases > 0:
		order = deque()
		nodes, edges = list(map(int, stdin.readline().split()))
		for i in range(0, edges):
			node1, node2 = list(map(int, stdin.readline().split()))
			ady[node1 - 1].append(node2 - 1)

		result = kosaraju(nodes, visited, ady, order)

		print(result)
		for i in range(0, nodes):
			ady[i] = []
			visited[i] = False
		cases -= 1

main()