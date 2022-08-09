x, y = map(int, input().split())


def win_proper(a,b):
    return int(100 * a / b)

start = 1
end = 1000000000
standard_proper = win_proper(y,x)
ans = 1000000001

while start<=end:
    mid = (start+end)//2
    total = x+mid
    win = y+mid
    
    result = win_proper(win, total)
    
    if result > standard_proper:
        ans = min(mid, ans)
        end = mid-1
    else:
        start = mid+1
        
if ans == 1000000001:
    print(-1)
else:
    print(ans)