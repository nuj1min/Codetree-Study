n = int(input())

for i in range(n,0,-1):
    for j in range(n-i,n):
        print("*",end = "")
    for j in range(i,n):
        print(" ",end = "")

    for j in range(i,n):
        print(" ",end = "")
    for j in range(n-i,n):
        print("*",end = "")
    print()        
