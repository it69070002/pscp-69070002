"""3360"""
w,h,_,_ = list(map(int,input().split()))
x = list(map(int,input().split()))
y = list(map(int,input().split()))
x.append(w)
y.append(h)
x0,y0 = 0,0
area = []
for i in y:
    h1 = i - y0
    for j in x:
        w1 = j - x0
        area.append(h1*w1)
        x0 = j
    x0 = 0
    y0 = i
area.sort(reverse=True)
print(area[0],area[1])
