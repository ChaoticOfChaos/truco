import time
import os
import socket

cards = {
    0: ["A-E", 8, "E"],
    1: ["2-E", 9, "E"],
    2: ["3-E", 10, "E"],
    3: ["4-E", 1, "E"],
    4: ["5-E", 2, "E"],
    5: ["6-E", 3, "E"],
    6: ["7-E", 4, "E"],
    7: ["Q-E", 5, "E"],
    8: ["J-E", 6, "E"],
    9: ["K-E", 7, "E"],
    10: ["A-C", 8, "C"],
    11: ["2-C", 9, "C"],
    12: ["3-C", 10, "C"],
    13: ["4-C", 1, "C"],
    14: ["5-C", 2, "C"],
    15: ["6-C", 3, "C"],
    16: ["7-C", 4, "C"],
    17: ["Q-C", 5, "C"],
    18: ["J-C", 6, "C"],
    19: ["K-C", 7, "C"],
    20: ["A-P", 8, "P"],
    21: ["2-P", 9, "P"],
    22: ["3-P", 10, "P"],
    23: ["4-P", 1, "P"],
    24: ["5-P", 2, "P"],
    25: ["6-P", 3, "P"],
    26: ["7-P", 4, "P"],
    27: ["Q-P", 5, "P"],
    28: ["J-P", 6, "P"],
    29: ["K-P", 7, "P"],
    30: ["A-O", 8, "O"],
    31: ["2-O", 9, "O"],
    32: ["3-O", 10, "O"],
    33: ["4-O", 1, "O"],
    34: ["5-O", 2, "O"],
    35: ["6-O", 3, "O"],
    36: ["7-O", 4, "O"],
    37: ["Q-O", 5, "O"],
    38: ["J-O", 6, "O"],
    39: ["K-O", 7, "O"]
}

# Quantidade de Valor Adicionado para a Manilha
lib_add = {
    "O": 10,
    "E": 11,
    "C": 12,
    "P": 13
}

class card:
    def __init__(self, num: int) -> None:
        self.card = cards.get(num)[0]
        self.num = num
        self.value = cards.get(num)[1]
        self.naipe = cards.get(num)[2]

class player:
    def __init__(self, mao: list[card]) -> None:
        self.mao = mao
        self.can_truco = True

    def display_hand(self) -> None:
        for c in self.mao:
            print(c.card)

    def debug_card(self) -> None:
        for c in self.mao:
            print(f"Display : {c.card} ; Naipe : {c.naipe} ; Value : {c.value} ; Number : {c.num}")

    def self_display(self) -> None:
        print("Suas Cartas:")
        for c in self.mao:
            print(f"|{c.card}|", end=" ")

        print("\n")

    def ask_play_card(self) -> card:
        for num, c in enumerate(self.mao):
            print(f"({num}) -> {c.card}")

        while True:
            try:
                index = int(input(">>> "))
                carta = self.mao[index]
                self.mao.remove(carta)
                break
            
            except IndexError:
                print("Insert a Valid Input")

            except ValueError:
                print("Insert a Number")

        return carta
    
    def response_truco(self):
        print("(1) -> Aceitar")
        print(f"(2) -> Truco!")
        print("(0) -> Pula Fora")

        while True:
            try:
                inp = int(input(">>> "))
                if (inp in [1, 2, 0]):
                    break

            except ValueError:
                print("Insert a Number")

        return inp
    
    def ask_action(self, can_truqued: bool) -> int:
        print("(1) -> Jogar Carta")
        if (self.can_truco and can_truqued):
            print("(2) -> Truco!")
        print("(0) -> Pular Fora")

        while True:
            try:
                inp = int(input(">>> "))
                if (self.can_truco and can_truqued):
                    if (inp in [1, 2, 0]):
                        break

                else:
                    if (inp in [1, 0]):
                        break

            except ValueError:
                print("Insert a Number")

        return inp
    
    def truqued(self) -> None:
        self.can_truco = False

    def can_truqued(self) -> None:
        self.can_truco = True


class jogo:
    def __init__(self, player1: player, player2: player, vira: card) -> None:
        self.player1 = player1
        self.player2 = player2
        self.vira = vira
        self.value = 1
        self.trucos = 0
        self.dict_trucos = {0: 1, 1: 3, 2: 6, 3: 9, 4: 12}
        self.can_truco = True
        self.pular_fora_dict = {0: 1, 1: 1, 2: 3, 3: 6, 4: 9}
        self.p1_v = 0
        self.p2_v = 0
        self.mesa = []

    def play(self, host: str, port: int) -> None:
        server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server.bind((host, port))
        server.listen(1)
        print(f"Escutando em: {host}:{port}")
        conexao, endereco = server.accept()
        print(endereco)
        for i in range(3):
            os.system("clear")
            print("Jogador 1")
            print(f"Rodada {i+1}")
            print(f"Valor da Partida: {self.value}")
            print(f"Manilha: {self.vira.card}")
            print("Mesa:", end=" ")
            for c in self.mesa:
                print(f"|{c}|", end=" ")
            print("")
            print(f"Suas Vitórias: {self.p1_v}")
            self.player1.self_display()
            action_p1 = self.player1.ask_action(self.can_truco)
            
            # Player 1 Aumenta Valor
            if (action_p1 == 2):
                self.player1.truqued()
                self.player2.can_truqued()
                self.trucos += 1
                self.value = self.dict_trucos[self.trucos]
                if (self.value == 12):
                    self.can_truco = False
                

            # Player 1 Pula Fora
            elif (action_p1 == 0):
                print("Jogador 1 Pulou Fora!")
                print("Vitória do Jogador 2")
                print(f"Jogador 2 +{self.pular_fora_dict[self.trucos]}")
                conexao.close()
                return None
            
            elif (action_p1 == 1):
                pass

            else:
                print("ERROR!")
                conexao.close()
                return None

            carta_p1 = self.player1.ask_play_card()
            self.mesa.append(carta_p1.card)
            os.system("clear")
            print("Vez do Jogador 2")

            # Enviar "Can_truco" do P2
            conexao.send(f"{self.player2.can_truco}".encode())
            time.sleep(0.7)
            # Enviar "Can_truqued" da Mesa
            conexao.send(f"{self.can_truco}".encode())
            time.sleep(0.7)

            msg_p2 = f"Jogador 2\nRodada: {i+1}\nValor da Partida: {self.value}\nManilha: {self.vira.card}\nMesa:"
            for c in self.mesa:
                msg_p2 += f"|{c}| "
            msg_p2 += f"\nSuas Vitórias: {self.p2_v}\nSuas Cartas:"

            for c in self.player2.mao:
                msg_p2 += f"|{c.card}| "
            conexao.send(msg_p2.encode())
            time.sleep(0.7)
            # action_p2 = self.player2.ask_action(self.can_truco)
            action_p2 = int(conexao.recv(1024).decode())

            # Player 2 Aumenta Valor
            if (action_p2 == 2):
                self.player1.can_truqued()
                self.player2.truqued()
                self.trucos += 1
                self.value = self.dict_trucos[self.trucos]
                if (self.value == 12):
                    self.can_truco = False

            # Player 2 Pula Fora 
            elif (action_p2 == 0):
                print("Jogador 2 Pulou Fora")
                print("Vitória do Jogador 1")
                print(f"Jogador 1 +{self.pular_fora_dict[self.trucos]}")
                conexao.close()
                return None
            
            elif (action_p2 == 1):
                pass

            else:
                print("ERROR!")
                conexao.close()
                return None

            cartas = ""
            for c in self.player2.mao:
                if (len(self.player2.mao) == 1):
                    cartas += f"{c.card}"

                else:
                    cartas += f"{c.card};"

            if (cartas[-1] == ';'):
                cartas = cartas[:-1]

            conexao.send(cartas.encode())
            time.sleep(0.7)

            # Sempre será um int
            index_carta = int(conexao.recv(1024).decode())
            carta_p2 = self.player2.mao[index_carta]
            self.player2.mao.remove(carta_p2)
            self.mesa.append(carta_p2.card)

            if (carta_p1.value > carta_p2.value):
                print("Jogador 1 Ganhou!")
                self.p1_v += 1

            elif (carta_p1.value < carta_p2.value):
                print("Jogador 2 Ganhou!")
                self.p2_v += 1

            else:
                print("Empate!")

            conexao.send("0".encode())

        # Fim do Jogo

        if (self.p1_v > self.p2_v):
            print("Jogador 1 Ganhou")
            print(f"Jogador 1 +{self.value}")
        
        elif (self.p1_v < self.p2_v):
            print("Jogador 2 Ganhou")
            print(f"Jogador 2 +{self.value}")

        else:
            print("Empate")

        conexao.close()
