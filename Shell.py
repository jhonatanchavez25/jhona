#Importamos librerias
import tkinter as tk
from PIL import Image, ImageTk
import subprocess
import webbrowser


def abrir_terminal():
    subprocess.Popen("start cmd", shell=True)

def abrir_navegador():
    webbrowser.open("https://www.google.com")

def abrir_calculadora():
    subprocess.Popen("calc")

root = tk.Tk()
root.title("shell Grafico(Sistemas operativos)")
root.geometry("450x200")
root.resizable(False,False)

def cargar_imagen(ruta):
    img = Image.open(ruta)
    img = img.resize((100, 100), Image.LANCZOS)
    return ImageTk.PhotoImage(img)

img_terminal = cargar_imagen("C:/Users/Oscar Eduardo Lozada/OneDrive - KONSTRUIR/Documentos/sistemas operativos/WINDOS-TERMINAL.png")
img_navegador = cargar_imagen("C:/Users/Oscar Eduardo Lozada/OneDrive - KONSTRUIR/Documentos/sistemas operativos/unnamed.png")
img_calculadora = cargar_imagen("C:/Users/Oscar Eduardo Lozada/OneDrive - KONSTRUIR/Documentos/sistemas operativos/calculadora-casio-mx-12b-bk.jpg")

btn_terminal = tk.Button(root, image=img_terminal, command=abrir_terminal)
btn_navegador = tk.Button(root, image=img_navegador, command=abrir_navegador)
btn_calculadora = tk.Button(root, image=img_calculadora, command=abrir_calculadora)

btn_terminal.grid(row=0, column=0, padx=20, pady=20)
btn_navegador.grid(row=0, column=1, padx=20, pady=20)
btn_calculadora.grid(row=0, column=2, padx=20, pady=20)
root.mainloop()