from sys import stdin
import math

def digits2(n):
	aux = math.floor(math.log10( n ))
	aux2 = 0
	for i in range(1,aux+1):
		aux2 += ((n-pow(10,i) + 1)*((n-pow(10,i) + 1)+1))/2
	count = (n*(n+1))/2 +aux2
	return count
					
def main():
	largest = []
	for i in range(1, 32000):
		for j in str(i):
			largest.append(j)
	cases = int(stdin.readline())
	while cases > 0:
		index = int(stdin.readline())
		lowI = 1
		highI = index	
		low = digits2(lowI)
		high = digits2(highI)
		flag = 0	
		flag2 = 0
		while lowI + 1 < highI:
			flag2 = 1
			midI = lowI + ((highI - lowI) >> 1)
			mid = digits2(midI)
			if mid <= index:
				lowI = midI
				low = digits2(lowI)
			else:
				highI = midI
				high = digits2(highI)	
		count2 = 0
		
		if flag2 == 0:
			midI = lowI + ((highI - lowI) >> 1)
			mid = digits2(midI)
		if midI == 1:
			print("1")		
		else:
			if mid == index:
				midI = str(midI)
				print(midI[len(midI)-1])
			elif low == index:
				lowI = str(lowI)
				print(lowI[len(lowI)-1])
			elif high == index:
				highI = str(highI)
				print(highI[len(highI)-1])
			else:
				if mid == index - 1 or low == index - 1 or high == index - 1:
					print("1")
				else:
					if digits2(midI) > index and digits2(midI-1) < index:
						temp = index - digits2(midI - 1) 
						print(largest[int(temp)-1])
					elif digits2(midI) < index and digits2(midI + 1) > index:
						temp = index - digits2(midI) 
						print(largest[int(temp)-1])

		
		cases -= 1
	
main()