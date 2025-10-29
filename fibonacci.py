def fibonacci(n):
    series = []
    a, b = 0, 1
    for _ in range(n):
        series.append(a)
        a, b = b, a + b
    return series

n = int(input("Enter how many terms of Fibonacci you want: "))
fib_list = fibonacci(n)
print("Fibonacci series:")
for num in fib_list:
    print(num, end=" ")
