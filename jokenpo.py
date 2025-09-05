import tkinter as tk
from random import randint

def jogar():
    escolhas = ["Pedra", "Papel", "Tesoura"]
    computador = randint(0, 2)
    jogador = int(var_escolha.get())

    resultado = "Empate!" if jogador == computador else (
        "Você venceu!" if (jogador == 0 and computador == 2) or
        (jogador == 1 and computador == 0) or
        (jogador == 2 and computador == 1) else "Computador venceu!"
    )

    label_resultado.config(text=f"Computador jogou {escolhas[computador]}\n{resultado}")

# Criando a janela
janela = tk.Tk()
janela.title("Jogo Pedra, Papel, Tesoura")

# Mensagem inicial
tk.Label(janela, text="Escolha sua jogada:").pack()

# Opções do jogador
var_escolha = tk.IntVar()
tk.Radiobutton(janela, text="Pedra", variable=var_escolha, value=0).pack()
tk.Radiobutton(janela, text="Papel", variable=var_escolha, value=1).pack()
tk.Radiobutton(janela, text="Tesoura", variable=var_escolha, value=2).pack()

# Botão para jogar
tk.Button(janela, text="Jogar!", command=jogar).pack()

# Label para exibir o resultado
label_resultado = tk.Label(janela, text="")
label_resultado.pack()

# Iniciar a interface
janela.mainloop()