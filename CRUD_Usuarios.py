from tkinter import *
from tkinter import messagebox
from dbconfig import dbconfig   # Importamos el diccionario sqlserver_config para poder usar sus datos
import pypyodbc # Muy importante, modulo necesario para conectar python con SQL Server pip install pypyodbc

# Creamos una variable para la conexion, de esta manera podemos llamar a la conexion a la db de manera más sencilla
con = pypyodbc.connect(**dbconfig)

# Metodo cursor
# El cursor en python nos permite interactuar con la db y ejecutar comandos sin necesidad de ser en la consola de la db, muy importante para realizar operaciones
cursor = con.cursor() 

class Bookdb:
    def __init__(self):
        self.con = pypyodbc.connect(**dbconfig)
        self.cursor = con.cursor()
        print("Te has conectado a la base de datos. ")
        print(con)

    def __del__(self):
        self.con.close()

    def view(self):
        self.cursor.execute("SELECT * FROM usuarios")
        row = self.cursor.fetchall()
        return row

    # Funcion de insercion de datos
    def insert(self, usuario, password, email):
        sql = ("INSERT INTO usuarios(usuario, password, email) VALUES(?, ?, ?)")
        value = [usuario, password, email]
        self.cursor.execute(sql, value)
        self.con.commit()

    # Funcion de modificacion de datos
    def update(self, id, usuario, password, email):
        tsql = 'UPDATE usuarios SET  usuario = ?, password = ?, email = ? WHERE id=?'
        self.cursor.execute(tsql, [usuario,password,email,id])
        self.con.commit()

    # Funcion para borrar datos
    def delete(self, id):
        defquery = "DELETE FROM usuarios WHERE id = ?"
        self.cursor.execute(defquery, [id])
        self.con.commit()

db = Bookdb()

# Lista de funciones para los botones y cursor

# Importante, una funcion que indica cuando tienes selectionado algo en la lista de registros
def get_selected_row(event):
    global selected_tuple
    index = list_bx.curselection()[0]
    selected_tuple = list_bx.get(index)
    usuario_entry.delete(0, 'end')
    usuario_entry.insert('end', selected_tuple[1])
    password_entry.delete(0, 'end')
    password_entry.insert('end', selected_tuple[2])
    email_entry.delete(0, 'end')
    email_entry.insert('end', selected_tuple[3])

# Funcion para ver todos los registros
def view_record():
    list_bx.delete(0, 'end')
    for row in db.view():
        list_bx.insert('end', row)

# Funcion para añadir usuario mediante el boton
def add_user():
    db.insert(usuario_text.get(), password_text.get(), email_text.get())
    list_bx.delete(0, 'end')
    list_bx.insert('end', (usuario_text.get(), password_text.get(), email_text.get()))
    usuario_entry.delete(0, 'end')
    password_entry.delete(0, 'end')
    email_entry.delete(0, 'end')
    con.commit()

# Funcion para borrar un registro selecionado
def delete_records():
    db.delete(selected_tuple[0])
    con.commit()

# Funcion para limpiar la pantalla
def clear_screen():
    list_bx.delete(0, 'end')
    usuario_entry.delete(0, 'end')
    password_entry.delete(0, 'end')
    email_entry.delete(0, 'end')

# Funcion para modificar un registro 
def update_records():
    db.update(selected_tuple[0], usuario_text.get(), password_text.get(), email_text.get())
    usuario_entry.delete(0, 'end')
    password_entry.delete(0, 'end')
    email_entry.delete(0, 'end')
    con.commit()

# Funcion para cerrar la app con un caja de alerta
def on_closing():
    dd = db
    if messagebox.askokcancel("Salir", "Quieres salir? "):
        root.destroy()
        del dd

root = Tk()    # Crea la ventana

root.title("Administrador de usuarios CRUD")    # Titulo de la ventana
root.configure(background="light green")    # EL color del findo de la ventana
root.geometry("970x525")    # Tamaño de la ventana
root.resizable(width=False, height=False)    # Previene que la ventana se redimensione de forma automática

# Creamos los rectangulos de informacion
Label(root, text="usuario:", padx=15, pady=10, background="light green", font=("TKDefaultFont", 16)).grid(row=0, column=0, sticky=W)
usuario_text = StringVar()
usuario_entry = Entry(root, width = 24,textvariable = usuario_text)
usuario_entry.grid(row=0, column=1, sticky=W)

usuario_label = Label(root, text="contraseña:", padx=15, pady=10, background="light green", font=("TKDefaultFont", 16))
usuario_label.grid(row=0, column=2, sticky=W)
password_text = StringVar()
password_entry = Entry(root, width = 24,textvariable = password_text)
password_entry.grid(row=0, column=3, sticky=W)

usuario_label = Label(root, text="correo:", padx=15, pady=10, background="light green", font=("TKDefaultFont", 16))
usuario_label.grid(row=0, column=4, sticky=W)
email_text = StringVar()
email_entry = Entry(root, width = 24,textvariable = email_text)
email_entry.grid(row=0, column=5, sticky=W)

# Boton para insertar usuario
add_btn = Button(root, text="Añadir", padx=5, pady=5, bg="blue", fg="white", font="helvetica 10 bold", command=add_user)
add_btn.grid(row=0, column=7, sticky=W)

# Boton para mostrar los registros actuales
list_bx = Listbox(root, height=16, width=45, font="helvetica 13", bg="light blue")
list_bx.grid(row=3, column=1, columnspan=14, sticky=W+E, pady=40, padx=15)
list_bx.bind('<<ListboxSelect>>', get_selected_row)

# Una scrollbar (la barra para que se mueva para arriba y para abajo)
scroll_bar = Scrollbar(root)
scroll_bar.grid(row=1, column=8, rowspan=14, sticky=W)

list_bx.configure(yscrollcommand=scroll_bar.set)  # Muy importante para que puedas scrolear hacia arriba
scroll_bar.configure(command=list_bx.yview)

# Botones para las editar, borrar, mostrar, limpiar pantalla, y salir de la app
modify_btn = Button(root, text="Modificar registro", bg="purple", fg="white", font="helvetica 10 bold", command=update_records)
modify_btn.grid(row=15, column=4)

delete_btn = Button(root, text="Borrar registro", bg="red", fg="white", font="helvetica 10 bold", command=delete_records)
delete_btn.grid(row=15, column=5)

view_btn = Button(root, text="Ver todos los registros", bg="black", fg="white", font="helvetica 10 bold", command=view_record)
view_btn.grid(row=15, column=1)

clear_btn = Button(root, text="Limpiar pantalla", bg="maroon", fg="white", font="helvetica 10 bold", command=clear_screen)
clear_btn.grid(row=15, column=2)

exit_btn = Button(root, text="Salir de la app", bg="dark blue", fg="white", font="helvetica 10 bold", command=on_closing)
exit_btn.grid(row=15, column=3)

# Muy importante en cualquier programa o juego, un loop principal, para que la aplicacion siempre se esté ejecutando
root.mainloop()