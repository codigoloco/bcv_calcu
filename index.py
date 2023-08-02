import pyBCV
import tkinter as tk
from datetime import datetime




def data():
    curren= pyBCV.Currency()
    valor=curren.get_rate(currency_code='USD',prettify=False)#Falor referencial por cada moneda y sin prefijo cambiar a true si desea el prefijo
    f_act=curren.get_rate(currency_code='Fecha')#Fecha de la actualizacion
    resul.set("Bs "+valor)
    fecha_ac.set(f_act)
    ahora= datetime.now()
    f_sistem=ahora.strftime("%Y-%m-%d %H:%M:%S")
    fecha_sis.set(f_sistem)
    return valor

def operacion():

    num1= entry1.get()
    res=float(valor)*float(num1)
    res=round(res,4)
    resultado.set(res)
    
def validate_number(text):
    return text.isdigit() or text == "."

def read_entry(event):
    operacion()

ventana =tk.Tk()
ventana.geometry('150x170')
ventana.resizable(False, False)
resul=tk.StringVar()
fecha_ac=tk.StringVar()
fecha_sis=tk.StringVar()
resultado=tk.StringVar()
etiqueta= tk.Label(ventana,textvariable=resul)
etiqueta.grid(row=0,column=1)
etiqueta= tk.Label(ventana,textvariable=fecha_ac)
etiqueta.grid(row=1,column=1)
etiqueta2= tk.Label(ventana,textvariable=fecha_sis)
etiqueta2.grid(row=2,column=1)
etiqueta2= tk.Entry(ventana,textvariable=resultado)
etiqueta2.config(state="disabled")
etiqueta2.grid(row=3,column=1)
entry1= tk.Entry(ventana, validate="key", validatecommand=(ventana.register(validate_number), '%S'))
entry1.grid(row=4,column=1)
bot=tk.Button(ventana,text="Actualizar",command=data).grid(row=5,column=1,sticky="w")
bot2=tk.Button(ventana,text="Dolares",command=operacion).grid(row=5,column=1,sticky="e")
valor=data()
entry1.bind("<Return>", read_entry)

ventana.mainloop()



