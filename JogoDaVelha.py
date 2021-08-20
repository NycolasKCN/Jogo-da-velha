from time import sleep
try:
    import tkinter as tk
    from tkinter.messagebox import showinfo
except ImportError:
    print("Não foi possivel rodar o jogo pois não se possue o tkinter, instali-o via pip e tente novamente")
    sleep(60)
except:
    print("Aconteceu um erro desconhecido")

main = tk.Tk() # Criando tela

main.geometry("400x400")
main.resizable(width=False, height=False)

# Estrategia para definir empate atraves da contagem das rodadas
count = 0

player1 = 1  # Player 1 vale "1", logo admitimos que ele será o X
player2 = -1  # Player 2 vale "-1", logo admitimos que ele será o O
jogador = [player1]
board = [
    [0, 0, 0],
    [0, 0, 0],
    [0, 0, 0]
]

# Declarando todas as posições do board do frontend com dicionarios
posBord1 = {"x": (35+40), "y": (10+40)}
posBord2 = {"x": (145+40), "y": (10+40)}
posBord3 = {"x": (255+40), "y": (10+40)}

posBord4 = {"x": (35+40), "y": (120+40)}
posBord5 = {"x": (145+40), "y": (120+40)}
posBord6 = {"x": (255+40), "y": (120+40)}

posBord7 = {"x": (35+40), "y": (230+40)}
posBord8 = {"x": (145+40), "y": (230+40)}
posBord9 = {"x": (255+40), "y": (230+40)}


def resultado(ganhador=""):
    showinfo(title="GANHADOR",
             message=f"O jogador que estava jogando com o '{ganhador}' GANHOU")
    main.destroy()


def clique(pos, lin="", col=""):
    # Apagando Botão da tela apos o clique e Substituindo a Label
    pos.destroy()

    global texto, jogador, board

    # Verificando o ultimo jogador a jogar
    # Se o Ultimo Player for o "X" então a Proxima jogada será do player "O"
    if jogador[0] == 1:
        try:
            texto.destroy()
        except:
            print("Label já foi apagado")

        # Alterando os valores no board backend
        board[lin][col] = jogador[0]

        # Trocando o player na lista "jogador"
        # Até aqui a lista "jogador" inidica que quem jogou foi o "X"
        jogador.pop()
        jogador.append(player2)

        # Texto de apresentação, tem que ficar como ultima instancia, senão ocorre um bug de pontuação
        texto = tk.Label(main, text="Vez do jogador: O",
                         font=("Retrosans", 16))
        texto.place(x=150, y=345)

    # Se o ultimo player for o "O" então o proximo será o player "X"
    elif jogador[0] == -1:
        try:
            texto.destroy()
        except:
            print("Label já foi apagado")

        # Alterando os valores no board backend
        board[lin][col] = jogador[0]

        # Trocando o player na lista "jogador"
        # Até aqui a lista "jogador" inidica que quem jogou foi o "O"
        jogador.pop()
        jogador.append(player1)

        # Texto de Declaração do player, tem que ficar como ultima instancia, senão ocorre um bug de pontuação
        texto = tk.Label(main, text="Vez do jogador: X",
                         font=("Retrosans", 16))
        texto.place(x=150, y=345)


def mark(pos_x, pos_y):
    # Mark será nosso marcardor no frontend e irar ser modificado dependendo do botão que for clicado
    # Neste caso como os valores são alterados a cada clique e no escopo do projeto a chamada da função deve vir por Ultimo
    # os valores serão inversos
    if jogador[0] == -1:
        mark = tk.Label(main, text="X", font=("Retrosans", 26))
        mark.place(x=pos_x, y=pos_y)

    elif jogador[0] == 1:
        mark = tk.Label(main, text="O", font=("Retrosans", 26))
        mark.place(x=pos_x, y=pos_y)

    else:
        print("passei pelos dois if's e nada aconteceu")


def ganhou():
    global count
    count += 1

    # Checando as linhas e declarando o ganhador
    for i in range(3):
        soma = board[i][0] + board[i][1] + board[i][2]
        if soma == 3:
            resultado("X")

        elif soma == -3:
            resultado("O")

    # Checando as colunas e declarando o ganhador
    for i in range(3):
        soma = board[0][i] + board[1][i] + board[2][i]
        if soma == 3:
            resultado("X")

        elif soma == -3:
            resultado("O")

    # Checando as diagonais e declarando ganhador
    diagonal1 = board[0][0]+board[1][1]+board[2][2]
    diagonal2 = board[0][2]+board[1][1]+board[2][0]

    if diagonal1 == 3 or diagonal2 == 3:
        resultado("X")

    if diagonal1 == -3 or diagonal2 == -3:
        resultado("O")

    if count == 9:
        showinfo(title="Empate",
                 message="O jogo Empatou")
        main.destroy()


# Texto que ira aparecer na primeira jogada
texto = tk.Label(main, text="Vez do jogador: X", font=("Retrosans", 16))
texto.place(x=(400/2-60), y=345)

# Primeira fileira de botões
pos1 = tk.Button(main, command=lambda: (clique(pos1, 0, 0), mark(posBord1["x"], posBord1["y"]), ganhou()),
                 bg="#3399ff")
pos2 = tk.Button(main, command=lambda: (clique(pos2, 0, 1), mark(posBord2["x"], posBord2["y"]), ganhou()),
                 bg="#3399ff")
pos3 = tk.Button(main, command=lambda: (clique(pos3, 0, 2), mark(posBord3["x"], posBord3["y"]), ganhou()),
                 bg="#3399ff")

# Segunda fileira dos Botões
pos4 = tk.Button(main, command=lambda: (clique(pos4, 1, 0), mark(posBord4["x"], posBord4["y"]), ganhou()),
                 bg="#3399ff")
pos5 = tk.Button(main, command=lambda: (clique(pos5, 1, 1), mark(posBord5["x"], posBord5["y"]), ganhou()),
                 bg="#3399ff")
pos6 = tk.Button(main, command=lambda: (clique(pos6, 1, 2), mark(posBord6["x"], posBord6["y"]), ganhou()),
                 bg="#3399ff")

# Terceira fileira dos botões
pos7 = tk.Button(main, command=lambda: (clique(pos7, 2, 0), mark(posBord7["x"], posBord7["y"]), ganhou()),
                 bg="#3399ff")
pos8 = tk.Button(main, command=lambda: (clique(pos8, 2, 1), mark(posBord8["x"], posBord8["y"]), ganhou()),
                 bg="#3399ff")
pos9 = tk.Button(main, command=lambda: (clique(pos9, 2, 2), mark(posBord9["x"], posBord9["y"]), ganhou()),
                 bg="#3399ff")

# Primeira fileira de botões
pos1.place(x=35, y=10, width=100, height=100)
pos2.place(x=145, y=10, width=100, height=100)
pos3.place(x=255, y=10, width=100, height=100)

# Segunda fileira dos Botões
pos4.place(x=35, y=120, width=100, height=100)
pos5.place(x=145, y=120, width=100, height=100)
pos6.place(x=255, y=120, width=100, height=100)

# Terceira fileira dos botões
pos7.place(x=35, y=230, width=100, height=100)
pos8.place(x=145, y=230, width=100, height=100)
pos9.place(x=255, y=230, width=100, height=100)


main.mainloop()
