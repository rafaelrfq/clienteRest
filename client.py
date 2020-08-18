from pprint import pprint
from tkinter import *
from tkinter import messagebox, ttk
import requests
import json

# Requests al api

# get = requests.get('http://localhost:5000/api/formularios')
# post = requests.post('https://httpbin.org/post', data=json.dumps(userExample))

def enviar():
    if nombreInput.get() == '' or sectorInput.get() == '' or nivelEscolarCombo.get() == '---Seleccione---' or latitudInput.get() == '' or longitudInput.get() == '':
        messagebox.showerror('Campos Requeridos','Debe llenar todos los campos y seleccionar un nivel escolar.')
    else:
        formulario = {
            "nombre": nombreInput.get(),
            "sector": sectorInput.get(),
            "nivelEscolar": nivelEscolarCombo.get(),
            "latitud": latitudInput.get(),
            "longitud": longitudInput.get()
        }
        post = requests.post('http://localhost:5000/api/formularios', data=json.dumps(formulario))
        messagebox.showinfo('Datos Enviados', 'Los datos fueron enviados.')
        print(post)
    popularLista()

def popularLista():
    get = requests.get('http://localhost:5000/api/formularios')
    lista.delete(0, END)
    for o in get:
        lista.insert(END, o)

app = Tk()
app.title('Cliente REST')
app.geometry('500x450')

nombreLabel = Label(app, text='Nombre:', font=('bold', 14)).pack()
nombreInput = StringVar()
nombreEntry = Entry(app, textvariable=nombreInput).pack()

sectorLabel = Label(app, text='Sector:', font=('bold', 14)).pack()
sectorInput = StringVar()
sectorEntry = Entry(app, textvariable=sectorInput).pack()

nivelEscolarLabel = Label(app, text='Nivel Escolar:', font=('bold', 14)).pack()
nivelEscolarCombo = ttk.Combobox(app, values=['---Seleccione---', 'Basico', 'Medio', 'Grado Universitario', 'Postgrado', 'Doctorado'])
nivelEscolarCombo.current(0)
nivelEscolarCombo.pack()

latitudLabel = Label(app, text='Latitud:', font=('bold', 14)).pack()
latitudInput = StringVar()
latitudEntry = Entry(app, textvariable=latitudInput).pack()

longitudLabel = Label(app, text='Longitud:', font=('bold', 14)).pack()
longitudInput = StringVar()
longitudEntry = Entry(app, textvariable=longitudInput).pack()

enviarBtn = Button(app, text='Enviar Datos', font=('bold', 14), command=enviar, pady=3).pack()
listadoBtn = Button(app, text='Listar Formularios', font=('bold', 14), command=popularLista, pady=3).pack(side=BOTTOM)

frameLista = Frame(app)
frameLista.pack()

lista = Listbox(frameLista, height=8, width=70)
yscrollbar = Scrollbar(frameLista, orient='vertical')
xscrollbar = Scrollbar(frameLista, orient='horizontal')
lista.configure(yscrollcommand=yscrollbar.set, xscrollcommand=xscrollbar.set)
yscrollbar.configure(command=lista.yview)
xscrollbar.configure(command=lista.xview)
xscrollbar.pack(side=BOTTOM, fill='x')
lista.pack(side=LEFT)
yscrollbar.pack(side=RIGHT, fill='y')

app.mainloop()