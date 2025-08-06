import math
from tkinter import *

window = Tk()
window.title ("Calculadora")
window.geometry("420x420+550+200" ) # it goes like: ANCHO X ALTO + Position X + Y
window.config(bg="#4a494a")

def suma ():
    print("operacion suma")
    n1 = text1.get()
    n2 = text2.get()
    r = float(n1) + float(n2)
    text3.delete (0, "end")
    text3.insert (0,r)

def resta ():
    print("operacion resta")
    n1 = text1.get()
    n2 = text2.get()
    r = float(n1) - float(n2)
    text3.delete (0, "end")
    text3.insert (0,r)

def mult ():
    print("operacion multiplicacion")
    n1 = text1.get()
    n2 = text2.get()
    r = float(n1) * float(n2)
    text3.delete (0, "end")
    text3.insert (0,r)

def div ():
    print("operacion division")
    n1 = text1.get()
    n2 = text2.get()
    r = float(n1) / float(n2)
    text3.delete (0, "end")
    text3.insert (0,r)


def elevado ():
    print("operacion elevado")
    n1 = text1.get()
    n2 = text2.get()
    r = float(n1)**float(n2)
    text3.delete (0, "end")
    text3.insert (0,r)

def raiz ():
    print("operacion raiz")
    n1 = float(text1.get())
    n2 = float(text2.get())
    r = math.sqrt(n1 + n2)
    text3.delete (0, "end")
    text3.insert (0,r)

def porcentaje():
    print("operacion porcentaje")
    n1 = float(text1.get())
    n2 = float(text2.get())
    r = (n1 / n2) * 100 
    text3.delete (0, "end")
    text3.insert (0,r)
    
    

label1 = Label(window, text="primer numero: ",
               bg="white")
label1.place(x= 10, y =10, width=200, height=30)

text1 = Entry(window, bg="lightblue")
text1.place(x=200, y =10,width=200, height=30)

label2 = Label (window, text="segundo numero: ",
               bg="white")
label2.place(x= 10, y =45, width=200, height=30)

text2 = Entry(window, bg="lightblue")
text2.place(x=200, y =45,width=200, height=30)

label3 = Label (window, text=" resultado: ",
                bg="white")
label3.place(x= 10, y =80, width=200, height=30)

text3 = Entry(window,
              bg="lightgreen")
text3.place(x=200, y =80,
            width=200, height=30)

#botones de la calculadora

suma_Button = Button(window, text="+",
                     bg="#fb1d9e", command=suma)
suma_Button.place(x= 10, y =200,
                  width=75, height=30)

res_Button = Button(window, text="-",
                    bg="#f759b5", command=resta)
res_Button.place(x= 100, y =200,
                 width=75, height=30)

mul_Button = Button(window, text="x",
                    bg="#fba8d9",command=mult)
mul_Button.place(x=190 , y =200,
                 width=75, height=30)

div_Button = Button(window, text="/",
                    bg="#fba8f9", command=div)
div_Button.place(x= 280, y =200, 
                 width=75, height=30)

elevado_Button = Button(window, text="^",
                    bg="#fb67f7", command=elevado)
elevado_Button.place(x= 230, y =250, 
                 width=75, height=30)

raiz_Button = Button(window, text="√",
                    bg="#f81bf2", command=raiz)
raiz_Button.place(x=50, y =250, 
                 width=75, height=30)

boton_PJ = Button(window, text=" % ",
                  bg="#9b2a97", command=porcentaje)
boton_PJ.place(x=140, y=250, width=75, height=30)


window.mainloop()

