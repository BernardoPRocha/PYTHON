from tkinter import *

window = Tk()
window.title("Imagem na Janela")
imagem = PhotoImage(file="./imagens/spiderman.png")
rotulo = Label(window)
rotulo["image"] = imagem
rotulo.pack()
window.mainloop()