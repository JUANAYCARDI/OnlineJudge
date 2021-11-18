from sys import stdin
from collections import deque

def main():
	cases = stdin.readlines()
	for line in cases:
		if line != '\n':
			l = list(map(int,line.split()))
			stack = deque()
			sums = deque()
			count = 0
			count2 = 0
			flag = True
			flag2 = True
			for i in l:
				if i < 0:
					if count == 0:
						stack.appendleft(i)						
					else:
						if flag == False:
							aux = sums[0]
							stack.appendleft(i)
							sums.popleft()
							sums.appendleft(-i + aux)
						else:
							if stack:
								if i > stack[0]:
									stack.appendleft(i)
									sums.appendleft(-i)
								else:
									print(":-( Try again.")
									flag2 = False
									break					
					flag = True
				else:
					if count == 0:
						print(":-( Try again.")
						flag2 = False
						break
					if -i == stack[0]:
						if flag == False:
							stack.popleft()
							if i > sums[0]:
								sums.popleft()
								flag = False
							else:
								print(":-( Try again.")
								flag2 = False
								break
						else:
							stack.popleft()
							flag = False
							
					else:
						print(":-( Try again.")
						flag2 = False
						break
				count += 1
				count2 += 1
				if len(stack) == 0 and len(sums) == 0:
					if count2 == len(l):
						print(":-) Matrioshka!")
						break
					else:
						flag = True
						count = 0
			if len(stack) != 0 or len(sums) != 0:
				if flag2 == True:
					print(":-( Try again.")
		else:
			print(":-) Matrioshka!")

main()