import random
import lib
from os import system

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
            print(f"Manilha! : {card1.card} ; {card1.value} ; {card1.naipe}")

        mao1.append(card1)

        num2 = random.randint(0, len(list(lib.cards.keys()))-1)
        card2 = lib.card(num2)

        if card2.value == vira.value:
            card2.value += lib.lib_add[card2.naipe]
            print(f"Manilha! : {card2.card} ; {card2.value} ; {card2.naipe}")

        mao2.append(card2)

    return (mao1, mao2, [vira])

def main() -> None:
    system("clear")
    (mao1, mao2, vira) = shuffle()
    player1 = lib.player(mao1)
    player2 = lib.player(mao2)

    game = lib.jogo(player1, player2, vira[0])

    print(f"Manilha : {game.vira.card}")
    game.player1.debug_card()
    game.player2.debug_card()

    game.play()

if __name__ == '__main__':
    main()
