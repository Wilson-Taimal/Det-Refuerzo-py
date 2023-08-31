# Calculo long de gancho estribos y barras
from Ecuaciones import*
import math
fc = 21         # Resistencia del concreto _ MPa
fy = 420        # Fluencia del acero _ MPa
we = 1          # Ψe: Factor por ubicación          
wt = 1          # Ψt: Factor por ubicación
n = 1           # λ: Factor peso del concreto 
Nb = 5          # Numero de la barra selecionanda se permite hasta la N° 10    

dbp = f_dbp(Nb);                       print(' dbp = ', dbp)
db = f_db(Nb);                         print(" db  = %.2f _ cm" %db)
Asb = f_Asb(Nb);                       print(" Asb = %.2f _ cm²" %Asb)
Wb = f_Wb(Nb);                         print(" Wb  = %.2f _ kg/m" %Wb)

# Gancho estribo a 90°
print ("")
print ("Long de gancho en estribos a 90° _ cm")

if (Nb <= 5):
    D = 4*db
    K = max(7.5, 6*db)
    L = (1/4*math.pi*D)+K
    H = K + D/2 + db 
else:
    D = 6*db
    K = 12*db
    L = (1/4*math.pi*D)+K
    H = K + D/2 + db
print(' D = ', D)
print(' K = ', K)
print(' L = ', L)
print(' H = ', H)

# Gancho estribo a 135°
print ("")
print ("Long de gancho en estribos a 135° _ cm")
K = max(7.5, 6*db)
if (Nb <= 5):
    D = 4*db
    H = (0.707107*K)+D+db
    L = (0.375*math.pi*D)+K
else:
    D = 6*db
    H = (0.707107*K)+D+db
    L = (0.375*math.pi*D)+K
print(' D = ', D)
print(' K = ', K)
print(' L = ', L)
print(' H = ', H)

# Gancho estribo a 180°
print ("")
print ("Long de gancho en estribos a 180° _ cm")
K = max(6.5, 4*db)
if (Nb <= 5):
    D = 4*db
    L = (0.5*math.pi*D)+K
    H = D + 2*db 
else:
    D = 6*db
    L = (0.5*math.pi*D)+K
    H = D + 2*db
print(' D = ', D)
print(' K = ', K)
print(' L = ', L)
print(' H = ', H)

# Gancho en barras a 90°
print ("")
print ("Long de gancho en barras a 90° _ cm")

if (Nb <= 8):
    D = 6*db
    K = 12*db
    L = (1/4*math.pi*D)+K
    H = K + D/2 + db 

else:
    D = 8*db
    K = 8*db
    L = (1/4*math.pi*D)+K
    H = K + D/2 + db
print(' D = ', D)
print(' K = ', K)
print(' L = ', L)
print(' H = ', H)

# Gancho barras a 180°
print ("")
print ("Long de gancho en barras a 180° _ cm")
K = max(6.5, 4*db)
if (Nb <= 8):
    D = 6*db
    L = (0.5*math.pi*D)+K
    H = D + 2*db 
else:
    D = 8*db
    L = (0.5*math.pi*D)+K
    H = D + 2*db
print(' D = ', D)
print(' K = ', K)
print(' L = ', L)
print(' H = ', H)

#Longitud de desarrollo ldh
print ("")
print ("Long de desarrollo ldh _ cm")

ldh = max(0.8*db , (0.24*we*fy)/(n*math.sqrt(fc))*db)
print(' ldh = ', ldh)
print(' ldh1 = ', ldh*0.8)

# Longitud de desarrollo ld
print ("")
print ("Long de desarrollo en tracción ld _ cm")
if (Nb <= 6):
    ld = (wt*we*fy)/(2.1*n*math.sqrt(fc))*db
else:
    ld = (wt*we*fy)/(1.7*n*math.sqrt(fc))*db
print(' ld clase A= ', ld)
print(' ld clase B= ', ld*1.3)
print ("")
