from tkinter import *
from tkinter import ttk

def calcular_interes(father_frame, delete_frames, back_to_last_frame, main_menu):
  delete_frames(father_frame)
  title_label = ttk.Label(father_frame, text="Calcularemos el Interes Simple.", font=("Consolas", 20)).grid(row=0, column=0, padx=50, pady=10,  columnspan=2)  
  Label1 = ttk.Label(father_frame, text="Ingresa el Capital: Q. ").grid(row=1, column=0, pady=10, sticky='w', padx=50)
  P = StringVar()
  ttk.Entry(father_frame, textvariable=P).grid(sticky='w', row=1, column=1, pady=10)
  label2 = ttk.Label(father_frame, text="Ingresa el porcentaje del interes anual: % ").grid(row=2, column=0, pady=10, sticky='w', padx=50)
  r = StringVar()
  ttk.Entry(father_frame, textvariable=r).grid(sticky='w', row=2, column=1, pady=10)
  label3 = ttk.Label(father_frame, text="Ingresa el periodo de tiempo en años: ").grid(row=3, column=0, pady=10, sticky='w', padx=50)
  t = StringVar()
  ttk.Entry(father_frame, textvariable=t).grid(sticky='w', row=3, column=1, pady=10)
 
  
  label_var = StringVar()
  text_response = ttk.Label(father_frame, textvariable=label_var)
  text_response.grid(sticky='w', row=4, column=0, pady=10, columnspan=2, padx=50)
  text_response.config(foreground="green")
  
  def calcular():
    I = float(P.get()) * (float(r.get()) / 100) * float(t.get())
    label_var.set(f"El Interes es de: Q. {I}")
    
  button_calculate = ttk.Button(father_frame, text="Calcular", command=lambda:calcular()).grid(row=5, column=0, padx=100, ipady=(3), pady=(0, 10), columnspan=2)
  
  back_button = ttk.Button(father_frame, text="Regresar", command=lambda:back_to_last_frame(father_frame, delete_frames, main_menu)).grid(row=6, column=0, padx=100, ipady=(3), pady=(0, 10), columnspan=2)

def calcular_capital(father_frame, delete_frames, back_to_last_frame, main_menu):
  delete_frames(father_frame)
  title_label = ttk.Label(father_frame, text="Calcularemos el Capital.", font=("Consolas", 20)).grid(row=0, column=0, padx=50, pady=10,  columnspan=2)
  
  label1 = ttk.Label(father_frame, text="Ingrese el interés ganado o adeudado: Q. ").grid(row=1, column=0, pady=10, sticky='w', padx=50)
  I = StringVar()
  ttk.Entry(father_frame, textvariable=I).grid(sticky='w', row=1, column=1, pady=10)
  
  label2 = ttk.Label(father_frame, text="Ingresa el porcentaje del interes anual: % ").grid(row=2, column=0, pady=10, sticky='w', padx=50)
  r = StringVar()
  ttk.Entry(father_frame, textvariable=r).grid(sticky='w', row=2, column=1, pady=10)
  
  label3 = ttk.Label(father_frame, text="Ingresa el periodo de tiempo en años: ").grid(row=3, column=0, pady=10, sticky='w', padx=50)
  t = StringVar()
  ttk.Entry(father_frame, textvariable=t).grid(sticky='w', row=3, column=1, pady=10)
  
  
  response_var = StringVar()
  response_label = ttk.Label(father_frame, textvariable=response_var)
  response_label.grid(sticky='w', row=4, column=0, pady=10, columnspan=2, padx=50)
  response_label.config(foreground="green")
  
  def calcular():
    P = float(I.get()) / ((float(r.get())/100) * float(t.get()))  
    response_var.set(f"El Capital es de: Q. {P}")
    
  button_calculate = ttk.Button(father_frame, text="Calcular", command=lambda:calcular()).grid(row=5, column=0, padx=100, ipady=(3), pady=(0, 10), columnspan=2)
  back_button = ttk.Button(father_frame, text="Regresar", command=lambda:back_to_last_frame(father_frame, delete_frames, main_menu)).grid(row=6, column=0, padx=100, ipady=(3), pady=(0, 10), columnspan=2)

def calcular_tasainteres(father_frame, delete_frames, back_to_last_frame, main_menu):
  delete_frames(father_frame)
  title_label = ttk.Label(father_frame, text="Calcularemos la Tasa de Interés Anual.", font=("Consolas", 20)).grid(row=0, column=0, padx=50, pady=10,  columnspan=2)
  
  label1 = ttk.Label(father_frame, text="Ingresa el Capital: Q. ").grid(row=1, column=0, pady=10, sticky='w', padx=50)
  P = StringVar()
  ttk.Entry(father_frame, textvariable=P).grid(sticky='w', row=1, column=1, pady=10)
  
  label2 = ttk.Label(father_frame, text="Ingrese el interés ganado o adeudado: Q.").grid(row=2, column=0, pady=10, sticky='w', padx=50)
  I = StringVar()
  ttk.Entry(father_frame, textvariable=I).grid(sticky='w', row=2, column=1, pady=10)
  
  label3 = ttk.Label(father_frame, text="Ingresa el periodo de tiempo en años: ").grid(row=3, column=0, pady=10, sticky='w', padx=50)
  t = StringVar()
  ttk.Entry(father_frame, textvariable=t).grid(sticky='w', row=3, column=1, pady=10)
  
  response_var = StringVar()
  response_label = ttk.Label(father_frame, textvariable=response_var)
  response_label.grid(sticky='w', row=4, column=0, pady=10, columnspan=2, padx=50)
  response_label.config(foreground="green")
  
  def calcular():
    r = float(I.get()) / (float(P.get()) * float(t.get())) * 100
    response_var.set(f"La Tasa de Interés Anual es de: % {r}")
  
  button_calculate = ttk.Button(father_frame, text="Calcular", command=lambda:calcular()).grid(row=5, column=0, padx=100, ipady=(3), pady=(0, 10), columnspan=2)
  back_button = ttk.Button(father_frame, text="Regresar", command=lambda:back_to_last_frame(father_frame, delete_frames, main_menu)).grid(row=6, column=0, padx=100, ipady=(3), pady=(0, 10), columnspan=2)
  
  
  
def calcular_tiempo(father_frame, delete_frames, back_to_last_frame, main_menu):
  delete_frames(father_frame)
  
  title_label = ttk.Label(father_frame, text="Calcularemos el Tiempo.", font=("Consolas", 20)).grid(row=0, column=0, padx=50, pady=10,  columnspan=2)
  
  label1 = ttk.Label(father_frame, text="Ingresa el Capital: Q. ").grid(row=1, column=0, pady=10, sticky='w', padx=50)
  P = StringVar()
  ttk.Entry(father_frame, textvariable=P).grid(sticky='w', row=1, column=1, pady=10)
  r = StringVar()
  label2 = ttk.Label(father_frame, text="Ingresa el porcentaje del interes anual: % ").grid(row=2, column=0, pady=10, sticky='w', padx=50)
  ttk.Entry(father_frame, textvariable=r).grid(sticky='w', row=2, column=1, pady=10)
  I = StringVar()
  label3 = ttk.Label(father_frame, text="Ingrese el interés ganado o adeudado: Q. ").grid(row=3, column=0, pady=10, sticky='w', padx=50)
  ttk.Entry(father_frame, textvariable=I).grid(sticky='w', row=3, column=1, pady=10)
  
  
  response_var = StringVar()
  response_label = ttk.Label(father_frame, textvariable=response_var)
  response_label.grid(sticky='w', row=4, column=0, pady=10, columnspan=2, padx=50)
  response_label.config(foreground="green")
  
  def calcular():
    t = float(I.get()) / (float(P.get()) * (float(r.get()) / 100))
    response_var.set(f"El Tiempo transcurrido o a transcurrir es de: {t} años")
    
  button_calculate = ttk.Button(father_frame, text="Calcular", command=lambda:calcular()).grid(row=5, column=0, padx=100, ipady=(3), pady=(0, 10), columnspan=2)
  back_button = ttk.Button(father_frame, text="Regresar", command=lambda:back_to_last_frame(father_frame, delete_frames, main_menu)).grid(row=6, column=0, padx=100, ipady=(3), pady=(0, 10), columnspan=2)

def interes_simple(father_frame, delete_frames, main_menu):  
  delete_frames(father_frame)
  
  title_label = ttk.Label(father_frame, text="Interés Simple", font=("Consolas", 20)).grid(row=0, column=0, padx=100, pady=10)
  button1 = ttk.Button(father_frame, text="Calcular Interes Simple", command=lambda:calcular_interes(father_frame, delete_frames, interes_simple, main_menu)).grid(row=1, column=0, padx=100, ipady=(3), pady=(0, 10))
  button2 = ttk.Button(father_frame, text="Calcular Capital", command=lambda:calcular_capital(father_frame, delete_frames, interes_simple, main_menu)).grid(row=2, column=0, padx=100, ipady=(3), pady=(0, 10))
  button3 = ttk.Button(father_frame, text="Calcular Tasa de Interés", command=lambda:calcular_tasainteres(father_frame, delete_frames, interes_simple, main_menu)).grid(row=3, column=0, padx=100, ipady=(3), pady=(0, 10))
  button4 = ttk.Button(father_frame, text="Calcular Tiempo", command=lambda:calcular_tiempo(father_frame, delete_frames, interes_simple, main_menu)).grid(row=4, column=0, padx=100, ipady=(3), pady=(0, 10))
  button5 = ttk.Button(father_frame, text="Regresar al Menu Principal", command=lambda:main_menu()).grid(row=5, column=0, padx=100, ipady=(3), pady=(0, 10))
