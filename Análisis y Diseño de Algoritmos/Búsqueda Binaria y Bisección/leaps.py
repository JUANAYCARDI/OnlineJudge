from sys import stdin
import math

def check(buildings, v0, theta, eps):
	distance = 0
	ans = True
	distance += buildings[0][1]
	i = 1
	while ans and i < len(buildings):
		t = distance / (v0*math.cos(theta))
		y = (v0 * math.sin(theta) * t) - (4.9 * pow(t,2))
		if buildings[i][0] - eps < y:
			distance += buildings[i][1]
			t = distance / (v0*math.cos(theta))
			y = (v0 * math.sin(theta) * t) - (4.9 * pow(t,2))
			if buildings[i][0] - eps < y:
				ans = True
			else:
				ans = False
		else:
			ans = False
		i += 1

	return ans

def calculate(xmax, thetalow, thetahi, buildings):
	eps = 0.000001
	while thetalow + eps < thetahi:
		thetamid = (thetahi + thetalow) / 2

		sin = math.sin(2*thetamid)
		v0 = math.sqrt((xmax * 9.8)/(sin))
		verify = check(buildings, v0, thetamid, eps)
		if verify:
			thetahi = thetamid
		else:
			thetalow = thetamid
	thetamid = math.degrees(thetamid)

	print("{0:.2f} {1:.2f}".format(thetamid, v0))


def main():
	n = list(map(int, stdin.readline().split()))
	case = 1
	while len(n) > 0:
		n = int(n[0])
		buildings = []
		xmax = 0
		for i in range(0,n):
			height, distance = map(float, stdin.readline().split())
			buildings.append([height, distance])
			xmax += distance
		calculate(xmax, 0, math.pi/2, buildings)
		n = list(map(int, stdin.readline().split()))
		case += 1

main()