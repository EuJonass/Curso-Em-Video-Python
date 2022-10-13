print("*" * 40 )

m = float(input("DIGITE A METRAGEM:"))
km = m / 1000
hm = m / 100
da = m / 10
me = m
dm = m * 10
cm = m * 100
mm = m * 100

print("*" * 40)
print("O valor {:.0f} corresponde à:".format(m))
print("{:.3f} Quilômetros:".format(km))
print("{:.3f} Hectômetros:".format(hm))
print("{:.0f} Decâmetros:".format(da))
print("{:.0f} Metros:".format(me))
print("{:.0f} Decímetros:".format(dm))
print("{:.0f} Centímetros:".format(cm))
print("{:.0f} Milímetros:".format(mm))
print("*" * 40 )
