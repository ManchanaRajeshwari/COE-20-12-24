def prime_number(n):
    if n>1:
        for i in range(2,(n//2)+1):
            if (n%i==0):
                return "Not a prime number"
        return "Prime number"
    else:
        return "Not a prime number"
n=int(input("Enter number to check whether prime or not"))
print(prime_number(n))