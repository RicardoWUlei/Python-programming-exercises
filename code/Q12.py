def is_digit_even(item) -> bool:
    for digit in item:
        if int(digit) % 2:
            return False
    return True

print(','.join(filter(is_digit_even, [str(i) for i in range(1000,3001)])))