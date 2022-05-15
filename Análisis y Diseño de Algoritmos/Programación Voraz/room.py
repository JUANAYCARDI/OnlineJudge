from sys import stdin

def solve(events):
	ans = 1
	act = events[0][1]
	for i in range(1, len(events)):
		if act <= events[i][0]:
			ans += 1
			act = events[i][1]
	return ans

def main():
	cases = int(stdin.readline())
	while cases > 0:
		events = []
		s,f = map(int, stdin.readline().split())
		while f != 0:
			events.append([s,f])
			s,f = map(int, stdin.readline().split())
		events.sort(key=lambda x : x[1])
		print(solve(events))
		cases -= 1
		
main()