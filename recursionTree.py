def solve(n, a, b, k):

    # Base condition
    if n <= 1:
        return 1

    total = 0

    # Make a recursive call a times
    for i in range(a):
        total += solve(n // b, a, b, k)

    # Add work done at current level
    total += n ** k

    return total


a = int(input("Enter a: "))
b = int(input("Enter b: "))
k = int(input("Enter power k: "))
n = int(input("Enter n: "))

print("Result:", solve(n, a, b, k))