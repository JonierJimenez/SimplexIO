from tkinter import *
from Tabla  import Tabla
from tkinter import messagebox
from especiales import CEspeciales
from Matriz_sig import Matriz
1
class Resolver:
    def __init__(self,funcion,variables,restricciones,desig,result):
        self.funcion = funcion
        self.variables = variables
        self.restricciones = restricciones
        self.desig = desig
        self.result = result
        self.window = Tk()
        self.matriz = []
        self.degenerado = []
        self.bandera = False
        self.count = 0
        self.empezar()
        self.ventana()
        self.boton = None
        self.inicio = None
        self.pivote = None

    def mostrar(self):
        print("funcion: ",self.funcion,"\n\n")

        for i in range(len(self.variables)):
            print("X%d="%i+str(self.variables[i])+"\t\t",end="")

        print("\n")
        for i in range(len(self.restricciones)):
            print("Restriccion %d" % (i+1))
            for j in range(len(self.restricciones[i])):
                print("X%d=" % (j) + str(self.restricciones[i][j])+"\t\t",end="")
            print("\n")

        for i in range(len(self.desig)):
            print("desigualdad %d" % i+str(self.desig[i])+"\t",end="")
        print("\n")

        for i in range(len(self.result)):
            print("Resultado %d" % i+str(self.result[i])+"\t",end="")
        print("\n")

    def ventana(self):
        self.window.title("Metodo simplex")
        w, h = self.window.winfo_screenwidth(), self.window.winfo_screenheight()
        self.window.geometry("%dx%d+0+0" % (w, h))
        scrollbar = Scrollbar(self.window, orient="horizontal")
        scrollbar2 = Scrollbar(self.window)
        c = Canvas(self.window, xscrollcommand=scrollbar.set, yscrollcommand=scrollbar2.set, bg="#34495e", width="1000",height="768")
        scrollbar.config(command=c.xview)
        scrollbar2.config(command=c.yview)
        scrollbar2.pack(side=RIGHT, fill=Y)
        scrollbar.pack(side=BOTTOM, fill=X)
        self.inicio = Frame(c,bg="#34495e") #el frame
        self.inicio.columnconfigure(0, weight=1)
        self.inicio.rowconfigure(0, weight=1)
        c.pack(side="left", fill="both", expand=True)
        c.create_window(0, 0, window=self.inicio, anchor="nw")



        Label(self.inicio, width="4", height="2", bg="#34495e",font=("Comic Sans MS", 19)).grid(row=0, column=0, pady=50,padx=50)

        self.crearMatriz()

        self.boton = Button(self.inicio, text="Continuar", fg="#34495e", bg="#95a5a6", font=("Comic Sans MS", 19), cursor="hand2", command=lambda: self.obtenerPivote())
        self.boton.grid()

        self.window.update()
        c.config(scrollregion=c.bbox("all"))
        self.window.mainloop()

    def empezar(self):
        matriz1 = Tabla(self.funcion, self.variables, self.restricciones, self.desig, self.result)
        self.matriz = matriz1.matrizlol()

    def crearMatriz(self):
        label = []
        for i in range(4 + len(self.result)):
            label.append([])
            for j in range(len(self.matriz[0])):
                if self.matriz[i][j] == "":
                    label[i].append(Label(self.inicio, width="6", height="2", bg="#7f8c8d", font=("Comic Sans MS", 14),borderwidth=2, relief="solid"))
                    label[i][j].grid(row=i + 1, column=j + 1)
                else:
                    label[i].append(Label(self.inicio, text=self.matriz[i][j], fg="#d63031", width="6", height="2",bg="#95a5a6", font=("Comic Sans MS", 14), borderwidth=2, relief="solid"))
                    label[i][j].grid(row=i + 1, column=j + 1)

        pivote = CEspeciales(self.matriz, self.funcion)
        pivote.pivoteE()
        pivote.pivoteS()
        self.pivote = pivote.pivotefc
        if (pivote.nacotada):
            self.boton.config(state='disabled')


        if pivote.degenerado:
            self.bandera = True


        if pivote.solucion:
            self.bandera = False
            self.boton.config(state = 'disabled')
            a = str(self.matriz[len(self.matriz)-2][2])
            mult = False
            if(a.find("M")==-1):
                Label(self.inicio, text="Solucion = "+str(self.matriz[len(self.matriz)-2][2]), font=("Comic Sans MS", 19), bg="#34495e",fg="#fff200").grid(columnspan=3,row = 0 , column=1)
            else:
                messagebox.showwarning("Advertencia", "Problema no acotado hay variables artificiales en la solucion")
            for i in range(len(self.variables)):
                for j in range(2,len(self.matriz)-2):
                    if self.matriz[j][1].count("X"+str(i+1)) > 0: mult = True
                if mult == False: break
            if(mult==False):
                messagebox.showwarning("Advertencia", "Es una solucion optima multiple")

        if (pivote.abierto):
            self.boton.config(state='disabled')
        else:
            for i in range(len(self.matriz[0])):
                label[pivote.pivotefc[1]][i].config(bg="#1abc9c")
            for i in range(len(self.matriz)):
                label[i][pivote.pivotefc[0]].config(bg="#1abc9c")
            label[pivote.pivotefc[1]][pivote.pivotefc[0]].config(bg="#8e44ad")

        if self.bandera:
            degenerado = []
            for i in range(len(self.matriz)):
                degenerado.append(str(self.matriz[i][2]))
            if(degenerado == self.degenerado):
                self.count += 1
                if(self.count == 3):
                    self.boton.config(state='disabled')
                    messagebox.showwarning("Advertencia", "Es un problema con ciclajes")
                    Label(self.inicio, text="Solucion = " + str(self.matriz[len(self.matriz) - 2][2]),font=("Comic Sans MS", 19), bg="#34495e").grid(columnspan=3, row=0, column=1)
            self.degenerado = degenerado

    def obtenerPivote(self):
        matriz = Matriz(self.matriz,self.pivote)
        self.matriz = matriz.convinar()
        self.crearMatriz()