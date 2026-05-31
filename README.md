# Nome do Jogo

Projeto final da disciplina de Introdução a Algoritmos/Programação, desenvolvido com Python e Pygame.

Este repositório é um template para os grupos da disciplina. A proposta é começar com uma base funcional e evoluir o jogo ao longo do semestre.

## Integrantes do grupo

- Nome do integrante 1
- Nome do integrante 2
- Nome do integrante 3
- Nome do integrante 4

## Estrutura do projeto

- `main.py`: ponto de entrada da aplicação.
- `src/`: código-fonte principal do jogo (loop, regras, sprites e dados).
- `assets/`: imagens, fontes e sons.
- `data/`: arquivos persistentes (recorde/ranking).
- `tests/`: testes unitários com `pytest`.
- `docs/`: documentação do projeto, incluindo proposta inicial.

## Descrição do jogo

O jogo consiste em controlar um sobrevivente em uma cidade tomada por zumbis. O jogador começa sozinho em uma área urbana abandonada e precisa tomar decisões para continuar vivo. A cada rodada, uma situação será apresentada, como procurar comida, explorar locais abandonados, fugir de zumbis ou descansar. Cada escolha altera atributos como vida, fome, energia, munição e pontuação.


## Objetivo do jogador

O objetivo do jogador é sobreviver por 7 dias na cidade, administrando seus recursos e evitando situações perigosas. Para vencer, o jogador precisa chegar ao final do 7º dia com a vida maior que zero, encontrando uma rota segura para sair da cidade.

## Regras do jogo

Liste as principais regras do jogo.

- O jogo será no modo single player.
- O jogador controla um único sobrevivente.
- A cada rodada, uma situação será apresentada na tela.
- O jogador deverá escolher uma entre três opções disponíveis.
- Cada escolha pode alterar vida, fome, energia, munição e pontuação.
- Escolhas boas podem aumentar a pontuação ou recuperar recursos.
- Escolhas ruins podem reduzir vida, aumentar fome, gastar energia ou consumir munição.
- A vida não pode chegar a zero.
- O jogador vence se sobreviver até o 7º dia.
- O jogador perde se a vida chegar a zero antes do final.

## Controles

Informe as teclas ou comandos utilizados no jogo.

- Mouse: clicar nos botões de escolha.
- Tecla 1: selecionar a primeira opção.
- Tecla 2: selecionar a segunda opção.
- Tecla 3: selecionar a terceira opção.
- ESC: sair do jogo.

## Como executar o projeto

### 1. Clonar o repositório

```bash
git clone LINK_DO_REPOSITORIO
cd NOME_DA_PASTA
pip install -r requirements.txt
python main.py
```

## Como executar os testes

```bash
python -m pytest
```

## Checklist mínimo para entrega

- Preencher este README com nome final, descrição real, regras e controles do jogo.
- Atualizar `docs/proposta.MD` com a proposta do grupo.
- Garantir que o jogo executa com `python main.py`.
- Garantir que os testes passam com `pytest`.

## Observações para os alunos

- Mantenham o código organizado em módulos pequenos e com responsabilidade clara.
- Comentem partes importantes da lógica, principalmente regras do jogo.
- Registrem decisões técnicas no README do grupo ao longo do desenvolvimento.
