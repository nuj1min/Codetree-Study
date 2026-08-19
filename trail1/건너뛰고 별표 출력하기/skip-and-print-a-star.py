n = int(input())

for i in range(1,n+1):
    for _ in range(i):
        print("*",end = "")
    print()
    print()

for i in range(n-2,-1,-1):
    for _ in range(i,-1,-1):
        print("*", end = "")
    print()
    print()