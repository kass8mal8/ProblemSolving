def is_palindrome(num):
    result, num_remaining = 0, abs(num)

    while num_remaining:
        result = result * 10 + num_remaining % 10
        num_remaining //= 10

    return True if num == result else False


num = 12219
print(is_palindrome(num))
