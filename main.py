import tkinter as tk
from tkinter import ttk
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg




def choose_pt():
    print("You've chosen" + str(Radio_pt.get()))


window = tk.Tk()
height = 750
width = 620
d_x = 500
d_y = 20
Radio_pt = tk.IntVar() # variable for the radiobutton choosing






window.title('Configuration of the SPI Potentiometer')
window.geometry(f"{height}x{width}+{d_x}+{d_y}")
window.minsize(width, height)
window.maxsize(width, height)
window.resizable(True, True)

photo = tk.PhotoImage(file='setting.png')
window.iconphoto(True, photo)


Label_number_of_pt = tk.Label(window, text="Potentiometer №1", pady= 10)
Label_number_of_pt.grid(row=0, column=0)

First_pt_1 = tk.Radiobutton(window, text='Activate', variable= Radio_pt, value=1, command= choose_pt)
First_pt_1.grid(row=0, column=1)

Label_entry_send = tk.Label(window, text="Value of potentiometer [Ω]", padx= 10, pady= 10)
Label_entry_send.grid(row=1, column=0)

Entry_entry_send = ttk.Combobox(window)
Entry_entry_send.grid(row=1, column=1)

Button_entry_send = tk.Button(window, text="Send")
Button_entry_send.grid(row=2, column=0, columnspan=2, stick='NWSE', padx=10)

Label_number_of_pt = tk.Label(window, text="Potentiometer №2", pady= 10)
Label_number_of_pt.grid(row=3, column=0)

First_pt_1 = tk.Radiobutton(window, text='Activate', variable= Radio_pt, value=2, command= choose_pt)
First_pt_1.grid(row=3, column=1)

tk.Checkbutton(window,text='Smth').grid(row=4, column=0)

tk.Scale(window, orient=tk.HORIZONTAL).grid(row=5,column=0)

Entry_entry_send = tk.Entry(window)
Entry_entry_send.grid(row=6, column=1)


figure = plt.Figure(figsize=(6,5), dpi=100)
ax = figure.add_subplot(111)
chart_type = FigureCanvasTkAgg(figure, window)
chart_type.get_tk_widget().grid(row=8, column=0, columnspan=2, padx=10, pady=10)


window.mainloop()
