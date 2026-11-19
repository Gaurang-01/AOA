jobs = [
    ('A', 2, 100),
    ('B', 1, 50),
    ('C', 2, 10),
    ('D', 1, 20)
]
jobs.sort(key=lambda x:x[2],reverse=True)

slots=[False]*3
total = 0

for id,deadline,profit in jobs:
    for j in range(deadline-1,-1,-1):
        if not slots[j]:
            slots[j]=True
            total+=profit
            break

print(total)