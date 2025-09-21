n = int(input())
swapped = ((n & 0xAA) >> 1) | ((n & 0x55) << 1)
print(swapped)
