orders = [15.99, 4.39, 123.45, 7.00]
total = 0

for i in range(2):
    total += orders.pop(0)

print(total)
