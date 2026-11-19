import math

a = int(input("Enter a: "))
b = int(input("Enter b: "))
k = int(input("Enter power of n in f(n): "))

p = math.log(a, b)

print("n^log_b(a) =", p)

if p > k:
    print("Case 1")
    print("Time Complexity: O(n^", p, ")")

elif math.isclose(p, k):
    print("Case 2")
    print("Time Complexity: O(n^", k, "log n)")

else:
    print("Case 3")
    print("Time Complexity: O(n^", k, ")")
    print("Check regularity condition: a*f(n/b) <= c*f(n), c < 1")