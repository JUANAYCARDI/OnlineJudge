from sys import stdin

def main():
	s = stdin.readline().strip()
	queries = int(stdin.readline())
	positions = dict()
	for k in range(0, len(s)):
		if s[k] in positions:
			positions[s[k]][0].append(k)
		else:
			positions[s[k]] = [[k], 0]
	for i in range(queries):
		x = stdin.readline().strip()
		for j in positions:
			positions[j][1] = 0
		start = -1
		flag = True
		actualPos = -1
		pos = 0
		while flag and pos < len(x):
			value = x[pos]
			if value in positions: 
				current = positions[value][0]
				hi = len(current)
				low = positions[value][1]
				mid = low + ((hi - low) >> 1)
				while low < hi:
					mid = low + ((hi - low) >> 1)
					if actualPos <= current[mid]:
						hi = mid
					else:
						low = mid + 1			
				if low == len(current):
					flag = False
				else:
					if pos == 0:
						start = current[low]
					if current[low] < actualPos:
						low += 1
					actualPos = current[low]
					positions[value][1] = low + 1			
					pos += 1
			else:
				flag = False
		if pos == len(x) and flag:
			print("Matched", start, actualPos)
		else:
			print("Not matched")

main()