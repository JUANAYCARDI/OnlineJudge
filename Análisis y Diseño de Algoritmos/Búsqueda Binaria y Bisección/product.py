from sys import stdin

def msp(A, low, hi):
    ans = -999999
    if low==hi: ans = -999999
    elif low+1==hi: ans = A[low]
    else:
        mid = low+((hi-low)>>1)
        ans = max(msp(A, low, mid), msp(A, mid, hi))
        ans = max(ans, best_crossing(A, low, mid, hi))
    return ans

def best_crossing(A, low, mid, hi):
    bl,wl,sl,l = A[mid-1],A[mid-1],A[mid-1],mid-2
    while l>=low:
        sl *= A[l]
        bl = max(bl, sl)
        wl = min(wl, sl)
        l -= 1
    br,wr,sr,r = A[mid],A[mid],A[mid],mid+1
    while r<hi:
        sr *= A[r]
        br = max(br, sr)
        wr = min(wr, sr)
        r += 1
    return max(wr * wl, bl * br , wr * bl,wl * br)

def main():
	test = list()
	for l in stdin.readlines():
		for x in map(int, l.split()):
			if x==-999999:
				print(msp(test, 0, len(test)))
				test = list()
			else: test.append(x)
main()
