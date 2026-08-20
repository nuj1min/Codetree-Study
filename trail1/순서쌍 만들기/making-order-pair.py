n = int(input())

for i in range(n,0,-1):
    for j in range(n,0,-1):
        print("(",end = "")
        print(i, end = "")
        print(",",end = "")
        print(j,end = "")
        print(")",end = " ")    
    print()