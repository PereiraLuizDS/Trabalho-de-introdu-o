# Seven Days of Fear

Projeto final da disciplina de Introdução a Algoritmos/Programação, desenvolvido com **Python** e **Pygame**.

Seven Days of Fear é um jogo narrativo de sobrevivência em um apocalipse zumbi. O jogador assume o papel de um sobrevivente e precisa tomar decisões durante 7 dias, administrando recursos, evitando riscos e buscando uma forma de escapar da cidade.

## Integrantes do grupo

- Luiz Otávio Pereira Dos Santos
- Iago Paiva Faria
- Gustavo Eugênio Ferreira
- Luanna Rodrigues Campos

## Estrutura do projeto

- `main.py`: arquivo principal do jogo. É por ele que o jogo deve ser executado.
- `assets/`: pasta usada para guardar as imagens das cenas do jogo.
- `pontuacoes.txt`: arquivo onde são salvas as pontuações/ranking dos jogadores.
- `README.md`: documentação do projeto.
- `requirements.txt`: lista de dependências necessárias para executar o jogo.
- `test_jogo_semana3.py`: primeira versão dos testes automatizados do projeto.

## Descrição do jogo

**Seven Days of Fear** é um jogo narrativo em que o jogador acompanha a jornada de um sobrevivente em uma cidade tomada por zumbis.

A cada cena, o jogador recebe uma situação e precisa escolher uma ação. Cada escolha pode levar a uma nova cena, alterar os status do personagem, adicionar itens ao inventário, aumentar a pontuação ou causar uma derrota imediata.

Durante a jornada, o jogador pode encontrar aliados, coletar recursos, descobrir informações sobre a origem da infecção e escolher diferentes caminhos até chegar ao 7º dia. No final, existem diferentes possibilidades de vitória, dependendo das escolhas feitas e dos itens encontrados.

## Objetivo do jogador

O objetivo principal é **sobreviver por 7 dias** e chegar a um dos finais de vitória.

Para isso, o jogador precisa:

- tomar decisões estratégicas;
- manter a vida acima de zero;
- administrar recursos como comida, água, energia e munição;
- coletar itens importantes;
- evitar escolhas perigosas;
- tentar chegar ao final da história com a maior pontuação possível.

## Regras do jogo

- O jogo é single player.
- O jogador controla um único personagem sobrevivente.
- A história é dividida em 7 dias.
- Cada cena pode apresentar uma ou mais opções de escolha.
- O jogador pode selecionar escolhas com o mouse ou com as teclas numéricas.
- Cada escolha pode alterar os status do personagem.
- Algumas escolhas podem adicionar itens ao inventário.
- Algumas escolhas exigem itens específicos para serem liberadas.
- Escolhas boas aumentam a pontuação.
- Escolhas médias também pontuam, mas normalmente trazem menos vantagens.
- Escolhas ruins podem causar perda de recursos, perda de vida ou derrota.
- Ao concluir um dia, o jogador recebe pontos extras.
- O jogo termina quando o jogador chega a um final de vitória ou derrota.
- A pontuação final é salva automaticamente no arquivo `pontuacoes.txt`.

## Sistemas implementados

### Status do jogador

O jogo possui os seguintes status:

- **Vida**: representa a condição física do personagem.
- **Energia**: representa o cansaço do personagem.
- **Comida**: representa os alimentos disponíveis.
- **Água**: representa a quantidade de água disponível.
- **Moral**: representa o estado emocional do personagem.
- **Confiança**: representa o nível de confiança conquistado com outros sobreviventes.
- **Munição**: representa a quantidade de tiros disponíveis.

### Inventário

O jogador pode receber itens durante a história, como:

- faca;
- mochila;
- rádio;
- pé de cabra;
- aliados;
- arma de fogo;
- munição;
- soro sete;
- sinalizadores;
- rota subterrânea.

Alguns itens desbloqueiam escolhas futuras. Por exemplo, determinadas ações só podem ser feitas se o jogador tiver o item necessário.

### Pontuação

O sistema de pontuação funciona da seguinte forma:

- escolhas boas valem 75 pontos;
- escolhas médias valem 50 pontos;
- escolhas que levam à morte valem 0 pontos;
- cada dia concluído adiciona 100 pontos.

### Ranking

Ao vencer ou perder, o jogo salva automaticamente os dados da partida no arquivo `pontuacoes.txt`.

As informações salvas incluem:

- nome do jogador;
- pontuação final;
- quantidade de dias concluídos;
- resultado da partida;
- nome do final alcançado.

O ranking pode ser acessado dentro do jogo pela tecla **F1**.

## Condições de vitória e derrota

### Vitória

O jogador vence ao chegar ao 7º dia e escolher um dos finais de vitória disponíveis.

Existem diferentes finais de vitória, como:

- entrar no navio de evacuação;
- entregar o Soro Sete aos cientistas;
- salvar sobreviventes fora do portão;
- usar a rota subterrânea para começar de novo.

### Derrota

O jogador perde quando toma uma decisão fatal ou quando a vida chega a zero.

Existem várias situações de derrota ao longo da história, como ataques de zumbis, decisões arriscadas, armadilhas, barulhos que atraem hordas e escolhas sem os recursos necessários.

## Controles

- **Mouse**: clicar nos botões de escolha.
- **Teclas 1 a 4**: selecionar opções de escolha.
- **Enter**: continuar cenas sem escolha.
- **Espaço**: continuar cenas sem escolha.
- **F1**: abrir ou fechar o ranking.
- **Backspace**: voltar da tela de ranking ou apagar o nome na tela inicial.
- **R**: reiniciar após uma derrota.
- **ESC**: sair do jogo.

## Como executar o projeto

### 1. Instalar as dependências

No terminal, dentro da pasta do projeto, execute:

```bash
pip install -r requirements.txt
```

### 2. Executar o jogo

Depois, execute:

```bash
python main.py
```

## Como executar os testes

O projeto possui uma primeira versão de testes automatizados usando `pytest`.

Para executar os testes, use:

```bash
python -m pytest test_jogo_semana3.py
```

Os testes verificam partes importantes do jogo, como:

- limites dos status;
- pontuação das escolhas;
- existência dos 7 dias;
- existência de finais de vitória e derrota;
- bloqueio de escolhas por item necessário;
- leitura e ordenação do ranking.

## Como adicionar imagens

As imagens devem ser colocadas na pasta `assets`.

O jogo procura automaticamente uma imagem com o mesmo nome da chave da cena. Por exemplo:

```text
d1_apartamento -> assets/d1_apartamento.png
```

Também é possível indicar manualmente uma imagem dentro do dicionário da cena usando o campo `imagem`.

Caso a imagem não exista, o jogo mostra um espaço reservado na tela informando o caminho esperado do arquivo.

## Checklist da Semana 3

- Janela do Pygame funcionando.
- Loop principal implementado.
- Sistema de escolhas por mouse e teclado.
- História dividida em 7 dias.
- Sistema de vida, energia, comida, água, moral, confiança e munição.
- Sistema de pontuação.
- Sistema de progresso por dias.
- Condições de vitória e derrota.
- Uso de estruturas de dados, como dicionários, listas e conjuntos.
- Escrita de dados em arquivo com `pontuacoes.txt`.
- Leitura do arquivo de pontuações para exibir ranking.
- Primeira versão dos testes com `pytest`.
- README atualizado com informações do jogo.

## Observações finais

Este projeto foi desenvolvido como uma versão quase completa do jogo para a entrega da Semana 3. A estrutura atual já permite jogar do início ao fim, salvar pontuações, visualizar ranking, testar regras principais e expandir o jogo com novas imagens, cenas e melhorias futuras.
