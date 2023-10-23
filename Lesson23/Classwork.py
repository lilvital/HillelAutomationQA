def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

def func(start, end):
    for i in range(max(2, start), end + 1):
        if is_prime(i):
            yield i

start = 10
end = 50

print(f"Знайдено прості числа у діапазоні {start}:{end}")
for i in func(start, end):
    print(i, end=", ")
