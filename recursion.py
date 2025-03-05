def factorial(n):
    # bas case
    if n==0:
        return 1
    ans=n * factorial(n-1)
    return ans
n=int(input("enter n :"))
print(factorial(n))

