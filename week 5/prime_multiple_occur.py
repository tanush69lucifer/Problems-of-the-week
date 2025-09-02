def is_prime(num):
    if num <= 1: 
        return False
    if num == 2: 
        return True
    if num % 2 == 0: 
        return False
    i = 3
    while i * i <= num:
        if num % i == 0:
            return False
        i += 2
    return True

def find_prime_duplicates(arr):
    freq = {}
    result = []
    for num in arr:
        if is_prime(num):
            freq[num] = freq.get(num, 0) + 1
    for num in arr:   # maintain first appearance order
        if num in freq and freq[num] > 1 and num not in result:
            result.append(num)
    return result if result else [-1]

# Example usage:
N = 10
A = [2, 3, 5, 7, 11, 3, 2, 15, 17, 5]
print(find_prime_duplicates(A))  # [2, 3, 5]
