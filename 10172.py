from sys import stdin

def main():
	sets = int(stdin.readline())
	while sets > 0:
		n, s, q = list(map(int, stdin.readline().split()))
		stations = [None]*n
		total = 0
		for i in range(n):
			station = list(map(int, stdin.readline().split()))
			stationCap = station[0]
			total += stationCap
			stations[i] = list()
			for j in range(1, stationCap + 1):
				stations[i].append(station[j])
		
		carrier = []
		pos = 0
		time = 0
		while total > 0:
			maxCap = 1		
			while len(carrier) > 0 and len(stations[pos]) <= q and maxCap == 1:
				if carrier[len(carrier) - 1] == pos + 1:
					carrier.pop()
					total -= 1
					time += 1
				else: 
					if len(stations[pos]) < q:
						stations[pos].append(carrier[len(carrier) - 1])
						carrier.pop()
						time += 1
					else:
						maxCap = 0

			while len(carrier) < s and len(stations[pos]) > 0:
				carrier.append(stations[pos][0])
				stations[pos].pop(0)
				time += 1

			pos = (pos + 1) % n
			
			if total != 0:
				time += 2
	
		print(time)

		sets -= 1

main()