import tkinter as tk

window = tk.Tk()
height = 500
width = 500
d_x = 500
d_y = 100
window.title('Configuration of the SPI Potentiometer')
window.geometry(f"{height}x{width}+{d_x}+{d_y}")
window.minsize(300, 300)
window.maxsize(700, 700)
window.resizable(True, True)

photo = tk.PhotoImage(file='setting.png')
window.iconphoto(True, photo)

window.mainloop()
