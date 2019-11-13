#Jesus Lopez Florez Email: jeespoping@gmail.com
import re
import tkinter as tk
from tkinter import messagebox
from Pregunta import Pregunta


class Main:
    def __init__(self):
        self.window = tk.Tk()
        self.ventana()
        self.numvariables = None
        self.numvarestricciones = None

    def userText(self,even):
        self.numvariables.delete(0, tk.END)
        self.numvariables.config(fg="#ecf0f1")

    def userText1(self, even):
        self.numvarestricciones.delete(0, tk.END)
        self.numvarestricciones.config(fg="#ecf0f1")

    def ventana(self):
        self.window.title("Metodo simplex")
        self.window.resizable(0,0)  #No redimension
        inicio = tk.Frame() #el frame
        inicio.pack(fill="both", expand="true") #adaptarse
        inicio.config(bg="#34495e", width = "1000", height = "768")

        #numero de variables
        tk.Label(inicio,text="Cantidad de variables: ",fg="#ecf0f1", bg="#34495e", font = ("Comic Sans MS",18)).place(x=10, y = 10)
        self.numvariables = tk.Entry(inicio,bg="#34495e",font = ("Comic Sans MS",18), fg="#bdc3c7", justify = tk.CENTER, width = 10, borderwidth=5)
        self.numvariables.place(x=270, y = 10)
        self.numvariables.insert(0,"Digite")
        self.numvariables.bind("<Button>",self.userText)

        #numero de restricciones
        tk.Label(inicio, text="Cantidad de restricciones: ", fg="#ecf0f1", bg="#34495e", font=("Comic Sans MS", 18)).place(x=10, y=80)
        self.numvarestricciones = tk.Entry(inicio,bg="#34495e",font = ("Comic Sans MS",18), fg="#bdc3c7", justify = tk.CENTER, width = 10, borderwidth=5)
        self.numvarestricciones.place(x=320, y=80)
        self.numvarestricciones.insert(0, "Digite")
        self.numvarestricciones.bind("<Button>",self.userText1)

        #Boton
        tk.Button(inicio,text="Continuar", fg = "#34495e", bg = "#95a5a6", font=("Comic Sans MS", 19), cursor = "hand2", command=self.validar).place(x=350,y=200)

        self.window.mainloop()

    def validar(self):
        estructuraentero = re.compile('^\d{1,2}$')
        if (re.search(estructuraentero, self.numvarestricciones.get()) is None) or (re.search(estructuraentero, self.numvariables.get()) is None):
            messagebox.showwarning("Cuidado", "Ingrese maximo 2 numeros entero")
        else:
            rest = self.numvariables.get()
            var = self.numvarestricciones.get()
            self.window.destroy()
            Pregunta(rest,var)




if __name__== '__main__':
    aplication = Main()