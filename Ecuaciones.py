import math

# FUNCIÓN DIÁMETRO EN PULG'S BARRAS DE REFUERZO
# Nb: Número de la barra
# Db: Diametro de la barra en pulgadas

def f_dbp(Nb):
    Nb = Nb
#    print ('Nb =',Nb)
    match Nb:
        case 2:
            dbp = '1/4'
        case 3:
            dbp = '3/8'
        case 4:
            dbp = '1/2'
        case 5:
            dbp = '5/8'
        case 6:
            dbp = '3/4'
        case 7:
           dbp = '7/8'
        case 8:
            dbp = '1'            
        case 9:
            dbp = '1 1/8'
        case 10:
            dbp = '1 1/4'
        case _ :
            print ('Nb no valido')
    return (dbp)

# FUNCIÓN DIÁMETRO BARRAS DE REFUERZO
# Nb: Número de la barra
# Db: Diametro de la barra _ cm

def f_db(Nb):
    Nb = Nb
#    print ('Nb =',Nb)
    match Nb:
        case 2:
            db = 0.64
        case 3:
            db = 0.95
        case 4:
            db = 1.27
        case 5:
            db = 1.59
        case 6:
            db = 1.91
        case 7:
           db = 2.22
        case 8:
            db = 2.54            
        case 9:
            db = 2.87
        case 10:
            db = 3.23
        case _ :
            print ('Nb no valido')
    return (db)

# FUNCIÓN AREA BARRAS DE REFUERZO
# Nb: Número de la barra
# Asb: Área de la barra _ cm²

def f_Asb(Nb):
    Nb = Nb
#    print ('Nb =',Nb)
    match Nb:
        case 2:
            Asb = 0.32
        case 3:
            Asb = 0.71
        case 4:
            Asb = 1.29
        case 5:
            Asb = 1.99
        case 6:
            Asb = 2.84
        case 7:
           Asb = 3.87
        case 8:
            Asb = 5.10            
        case 9:
            Asb = 6.45
        case 10:
            Asb = 8.19
        case _ :
            print ('Nb no valido')
    return (Asb)

# FUNCIÓN PESO UNITARIO BARRAS DE REFUERZO
# Nb: Número de la barra
# wb: Peso unitario de la barra _ kg/m

def f_Wb(Nb):
    Nb = Nb
#    print ('Nb =',Nb)
    match Nb:
        case 2:
            Wb = 0.250
        case 3:
            Wb = 0.560
        case 4:
            Wb = 0.994
        case 5:
            Wb = 1.552
        case 6:
            Wb = 2.235
        case 7:
           Wb = 3.042
        case 8:
            Wb = 3.973            
        case 9:
            Wb = 5.060
        case 10:
            Wb = 6.404
        case _ :
            print ('Nb no valido')
    return (Wb)

def f_GE90(Nb, db):
    import math 
    if (Nb <= 5):
        D = 4*db
        K = max(7.62, 6*db)
        L = (1/4*math.pi*D)+K
        H = L + db 
    else:
        D = 6*db
        K = 12*db
        L = (1/4*math.pi*D)+K
        H = L + db
        
    return (D, K, L, H)


