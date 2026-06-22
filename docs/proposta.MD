# Proposta Inicial do Jogo

Este documento apresenta a proposta inicial do jogo **Seven Days of Fear**, desenvolvido como projeto final da disciplina de Introdução a Algoritmos/Programação.

A proposta foi organizada para orientar o desenvolvimento do jogo e registrar os principais elementos planejados: tema, objetivo, regras, controles, recursos, estrutura do código, formas de pontuação, ranking, testes e critérios mínimos para a entrega final.

---

## 1. Nome do jogo

**Seven Days of Fear**

Nome provisório utilizado no início do projeto: **Day 7 Survival**.

---

## 2. Integrantes do grupo

- Luiz Otávio Pereira dos Santos
- Iago Paiva Faria
- Gustavo Eugênio Ferreira
- Luanna Rodrigues Campos

---

## 3. Tipo de jogo

Jogo narrativo de sobrevivência por escolhas, no modo **single player**, desenvolvido em **Python** com uso da biblioteca **Pygame**.

---

## 4. Descrição geral do jogo

**Seven Days of Fear** é ambientado em uma cidade tomada por um apocalipse zumbi. O jogador controla um sobrevivente que acorda sozinho em um apartamento enquanto a cidade entra em colapso.

A partir da primeira cena, o jogador precisa tomar decisões para sobreviver durante 7 dias. Cada escolha pode mudar o rumo da história, alterar os status do personagem, adicionar itens ao inventário, aumentar a pontuação, abrir novos caminhos ou causar uma derrota imediata.

As situações do jogo envolvem fugir de infectados, procurar comida e água, explorar locais abandonados, ajudar ou abandonar sobreviventes, enfrentar saqueadores, encontrar rotas de evacuação e tentar alcançar um final de sobrevivência.

O jogo possui múltiplos caminhos narrativos, finais de derrota e finais de vitória. As escolhas feitas pelo jogador influenciam diretamente o progresso, a pontuação e o resultado final da partida.

---

## 5. Objetivo do jogador

O objetivo principal é **sobreviver até o Dia 7** e alcançar um dos finais de vitória disponíveis.

Para vencer, o jogador precisa:

- administrar recursos limitados;
- manter a vida acima de zero;
- tomar decisões estratégicas;
- evitar escolhas fatais;
- coletar itens importantes;
- lidar com outros sobreviventes;
- chegar a uma rota segura de sobrevivência.

Além de sobreviver, o jogador também pode tentar alcançar a maior pontuação possível.

---

## 6. Regras principais

- O jogo é single player.
- O jogador controla um único sobrevivente.
- O jogador informa o nome no início da partida.
- A história é dividida em 7 dias.
- Cada cena apresenta uma situação narrativa.
- Algumas cenas possuem opções de escolha.
- O jogador pode escolher usando o mouse ou as teclas numéricas.
- Algumas cenas avançam com Enter ou Espaço.
- Cada escolha pode alterar os status do jogador.
- Algumas escolhas adicionam itens ao inventário.
- Algumas escolhas podem exigir itens específicos.
- Escolhas boas ou estratégicas aumentam a pontuação.
- Escolhas médias permitem o progresso, mas podem gastar recursos.
- Escolhas ruins podem causar perda de recursos, perda de vida ou derrota imediata.
- A pontuação aumenta conforme o jogador visita cenas, faz escolhas e conclui dias.
- O ranking é salvo automaticamente ao final da partida.
- O jogador perde se chegar a uma cena de morte ou se a vida chegar a zero.
- O jogador vence se alcançar um dos finais positivos no Dia 7.

---

## 7. Condições de vitória

O jogador vence ao chegar ao Dia 7 e concluir uma rota positiva de sobrevivência.

Os finais de vitória podem envolver:

- alcançar uma zona segura;
- passar por uma triagem militar;
- chegar a um ponto de evacuação;
- escapar com um grupo de sobreviventes;
- sobreviver por uma rota alternativa.

---

## 8. Condições de derrota ou encerramento

O jogador perde se:

- escolher uma opção fatal;
- ficar sem vida;
- ser cercado por infectados;
- cair em armadilhas;
- ser morto por saqueadores;
- provocar barulho em locais perigosos;
- entrar em situações sem os recursos necessários.

A partida também é encerrada quando o jogador alcança qualquer final, seja de vitória ou derrota.

---

## 9. Elementos do jogo

### Personagem principal

O jogador controla um sobrevivente cujo nome pode ser informado na tela inicial.

### Cenário principal

O jogo se passa em uma cidade urbana durante um apocalipse zumbi.

### Ameaças e desafios

- Infectados.
- Hordas.
- Falta de comida e água.
- Cansaço.
- Ferimentos.
- Decisões perigosas.
- Saqueadores.
- Sobreviventes desesperados.
- Ambientes instáveis, como prédios, garagens, terminais, escolas, rodovias, pontes e bases militares.

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

- mochila;
- canivete;
- faca de caça;
- barra de ferro;
- rádio;
- lanterna;
- corda;
- kit médico;
- pé de cabra;
- combustível;
- ferramentas;
- peça de veículo;
- pistola;
- munição;
- alimentos;
- água;
- aliados.

Alguns itens podem desbloquear escolhas futuras ou representar vantagens narrativas durante a sobrevivência.

---

## 10. Locais previstos

O jogo possui cenas ambientadas em diferentes locais, como:

- apartamento;
- corredor do prédio;
- escada de emergência;
- beco;
- rua principal;
- garagem;
- loja;
- terminal de ônibus;
- escola;
- posto de gasolina;
- rodovia;
- ponte;
- fazenda;
- estacionamento;
- base militar;
- estádio;
- pontos de evacuação.

---

## 11. Telas previstas

- Tela inicial para inserir o nome do jogador.
- Tela principal com cena, imagem, texto, opções e status.
- Tela de consequência após escolhas.
- Tela de fim de dia.
- Tela de vitória.
- Tela de derrota.
- Tela de ranking.

---

## 12. Controles previstos

- **Mouse**: clicar nos botões de escolha.
- **Teclas 1 a 4**: selecionar uma opção.
- **Enter**: continuar cenas sem escolha.
- **Espaço**: continuar cenas sem escolha.
- **F1**: abrir ou fechar o ranking.
- **Backspace**: apagar o nome na tela inicial ou voltar da tela de ranking.
- **R**: reiniciar após uma vitória ou derrota.
- **ESC**: sair do jogo.

---

## 13. Organização do código

O projeto utiliza estruturas de dados e funções para organizar a lógica do jogo.

### Estruturas utilizadas

- Dicionários para representar cenas, opções, efeitos e status do jogador.
- Listas para armazenar opções e itens coletados.
- Conjuntos para registrar dias concluídos e cenas pontuadas.
- Funções para organizar regras, efeitos, pontuação, ranking, desenho da tela e fluxo do jogo.
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
    "titulo": "DIA 1 - CENA DE EXEMPLO",
    "texto": "Descrição da situação apresentada ao jogador.",
    "opcoes": [
        {
            "texto": "Escolha do jogador",
            "resultado": "Consequência da escolha.",
            "proxima": "proxima_cena",
            "efeitos": {"energia": -5, "moral": 2},
            "itens_add": ["item exemplo"],
        }
    ],
}
```

### Funções previstas/implementadas

- Aplicar consequências das escolhas.
- Atualizar status do jogador.
- Controlar pontuação.
- Verificar vitória e derrota.
- Registrar dias concluídos.
- Salvar pontuação final.
- Ler ranking salvo.
- Desenhar cenas, botões, textos, imagens e status.
- Carregar imagens das cenas.
- Controlar entrada por mouse e teclado.

---

## 14. Persistência de dados

O jogo utiliza arquivo de texto para registrar o ranking dos jogadores.

Arquivo utilizado:

```text
ranking.txt
```

As informações salvas incluem:

- nome do jogador;
- pontuação final;
- dias concluídos;
- resultado da partida;
- final alcançado.

---

## 15. Recursos externos e assets

O projeto utiliza uma pasta de assets para armazenar imagens das cenas.

Pasta principal:

```text
assets/imagens/
```

As imagens podem ser produzidas pelo próprio grupo, geradas especificamente para o projeto ou obtidas de fontes externas gratuitas, desde que respeitem os direitos de uso.

Caso sejam utilizados recursos externos, como imagens, sons ou fontes de terceiros, suas referências devem ser registradas na documentação do projeto.

---

## 16. Testes previstos

Os testes automatizados foram planejados para validar partes importantes da lógica do jogo sem abrir a janela do Pygame.

Os testes verificam pontos como:

- limites dos status;
- pontuação das escolhas;
- existência dos 7 dias;
- existência de finais de vitória e derrota;
- funcionamento de requisitos por item;
- leitura e ordenação do ranking.

---

## 17. Principais dificuldades esperadas

Dificuldades previstas durante o desenvolvimento:

- Criar uma narrativa coerente durante 7 dias.
- Organizar muitas cenas sem deixar o código confuso.
- Equilibrar consequências entre escolhas boas, médias e ruins.
- Controlar status como vida, energia, comida, água, moral, confiança e munição.
- Implementar ranking com leitura e escrita em arquivo.
- Criar testes simples sem abrir a janela do Pygame.
- Integrar imagens às cenas do jogo.
- Preparar a documentação final para entrega.

---

## 18. Escopo mínimo para a entrega final

Para a entrega final, o jogo deverá possuir:

- janela principal feita em Pygame;
- modo single player;
- sistema de escolhas;
- história com 7 dias de sobrevivência;
- tema de cidade tomada por zumbis;
- atributos principais do jogador;
- exibição dos status na tela;
- pontuação;
- itens coletáveis;
- condição de vitória;
- condição de derrota;
- uso de listas, dicionários e conjuntos;
- leitura e escrita de dados em arquivo;
- ranking ou registro de pontuação;
- código organizado em funções;
- README explicando o jogo e como executar;
- testes automatizados;
- referências para assets externos utilizados.

---

## 19. Resultado esperado da versão final

A versão final do projeto deve permitir que o jogador execute o jogo, informe seu nome, acompanhe a narrativa, tome decisões, veja seus status, colete itens, avance pelos dias, chegue a finais de vitória ou derrota e tenha sua pontuação registrada no ranking.

O projeto também deve conter documentação suficiente para explicar a proposta, a organização dos arquivos, a execução do jogo, a execução dos testes e os recursos utilizados.

---

## 20. Possíveis melhorias futuras

Melhorias possíveis após a entrega final:

- Adicionar mais imagens para cenas específicas.
- Adicionar trilha sonora e efeitos sonoros.
- Criar animações simples.
- Expandir rotas e finais.
- Melhorar a tela de ranking.
- Criar sistema de dificuldade.
- Adicionar mais itens com efeitos específicos.
- Aumentar a modularização do código.
- Ampliar a cobertura dos testes automatizados.
