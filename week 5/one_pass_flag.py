def is_number(s: str) -> bool:
    s = s.strip()
    if not s:
        return False

    seen_digit = False
    seen_dot = False
    seen_exp = False
    digit_after_exp = True

    for i, ch in enumerate(s):
        if ch.isdigit():
            seen_digit = True
            if seen_exp:
                digit_after_exp = True
        elif ch in ['+', '-']:
            if i > 0 and s[i-1].lower() != 'e':  # sign only at start or after e/E
                return False
            if i == len(s) - 1:  # sign cannot be last char
                return False
        elif ch == '.':
            if seen_dot or seen_exp:  # only one dot, not after exponent
                return False
            seen_dot = True
        elif ch in ['e', 'E']:
            if seen_exp or not seen_digit:  # only one e/E, must follow digits
                return False
            seen_exp = True
            digit_after_exp = False
            if i == len(s) - 1:  # e/E cannot be last
                return False
        else:
            return False

    return seen_digit and (not seen_exp or digit_after_exp)
