# Write a generator that yields numbers from 1 to N.
# def numgen():
#     count = 0
#     while True:
#         yield print(f"{count+1}")
#         count+=1
# print_num = numgen()
# n = int(input())
# for _ in range(n):
#     next(print_num)


# def even_numbers(n):
#     for num in range(1, n + 1):
#         if num % 2 == 0:
#             yield num

# n = int(input())

# gen = even_numbers(n)

# for num in gen:
#     print(num)

# Create a generator that yields Fibonacci numbers up to N terms.
def fibonacci_series(n):
    if n <= 1:
        return n
    x = (fibonacci_series(n-1) + fibonacci_series(n-2))
    yield x

n = int(input())
fibo = fibonacci_series(n)

for num in fibo:
    print(num)