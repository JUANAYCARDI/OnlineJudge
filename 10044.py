from sys import stdin
from collections import deque

def bfsAux(adj, visitados, s, iD, erd):
	if s not in iD:
		return - 1
	cola = deque()
	cola.append(s)
	visitados[iD[s]] = True
	count = 1
	count2 = len(cola);
	min = -2
	while len(cola) != 0:		
		v = cola.popleft()		
		if count2 == 0:			
			count += 1;
			count2 = len(cola);
		else:
			count2 -= 1
		for i in range(len(adj[iD[v]])):
			w = adj[iD[v]][i]			
			if not visitados[iD[w]]:
				erd[w] = count
				cola.append(w)
				visitados[iD[w]] = True
		
	return -1            


def bfs(adj, n, s, iD, erd):
	visitados = [False for _ in range(n)]
	return bfsAux(adj, visitados, s, iD, erd)


def main():
	scenarios = int(stdin.readline())
	scenario = 1
	adj = [[] for i in range(100000)]
	while scenarios > 0:
				
		p, n = list(map(int, stdin.readline().split()))	
		iD = dict()
		erd = dict()
		index = 0
		for i in range(p):
			db = stdin.readline()
			if db != '\n':
				paperAux = db.split(':')
				paper = paperAux[0].split(',')
				l = []
				for i in range(1, len(paper)):
					if i == 1:
						l.append(paper[i-1] + ',' + paper[i])
					else:
						if (i + 1) % 2 == 0:
							aux = paper[i-1] + ',' + paper[i]
							aux = aux[1:]
							l.append(aux)
				
			pos = 0
			for i in l:
				if i not in iD:
					iD[l[pos]] = index;
					index += 1
				pos += 1
					
			for i in range(0, len(l)):
				j = i + 1
				while j < len(l):
					if l[i] != l[j]:
						if iD[l[j]] not in adj[iD[l[i]]]:
							adj[iD[l[i]]].append(l[j])
						if iD[l[i]] not in adj[iD[l[j]]]:
							adj[iD[l[j]]].append(l[i])
					j += 1
												
		print("Scenario", scenario)
		bfs(adj, len(iD), "Erdos, P.", iD, erd);	
		for i in range(n):
			search = stdin.readline()
			if search != '\n':
				if search[:-1] not in erd:
					print(str(search[:-1] + " infinity"))
				else:
					print(str(search[:-1] + ' ' + str(erd[search[:-1]])))
		scenario += 1	
		scenarios -= 1
		
		for i in range(0, len(iD)):
			adj[i] = []
		
main()