from tkinter import *
from tkinter import ttk

def calcular_caso1(father_frame, delete_frames, back_to_last_frame, main_menu):
  delete_frames(father_frame)
  
  title_label = ttk.Label(father_frame, text="Caso 1.", font=("Consolas", 20)).grid(row=0, column=0, padx=50, pady=10,  columnspan=2)
  
  
  label1 = ttk.Label(father_frame, text="Ingresa la Renta de la anualidad: Q. ").grid(row=1, column=0, pady=10, sticky='w', padx=50)
  R = StringVar()
  ttk.Entry(father_frame, textvariable=R).grid(sticky='w', row=1, column=1, pady=10)
  
  label2 = ttk.Label(father_frame, text="Tasa de interes anual: %").grid(row=2, column=0, pady=10, sticky='w', padx=50)
  i = StringVar()
  ttk.Entry(father_frame, textvariable=i).grid(sticky='w', row=2, column=1, pady=10)
  
  label3 = ttk.Label(father_frame, text="Numero de capitalización:").grid(row=3, column=0, pady=10, sticky='w', padx=50)
  n = StringVar()
  ttk.Entry(father_frame, textvariable=n).grid(sticky='w', row=3, column=1, pady=10)
  
  response_var = StringVar()
  response_label = ttk.Label(father_frame, textvariable=response_var)
  response_label.grid(sticky='w', row=4, column=0, pady=10, columnspan=2, padx=50)
  response_label.config(foreground="green")
  
  def calcular():
    s = float(R.get()) * (((1+(float(i.get())/100))**float(n.get()) -1) /(float(i.get())/100))
    response_var.set(f"Resultado del monto de la anualidad vencida: Q. {s}")
    
  button_calculate = ttk.Button(father_frame, text="Calcular", command=lambda:calcular()).grid(row=5, column=0, padx=100, ipady=(3), pady=(0, 10), columnspan=2)
  back_button = ttk.Button(father_frame, text="Regresar", command=lambda:back_to_last_frame(father_frame, delete_frames, main_menu)).grid(row=6, column=0, padx=100, ipady=(3), pady=(0, 10), columnspan=2)
  
def calcular_caso2(father_frame, delete_frames, back_to_last_frame, main_menu):
  delete_frames(father_frame)
  
  title_label = ttk.Label(father_frame, text="Caso 2.", font=("Consolas", 20)).grid(row=0, column=0, padx=50, pady=10,  columnspan=2)
  
  label1 = ttk.Label(father_frame, text="Ingresa la Renta de la anualidad: Q. ").grid(row=1, column=0, pady=10, sticky='w', padx=50)
  R = StringVar()
  ttk.Entry(father_frame, textvariable=R).grid(sticky='w', row=1, column=1, pady=10)
  
  label2 = ttk.Label(father_frame, text="Tasa de interes nominal: %").grid(row=2, column=0, pady=10, sticky='w', padx=50)
  j = StringVar()
  ttk.Entry(father_frame, textvariable=j).grid(sticky='w', row=2, column=1, pady=10)
  
  label3 = ttk.Label(father_frame, text="Ingrese el Tiempo: ").grid(row=3, column=0, pady=10, sticky='w', padx=50)
  n = StringVar()
  ttk.Entry(father_frame, textvariable=n).grid(sticky='w', row=3, column=1, pady=10)
  
  label4 = ttk.Label(father_frame, text="Frecuencia:").grid(row=4, column=0, pady=10, sticky='w', padx=50)
  m = StringVar()
  ttk.Entry(father_frame, textvariable=m).grid(sticky='w', row=4, column=1, pady=10)
  
  response_var = StringVar()
  response_label = ttk.Label(father_frame, textvariable=response_var)
  response_label.grid(sticky='w', row=5, column=0, pady=10, columnspan=2, padx=50)
  response_label.config(foreground="green")
  
  def calcular():
    S = float(R.get()) * (((1+(float(j.get())/100/float(m.get())))**(float(n.get())*float(m.get())) -1) / (((1+(float(j.get())/100/float(m.get())))**float(m.get())) - 1))
    response_var.set(f"Resultado del monto de la anualidad vencida: Q. {S}")
  
  button_calculate = ttk.Button(father_frame, text="Calcular", command=lambda:calcular()).grid(row=6, column=0, padx=100, ipady=(3), pady=(0, 10), columnspan=2)
  back_button = ttk.Button(father_frame, text="Regresar", command=lambda:back_to_last_frame(father_frame, delete_frames, main_menu)).grid(row=7, column=0, padx=100, ipady=(3), pady=(0, 10), columnspan=2)
  
def calcular_caso3(father_frame, delete_frames, back_to_last_frame, main_menu):
  delete_frames(father_frame)
  
  title_label = ttk.Label(father_frame, text="Caso 3.", font=("Consolas", 20)).grid(row=0, column=0, padx=50, pady=10,  columnspan=2)
  
  label1 = ttk.Label(father_frame, text="Ingresa la Renta de la anualidad: Q. ").grid(row=1, column=0, pady=10, sticky='w', padx=50)
  R = StringVar()
  ttk.Entry(father_frame, textvariable=R).grid(sticky='w', row=1, column=1, pady=10)
  
  label2 = ttk.Label(father_frame, text="Tasa de interes anual: %").grid(row=2, column=0, pady=10, sticky='w', padx=50)
  i = StringVar()
  ttk.Entry(father_frame, textvariable=i).grid(sticky='w', row=2, column=1, pady=10)
  
  label3 = ttk.Label(father_frame, text="Numero de capitalización:").grid(row=3, column=0, pady=10, sticky='w', padx=50)
  n = StringVar()
  ttk.Entry(father_frame, textvariable=n).grid(sticky='w', row=3, column=1, pady=10)
  
  label4 = ttk.Label(father_frame, text="Ingrese número de pagos realizados o a realizar:").grid(row=4, column=0, pady=10, sticky='w', padx=50)
  p = StringVar()
  ttk.Entry(father_frame, textvariable=p).grid(sticky='w', row=4, column=1, pady=10)
  
  response_var = StringVar()
  response_label = ttk.Label(father_frame, textvariable=response_var)
  response_label.grid(sticky='w', row=5, column=0, pady=10, columnspan=2, padx=50)
  response_label.config(foreground="green")
  
  def calcular():
    S = float(R.get()) * (((1+(float(i.get())/100))**float(n.get()) -1) /((1+(float(i.get())/100)**(1/float(p.get())))-1))
    response_var.set(f"Resultado del monto de la anualidad vencida: Q. {S}")
  
  button_calculate = ttk.Button(father_frame, text="Calcular", command=lambda:calcular()).grid(row=6, column=0, padx=100, ipady=(3), pady=(0, 10), columnspan=2)
  back_button = ttk.Button(father_frame, text="Regresar", command=lambda:back_to_last_frame(father_frame, delete_frames, main_menu)).grid(row=7, column=0, padx=100, ipady=(3), pady=(0, 10), columnspan=2)

def calcular_caso4(father_frame, delete_frames, back_to_last_frame, main_menu):
  delete_frames(father_frame)
  
  title_label = ttk.Label(father_frame, text="Caso 4.", font=("Consolas", 20)).grid(row=0, column=0, padx=50, pady=10,  columnspan=2)
  
  label1 = ttk.Label(father_frame, text="Ingresa la Renta de la anualidad: Q. ").grid(row=1, column=0, pady=10, sticky='w', padx=50)
  R = StringVar()
  ttk.Entry(father_frame, textvariable=R).grid(sticky='w', row=1, column=1, pady=10)
  
  label2 = ttk.Label(father_frame, text="Tasa de interes nominal: %").grid(row=2, column=0, pady=10, sticky='w', padx=50)
  j = StringVar()
  ttk.Entry(father_frame, textvariable=j).grid(sticky='w', row=2, column=1, pady=10)
  
  label3 = ttk.Label(father_frame, text="Ingrese el Tiempo: ").grid(row=3, column=0, pady=10, sticky='w', padx=50)
  n = StringVar()
  ttk.Entry(father_frame, textvariable=n).grid(sticky='w', row=3, column=1, pady=10)
  
  label4 = ttk.Label(father_frame, text="Frecuencia:").grid(row=4, column=0, pady=10, sticky='w', padx=50)
  m = StringVar()
  ttk.Entry(father_frame, textvariable=m).grid(sticky='w', row=4, column=1, pady=10)
  
  label5 = ttk.Label(father_frame, text="Ingrese número de pagos realizados o a realizar:").grid(row=5, column=0, pady=10, sticky='w', padx=50)
  p = StringVar()
  ttk.Entry(father_frame, textvariable=p).grid(sticky='w', row=5, column=1, pady=10)
  
  response_var = StringVar()
  response_label = ttk.Label(father_frame, textvariable=response_var)
  response_label.grid(sticky='w', row=6, column=0, pady=10, columnspan=2, padx=50)
  response_label.config(foreground="green")
  
  def calcular():
    S = float(R.get()) * (((1+(float(j.get())/100/float(m.get())))**(float(n.get())*float(m.get())) -1) / (((1+(float(j.get())/100/float(m.get())))**(float(m.get())/float(p.get()))) - 1))  
    response_var.set(f"Resultado del monto de la anualidad vencida: Q. {S}")
    
  button_calculate = ttk.Button(father_frame, text="Calcular", command=lambda:calcular()).grid(row=7, column=0, padx=100, ipady=(3), pady=(0, 10), columnspan=2)
  back_button = ttk.Button(father_frame, text="Regresar", command=lambda:back_to_last_frame(father_frame, delete_frames, main_menu)).grid(row=8, column=0, padx=100, ipady=(3), pady=(0, 10), columnspan=2)
  
  
  
  
def anualidades_vencidas(father_frame, delete_frames, main_menu):
  delete_frames(father_frame)
  
  title_label = ttk.Label(father_frame, text="Anualidades Vencidas.", font=("Consolas", 20)).grid(row=0, column=0, padx=50, pady=10,  columnspan=2)
  
  button1 = ttk.Button(father_frame, text="Primer Caso", command=lambda:calcular_caso1(father_frame, delete_frames, anualidades_vencidas, main_menu)).grid(row=1, column=0, padx=100, ipady=(3), pady=(0, 10), columnspan=2)
  
  button2 = ttk.Button(father_frame, text="Segundo Caso", command=lambda:calcular_caso2(father_frame, delete_frames, anualidades_vencidas, main_menu)).grid(row=2, column=0, padx=100, ipady=(3), pady=(0, 10), columnspan=2)
  
  button3 = ttk.Button(father_frame, text="Tercer Caso", command=lambda:calcular_caso3(father_frame, delete_frames, anualidades_vencidas, main_menu)).grid(row=3, column=0, padx=100, ipady=(3), pady=(0, 10), columnspan=2)
  
  button4 = ttk.Button(father_frame, text="Cuarto Caso", command=lambda:calcular_caso4(father_frame, delete_frames, anualidades_vencidas, main_menu)).grid(row=4, column=0, padx=100, ipady=(3), pady=(0, 10), columnspan=2)
  
  ttk.Button(father_frame, text="Regresar al Menu Principal", command=lambda:main_menu()).grid(row=5, column=0, padx=100, ipady=(3), pady=(0, 10))
  