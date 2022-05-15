from sys import stdin

ans = None
elements = None
elements2 = None

def solve(n,k,i,dna,change):
	global ans
	if k > 0 and i >= 0 and i < n and change < 3:
		l = list(dna)		
		l[i] = elements2[(elements[dna[i]] + 1) % 4]
		new = ''.join(l)
		ans[new] = new
		solve(n,k,i,new,change+1)
		solve(n,k-1,i+1,new,0)
		if change > 0:
			solve(n,k-1,i+1,dna,change)
		else:
			solve(n,k,i+1,dna,change)
	return ans

def main():
    global ans, elements, elements2
    t = int(stdin.readline())
    elements = {"A" : 0, "C" : 1, "G" : 2, "T" : 3}
    elements2 = ["A", "C", "G", "T"]
    while t > 0:
        ans = dict()
        n,k = map(int, stdin.readline().split())
        dna = stdin.readline().strip()
        ans[dna] = dna
        sol = list(solve(n,k,0,dna,0).values())    
        sol.sort()
        print(len(sol))
        for i in sol:
        	print(i)
        t -= 1

main()