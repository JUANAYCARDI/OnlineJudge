from sys import stdin

adj = None
k = None
total = None

def dfs(u):
	global adj, k, total
	ans = None
	if len(adj[u]) == 0:
		ans = 1
	else:
		best = 0
		for i in range(0, len(adj[u])):
			v = adj[u][i]
			aux = dfs(v)
			if aux > best:
				best = aux
		if best == k:
			ans = 0
			total += 1
		else:
			ans = best + 1
	return ans

def main():
	global adj, k, total
	line = stdin.readline().strip()
	while line != "":
		n,m,k = map(int, line.split())
		adj = [[] for i in range(n)]
		total = 0
		for i in range(m):
			l = list(map(int, stdin.readline().split()))
			father = l[0]
			for j in range(1, len(l)):
				adj[father].append(l[j])
		dfs(0)
		print(total)
		line = stdin.readline().strip()

main()