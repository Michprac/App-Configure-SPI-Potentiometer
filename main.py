import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showerror

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




height = 980
width = 859
d_x = 500
d_y = 0
Radio_pt = tk.IntVar()  # variable for the radiobutton choosing


setvalue1 = tk.StringVar()  # actual value for the potentiometer 1
scale1 = tk.IntVar()

setvalue2 = tk.StringVar()  # actual value for the potentiometer 2
scale2 = tk.IntVar()


pt1_active = tk.IntVar()
pt1_active.set(0)
ValuesForPotentiometer = {'Choose value': 'Choose value',
                          '10 000': 10000,
                          '20 000': 20000,
                          '30 000': 30000,
                          '40 000': 40000,
                          '50 000': 50000}

previous_values_pt_1 = [0]*10
actual_value_number_1 = list(range(1,11))
previous_values_pt_2 = [0]*10
actual_value_number_2 = list(range(1,11))

#Creating a plot of previous values
def create_plot1():

    print(previous_values_pt_1)
    print(actual_value_number_1)

    fig = plt.figure(figsize=(3,3), dpi=90)
    plot1 = fig.add_subplot(1,1,1)
    plot1.set_ylabel('Value of the potentiometer 1')
    plot1.set_xlabel('Previous value number')
    plot1.set_title('Graph for potentiometer 1')
    plot1.plot(actual_value_number_1, previous_values_pt_1, marker='o')


    plot_on_window = FigureCanvasTkAgg(fig, window)
    plot_on_window.draw()
    plot_on_window.get_tk_widget().grid(row=5, column=0, columnspan=8, sticky='NWES', pady=5, ipady=50, padx=20)


def create_plot2():

    print(previous_values_pt_2)
    print(actual_value_number_2)


    global fig, axis

    fig = plt.figure(figsize=(3,3), dpi=90)
    plot1 = fig.add_subplot(1,1,1)
    plot1.set_ylabel('Value of the potentiometer 2')
    plot1.set_xlabel('Previous value number')
    plot1.set_title('Graph for potentiometer 2')

    plot1.plot(actual_value_number_2, previous_values_pt_2, marker='o')

    plot_on_window = FigureCanvasTkAgg(fig, window)
    plot_on_window.draw()
    plot_on_window.get_tk_widget().grid(row=6, column=0, columnspan=8, sticky='NWES', pady=5, ipady=50, padx=20)









def unlock_widgets1():
    if int(pt1_active.get()):
        label1.config(state="normal")
        box1.config(state="readonly")
        entry1.config(state="normal")
        scale1_widg.config(state='normal')
        send_btn1.config(state="normal")
        actual_val_1.config(state="normal")
        val_1.config(state="normal")

    else:
        label1.config(state="disabled")
        box1.config(state="disabled")
        entry1.config(state="disabled")
        scale1_widg.config(state=tk.DISABLED)
        send_btn1.config(state="disabled")
        actual_val_1.config(state="disabled")
        val_1.config(state="disabled")


def unlock_widgets2():
    if int(pt2_active.get()):
        box2.config(state="readonly")
        label2.config(state="normal")
        entry2.config(state="normal")
        scale2_widg.config(state='normal')
        send_btn2.config(state="normal")
        actual_val_2.config(state="normal")
        val_2.config(state="normal")

    else:
        box2.config(state="disabled")
        label2.config(state="disabled")
        entry2.config(state="disabled")
        scale2_widg.config(state=tk.DISABLED)
        send_btn2.config(state="disabled")
        actual_val_2.config(state="disabled")
        val_2.config(state="disabled")


def set_values_box_1(event):
    if box1.get() == 'Choose value':
        newval = '0'
    else:
        newval = ValuesForPotentiometer[box1.get()]

    setvalue1.set(newval)

    entry1.delete(0, tk.END)
    entry1.insert(0, newval)

    scale1.set(round(int(newval) / max(list(ValuesForPotentiometer.values())[1:]) * 100))

    val_1['text'] = str(newval) + '[Ω]'

def set_values_box_2(event):
    if box2.get() == 'Choose value':
        newval2 = '0'
    else:
        newval2 = ValuesForPotentiometer[box2.get()]

    setvalue2.set(newval2)

    entry2.delete(0, tk.END)
    entry2.insert(0, newval2)

    scale2.set(round(int(newval2) / max(list(ValuesForPotentiometer.values())[1:]) * 100))

    val_2['text'] = str(newval2) + '[Ω]'


def set_values_entry_1(event):
    try:
        newval = int(entry1.get())
    except ValueError:
        entry1.delete(0, tk.END)
        entry1.insert(0, 'Write number')
        return

    if newval >= 0 and newval <= 50000:
        setvalue1.set(newval)
    else:
        return

    box1.set(list(ValuesForPotentiometer.keys())[0])

    scale1.set(round(int(newval) / max(list(ValuesForPotentiometer.values())[1:]) * 100))

    val_1['text'] = str(newval) + '[Ω]'


def set_values_entry_2(event):
    try:
        newval = int(entry2.get())
    except ValueError:
        entry2.delete(0, tk.END)
        entry2.insert(0, 'Write number')
        return

    if newval >= 0 and newval <= 50000:
        setvalue2.set(newval)
    else:
        return

    box2.set(list(ValuesForPotentiometer.keys())[0])

    scale2.set(round(int(newval) / max(list(ValuesForPotentiometer.values())[1:]) * 100))

    val_2['text'] = str(newval) + '[Ω]'

def set_values_scale_1(event):
    if scale1_widg["state"] == "disabled":
        return
    newval = int(round(scale1.get() / 100 * max(list(ValuesForPotentiometer.values())[1:])))
    setvalue1.set(newval)

    box1.set(list(ValuesForPotentiometer.keys())[0])

    entry1.delete(0, tk.END)
    entry1.insert(0, newval)

    val_1['text'] = str(newval) + '[Ω]'


def set_values_scale_2(event):
    if scale2_widg["state"] == "disabled":
        return

    newval = int(round(scale2.get() / 100 * max(list(ValuesForPotentiometer.values())[1:])))
    setvalue2.set(newval)

    box2.set(list(ValuesForPotentiometer.keys())[0])

    entry2.delete(0, tk.END)
    entry2.insert(0, newval)

    val_2['text'] = str(newval) + '[Ω]'



def send_value_1():
    try:
        int(setvalue1.get())
    except ValueError:
        showerror(title="Error", message="Write a NUMBER, not string")
        return

    global previous_values_pt_1, actual_value_number_1



    # configure_byte = 0b00010001
    # value_of_pt_hex_1 = int(setvalue1.get()) * 255 // max(list(ValuesForPotentiometer.values())[1:])
    # text_to_send = str(configure_byte)[2:] + str(bin(value_of_pt_1))
    # serial_object.write(text_to_send)


    previous_values_pt_1 = previous_values_pt_1[1:]
    previous_values_pt_1.append(int(setvalue1.get()))

    actual_value_number_1 = actual_value_number_1[1:]
    actual_value_number_1.append(actual_value_number_1[-1]+1)

    create_plot1()



def send_value_2(list1):

    try:
        int(setvalue2.get())
    except ValueError:
        showerror(title="Error", message="Write a NUMBER, not string")
        return

    global previous_values_pt_2, actual_value_number_2


    # configure_byte = 0b00010010
    # value_of_pt_1 = int(setvalue2.get()) * 255 // max(list(ValuesForPotentiometer.values())[1:])
    # text_to_send = str(configure_byte)[2:] + str(bin(value_of_pt_1))
    # serial_object.write(text_to_send)

    previous_values_pt_2 = previous_values_pt_2[1:]
    previous_values_pt_2.append(int(setvalue2.get()))

    actual_value_number_2 = actual_value_number_2[1:]
    actual_value_number_2.append(actual_value_number_2[-1]+1)

    create_plot2()



create_plot1()
create_plot2()

window.title('Configuration of the SPI Potentiometer')
window.geometry(f"{height}x{width}+{d_x}+{d_y}")
window.minsize(width, height)
window.maxsize(width, height)

photo = tk.PhotoImage(file='setting.png')
window.iconphoto(True, photo)

tk.Label(window, text="Port").grid(row=0, column=0, pady=10)

ports_box = ttk.Combobox(window, values=all_ports_str)
ports_box.current(0)
ports_box.grid(row=0, column=1)

################## FOR POTENTIOMETER 1 #####################################
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
box1.bind("<<ComboboxSelected>>", set_values_box_1)
box1.current(0)
box1.grid(row=2, column=2)

entry1 = ttk.Entry(window)
entry1.insert(0, 'Set value')
entry1.config(state="disabled")
entry1.bind("<Return>", set_values_entry_1)
entry1.grid(row=2, column=3, padx=10)

scale1_widg = tk.Scale(window, orient=tk.HORIZONTAL, variable=scale1)
scale1_widg.grid(row=2, column=4, ipady=10)
scale1_widg.config(state=tk.DISABLED)
scale1_widg.bind("<ButtonRelease-1>", set_values_scale_1)

send_btn1 = tk.Button(window, text="Send", command=send_value_1)
send_btn1.grid(row=2, column=5, padx=10)
send_btn1.config(state="disabled")

actual_val_1 = tk.Label(window, text="Actual Value: ")
actual_val_1.grid(row=2, column=6, padx=10)
actual_val_1.config(state="disabled")

val_1 = tk.Label(window, text=0)
val_1.grid(row=2, column=7)
val_1.config(state="disabled")

############################# FOR POTENTIOMETER 2 ############################

tk.Label(window, text="Potentiometer №2").grid(row=3, column=0)

pt2_active = tk.IntVar()
pt2_active.set(0)
tk.Checkbutton(window, text='Activate',
               variable=pt2_active,
               offvalue=0,
               onvalue=1,
               command=unlock_widgets2).grid(row=4, column=0)

label2 = tk.Label(window, text="Value [Ω]")
label2.grid(row=4, column=1, padx=10)
label2.config(state="disabled")

box2 = ttk.Combobox(window, values=list(ValuesForPotentiometer.keys()), )
box2.bind("<<ComboboxSelected>>", set_values_box_2)
box2.current(0)
box2.grid(row=4, column=2)
box2.config(state="disabled")

entry2 = ttk.Entry(window)
entry2.insert(0, 'Set value')
entry2.config(state="disabled")
entry2.bind("<Return>", set_values_entry_2)
entry2.grid(row=4, column=3, padx=10)

scale2_widg = tk.Scale(window, orient=tk.HORIZONTAL, variable=scale2)
scale2_widg.grid(row=4, column=4, ipady=10)
scale2_widg.config(state="disabled")
scale2_widg.bind("<ButtonRelease-1>", set_values_scale_2)

send_btn2 = tk.Button(window, text="Send", command=lambda list1=previous_values_pt_2: send_value_2(list1))
send_btn2.grid(row=4, column=5, padx=10)
send_btn2.config(state="disabled")

actual_val_2 = tk.Label(window, text="Actual Value: ")
actual_val_2.grid(row=4, column=6, padx=10)
actual_val_2.config(state="disabled")

val_2 = tk.Label(window, text=0)
val_2.grid(row=4, column=7)
val_2.config(state="disabled")





window.mainloop()
