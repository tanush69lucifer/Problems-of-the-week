import bisect
arr = list(map(int, input().split()))
lis = []
for x in arr:
    pos = bisect.bisect_left(lis, x)
    if pos < len(lis):
        lis[pos] = x
    else:
        lis.append(x)
print(len(lis))
