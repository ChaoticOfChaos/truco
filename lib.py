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

class jogo:
    def __init__(self, player1: player, player2: player, vira: card) -> None:
        self.player1 = player1
        self.player2 = player2
        self.vira = vira