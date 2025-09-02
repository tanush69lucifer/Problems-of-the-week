def misere_nim(heaps):
    # All heaps are 1
    if all(h == 1 for h in heaps):
        return len(heaps) % 2 == 0  # first player wins if even number of heaps
    # Normal Nim rule
    xor_sum = 0
    for h in heaps:
        xor_sum ^= h
    return xor_sum != 0

# Examples
print(misere_nim([3, 4, 5]))  # True
print(misere_nim([1, 1, 1]))  # False
print(misere_nim([1, 1, 2]))  # True
