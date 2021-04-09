l = [7,1,4,6,8]
for i in range(len(l)-1,0,-1):
    l[i] = l[i-1] + l[i]
    l[i-1] = l[i] - l[i-1]
    l[i] = l[i] - l[i-1]
print(l)
