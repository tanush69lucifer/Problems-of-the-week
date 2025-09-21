M, N = map(int, input().split())
shift = 0
while M < N:
    M >>= 1
    N >>= 1
    shift += 1
print(M << shift)
