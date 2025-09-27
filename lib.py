import time

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

    def display_hand(self) -> None:
        for c in self.mao:
            print(c.card)

    def debug_card(self) -> None:
        for c in self.mao:
            print(f"Display : {c.card} ; Naipe : {c.naipe} ; Value : {c.value} ; Number : {c.num}")

    def self_display(self) -> None:
        print("Suas Cartas:")
        for c in self.mao:
            print(f"{c.card}", end=" ")

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
    
    def ask_action(self) -> int:
        print("(1) -> Jogar Carta")
        print("(2) -> Truco!")
        print("(6) -> 6!")
        print("(9) -> 9!")
        print("(12) -> 12!")
        print("(0) -> Pular Fora")

        while True:
            try:
                inp = int(input(">>> "))
                if (inp in [1, 2, 6, 9, 12, 0]):
                    break

            except ValueError:
                print("Insert a Number")

        return inp


class jogo:
    def __init__(self, player1: player, player2: player, vira: card) -> None:
        self.player1 = player1
        self.player2 = player2
        self.vira = vira
        self.value = 1

    def play(self) -> None:
        for i in range(3):
            print(f"Rodada {i}")
            time.sleep(1)
            print("Vez do Player 1")
            time.sleep(1)
            carta_p1 = self.player1.ask_play_card()

            print("Vez do Player 2")
            time.sleep(1)
            carta_p2 = self.player2.ask_play_card()

            if (carta_p1.value > carta_p2.value):
                print("Jogador 1 Ganhou!")

            elif (carta_p1.value < carta_p2.value):
                print("Jogador 2 Ganhou!")

            else:
                print("Empate!")
