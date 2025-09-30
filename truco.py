import random
import lib
import socket
import os
import sys

def ask_action(can_truco: bool, can_truqued: bool) -> int:
    print("(1) -> Jogar Carta")
    if (can_truco and can_truqued):
        print("(2) -> Truco!")
    print("(0) -> Pular Fora")

    while True:
        try:
            inp = int(input(">>> "))
            if (can_truco and can_truqued):
                if (inp in [1, 2, 0]):
                    break

            else:
                if (inp in [1, 0]):
                    break

        except ValueError:
            print("Insert a Number")

    return inp

def ask_card(cartas: list[str]) -> int:
    list_num = []
    for num, card in enumerate(cartas):
        print(f"({num}) -> {card}")
        list_num.append(num)

    while True:
        try:
            inp = int(input(">>> "))
            if (inp in list_num):
                break

        except ValueError:
            print("Insert a Number")

    return inp

def connection(host: str, port: int) -> None:
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect((host, port))

    for _ in range(3):
        os.system("clear")
        # Se o Jogador Pode Trucar
        can_truco = True if client.recv(1024).decode() == "True" else False
        # se a Mesa Pode Trucar
        can_truqued = True if client.recv(1024).decode() == "True" else False
        # Ambos a Resposta Apenas pode Ser True ou False
        

        resp_truco = client.recv(1024).decode()
        print(resp_truco)
        resp_user = ask_action(can_truco, can_truqued)
        client.send(f"{resp_user}".encode())

        # Ex. Q-E;K-O;A-P
        cartas = client.recv(1024).decode()
        cartas = cartas.split(';')

        carta = ask_card(cartas)

        client.send(f"{carta}".encode())

        os.system("clear")
        print("Vez do Player 1")

        resposta = client.recv(1024).decode()

        if (resposta == "1"):
            pontos = client.recv(1024).decode()
            print("Jogador 1 Pulou Fora")
            print("Vitória do Jogador 2")
            print(f"Jogador 2 +{pontos}")

        elif (resposta == "2"):
            pontos = client.recv(1024).decode()
            print("Jogador 1 Ganhou")
            print(f"Jogador 1 +{pontos}")

        elif (resposta == "3"):
            pontos = client.recv(1024).decode()
            print("Jogador 2 Ganhou")
            print(f"Jogador 2 +{pontos}")

        elif (resposta == "4"):
            print("Empate!")

        elif (resposta == "0"):
            pass

        else:
            print("ERROR!")
            client.close()
            return None

        # Receber o último Valor
        # 0 -> Apenas Continua
        # 1 -> Jogador 1 Pulou Fora
        # 2 -> Vitória do Jogador 1
        # 3 -> Vitória do Jogador 2
        # 4 -> Empate

    client.close()

def shuffle() -> tuple[list, list, list]:
    mao1 = []
    mao2 = []

    num_vira = random.randint(0, len(list(lib.cards.keys()))-1)
    vira = lib.card(num_vira)

    for _ in range(3):
        num1 = random.randint(0, len(list(lib.cards.keys()))-1)
        card1 = lib.card(num1)

        if card1.value == vira.value:
            card1.value += lib.lib_add[card1.naipe]

        mao1.append(card1)

        num2 = random.randint(0, len(list(lib.cards.keys()))-1)
        card2 = lib.card(num2)

        if card2.value == vira.value:
            card2.value += lib.lib_add[card2.naipe]

        mao2.append(card2)

    return (mao1, mao2, [vira])

def main(host: str, port: int) -> None:
    os.system("clear")
    (mao1, mao2, vira) = shuffle()
    player1 = lib.player(mao1)
    player2 = lib.player(mao2)

    game = lib.jogo(player1, player2, vira[0])

    game.play(host, port)

if __name__ == '__main__':
    if (sys.argv[1] == "host"):
        # Ex. python3 truco.py host 127.0.0.1 12345
        main(sys.argv[2], int(sys.argv[3]))

    elif (sys.argv[1] == "client"):
        connection(sys.argv[2], int(sys.argv[3]))

    else:
        print("Argument Error")
        print("Try: 'python3 truco.py host 127.0.0.1 12345' To Host")
        print("Or: 'python3 truco.py client 127.0.0.1 12345' To Connect an Existent Game")
