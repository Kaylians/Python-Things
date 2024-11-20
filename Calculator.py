import tkinter as tk
import tkinter.simpledialog
import math 
#libreria usada para las funciones matematicas: https://docs.python.org/3/library/math.html

#funcion para actualizar la informacion en la pantalla
def button_click(char):
	current = entry.get()
	entry.delete(0,tk.END)
	entry.insert(tk.END, current + char)

#funcion para calcular el resultado
def calculate():
	try:
		fix_entry = entry.get().replace("^","**") #reemplazar "^" esta reservado para "XOR", por lo que se reemplaza por "**" que es usado para exponenciales  
		result = eval(fix_entry)
		operation = entry.get() + " = " +str(result)
		record.append(operation) #agregar operacion al historial
		entry.delete(0,tk.END)
		entry.insert(tk.END, str(result))
	except Exception as e:
		entry.delete(0,tk.END)
		entry.insert(tk.END, "ERROR")

def scientific_function(func):
	try:
		current = entry.get()
		if not current:
			raise ValueError("no input")
		entry.delete(0,tk.END)
		
		if func == "root": #raiz 
			root_value = tk.simpledialog.askinteger("X:","Y:")
			if root_value is None or root_value <= 0:
				raise ValueError("Error, invalid value")
			result = float(current) ** (1/root_value)	
		elif func == "log": #logaritmo
			result = math.log10(float(current))
		elif func == "ln": 
			result = math.log(float(current))
		elif func == "sin":
			result = math.sin(math.radians(float(current)))
		elif func == "cos":
			result = math.cos(math.radians(float(current)))
		elif func == "tan":
			result = math.tan(math.radians(float(current)))
		elif func == "sec":
			result = 1/math.cos(math.radians(float(current)))
		elif func == "csc":
			result = 1/math.sin(math.radians(float(current)))
		elif func == "cot":
			result = 1/math.tan(math.radians(float(current)))
		elif func == "sinh":
			result = math.sinh(float(current))
		elif func == "cosh":
		    	result = math.cosh(float(current))
		elif func == "tanh":
		    	result = math.tanh(float(current))
		elif func == "π":
		    	result = math.pi
		elif func == "e":
		    	result = math.e
		elif func == "factorial":
			result = math.factorial(int(current))
		else:
			raise ValueError("Invalid function")
		entry.insert(tk.END, str(result))
	except Exception as e:
		entry.delete(0, tk.END)
		entry.insert(tk.END, "error")

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
	('sin','cos','tan','sec','csc','cot'),
	('sinh','cosh','tanh','π','n!','e'),
	('log','ln','x√y','^','(',')'),
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
		if char in ['sin','cos','tan','root','log','ln', 'sec', 'csc', 'cot', 'sinh', 'cosh','tanh','π','e']:	
			button = tk.Button(frame, text = char, font = ("Arial", 14), command = lambda f = char: scientific_function(f), width = 2, height = 2)
		elif char == '=':
			button = tk.Button(frame, text = char, font = ("Arial", 14), command = calculate, width = 2, height = 2)
		elif char == '^':
			button = tk.Button(frame, text = char, font = ("Arial", 14), command = lambda: button_click("^"), width = 2, height = 2)
		elif char == 'n!':
			button = tk.Button(frame, text = char, font = ("Arial", 14), command = lambda f = "factorial": scientific_function(f))
		elif char == 'x√y':
			button = tk.Button(frame, text = char, font = ("Arial", 14), command = lambda f = "root": scientific_function(f))
		else:
			button = tk.Button(frame, text = char, font = ("Arial", 18), command = lambda c=char: button_click(c), width = 2, height = 2)
		button.pack(side="left", fill = "both", expand = True)	

#button para limpiar la pantalla
clear_button = tk.Button(root, text="Clear", font= ("Arial",14), command = clear)
clear_button.pack(side =  tk.LEFT, fill = "x", expand = True)

#button para mostrar historial
record_button = tk.Button(root, text="Record", font= ("Arial",14), command = show_record)
record_button.pack(side =  tk.LEFT, fill = "x", expand = True)

root.mainloop()
