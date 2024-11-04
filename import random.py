import random

n = int(input("Masukkan nilai N: "))

for i in range(n):
    bilangan_acak = random.uniform(0, 0.5)
    print(f"Data ke-{i+1}: {bilangan_acak}")

print("-FINISH-")