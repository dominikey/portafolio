import tkinter as tk
from tkinter import messagebox

class Calculadora:
    def __init__(self, master):
        self.master = master
        master.title("Calculadora ")

        self.entrada = tk.Entry(master, width=35, borderwidth=5, font=('NEW HANSPIRE', 14))
        self.entrada.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

        self.primer_numero = None
        self.operacion = None
        self.nuevo_numero = True 

        # Definir los botones
        self.crear_botones()

    def crear_botones(self):
        # Números
        botones_numeros = [
            '7', '8', '9',
            '4', '5', '6',
            '1', '2', '3',
            '0'
        ]
        # Operaciones
        botones_especiales = [
            'C', '/', '*',
            '-', '+', '=',
            '.'
        ]

        fila = 1
        columna = 0
        for boton in botones_numeros:
            tk.Button(self.master, text=boton, padx=30, pady=20, font=('Arial', 12),
                      command=lambda b=boton: self.clic_numero(b)).grid(row=fila, column=columna, padx=2, pady=2)
            columna += 1
            if columna > 2:
                columna = 0
                fila += 1

        tk.Button(self.master, text='0', padx=70, pady=20, font=('Arial', 12),
                  command=lambda: self.clic_numero('0')).grid(row=fila, column=0, columnspan=2, padx=2, pady=2)

        tk.Button(self.master, text='.', padx=30, pady=20, font=('Arial', 12),
                  command=lambda: self.clic_numero('.')).grid(row=fila, column=2, padx=2, pady=2)

        fila_operaciones = 1
        columna_operaciones = 3
        tk.Button(self.master, text='C', padx=30, pady=20, font=('Arial', 12),
                  command=self.limpiar).grid(row=fila_operaciones, column=columna_operaciones, padx=2, pady=2)
        fila_operaciones += 1

        tk.Button(self.master, text='/', padx=30, pady=20, font=('Arial', 12),
                  command=lambda: self.clic_operacion('/')).grid(row=fila_operaciones, column=columna_operaciones, padx=2, pady=2)
        fila_operaciones += 1

        tk.Button(self.master, text='*', padx=30, pady=20, font=('Arial', 12),
                  command=lambda: self.clic_operacion('*')).grid(row=fila_operaciones, column=columna_operaciones, padx=2, pady=2)
        fila_operaciones += 1

        tk.Button(self.master, text='-', padx=30, pady=20, font=('Arial', 12),
                  command=lambda: self.clic_operacion('-')).grid(row=fila_operaciones, column=columna_operaciones, padx=2, pady=2)
        fila_operaciones += 1

        tk.Button(self.master, text='+', padx=30, pady=20, font=('Arial', 12),
                  command=lambda: self.clic_operacion('+')).grid(row=fila_operaciones, column=columna_operaciones, padx=2, pady=2)
        fila_operaciones += 1

        tk.Button(self.master, text='=', padx=30, pady=20, font=('Arial', 12),
                  command=self.calcular).grid(row=fila, column=3, padx=2, pady=2)


    def clic_numero(self, numero):
        if self.nuevo_numero:
            self.entrada.delete(0, tk.END)
            self.nuevo_numero = False
        current = self.entrada.get()

        # Evitar múltiples puntos decimales
        if numero == '.' and '.' in current:
            return
        self.entrada.insert(tk.END, str(numero))

    def limpiar(self):
        self.entrada.delete(0, tk.END)
        self.primer_numero = None
        self.operacion = None
        self.nuevo_numero = True

    def clic_operacion(self, op):
        try:
            self.primer_numero = float(self.entrada.get())
            self.operacion = op
            self.nuevo_numero = True # Para que el sig número reemplace el anterior
        except ValueError:
            messagebox.showerror("Error de Entrada", "Por favor, ingresa un número válido antes de una operación.")
            self.limpiar()


    def calcular(self):
        try:
            segundo_numero = float(self.entrada.get())
            resultado = 0

            if self.operacion == '+':
                resultado = self.primer_numero + segundo_numero
            elif self.operacion == '-':
                resultado = self.primer_numero - segundo_numero
            elif self.operacion == '*':
                resultado = self.primer_numero * segundo_numero
            elif self.operacion == '/':
                if segundo_numero == 0:
                    messagebox.showerror("Error", "¡No se puede dividir por cero!")
                    self.limpiar()
                    return
                resultado = self.primer_numero / segundo_numero

            self.entrada.delete(0, tk.END)
            if resultado == int(resultado):
                 self.entrada.insert(0, int(resultado))
            else:
                self.entrada.insert(0, resultado)

            self.primer_numero = resultado # Para encadenar operaciones
            self.operacion = None
            self.nuevo_numero = True

        except (ValueError, TypeError):
            messagebox.showerror("Error", "Operación inválida. Asegúrate de ingresar números.")
            self.limpiar()

root = tk.Tk()
mi_calculadora = Calculadora(root)
root.mainloop()