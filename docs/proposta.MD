# Proposta Inicial do Jogo

Este documento apresenta a proposta inicial do jogo desenvolvido pelo grupo para a disciplina de Introdução a Algoritmos/Programação.

A ideia do projeto é criar um jogo simples, claro e viável utilizando Python e Pygame, aplicando conceitos como estruturas condicionais, funções, listas, dicionários, leitura e escrita de arquivos, pontuação e testes.

## 1. Nome do jogo

**Seven Days of Fear**

Nome provisório inicial: **Dy 7 Survival**

## 2. Integrantes do grupo

- Luiz Otávio Pereira Dos Santos
- Iago Paiva Faria
- Gustavo Eugênio Ferreira
- Luanna Rodrigues Campos

## 3. Tipo de jogo

Jogo narrativo de sobrevivência por escolhas, no modo single player.

## 4. Descrição geral do jogo

O jogo é ambientado em uma cidade tomada por zumbis. O jogador controla um sobrevivente que começa sozinho em uma área urbana abandonada e precisa tomar decisões para continuar vivo durante 7 dias.

A cada cena, uma situação é apresentada na tela. Essas situações podem envolver procurar comida, explorar locais abandonados, fugir de zumbis, descansar, buscar munição, encontrar aliados ou escolher caminhos pela cidade.

O jogador deve escolher entre as opções disponíveis. Cada escolha gera consequências nos atributos do personagem, como vida, energia, comida, água, moral, confiança, munição, itens e pontuação.

O jogo possui múltiplos caminhos narrativos, finais de vitória e finais de derrota. As escolhas feitas pelo jogador influenciam diretamente o progresso e o resultado da partida.

## 5. Objetivo do jogador

O objetivo do jogador é sobreviver durante 7 dias em uma cidade dominada por zumbis, administrando seus recursos e evitando situações perigosas.

Para vencer, o jogador precisa chegar ao final do 7º dia e escolher uma rota de sobrevivência possível, como evacuação, cura, salvamento de sobreviventes ou fuga por uma rota alternativa.

## 6. Regras principais

- O jogo é single player.
- O jogador controla um único sobrevivente.
- O jogador começa com valores iniciais de vida, energia, comida, água, moral, confiança, munição e pontuação.
- A cada cena, uma situação é apresentada.
- O jogador escolhe uma opção usando o mouse ou o teclado.
- Algumas cenas possuem até 4 opções.
- Cada escolha pode alterar os atributos do jogador.
- Algumas escolhas adicionam itens ao inventário.
- Algumas escolhas exigem itens específicos para serem usadas.
- Escolhas boas aumentam a pontuação ou melhoram a situação do jogador.
- Escolhas médias permitem progresso, mas podem gastar recursos.
- Escolhas ruins podem causar perda de vida, recursos ou derrota imediata.
- A pontuação aumenta conforme o jogador faz escolhas e conclui dias.
- O jogo avança conforme o jogador sobrevive aos eventos.
- O jogador perde se chegar a uma cena de morte ou se a vida chegar a zero.
- O jogador vence se alcançar um dos finais de vitória no 7º dia.
- Ao final da partida, a pontuação é salva em arquivo.

## 7. Condição de vitória

O jogador vence se chegar ao 7º dia e concluir um dos finais positivos disponíveis.

Os finais de vitória incluem possibilidades como:

- Entrar no navio de evacuação.
- Entregar o Soro Sete aos cientistas.
- Salvar sobreviventes fora do portão.
- Usar uma rota subterrânea para escapar da cidade.

## 8. Condição de derrota ou encerramento

O jogador perde se:

- Escolher uma opção fatal.
- Ficar sem vida.
- Ser cercado por zumbis.
- Cair em armadilhas.
- Tomar decisões que levem a finais de morte.

A partida também é encerrada quando o jogador alcança qualquer final, seja de vitória ou derrota.

## 9. Elementos previstos no jogo

### Personagem principal

O jogador controla um sobrevivente chamado Rafael. O nome do personagem pode ser personalizado na tela inicial.

### Cenário principal

O jogo se passa em uma cidade abandonada durante um apocalipse zumbi.

### Ameaças e desafios

- Zumbis.
- Hordas.
- Falta de recursos.
- Ferimentos.
- Escolhas perigosas.
- Sobreviventes hostis.
- Ambientes arriscados, como hospital, delegacia, metrô, túneis e ponte quebrada.

### Recursos e atributos do jogador

- Vida.
- Energia.
- Comida.
- Água.
- Moral.
- Confiança.
- Munição.
- Pontuação.
- Dias concluídos.
- Itens coletados.

### Itens e interações

O jogador pode encontrar itens durante a história, como:

- Faca.
- Mochila.
- Rádio.
- Pé de cabra.
- Mapa.
- Curativos.
- Antibióticos.
- Arma de fogo.
- Munição.
- Soro Sete.
- Sinalizadores.
- Rota subterrânea.

Alguns itens desbloqueiam escolhas específicas em cenas futuras.

### Locais da cidade

O jogo possui vários locais, como:

- Apartamento.
- Telhado.
- Garagem.
- Mercado.
- Escola.
- Farmácia.
- Becos.
- Torre de rádio.
- Shopping.
- Delegacia.
- Laboratório.
- Metrô.
- Ponte.
- Bairro militar.
- Túneis.
- Porto.

### Telas previstas

- Tela inicial para inserir nome do jogador.
- Tela principal com cena, imagem, texto, opções e status.
- Tela de consequência após escolhas.
- Tela de fim de dia.
- Tela de vitória.
- Tela de derrota.
- Tela de ranking.

## 10. Controles previstos

- Mouse: clicar nos botões de escolha.
- Teclas 1 a 4: selecionar uma opção.
- Enter ou Espaço: continuar em cenas sem escolhas.
- F1: abrir o ranking.
- R: reiniciar após derrota.
- ESC: sair do jogo.

## 11. Organização inicial do código

O projeto utiliza estruturas de dados como dicionários, listas e conjuntos.

### Estruturas utilizadas

- Dicionários para representar cenas, opções, efeitos e status do jogador.
- Listas para armazenar opções e itens coletados.
- Conjuntos para registrar dias concluídos.
- Funções para organizar regras, efeitos, pontuação, ranking, desenho da tela e controle do fluxo do jogo.
- Arquivo `.txt` para salvar pontuações.

### Exemplo de estrutura do jogador

```python
estado_inicial = {
    "vida": 100,
    "energia": 100,
    "comida": 3,
    "agua": 3,
    "moral": 50,
    "confianca": 0,
    "municao": 0,
}
```

### Exemplo de estrutura de cena

```python
"exemplo_cena": {
    "dia": 1,
    "titulo": "Cena de exemplo",
    "texto": "Descrição da situação apresentada ao jogador.",
    "opcoes": [
        {
            "texto": "Escolha do jogador",
            "resultado": "Consequência da escolha.",
            "proxima": "proxima_cena",
            "efeitos": {"energia": -5, "moral": 2},
            "itens_add": ["item exemplo"]
        }
    ]
}
```

### Funções previstas

- Aplicar consequências das escolhas.
- Atualizar status do jogador.
- Controlar pontuação.
- Verificar vitória e derrota.
- Registrar dias concluídos.
- Salvar pontuação final.
- Ler ranking salvo.
- Desenhar cenas, botões, textos, imagens e status.

## 12. Recursos externos previstos

Recursos previstos:

- Imagens para representar as cenas do jogo.
- Pasta `assets` para armazenar imagens.
- Possíveis sons ou trilha sonora em versões futuras.
- Fonte padrão do sistema ou fonte personalizada futuramente.
- Arquivo `pontuacoes.txt` para salvar o ranking.

### Fontes de imagens

As imagens podem ser criadas ou obtidas de bancos gratuitos, respeitando os direitos de uso.

## 13. Principais dificuldades esperadas

Dificuldades previstas:

- Criar pesos e consequências equilibradas entre as escolhas.
- Fazer a narrativa avançar de forma coerente durante os 7 dias.
- Controlar atributos como vida, energia, comida, água, moral, confiança e munição.
- Organizar muitas cenas sem deixar o código confuso.
- Implementar ranking com leitura e escrita em arquivo.
- Criar testes simples sem abrir a janela do Pygame.
- Adicionar imagens para todas as cenas do jogo.

## 14. Escopo mínimo para a entrega final

Para a entrega final, o jogo deverá possuir no mínimo:

- Janela principal feita em Pygame.
- Modo single player.
- Sistema de escolhas.
- História com 7 dias de sobrevivência.
- Tema de cidade tomada por zumbis.
- Atributos principais do jogador.
- Exibição dos status na tela.
- Pontuação.
- Itens coletáveis.
- Condição de vitória.
- Condição de derrota.
- Uso de listas e dicionários.
- Leitura ou escrita de dados em arquivo.
- Ranking ou registro de pontuação.
- Código organizado em funções.
- README explicando o jogo e como executar.
- Primeira versão dos testes.

## 15. Possíveis melhorias, caso haja tempo

Melhorias possíveis:

- Adicionar mais imagens para as cenas.
- Adicionar trilha sonora e efeitos sonoros.
- Criar animações simples.
- Expandir a quantidade de escolhas e finais.
- Melhorar a tela de ranking.
- Criar sistema de dificuldade.
- Adicionar mais itens com efeitos específicos.
- Melhorar a modularização do código em arquivos separados.
- Adicionar mais testes para as regras do jogo.
