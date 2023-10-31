from tkinter import *
window = Tk()
window.title("Título da Janela")
window.geometry("350x200+400+200")
window.configure(background="moccasin")
rotulo = Label(window)
rotulo["text"] = "Hello World"
rotulo["font"] = ("Impact", "20", "bold")
rotulo["fg"] = "brown"
rotulo["bg"] = "yellow"
rotulo["pady"] = 5
rotulo["padx"] = 10
rotulo["width"] = 20
rotulo["anchor"] = "w"
rotulo.pack()
window.mainloop()