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