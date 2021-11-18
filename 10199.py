from sys import stdin

def apAux(v, n, ady, visited, low, father, apNodes, t, iD2):
	numHijos = 0;
	visited[v] = low[v] = t
	t += 1
	for i in range(0,len(ady[v])):
		w = ady[v][i]
		if visited[w] == -1:
  			numHijos += 1
  			father[w] = v
  			apAux(w,n,ady,visited,low,father,apNodes,t,iD2)
  			low[v] = min(low[v], low[w])
  			if father[v] != -1 and low[w] >= visited[v]:
  				apNodes.add(iD2[v])
		elif w != father[v]:
  			low[v] = min(low[v], visited[w])

	if father[v] == -1 and numHijos > 1:
  		apNodes.add(iD2[v])

def ap(n, ady, visited, low, father, apNodes, t, iD2):
	for i in range(0,n):
		low[i] = visited[i] = father[i] = -1
	for i in range(0,n):
		if visited[i] == -1:
			apAux(i,n,ady,visited,low,father,apNodes,t,iD2)

def main():
	case = 1
	iD = dict()
	iD2 = dict()
	ady = [[] for i in range(100)]
	visited = [-1 for i in range(100)]
	father = [-1 for i in range(100)]
	low = [-1 for i in range(100)]
	apNodes = set()
	n = int(stdin.readline())
	while n != 0:
		t = 1
		for i in range(0,n):
			aux = str(stdin.readline().strip()) 
			iD[aux] = i
			iD2[i] = aux
		
		r = int(stdin.readline())
		for i in range(0,r):
			a, b = list(map(str, stdin.readline().split()))
			ady[iD[a]].append(iD[b])
			ady[iD[b]].append(iD[a])			

		ap(n,ady,visited,low,father,apNodes,t,iD2)
		result = []
		for i in apNodes:
			result.append(i)
		result.sort()
		if case > 1:
			print()
		print("City map #{0}: {1} camera(s) found".format(case, len(result)))
		for i in result:
			print(i)

		case += 1
		iD.clear()
		iD2.clear()
		apNodes.clear()
		for i in range(0,n):
			ady[i] = []

		n = int(stdin.readline())


main()