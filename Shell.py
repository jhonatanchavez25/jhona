import tkinter as tk #libreria para interfaz grafica
from PIL import Image, ImageTk #visualizacion de imagenes
import subprocess#ejecuta programas del sistema operativo
import webbrowser#ejecuta el navegador

# --- funciones para la ejecucion de los programas ---

def abrir_terminal():# Abre la terminal de Windows (CMD)
    subprocess.Popen("start cmd", shell=True)

def abrir_navegador():# Abre el navegador predeterminado en la URL especificada
    webbrowser.open("https://www.google.com")

def abrir_calculadora():
    subprocess.Popen("calc")# Abre la calculadora de Windows

    # --- codificacion de ingterfaz grafica ---

root = tk.Tk()#ventana principal
root.title("shell Grafico(Sistemas operativos)")# titulo
root.geometry("450x200")# tamaño
root.resizable(False,False)# Evita que la ventana se pueda redimensionar

# --- codificacion para cargar y mostrar las imagenes ---

def cargar_imagen(ruta):
    img = Image.open(ruta) #abre la imagen desde la ubicacion
    img = img.resize((100, 100), Image.LANCZOS) # ajusta el tamaño de la imagen
    return ImageTk.PhotoImage(img) # Devuelve la imagen lista para Tkinte

# --- imagene para los botones---

img_terminal = cargar_imagen("C:/Users/Oscar Eduardo Lozada/OneDrive - KONSTRUIR/Documentos/sistemas operativos/WINDOS-TERMINAL.png")
img_navegador = cargar_imagen("C:/Users/Oscar Eduardo Lozada/OneDrive - KONSTRUIR/Documentos/sistemas operativos/unnamed.png")
img_calculadora = cargar_imagen("C:/Users/Oscar Eduardo Lozada/OneDrive - KONSTRUIR/Documentos/sistemas operativos/calculadora-casio-mx-12b-bk.jpg")

# --- Crear botones con las imágenes y enlazarlos a sus funciones ---

btn_terminal = tk.Button(root, image=img_terminal, command=abrir_terminal)
btn_navegador = tk.Button(root, image=img_navegador, command=abrir_navegador)
btn_calculadora = tk.Button(root, image=img_calculadora, command=abrir_calculadora)

# --- Ubicar los botones en la ventana usando grid ---

btn_terminal.grid(row=0, column=0, padx=20, pady=20)
btn_navegador.grid(row=0, column=1, padx=20, pady=20)
btn_calculadora.grid(row=0, column=2, padx=20, pady=20)

# --- ejecuta la interfaz grafica ----
root.mainloop()