ans = 0
cnt = 0

while True:
    n = int(input())
    if n >= 30 or n <20:
        print(f"{(ans/cnt):.2f}")
        break
    
    ans += n
    cnt += 1