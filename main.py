from tkinter import *

janela = Tk()

janela.title("teste")
texto = Label(janela, text='click no botao e veja a magica! ')
texto.grid(column=0, row=0)
def texto():
    texto_magica = Label(janela, text='HELLO, Wolrd! ')
    texto_magica.grid(column=0, row=1)

botao_click = Button(janela, text= "Click AQUI", command=texto)
botao_click.grid(column=0, row=2)

texto2 = Label(janela, text=' ')
texto2.grid(column=0, row=3)
janela.mainloop()