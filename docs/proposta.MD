# Proposta Inicial do Jogo

Este documento deve ser preenchido pelo grupo na Semana 1 do projeto.

A proposta deve apresentar uma ideia simples, clara e viável para ser desenvolvida com Python e Pygame dentro do prazo disponível.

## 1. Nome provisório do jogo

Escreva aqui o nome provisório do jogo.

Exemplo:

> Corrida dos Obstáculos

## 2. Integrantes do grupo

Liste os integrantes do grupo.

- Nome 1: Luiz Otávio Pereira Dos Santos. 
- Nome 2: Iago Paiva Faria
- Nome 3: Gustavo Eugênio Ferreira
- Nome 4:Luanna Rodrigues Campos 

## 3. Tipo de jogo

Jogo de sobrevivência simples por escolhas, no modo *single player*.
## 4. Descrição geral do jogo

O jogo será ambientado em uma cidade tomada por zumbis. O jogador controlará um único sobrevivente que começa sozinho em uma área urbana abandonada e precisa tomar decisões para continuar vivo durante vários dias.

A cada rodada, uma situação será apresentada na tela. Essas situações podem envolver procurar comida, explorar prédios abandonados, fugir de zumbis, descansar, procurar munição ou escolher caminhos pela cidade.

O jogador deverá escolher uma entre três opções disponíveis. Cada escolha terá consequências nos atributos do personagem, como vida, fome, energia, munição e pontuação.


## 5. Objetivo do jogador

O objetivo do jogador é sobreviver na cidade por uma quantidade determinada de dias, administrando seus recursos e evitando morrer para os perigos da cidade.

Inicialmente, o objetivo será sobreviver por *7 dias* até encontrar uma rota segura para sair da cidade.

## 6. Regras principais
- O jogo será single player.
- O jogador controla um único sobrevivente.
- O jogador começa com valores iniciais de vida, fome, energia, munição e pontuação.
- A cada rodada, uma nova situação será apresentada.
- O jogador deverá escolher uma entre três opções.
- Cada escolha altera os atributos do jogador.
- Algumas escolhas podem aumentar a pontuação ou fornecer recursos.
- Escolhas perigosas podem reduzir vida, gastar energia, aumentar fome ou consumir munição.
- O jogador precisa administrar seus recursos para continuar sobrevivendo.
- O jogo avança conforme o jogador sobrevive aos eventos.
- O jogador perde se sua vida chegar a zero.
- O jogador vence se sobreviver até o último dia.

## 7. Condição de vitória

O jogador vence se conseguir sobreviver até o *7º dia* com a vida maior que zero, encontrando uma saída segura da cidade.

## 8. Condição de derrota ou encerramento
O jogador perde se a vida chegar a zero.

Também poderá ocorrer o encerramento da partida caso o jogador complete todos os eventos planejados.

## 9. Elementos previstos no jogo

- Um personagem principal controlado pelo jogador.
- Cidade abandonada como cenário principal.
- Eventos relacionados à sobrevivência urbana.
- Zumbis como ameaça principal.
- Opções de escolha para cada evento.
- Recursos e atributos do jogador:
  - Vida;
  - Fome;
  - Energia;
  - Munição;
  - Pontuação;
  - Dia atual.
- Locais da cidade, como:
  - mercado;
  - hospital;
  - delegacia;
  - rua abandonada;
  - prédio;
  - garagem.
- Tela principal de jogo.
- Tela de vitória.
- Tela de derrota.
- Sistema de recorde.

## Jogador ou elemento principal

- Mouse, clicando nos botões de escolha;
- Ou teclado, usando as teclas 1, 2 e 3 para selecionar uma opção.


## Obstáculos, inimigos ou desafios

O jogo conta com possivés doenças, Zumbis e perca de vida. 

## Itens, alvos ou objetos de interação
Conquistas, Ranks, intens durande a sobrevivencia.


## Pontuação, vidas, tempo ou progresso

A pontução é baseada em pontuação por dia, quanto melhor for a sua escolhar melhor será suapontuação.

## 10. Controles previstos

Escolhas baseadas em botoes ou teclas 1,2,3.

## 11. Organização inicial do código

- *Dicionários*, para armazenar os dados do jogador, como vida, fome, energia, munição, pontuação e dia.
- *Listas*, para armazenar os eventos do jogo.
- *Dicionários dentro de listas*, para representar cada evento e suas opções.
- *Tuplas*, caso sejam utilizadas posições, cores ou tamanhos de elementos na tela.

Exemplo de estrutura prevista para o jogador:
jogador = {
    "vida": 100,
    "fome": 0,
    "energia": 100,
    "municao": 3,
    "pontuacao": 0,
    "dia": 1
}
 eventos = [
    {
        "descricao": "Você encontrou um mercado abandonado. Há barulhos estranhos vindo de dentro.",
        "opcoes": [
            {
                "texto": "Entrar e procurar comida",
                "vida": -10,
                "fome": -20,
                "energia": -10,
                "municao": 0,
                "pontuacao": 15
            },
            {
                "texto": "Ignorar o mercado e continuar andando",
                "vida": 0,
                "fome": 10,
                "energia": -5,
                "municao": 0,
                "pontuacao": 5
            },
            {
                "texto": "Usar munição para afastar os zumbis e vasculhar o local",
                "vida": 0,
                "fome": -15,
                "energia": -5,
                "municao": -1,
                "pontuacao": 20
            }
        ]
    }
]
def aplicar_consequencia(jogador, escolha):
    pass

def verificar_derrota(jogador):
    pass

def verificar_vitoria(jogador):
    pass

def atualizar_recorde(pontuacao, recorde):
    pass

## 12. Recursos externos previstos

- imagens obtidas de banco gratuito;
- sons gratuitos;
- tutorial usado apenas como referência;
- fonte personalizada.

Recursos previstos:

> Escreva aqui.

Fontes de imagens 

.

## 13. Principais dificuldades esperadas

Dificuldades previstas:

- Dificuldade 1: Colocar pesos entre encolhas
- Dificuldade 2: A animação mudando a cada dia. 
- Dificuldade 3: Como vai funcionar os, atributos de fome e pontuação por escolhas.

## 14. Escopo mínimo para a entrega final

Para a entrega final, o jogo deverá possuir no mínimo:

Uma tela principal feita em Pygame.
Modo single player.
Um personagem principal representando o sobrevivente.
Sistema de escolhas com pelo menos 3 opções por evento.
Pelo menos 7 eventos, representando os 7 dias de sobrevivência.
Tema de cidade tomada por zumbis.
Atributos básicos do jogador:
vida;
fome;
energia;
munição;
pontuação;
dia atual.
Exibição na tela das informações principais do jogador.
Condição de vitória ao sobreviver até o 7º dia.
Condição de derrota quando a vida chegar a zero.
Uso de listas e dicionários para armazenar jogador, eventos e opções.
Salvamento do maior recorde em um arquivo, como recorde.txt.
Código organizado em funções.
Arquivo README.md explicando o jogo e como executar.
Testes simples para funções de lógica, como aplicação de consequências, vitória, derrota e atualização de recorde.

## 15. Possíveis melhorias, caso haja tempo


Melhorias possíveis:

- Melhoria 1: Adicionar uma quantidade de opções para adicionar mais vertentes. 
- Melhoria 2: Mudança de Skyn 
- Melhoria 3: Trilha Sonora específicas. 
