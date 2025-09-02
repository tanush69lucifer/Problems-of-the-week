def add_subtract(x):
    total = x
    sign = -1  # next number will be subtracted

    def inner(y=None):
        nonlocal total, sign
        if y is None:
            return total
        total += sign * y
        sign *= -1
        return inner

    return inner

# Examples
print(add_subtract(7)())                # 7
print(add_subtract(1)(2)(3)())          # 0
print(add_subtract(-5)(10)(3)(9)())     # 11
print(add_subtract(5)(6)(7)())          # 4
