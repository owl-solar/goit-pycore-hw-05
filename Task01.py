def caching_fibonacci():   # Returns a Fibonacci function with caching
    cashe = {}

    def fibonacci(n):      # Inner Fibonacci function
        if n <= 0:
            return 0
        if n == 1:
            return 1
        if n in cashe:
            return cashe[n]
        # Store computed value in cache
        cashe[n] = fibonacci(n-1)+fibonacci(n-2)
        return cashe[n]
    return fibonacci       # Return the inner function

fib = caching_fibonacci()
print(f"F(20) is: {fib(20)}")