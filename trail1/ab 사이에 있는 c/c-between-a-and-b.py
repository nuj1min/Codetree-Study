a,b,c = map(int,input().split())

ans = False

for i in range(a,b+1):
    if i % c == 0:
        ans = True
        break

if ans:
    print("YES")
else:
    print("NO")