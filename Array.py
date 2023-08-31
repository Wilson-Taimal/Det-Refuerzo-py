
db = 0.95
D = 5.7

Long = 180      # cm
r = 5           # cm
sep = 20        # cm

print("")
print("Array Global")
i = r + db + (D/2)
Le = Long-(2*r)-(2*db)-D
CantEsp = Le/sep
SepReal = round(CantEsp,0)
SepFinal = Le/SepReal
CantBarr = SepReal+1
print("Cota de inicio = %.2f _ cm" %i)
print("Rows / Columns = %.2f _ cm" %CantBarr)
print("Rows / Columns offset = %.2f _ cm" %SepFinal)


print("")
print("Array Local")
L = 140
Esp = 15
CantEsp = L/sep
SepReal = round(CantEsp,0)
SepFinal = L/SepReal
CantBarr = SepReal+1

print("Rows / Columns = %.2f _ cm" %CantBarr)
print("Rows / Columns offset = %.2f _ cm" %SepFinal)

print("")
