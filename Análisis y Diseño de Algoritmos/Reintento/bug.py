from sys import stdin

def acumulated(st,end):
	total = 0
	for i in range(st,st+end+1):
		total += ans[i]
	return total

def backT(s,d,acum,st,end,flag):
	global ans
	if end >= 0 and end < 12:
		if end - st == 4:
			if acum + s < 0:
				acum += s
				ans.append(s)
				backT(s,d,acum-ans[st],st+1,end+1,True)
			elif acum - d < 0:
				acum -= d
				ans.append(-d)
				backT(s,d,acum-ans[st],st+1,end+1,True)
			else:
				acum -= d
				ans.append(-d)
				backT(s,d,acum,st,end-1,False)
				backT(s,d,acumulated(st,end)-ans[st],st+1,end+1,True)
		else:
			if flag:
				acum += s
				ans.append(s)
				backT(s,d,acum,st,end+1,True)
			else:
				acum -= d
				acum -= ans[end]
				ans[end]= -d
				if acum >= 0:
					backT(s,d,acum,st,end-1,False)

def main():
	global ans
	line = stdin.readline().strip()
	while line != "":
		ans = []
		s,d = map(int, line.split())
		backT(s,d,0,0,0,True)
		total = 0
		if len(ans) == 12:
			for i in range(0, len(ans)):
				total += ans[i]
			if total > 0:
				print(total)
			else:
				print("Deficit")
		else:
			print("Deficit")
		line = stdin.readline().strip()
main()