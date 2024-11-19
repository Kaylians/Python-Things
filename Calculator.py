import tkinter as tk

#funcion para actualizar la informacion en la pantalla
def button_click(char):
	current = entry.get()
	entry.delete(0,tk.END)
	entry.insert(tk.END, current +char)

#funcion para calcular el resultado
def calculate():
	try:
		result = eval(entry.get())
		operation = entry.get() + " = " +str(result)
		record.append(operation) #agregar operacion al historial
		entry.delete(0,tk.END)
		entry.insert(tk.END, str(result))
	except Exception as e:
		entry.delete(0,tk.END)
		entry.insert(tk.END, "ERROR")
		
def show_record():
	global record_frame
	if record_frame is not None:
		record_frame.destroy()
		record_frame = None
	else:
		record_frame = tk.Toplevel(root)
		record_frame.transient(root) #para ventana secundaria
		record_frame.title("Operation Record")
		record_frame.geometry(f"{window_width}x{window_height-200}+{fix_screen_width}+{fix_screen_height}")
		record_text = tk.Text(record_frame, width = 40, height = 10)
		record_text.pack(fill="both", expand = True)
		for operation in record:
			record_text.insert(tk.END, operation + '\n')

def clear():
	entry.delete(0,tk.END)
	record.clear()
		
#Ventana principal
root = tk.Tk()
root.title("Calculadora simple en Python")

#definir tamaño de la pantalla
window_width = 400
window_height = 600

screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

#ajuste para centrar la ventana en la pantalla
fix_screen_width =  (screen_width // 2) - (window_width // 2)
fix_screen_height =  (screen_height // 2) - (window_height // 2)

root.geometry(f"{window_width}x{window_height}+{fix_screen_width}+{fix_screen_height}")


#ventana para el despliegue de informacion
entry = tk.Entry(root, font=("Arial",20), bd = 10, relief = "sunken", justify = "right")
entry.pack(fill =  "both", expand = True)

#definicion de los botones
buttons = [
	('7','8','9','/'),
	('4','5','6','*'),
	('1','2','3','-'),
	('0','.','=','+'),
]


#lista para almacenamiento de historial
record = []
record_frame = None

#creacion de botones en base a la definicion
for row in buttons:
	frame = tk.Frame(root)
	frame.pack(fill="both", expand = True)
	for char in row:
		button = tk.Button(frame, text = char, font = ("Arial", 18), command = lambda c=char: button_click(c) if c != '=' else calculate())
		button.pack(side="left", fill = "both", expand = True)	

#button para limpiar la pantalla
clear_button = tk.Button(root, text="Clear", font= ("Arial",18), command = clear)
clear_button.pack(side =  tk.LEFT, fill = "x", expand = True)

#button para mostrar historial
record_button = tk.Button(root, text="Record", font= ("Arial",14), command = show_record)
record_button.pack(side =  tk.LEFT, fill = "x", expand = True)

root.mainloop()
