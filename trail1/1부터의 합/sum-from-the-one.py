n = int(input())

cnt = 0

for i in range(1,101):
    if cnt + i  >= n:
        print(i)
        break
    cnt += i
        