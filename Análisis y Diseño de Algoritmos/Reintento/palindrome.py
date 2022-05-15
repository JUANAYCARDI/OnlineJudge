from sys import stdin, setrecursionlimit

setrecursionlimit(12<<24)

def solve(l,k):
	ans = k
	if len(l) > 0 and k >= 0:
		if l[0] == l[-1]:
			l = l[1:-1]
			flag = True 
			while flag and len(l):
				if l[0] == l[-1]:
					l = l[1:-1]
				else:
					flag = False
			ans = solve(l,k)
		else:
			aux = l[:-1]
			l = l[1:]
			flag = True 
			while flag and len(l):
				if l[0] == l[-1]:
					l = l[1:-1]
				else:
					flag = False
			flag = True 
			while flag and len(aux):
				if aux[0] == aux[-1]:
					aux = aux[1:-1]
				else:
					flag = False
			ans = max(solve(l,k-1),solve(aux,k-1))
	return ans

def main():
	cases = int(stdin.readline())
	case = 1
	while case <= cases:
		n,k = map(int, stdin.readline().split())
		l = list(map(int, stdin.readline().split()))
		ans = solve(l,k)
		if ans < 0:
			print("Case " + str(case) + ": " + "Too difficult")
		elif ans == k:
			print("Case " + str(case) + ": " + "Too easy")
		else:
			print("Case " + str(case) + ": " + str(k - ans))
		case += 1

main()