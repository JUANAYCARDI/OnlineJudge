from sys import stdin

def solve(digits, d):
	stack = [digits[0]]
	limit = d
	minValues = 0
	flag = None
	for i in range(1, len(digits)):
		if i == limit:
			flag = True
			while len(stack) > minValues and flag:
				if digits[i] > stack[len(stack) - 1]:
					stack.pop()
				else:
					flag = False
			stack.append(digits[i])
			limit += 1		
			minValues += 1
		else:
			flag = True
			while len(stack) > minValues and flag:
				if digits[i] > stack[len(stack) - 1]:
					stack.pop()
				else:
					flag = False			
			stack.append(digits[i])							
	return stack

def main():
	n, d = map(int, stdin.readline().split())
	while n != 0:
		number = stdin.readline().strip()
		ans = solve(number, d)
		answer = ""
		#print(ans, len(number), d)
		cant = len(number) - d
		i = 0
		while cant > 0:
			answer += ans[i]
			i += 1
			cant -= 1
		print(answer)
		n, d = map(int, stdin.readline().split())

main()