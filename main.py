import tkinter as tk
from tkinter import ttk

from serial.tools import list_ports
import serial

import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

ports = list_ports.comports()
serial_object = serial.Serial()
all_ports_str = ['Port not selected']
element_to_combox = ''
# Adding COM-ports names to the list
for element in ports:
    element_str = str(element)

    position = 0
    while position <= len(element_str) + 1:
        if element_str[position] == ' ':
            print(element_to_combox)
            break
        element_to_combox = element_to_combox + element_str[position]
        position = position + 1

    all_ports_str.append(element_to_combox)


def choose_pt():
    print("You've chosen" + str(Radio_pt.get()))


window = tk.Tk()
height = 750
width = 850
d_x = 500
d_y = 20
Radio_pt = tk.IntVar()  # variable for the radiobutton choosing
setvalue1 = tk.StringVar()  # actual value for the potentiometer 1
scale1 = tk.IntVar()

pt1_active = tk.IntVar()
pt1_active.set(0)
ValuesForPotentiometer = {'Choose value': 'Choose value',
                          '10 000': 10000,
                          '20 000': 20000,
                          '30 000': 30000,
                          '40 000': 40000,
                          '50 000': 50000}



def unlock_widgets1():
    if int(pt1_active.get()):
        box1.config(state="readonly")
        label1.config(state="normal")
        entry1.config(state="normal")
        scale1_widg.config(state='normal')
        send_btn1.config(state="normal")
        actual_val_1.config(state="normal")
        val_1.config(state="normal")

    else:
        box1.config(state="disabled")
        label1.config(state="disabled")
        entry1.config(state="disabled")
        scale1_widg.config(state='disabled')
        send_btn1.config(state="disabled")
        actual_val_1.config(state="disabled")
        val_1.config(state="disabled")


def set_values(event):
    if box1.get() == 'Choose value':
        newval = '0'
    else:
        newval = ValuesForPotentiometer[box1.get()]

    setvalue1.set(newval)

    entry1.delete(0, tk.END)
    entry1.insert(0, newval)

    scale1.set(int(newval) / max(list(ValuesForPotentiometer.values())[1:]) * 100)

    val_1['text'] = str(newval) + '[Ω]'


window.title('Configuration of the SPI Potentiometer')
window.geometry(f"{height}x{width}+{d_x}+{d_y}")
window.minsize(width, height)
window.maxsize(width, height)
window.resizable(True, True)

photo = tk.PhotoImage(file='setting.png')
window.iconphoto(True, photo)

tk.Label(window, text="Port").grid(row=0, column=0, pady=10)

ports_box = ttk.Combobox(window, values=all_ports_str)
ports_box.current(0)
ports_box.grid(row=0, column=1)

################## FOR POTENTIOMETER 1
tk.Label(window, text="Potentiometer №1").grid(row=1, column=0)

tk.Checkbutton(window, text='Activate',
               variable=pt1_active,
               offvalue=0,
               onvalue=1,
               command=unlock_widgets1).grid(row=2, column=0)

label1 = tk.Label(window, text="Value [Ω]")
label1.grid(row=2, column=1, padx=10)
label1.config(state="disabled")

box1 = ttk.Combobox(window, state="readonly",
                    values=list(ValuesForPotentiometer.keys()))
box1.configure(state="disabled")
box1.bind("<<ComboboxSelected>>", set_values)
box1.current(0)
box1.grid(row=2, column=2)

entry1 = ttk.Entry()
entry1.grid(row=2, column=3, padx=10)
entry1.config(state="disabled")

scale1_widg = tk.Scale(window, orient=tk.HORIZONTAL, variable=scale1)
scale1_widg.grid(row=2, column=4, ipady=10)
scale1_widg.config(state='disabled')

send_btn1 = tk.Button(window, text="Send")
send_btn1.grid(row=2, column=5, padx=10)
send_btn1.config(state="disabled")

actual_val_1 = tk.Label(window, text="Actual Value: ")
actual_val_1.grid(row=2, column=6, padx=10)
actual_val_1.config(state="disabled")

val_1 = tk.Label(window, text=0)
val_1.grid(row=2, column=7)
val_1.config(state="disabled")

# FOR POTENTIOMETER 2
tk.Label(window, text="Potentiometer №2").grid(row=3, column=0)

pt2_active = tk.IntVar()
pt2_active.set(0)
tk.Checkbutton(window, text='Activate',
               variable=pt2_active,
               offvalue=0,
               onvalue=1).grid(row=4, column=0)

tk.Label(window, text="Value [Ω]").grid(row=4, column=1, padx=10)

box2 = ttk.Combobox(window, values=list(ValuesForPotentiometer.keys()))
box2.current(0)
box2.grid(row=4, column=2)

ttk.Entry().grid(row=4, column=3, padx=10)
tk.Scale(window, orient=tk.HORIZONTAL).grid(row=4, column=4, ipady=10)
tk.Button(window, text="Send").grid(row=4, column=5, padx=10)

abc = '0'
tk.Label(window, text="Actual Value: ").grid(row=4, column=6, padx=10)
val_2 = tk.Label(window, text=abc)
val_2.grid(row=4, column=7)

# figure = plt.Figure(figsize=(6,5), dpi=100)
# ax = figure.add_subplot(111)
# chart_type = FigureCanvasTkAgg(figure, window)
# chart_type.get_tk_widget().grid(row=8, column=0, columnspan=2, padx=10, pady=10)


window.mainloop()
