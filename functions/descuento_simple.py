from tkinter import *
from tkinter import ttk

def calcular_descuento_simple(father_frame, delete_frames, back_to_last_frame, main_menu):
  delete_frames(father_frame)
  title_label = ttk.Label(father_frame, text="Calcularemos el Descuento Simple.", font=("Consolas", 20)).grid(row=0, column=0, padx=50, pady=10,  columnspan=2)
  
  label1 = ttk.Label(father_frame, text="Ingresa el Valor de Vencimiento: Q. ").grid(row=1, column=0, pady=10, sticky='w', padx=50)
  s = StringVar()
  ttk.Entry(father_frame, textvariable=s).grid(sticky='w', row=1, column=1, pady=10)
  label2 = ttk.Label(father_frame, text="Ingresa la Tasa de Descuento anual: % ").grid(row=2, column=0, pady=10, sticky='w', padx=50)
  d = StringVar()
  ttk.Entry(father_frame, textvariable=d).grid(sticky='w', row=2, column=1, pady=10)
  label3 = ttk.Label(father_frame, text="Ingresa el Tiempo de Descuento en años: ").grid(row=3, column=0, pady=10, sticky='w', padx=50)
  t = StringVar()
  ttk.Entry(father_frame, textvariable=t).grid(sticky='w', row=3, column=1, pady=10)
  
  response_var = StringVar()
  response_label = ttk.Label(father_frame, textvariable=response_var)
  response_label.grid(sticky='w', row=4, column=0, pady=10, columnspan=2, padx=50)
  response_label.config(foreground="green")
  
  def calcular():
    Db = int(s.get()) * (int(d.get()) / 100) * int(t.get())
    response_var.set(f"El Descuento Simple es de: Q. {Db}")
  
  button_calculate = ttk.Button(father_frame, text="Calcular", command=lambda:calcular()).grid(row=5, column=0, padx=100, ipady=(3), pady=(0, 10), columnspan=2)
  back_button = ttk.Button(father_frame, text="Regresar", command=lambda:back_to_last_frame(father_frame, delete_frames, main_menu)).grid(row=6, column=0, padx=100, ipady=(3), pady=(0, 10), columnspan=2)

def calcular_valor_vencimiento(father_frame, delete_frames, back_to_last_frame, main_menu):
  delete_frames(father_frame)
  
  title_label = ttk.Label(father_frame, text="Calcularemos el Valor de Vencimiento.", font=("Consolas", 20)).grid(row=0, column=0, padx=50, pady=10,  columnspan=2)
  
  Label1 = ttk.Label(father_frame, text="Ingresa el valor del Descuento Bancario: Q. ").grid(row=1, column=0, pady=10, sticky='w', padx=50)
  Db = StringVar()
  ttk.Entry(father_frame, textvariable=Db).grid(sticky='w', row=1, column=1, pady=10)
  Label2 = ttk.Label(father_frame, text="Ingresa la Tasa de Descuento anual: % ").grid(row=2, column=0, pady=10, sticky='w', padx=50)
  d = StringVar()
  ttk.Entry(father_frame, textvariable=d).grid(sticky='w', row=2, column=1, pady=10)
  Label3 = ttk.Label(father_frame, text="Ingresa el Tiempo de Descuento en años: ").grid(row=3, column=0, pady=10, sticky='w', padx=50)
  t = StringVar()
  ttk.Entry(father_frame, textvariable=t).grid(sticky='w', row=3, column=1, pady=10)
  
  response_var = StringVar()
  response_label = ttk.Label(father_frame, textvariable=response_var)
  response_label.grid(sticky='w', row=4, column=0, pady=10, columnspan=2, padx=50)
  response_label.config(foreground="green")
  
  def calcular():
    s = int(Db.get()) / ((int(d.get()) / 100) * int(t.get()))
    response_var.set(f"El Valor de Vencimiento es de: Q. {s}")
    
  button_calculate = ttk.Button(father_frame, text="Calcular", command=lambda:calcular()).grid(row=5, column=0, padx=100, ipady=(3), pady=(0, 10), columnspan=2)
  back_button = ttk.Button(father_frame, text="Regresar", command=lambda:back_to_last_frame(father_frame, delete_frames, main_menu)).grid(row=6, column=0, padx=100, ipady=(3), pady=(0, 10), columnspan=2)

def calcular_tasa_descuento(father_frame, delete_frames, back_to_last_frame, main_menu):
  delete_frames(father_frame)
  
  title_label = ttk.Label(father_frame, text="Calcularemos la Tasa de Descuento.", font=("Consolas", 20)).grid(row=0, column=0, padx=50, pady=10,  columnspan=2)
  
  label1 = ttk.Label(father_frame, text="Ingresa el Valor de Vencimiento: Q. ").grid(row=1, column=0, pady=10, sticky='w', padx=50)
  s = StringVar()
  ttk.Entry(father_frame, textvariable=s).grid(sticky='w', row=1, column=1, pady=10)
  
  label2 = ttk.Label(father_frame, text="Ingresa el valor del Descuento Bancario: Q. ").grid(row=2, column=0, pady=10, sticky='w', padx=50)
  Db = StringVar()
  ttk.Entry(father_frame, textvariable=Db).grid(sticky='w', row=2, column=1, pady=10)
  
  label3 = ttk.Label(father_frame, text="Ingresa el Tiempo de Descuento en años: ").grid(row=3, column=0, pady=10, sticky='w', padx=50)
  t = StringVar()
  ttk.Entry(father_frame, textvariable=t).grid(sticky='w', row=3, column=1, pady=10)
  
  response_var = StringVar()
  response_label = ttk.Label(father_frame, textvariable=response_var)
  response_label.grid(sticky='w', row=4, column=0, pady=10, columnspan=2, padx=50)
  response_label.config(foreground="green")
  
  
  def calcular():
    d = (int(Db.get()) / int(s.get())) * 100 / int(t.get())
    response_var.set(f"La Tasa de Descuento es de: {d}%")
  
  button_calculate = ttk.Button(father_frame, text="Calcular", command=lambda:calcular()).grid(row=5, column=0, padx=100, ipady=(3), pady=(0, 10), columnspan=2)
  back_button = ttk.Button(father_frame, text="Regresar", command=lambda:back_to_last_frame(father_frame, delete_frames, main_menu)).grid(row=6, column=0, padx=100, ipady=(3), pady=(0, 10), columnspan=2)

def calcular_tiempo_descuento(father_frame, delete_frames, back_to_last_frame, main_menu):
  delete_frames(father_frame)
  
  title_label = ttk.Label(father_frame, text="Calcularemos el Tiempo de Descuento.", font=("Consolas", 20)).grid(row=0, column=0, padx=50, pady=10,  columnspan=2)
  
  label1 = ttk.Label(father_frame, text="Ingresa el Valor de Vencimiento: Q. ").grid(row=1, column=0, pady=10, sticky='w', padx=50)
  s = StringVar()
  ttk.Entry(father_frame, textvariable=s).grid(sticky='w', row=1, column=1, pady=10)
  
  label2 = ttk.Label(father_frame, text="Ingresa el valor del Descuento Bancario: Q. ").grid(row=2, column=0, pady=10, sticky='w', padx=50)
  Db = StringVar()
  ttk.Entry(father_frame, textvariable=Db).grid(sticky='w', row=2, column=1, pady=10)
  
  label3 = ttk.Label(father_frame, text="Ingresa la Tasa de Descuento anual: % ").grid(row=3, column=0, pady=10, sticky='w', padx=50)
  d = StringVar()
  ttk.Entry(father_frame, textvariable=d).grid(sticky='w', row=3, column=1, pady=10)
  
  response_var = StringVar()
  response_label = ttk.Label(father_frame, textvariable=response_var)
  response_label.grid(sticky='w', row=4, column=0, pady=10, columnspan=2, padx=50)
  response_label.config(foreground="green")
  
  def calcular():
    t = int(Db.get()) / ((int(s.get()) * (int(d.get()) / 100)))
    response_var.set(f"El Tiempo de Descuento es de: {t} años")
  
  button_calculate = ttk.Button(father_frame, text="Calcular", command=lambda:calcular()).grid(row=5, column=0, padx=100, ipady=(3), pady=(0, 10), columnspan=2)
  back_button = ttk.Button(father_frame, text="Regresar", command=lambda:back_to_last_frame(father_frame, delete_frames, main_menu)).grid(row=6, column=0, padx=100, ipady=(3), pady=(0, 10), columnspan=2)
  

def descuento_simple(father_frame, delete_frames, main_menu):
  delete_frames(father_frame)
  
  title_label = ttk.Label(father_frame, text="Descuento Bancario.", font=("Consolas", 20)).grid(row=0, column=0, padx=100, pady=10)
  
  button1 = ttk.Button(father_frame, text="Calcular Descuento Simple", command=lambda:calcular_descuento_simple(father_frame, delete_frames, descuento_simple, main_menu)).grid(row=1, column=0, padx=100, ipady=(3), pady=(0, 10))
  
  button2 = ttk.Button(father_frame, text="Calcular Valor de vencimiento", command=lambda:calcular_valor_vencimiento(father_frame, delete_frames, descuento_simple, main_menu)).grid(row=2, column=0, padx=100, ipady=(3), pady=(0, 10))
  
  button3 = ttk.Button(father_frame, text="Calcular Tasa de descuento", command=lambda:calcular_tasa_descuento(father_frame, delete_frames, descuento_simple, main_menu)).grid(row=3, column=0, padx=100, ipady=(3), pady=(0, 10))
  
  button4 = ttk.Button(father_frame, text="Calcular Tiempo de descuento", command=lambda:calcular_tiempo_descuento(father_frame, delete_frames, descuento_simple, main_menu)).grid(row=4, column=0, padx=100, ipady=(3), pady=(0, 10))