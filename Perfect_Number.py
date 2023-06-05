def is_perfect_number(n):
    if n <= 0:
        return False

    sum_of_divisors = sum(i for i in range(1, n) if n % i == 0)
    return sum_of_divisors == n


# Testing the function
num = int(input())
result = is_perfect_number(num)
print(result)