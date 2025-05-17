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