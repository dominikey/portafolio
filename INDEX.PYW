#PY IS ONLY FOR CONSOLA OR PYW IS IN WINDOWS ORIENTED, IT'S LIKE THE SAME


from tkinter import *
from PIL import Image, ImageTk

window = Tk ()

window.title("Dulce Equilibrio")
window.geometry("420x420+550+200")
window.resizable(0,0)
#window.iconbitmap("fotos\logo.ico") #revisar
window.configure(bg="lightblue")
window.resizable(0,0)

#container
container = Frame(window)
container.pack(fill="both", expand=True)
container.grid_rowconfigure(0, weight=1)
container.grid_configure(0, weight=1)

#frame principal
frame1 = Frame(container)
frame1.pack(fill="both", expand=True)

#cargar img
fondo_img = Image.open("fotos/logo.png") #otro
fondo_img = fondo_img.resize
#fondo_tk = ImageTk.PhotoImage(imgagen de foondo)

#crear label de imagen
fondo_label = Label(frame1, image= fondo_img)
fondo_label.place(x=0, y=0, relwidth=1, relheight=1)

#crear los demas elementos ecima de la imagen del frame 
#logotipo
logo_img = PhotoImage()
image_logo = Label(frame1, image = klakjdsk)
image_logo.pack (pady=20)

label_uduario = Label(frame1, text="usuario:", font=("arial",14, "bold"),bg="white")
label_uduario.pack(padx=10,pady=10)

campo_usuario = Entry(frame)
campo_usuario.pack(padx=10, pady=10)

window.mainloop()

