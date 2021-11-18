from sys import stdin
import heapq

def timeOrder():
	line = stdin.readline()
	timeOrdered = []
	while line != '\n':
		if line == "":
			return timeOrdered
		case = line.split()
		aux = stringTime(case[2])
		heapq.heappush(timeOrdered, (int(case[0]), aux, case[1], case[3]))
		line = stdin.readline()
	return timeOrdered

def stringTime(str):
	timeAux = str.split(":")
	time = (60 * int(timeAux[0])) + int(timeAux[1])
	return time


def main():
	cases = int(stdin.readline())
	stdin.readline()
	first = 0
	while cases > 0:
		if first == 1:
			print()
		first = 1
		teams = dict()
		priority = timeOrder()
		check = dict()
		while len(priority) > 0:
			if (priority[0][0],priority[0][2]) not in check:
				check[(priority[0][0],priority[0][2])] = priority[0][3]
			else:
				if check[(priority[0][0],priority[0][2])] == 'N' and priority[0][3] == 'Y':
					check[(priority[0][0],priority[0][2])] = 'Y'
			if priority[0][0] not in teams:
				teams[priority[0][0]] = dict()
				teams[priority[0][0]][priority[0][2]] = 0
				if priority[0][3] == 'N' and teams[priority[0][0]][priority[0][2]] <= 0:
					teams[priority[0][0]][priority[0][2]] -= 1
				else:
					if priority[0][3] == 'Y' and teams[priority[0][0]][priority[0][2]] <= 0:	
						teams[priority[0][0]][priority[0][2]] = ((teams[priority[0][0]][priority[0][2]] * -1) * 20) + priority[0][1]
			else:
				if priority[0][2] not in teams[priority[0][0]]:		
					teams[priority[0][0]][priority[0][2]] = 0
					if priority[0][3] == 'N' and teams[priority[0][0]][priority[0][2]] <= 0:
						teams[priority[0][0]][priority[0][2]] -= 1
					else:
						if priority[0][3] == 'Y' and teams[priority[0][0]][priority[0][2]] <= 0:	
							teams[priority[0][0]][priority[0][2]] = ((teams[priority[0][0]][priority[0][2]] * -1) * 20) + priority[0][1]

				else:
					if priority[0][3] == 'N' and teams[priority[0][0]][priority[0][2]] <= 0:
						teams[priority[0][0]][priority[0][2]] -= 1
					else:
						if priority[0][3] == 'Y' and teams[priority[0][0]][priority[0][2]] <= 0:	
							teams[priority[0][0]][priority[0][2]] = ((teams[priority[0][0]][priority[0][2]] * -1) * 20) + priority[0][1]
			maxTeam = priority[0][0]
			heapq.heappop(priority)	
			
		listed = []
		for i in range(maxTeam):
			listed.append(1)
		order = []
		for i in teams:
			auxTime = 0
			solved = 0
			for j in teams[i]:
				if teams[i][j] >= 0:
					auxTime += teams[i][j]
				if check[(i,j)] == 'Y':
					solved += 1
			order.append((solved,auxTime,int(i)))
		final = sorted(order, key=lambda s: (s[0], -s[1], -s[2]), reverse = True)	
		print("RANK TEAM PRO/SOLVED TIME")
		rank = 1
		sameSolved = 0
		sameTime = 0
		i = 0
		auxRank = 1
		for i in final:
			if i[0] > 0:
				if i == 0:
					sameSolved = i[0]
					sameTime = i[1]
					print("%4d %4d %4d %10d"%(rank, i[2], i[0], i[1]))
					listed[i[2] - 1] = 0 
				else:
					if i[0] == sameSolved:
						if i[1] == sameTime:
							sameSolved = i[0]
							sameTime = i[1]
							print("%4d %4d %4d %10d"%(rank, i[2], i[0], i[1]))
							listed[i[2] - 1] = 0 
						else:
							sameSolved = i[0]
							sameTime = i[1]
							print("%4d %4d %4d %10d"%(auxRank, i[2], i[0], i[1]))
							listed[i[2] - 1] = 0 
							rank = auxRank
					else:
						sameSolved = i[0]
						sameTime = i[1]
						print("%4d %4d %4d %10d"%(auxRank, i[2], i[0], i[1]))
						listed[i[2] - 1] = 0
						rank = auxRank
				auxRank += 1
				
		for i in range(maxTeam):
			if listed[i] == 1:
				print("%4d %4d"%(auxRank, i+1))
		cases -= 1					

main()
