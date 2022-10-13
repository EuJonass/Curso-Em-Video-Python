print("=" * 20)
print("  10 TERMOS DA PA")
print("=" * 20)
t = int(input("Primeiro termo:"))
r = int(input("Razão:"))
decimo = t + (10 - 1) * r


print("-x-" * 30)
for c in range(t, decimo + r, r):
    print("{}".format(c), end=" ➜ ")

print("ACABOU")
print("-x-" * 30)
