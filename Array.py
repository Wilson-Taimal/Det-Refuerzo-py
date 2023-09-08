
from Ecuaciones import*
import math

def Calcular():
    Nb = float (c1ent01.get()) 
    Long = float (c1ent02.get())*100 
    r = float (c1ent03.get()) 
    sep = float (c1ent04.get()) 

    db = f_db(Nb)
    print("db = %.2f _ cm" %db)

    if (Nb <= 8):
        D = 6*db     
    else:
        D = 8*db

    print("D = %.2f _ cm" %D)
    print("\nArray Global")
    i = r + db + (D/2)                                 
    c2ent01.delete(0, 'end');              
    c2ent01.insert (0, "{:.2f}".format(i))

    Le = Long-(2*r)-(2*db)-D
    CantEsp = Le/sep
    SepReal = round(CantEsp,0)

    SepFinal = Le/SepReal                                 
    c2ent03.delete(0, 'end');              
    c2ent03.insert (0, "{:.2f}".format(SepFinal))
    
    Cant = SepReal+1                                 
    c2ent02.delete(0, 'end');              
    c2ent02.insert (0, "{:.2f}".format(Cant))

    print("Cota de inicio = %.2f _ cm" %i)
    print("Rows / Columns = %.2f _ un" %Cant)
    print("Rows / Columns offset = %.2f _ cm" %SepFinal)

    print("\nArray Local")    
    CantEsp = Long/sep
    EspReal = round(CantEsp,0)                                     
    c3ent01.delete(0, 'end');              
    c3ent01.insert (0, "{:.2f}".format(EspReal))

    EspFinal = Long/EspReal                                 
    c3ent02.delete(0, 'end');              
    c3ent02.insert (0, "{:.2f}".format(EspFinal))

    print("Rows / Columns = %.2f _ un" %EspReal)
    print("Rows / Columns offset = %.2f _ cm" %EspFinal)


# ================================================================================================= #
from tkinter import *
vent = Tk()
vent.geometry("410x430")
vent.title(" DISTRIBUCION DE REFUERZO EN PLANOS ")
vent.iconbitmap('D:\\BIBLIOTECA PERSONAL\\Programación\\Python\\logo-wat.ico')

rec1 = LabelFrame(vent, text = ' Datos iniciales. ')
rec1.pack()
rec1.place(x=5, y=5, width=400, height=150)

rec2 = LabelFrame(vent, text = ' Array Global ')
rec2.pack()
rec2.place(x=5, y=160, width=400, height=120)

rec3 = LabelFrame(vent, text = ' Array Local ')
rec3.pack()
rec3.place(x=5, y=285, width=400, height=90)

# Recuadro 1 botones
c1tex01 = Label(rec1, text = "N° barra a usar");                    c1tex01.pack()
c1tex01.place(x=5, y=10, width=280, height=20)
c1ent01 = Entry(rec1, justify=CENTER);                              c1ent01.place(x=295, y=10, width=90, height=20)

c1tex02 = Label(rec1, text = "Longitud de la losa o tramo _ m");    c1tex02.pack()
c1tex02.place(x=5, y=40, width=280, height=20)
c1ent02 = Entry(rec1, justify=CENTER);                              c1ent02.place(x=295, y=40, width=90, height=20)

c1tex03 = Label(rec1, text = "Recubrimiento lateral _ cm");         c1tex03.pack()
c1tex03.place(x=5, y=70, width=280, height=20)
c1ent03 = Entry(rec1, justify=CENTER);                              c1ent03.place(x=295, y=70, width=90, height=20)

c1tex04 = Label(rec1, text = "Separación entre barras _ cm");       c1tex04.pack()
c1tex04.place(x=5, y=100, width=280, height=20)
c1ent04 = Entry(rec1, justify=CENTER);                              c1ent04.place(x=295, y=100, width=90, height=20)

# Recuadro 2 botones

c2tex01 = Label(rec2, text = "Punto de arranque del array");            c2tex01.pack();     c2tex01.place(x=5, y=10, width=280, height=20)
c2ent01 = Entry(rec2, justify=CENTER);                                  c2ent01.place(x=295, y=10, width=90, height=20); c2ent01.config(bg="#ecf0f1")

c2tex02 = Label(rec2, text = "Row / Columns _ Cantidad");               c2tex02.pack();     c2tex02.place(x=5, y=40, width=280, height=20)
c2ent02 = Entry(rec2, justify=CENTER);                                  c2ent02.place(x=295, y=40, width=90, height=20); c2ent02.config(bg="#ecf0f1")

c2tex03 = Label(rec2, text = "Row / Columns _ Offset");                  c2tex03.pack();     c2tex03.place(x=5, y=70, width=280, height=20)
c2ent03 = Entry(rec2, justify=CENTER);                                   c2ent03.place(x=295, y=70, width=90, height=20); c2ent03.config(bg="#ecf0f1")


# Recuadro 3 botones
c3tex01 = Label(rec3, text = "Row / Columns _ Cantidad");               c3tex01.pack();     c3tex01.place(x=5, y=10, width=280, height=20)
c3ent01 = Entry(rec3, justify=CENTER);                                  c3ent01.place(x=295, y=10, width=90, height=20); c3ent01.config(bg="#ecf0f1")

c3tex02 = Label(rec3, text = "Row / Columns _ Offset");                 c3tex02.pack();     c3tex02.place(x=5, y=40, width=280, height=20)
c3ent02 = Entry(rec3, justify=CENTER);                                  c3ent02.place(x=295, y=40, width=90, height=20); c3ent02.config(bg="#ecf0f1")


# Recuadro 4 botones

bot1 = Button(vent, text = 'Calcular', font='Helvetica 8 bold', command=Calcular); bot1.pack()
bot1.place(x=155, y=380, width=100, height=20)

# firma
label = Label(vent, text = "wilson.taimalc@gmail.com - 2023", font='Arial 7'); label.pack()
label.place(x=5, y=410, width=400, height=10)

vent.mainloop()
