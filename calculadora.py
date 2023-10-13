from functions.interes_simple import interes_simple
from functions.descuento_simple import descuento_simple
from tkinter import * 
from tkinter import ttk

root = Tk()
root.title("Calculadora")

my_frame = ttk.Frame(root)

def deleteFrames(father_frame): 
  for widget in father_frame.winfo_children():
    widget.destroy()

def main_menu():
  deleteFrames(my_frame)
  my_frame.grid()

  ttk.my_label = Label(my_frame, text="Menu Principal", font=("Consolas", 20)).grid(row=0, column=0, padx=100, pady=10)

  ttk.my_button = Button(my_frame, text="Interés Simple", command=lambda:interes_simple(my_frame, deleteFrames, main_menu)).grid(row=1, column=0, padx=100, ipady=(3), pady=(0, 10))   
  
  ttk.second_button = Button(my_frame, text="Descuento Simple", command=lambda:descuento_simple(my_frame, deleteFrames, main_menu)).grid(row=2, column=0, padx=100, ipady=(3), pady=(0, 10))

main_menu()

root.mainloop()