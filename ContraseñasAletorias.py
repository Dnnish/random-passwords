from tkinter import *
import random
import string
import mysql.connector


class Contraseña_Random:
    def __init__(self, master):
        self.master = master
        master.title("Contraseñas Aleatorias")

        # Cantidad de contraseñas a generar
        self.etiqueta = Label(master, text="Cantidad de contraseñas a generar:")
        self.etiqueta.pack()
        self.cantidadaText = Entry(master)
        self.cantidadaText.pack()

        # Longitud de la contraseña
        self.etiqueta = Label(master, text="Longitud de la contraseña:")
        self.etiqueta.pack()
        self.longitud_texto = Entry(master)
        self.longitud_texto.pack()

        # Boton para generar la contraseña
        self.boton = Button(master, text="Generar", command=self.generar)
        self.boton.pack()
        self.botonCerrar = Button(master, text="Cerrar", command=master.quit)
        self.botonCerrar.pack()

        # Contraseña generada
        self.contraseñaGenerada = Label(master, text="Contraseñas Generadas")
        self.etiqueta.pack()

        # Texto de la contraseña
        self.contraseñasText = Text(master, height=10, width=30)
        self.contraseñasText.pack()
        # Quita la opcion de editar el texto
        self.contraseñasText.config(state=DISABLED)

    # funcion para generar la contraseña
    def generar(self):
        number_of_strings = int(self.cantidadaText.get())
        length_of_string = int(self.longitud_texto.get())
        contraseñas = []
        for x in range(number_of_strings):
            contraseña = "".join(
                random.choice(string.ascii_letters + string.digits)
                for _ in range(length_of_string)
            )
            contraseñas.append(contraseña)

        self.mostrar_contraseñas(contraseñas)
        self.guardar_contraseñas(contraseñas)

    # funcion para mostrar la contraseña
    def mostrar_contraseñas(self, contraseñas):
        self.contraseñasText.config(state=NORMAL)
        self.contraseñasText.delete(1.0, END)
        for contraseña in contraseñas:
            self.contraseñasText.insert(END, contraseña + "\n")        
        self.contraseñasText.config(state=DISABLED)

    # funcion para guardar la contraseña
    def guardar_contraseñas(self, contraseñas):
        bd_host = 'localhost'
        bd = 'pythonPrueba'
        bd_user = 'root'
        bd_contraseña = 'Estefano123.'
        try:
            conexion = mysql.connector.connect(
                host=bd_host,
                user=bd_user,
                password=bd_contraseña,
                database=bd
            )
            cursor = conexion.cursor()

            for contraseña in contraseñas:
                query = "INSERT INTO passwords (con_contraseña) VALUES (%s)"
                valores = (contraseña,)
                cursor.execute(query, valores)

            conexion.commit()
            print("Contraseñas guardadas correctamente")

        except mysql.connector.Error as error:
            print("Error al guardar las contraseñas:", error)

        finally:
                cursor.close()
                conexion.close()


root = Tk()
root.geometry("500x300+560+240")
miVentana = Contraseña_Random(root)
root.mainloop()
