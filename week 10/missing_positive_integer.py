N = int(input())
arr = list(map(int, input().split()))
for i in range(N):
    while 1 <= arr[i] <= N and arr[arr[i]-1] != arr[i]:
        arr[arr[i]-1], arr[i] = arr[i], arr[arr[i]-1]
for i in range(N):
    if arr[i] != i+1:
        print(i+1)
        break
else:
    print(N+1)
