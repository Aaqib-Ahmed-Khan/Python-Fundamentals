def factorial(n):
    ans = 1  # Correct initialization
    if n == 0:
        return 1  # Ensure the function returns for n=0
    else:
        for i in range(1, n + 1):
            ans *= i
        return ans

n = int(input("enter n: "))
output = factorial(n)
print("The factorial is:", output)
