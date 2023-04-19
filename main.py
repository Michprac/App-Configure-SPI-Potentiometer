import tkinter as tk
from tkinter import ttk

import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

import serial
from serial.tools import list_ports


# TESTING USB COMMUNICATION

# serial_object = serial.Serial()
#
# ports = list_ports.comports()
# list_of_ports = []
#
# for single_port in ports:
#     list_of_ports.append(str(single_port))
#     print(str(single_port))

# serial_object.baudrate = 9600
# serial_object.port = "COM5"
# serial_object.open()
#
# serial_object.write('gf')
#
# while True:
#     if serial_object.in_waiting:
#         info = serial_object.readline()
#         print(info.decode('utf'))


def choose_pt():
    print("You've chosen" + str(Radio_pt.get()))


window = tk.Tk()
height = 750
width = 850
d_x = 500
d_y = 20
Radio_pt = tk.IntVar()  # variable for the radiobutton choosing

window.title('Configuration of the SPI Potentiometer')
window.geometry(f"{height}x{width}+{d_x}+{d_y}")
window.minsize(width, height)
window.maxsize(width, height)
window.resizable(True, True)

photo = tk.PhotoImage(file='setting.png')
window.iconphoto(True, photo)

tk.Label(window, text="Port").grid(row=0, column=0, pady=10)
ttk.Combobox().grid(row=0, column=1)

# FOR POTENTIOMETER 1
tk.Label(window, text="Potentiometer №1").grid(row=1, column=0)
tk.Checkbutton(window, text='Activate').grid(row=2, column=0)
tk.Label(window, text="Value [Ω]").grid(row=2, column=1, padx=10)
ttk.Combobox().grid(row=2, column=2)
ttk.Entry().grid(row=2, column=3, padx=10)
tk.Scale(window, orient=tk.HORIZONTAL).grid(row=2, column=4, ipady=10)
tk.Button(window, text="Send").grid(row=2, column=5, padx= 10)


abc = '0'
tk.Label(window, text="Actual Value: ").grid(row=2, column=6, padx=10)
val_1 = tk.Label(window, text=abc)
val_1.grid(row=2, column=7)

# FOR POTENTIOMETER 2
tk.Label(window, text="Potentiometer №2").grid(row=3, column=0)
tk.Checkbutton(window, text='Activate').grid(row=4, column=0)
tk.Label(window, text="Value [Ω]").grid(row=4, column=1, padx=10)
ttk.Combobox().grid(row=4, column=2)
ttk.Entry().grid(row=4, column=3, padx=10)
tk.Scale(window, orient=tk.HORIZONTAL).grid(row=4, column=4, ipady=10)
tk.Button(window, text="Send").grid(row=4, column=5, padx= 10)

abc = '0'
tk.Label(window, text="Actual Value: ").grid(row=4, column=6, padx=10)
val_1 = tk.Label(window, text=abc)
val_1.grid(row=4, column=7)


#
# First_pt_1 = tk.Radiobutton(window, text='Activate', variable=Radio_pt, value=1, command=choose_pt)
# First_pt_1.grid(row=0, column=1)
#
# Label_entry_send = tk.Label(window, text="Value of potentiometer [Ω]", padx=10, pady=10)
# Label_entry_send.grid(row=1, column=0)
#
# Entry_entry_send = ttk.Combobox(window)
# Entry_entry_send.grid(row=1, column=1)
#
# Button_entry_send = tk.Button(window, text="Send")
# Button_entry_send.grid(row=2, column=0, columnspan=2, stick='NWSE', padx=10)
#
# Label_number_of_pt = tk.Label(window, text="Potentiometer №2", pady=10)
# Label_number_of_pt.grid(row=3, column=0)
#
# First_pt_1 = tk.Radiobutton(window, text='Activate', variable=Radio_pt, value=2, command=choose_pt)
# First_pt_1.grid(row=3, column=1)
#
# tk.Checkbutton(window, text='Smth').grid(row=4, column=0)
#
# tk.Scale(window, orient=tk.HORIZONTAL).grid(row=5, column=0)
#
# Entry_entry_send = tk.Entry(window)
# Entry_entry_send.grid(row=6, column=1)

# figure = plt.Figure(figsize=(6,5), dpi=100)
# ax = figure.add_subplot(111)
# chart_type = FigureCanvasTkAgg(figure, window)
# chart_type.get_tk_widget().grid(row=8, column=0, columnspan=2, padx=10, pady=10)


window.mainloop()
