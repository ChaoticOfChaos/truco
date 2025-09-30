# TRUCO CLI
## Version 2.1.0

# Como Jogar
O jogador 1 deve usar o comando:<br>
```sh
python3 truco.py host 127.0.0.1 12345
```
Substituindo o Endereço '127.0.0.1' pelo endereço de IP Privado e a porta pela qual preferir<br>
Já o jogador 2 Deve se Conectar usando:
```sh
python3 truco.py client 127.0.0.1 12345
```
Substituindo o endereço '127.0.0.1' pelo IP do Jogador 1 a porta pela porta escolhida pelo Jogador 1<br>
O Jogo funciona semenlhante ao jogo original:<br>
3<br>
2<br>
A<br>
K<br>
J<br>
Q<br>
7<br>
6<br>
5<br>
4<br>
Sendo 3 a maior e 4 a menor<br>
E naipes:<br>
Paus<br>
Copas<br>
Espadas<br>
Ouros<br>
Sendo Paus o mais forte e Ouros o mais fraco<br>
Uma das grandes diferênças do jogo original, é que podem existir mais de uma da mesma carta no jogo. Ex:<br>
Pode existir três Q de Espadas<br>
Mas na prática não muda muita coisa, foi apenas uma escolha para diferênciar no jogo.<br>

# Regras
O baralho é embaralhado, é distribuido três cartas para cada e virada uma sobre a mesa. Aquela carta sobre a mesa é a manilha, ela representa a carta mais forte do jogo, mais forte que o 3. Essa é a única carta que sofre pelas regras dos naipes. Ficando algo como:<br>
Ex:<br>
Manilha: 6<br>
4, 5, 7, Q, J, K, A, 2, 3, 6-O, 6-E, 6-C, 6-P<br>
No jogo original a carta virada não representa exatamente a manilha.<br>
Caso a carta sobre a mesa seja um J, a manilha será K, mas no aqui até o momento caso a carta virada seja J, a manilha é J<br>
Na sua vez você pode: Jogar uma carta, pedir truco ou pular fora<br>
Caso você joguê uma carta será a vez do seu adversário, e o objetivo dele será jogar uma carta mais forte do que a sua. Caso consigua ele ganha a rodada. Caso não consiga você ganha.<br>
Caso você peça truco, a partida começa a valer 3, mas seu adversário pode aceitar, aumentar ou pular fora.<br>
Caso ele aceite a partida segue valendo 3.<br>
Caso ele aumente a partida começa a valer 6. e ai você pode responder aceitando, aumentando ou pulando fora. Pode ser aumentado até 12, [1, 3, 6, 9, 12]<br>
Caso ele pule fora o você ganha a quantidade de pontos do último truco. Caso você tenha pedido truco, ele aumentou para 6, você aumentou para 9, caso ele pule fora você ganha 6.<br>
Ganha quem ganhar pelo menos 2. E ganha o Jogo quem fizer 12 pontos primeiro<br>
Cada execução da aplicação é referente a uma rodada.<br>

# Plataformas
O jogo foi desenvolvido no Linux, funcionando normalmente caso instalado em um sistema Linux.<br>
mas caso tente rodar em um sistema Windows, apenas uma pequena coisa deve ser mudada.<br>
em algumas partes da função "play()" da classe "jogo" do arquivo "lib.py" existe a utilização da função "os.system("clear")" e "system("clear")" na função main do arquivo "truco.py" no qual o "clear" deve ser substituido por "cls", assim o jogo funciona normalmente nos sistemas Windows.<br>

# Atualizações
Mais para frente pretendo adicionar mais atualizações para o jogo.<br>
Outra Atualização, como dito no tópico anterior, o jogo foi desenvolvido em Linux, mais para frente pretendo disponibilizar oficialmente a versão para Windows.<br>
Outra atualização é tanto disponilizar em outro Branch a versão "legacy" aonde se joga localmente.<br>
E também em outro Branch uma versão com Bot para jogar sozinho.<br>
Não posso dar data de quando isso vai acontecer, já desenvolvo isso sozinho.<br>
Mas Acho Que Seja Breve ;)<br>

# Issue
Algo que possa irritar alguns é o fato de algumas mensagens principalmente de vitória e pontuação apenas aparece para o Jogador 1, Pretendo em breve corrigir isso<br>

# Extra
Caso você tenha olhado o código fonte, muito provavelmente percebeu que os nomes das variáveis são uma mistrura de português, inglês e "portugles" isso é apenas uma piada com o fato de estar misturando programação e jogo de buteco, assim misturando palavras em inglês e português.<br>
Existe uma "Sujeirinha" de programação escondida no código que é um protótipo da correção do erro de mensagens do tópico anterior. Não quis remover tanto por "Easter Egg", Quanto para ter parte da solução, quanto por preguiça.<br>
