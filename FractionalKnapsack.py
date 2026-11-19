n = int(input("Enter number of items: "))

weight = list(map(int, input("Enter weights: ").split()))
profit = list(map(int, input("Enter profits: ").split()))

capacity = int(input("Enter capacity: "))

ratio = [profit[i] / weight[i] for i in range(n)]

items = sorted(zip(ratio, weight, profit), reverse=True)

total = 0

for r, w, p in items:
    if capacity >= w:
        total += p
        capacity -= w
    else:
        total += r * capacity
        break

print("Maximum Profit:", total)