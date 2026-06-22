# Seven Days of Fear

Projeto final da disciplina de Introdução a Algoritmos/Programação, desenvolvido com **Python** e **Pygame**.

**Seven Days of Fear** é um jogo narrativo de sobrevivência ambientado em uma cidade tomada por um apocalipse zumbi. O jogador assume o papel de um sobrevivente e precisa tomar decisões ao longo de **7 dias**, administrando recursos, coletando itens, enfrentando riscos e buscando uma forma de chegar até uma zona segura.

---

## Integrantes do grupo

- Luiz Otávio Pereira dos Santos
- Iago Paiva Faria
- Gustavo Eugênio Ferreira
- Luanna Rodrigues Campos

---

## Descrição do jogo

**Seven Days of Fear** é um jogo de escolhas em que cada decisão altera o rumo da história.

O jogador acorda sozinho em um apartamento durante o início de um colapso urbano. A partir desse momento, precisa escolher como agir para sobreviver: fugir, ajudar outros moradores, procurar suprimentos, enfrentar ameaças, confiar em desconhecidos ou seguir sozinho.

A história é dividida em **7 dias**, com diferentes rotas, cenas, escolhas, finais de derrota e finais de vitória. Cada escolha pode alterar os status do personagem, adicionar itens ao inventário, aumentar a pontuação, liberar novas possibilidades ou levar a uma morte imediata.

---

## Objetivo do jogador

O objetivo principal é **sobreviver até o Dia 7** e alcançar um dos finais de vitória.

Para isso, o jogador precisa:

- tomar decisões estratégicas;
- manter a vida acima de zero;
- administrar recursos como comida, água, energia e munição;
- coletar itens importantes;
- evitar escolhas perigosas;
- chegar ao fim da história com a maior pontuação possível;
- salvar ou abandonar personagens conforme as consequências das escolhas.

---

## Regras do jogo

- O jogo é single player.
- O jogador controla um único personagem sobrevivente.
- A história é dividida em 7 dias.
- Cada cena apresenta uma situação narrativa.
- Algumas cenas possuem opções de escolha.
- O jogador pode selecionar escolhas com o mouse ou com as teclas numéricas.
- Algumas escolhas alteram os status do personagem.
- Algumas escolhas adicionam itens ao inventário.
- Algumas escolhas podem exigir itens específicos.
- Escolhas seguras ou estratégicas aumentam a pontuação.
- Escolhas arriscadas podem causar perda de recursos, perda de vida ou derrota.
- Ao concluir um dia, o jogador recebe pontos extras.
- O jogo termina ao alcançar um final de vitória ou um final de derrota.
- A pontuação final é salva automaticamente no arquivo de ranking.

---

## Sistemas implementados

### Status do jogador

O jogo possui os seguintes status:

- **Vida**: representa a condição física do personagem.
- **Energia**: representa o cansaço do personagem.
- **Comida**: representa os alimentos disponíveis.
- **Água**: representa a quantidade de água disponível.
- **Moral**: representa o estado emocional do personagem.
- **Confiança**: representa a relação do personagem com outros sobreviventes.
- **Munição**: representa a quantidade de tiros disponíveis.

---

### Inventário

Durante a história, o jogador pode receber itens importantes, como:

- mochila;
- canivete;
- faca de caça;
- barra de ferro;
- pé de cabra;
- rádio;
- lanterna;
- corda;
- kit médico;
- combustível;
- ferramentas;
- peça do ônibus;
- pistola;
- munição;
- alimentos;
- água;
- aliados.

Alguns itens podem desbloquear ações futuras ou representar vantagens narrativas durante a sobrevivência.

---

### Sistema de escolhas

As escolhas são o principal elemento de interação do jogo.

Cada opção pode:

- levar para uma nova cena;
- causar derrota imediata;
- alterar status do personagem;
- adicionar itens ao inventário;
- modificar a pontuação;
- influenciar o caminho da história;
- levar a diferentes finais.

---

### Pontuação

O jogo possui um sistema de pontuação para avaliar o desempenho do jogador.

A pontuação pode ser alterada por:

- cenas visitadas;
- escolhas boas;
- escolhas médias;
- conclusão de dias;
- finais alcançados;
- decisões que mantêm o personagem vivo por mais tempo.

O objetivo não é apenas sobreviver, mas também tentar alcançar a melhor pontuação possível.

---

### Ranking

O jogo possui um sistema de ranking salvo em arquivo.

Ao vencer ou perder, a partida é registrada automaticamente no arquivo:

```text
pontuacoes.txt
```

As informações salvas incluem:

- nome do jogador;
- pontuação final;
- quantidade de dias concluídos;
- resultado da partida;
- final alcançado.

O ranking pode ser acessado dentro do jogo pela tecla **F1**.

---

## Condições de vitória e derrota

### Vitória

O jogador vence ao chegar ao Dia 7 e alcançar um dos finais de sobrevivência.

Os finais de vitória variam de acordo com a rota escolhida e com as decisões tomadas ao longo da história. O jogador pode terminar a jornada chegando a locais de evacuação, entrando em zonas seguras ou sobrevivendo por meio de diferentes estratégias.

---

### Derrota

O jogador perde quando:

- toma uma decisão fatal;
- entra em uma situação sem preparo;
- é atacado por infectados;
- cai em armadilhas;
- é morto por saqueadores;
- provoca barulho em momentos perigosos;
- fica sem condições de sobreviver;
- a vida chega a zero.

Existem várias mortes possíveis durante os 7 dias de história.

---

## Controles

- **Mouse**: clicar nos botões de escolha.
- **Teclas 1 a 4**: selecionar opções de escolha.
- **Enter**: continuar cenas sem escolha.
- **Espaço**: continuar cenas sem escolha.
- **F1**: abrir ou fechar o ranking.
- **Backspace**: voltar da tela de ranking ou apagar o nome na tela inicial.
- **R**: reiniciar após uma vitória ou derrota.
- **ESC**: sair do jogo.

---

## Estrutura do projeto

```text
Seven-Days-of-Fear/
│
├── main.py
├── requirements.txt
├── pontuacoes.txt
├── README.md
│
├── assets/
│   └── imagens/
│
├── docs/
│   └── proposta.md
│
└── test_jogo_semana3.py
```

---

## Arquivos principais

- `main.py`: arquivo principal do jogo. É por ele que o jogo deve ser executado.
- `requirements.txt`: lista de dependências necessárias para executar o projeto.
- `pontuacoes.txt`: arquivo usado para salvar o ranking dos jogadores.
- `README.md`: documentação principal do projeto.
- `docs/proposta.md`: proposta inicial do jogo.
- `test_jogo_semana3.py`: arquivo com testes automatizados.
- `assets/imagens/`: pasta onde ficam as imagens utilizadas nas cenas.

---

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

---

## Como executar os testes

O projeto possui testes automatizados usando `pytest`.

Para executar os testes, use:

```bash
python -m pytest test_jogo_semana3.py
```

Os testes verificam partes importantes do projeto, como:

- limites dos status;
- funcionamento da pontuação;
- existência dos dias da história;
- existência de finais de vitória e derrota;
- estrutura das cenas;
- leitura e ordenação do ranking;
- funcionamento de regras principais do jogo.

---

## Como adicionar imagens

As imagens das cenas devem ser colocadas na pasta:

```text
assets/imagens/
```

O jogo procura automaticamente uma imagem com o mesmo nome da chave da cena.

Exemplo:

```text
inicio -> assets/imagens/inicio.png
d1_r1_c1 -> assets/imagens/d1_r1_c1.png
d2_r3_c5 -> assets/imagens/d2_r3_c5.png
```

Também é possível indicar manualmente uma imagem dentro do dicionário da cena usando o campo `imagem`.

Exemplo:

```python
'imagem': 'assets/imagens/minha_imagem.png'
```

Caso a imagem não exista, o jogo exibe um espaço reservado na tela.

---

## Recursos utilizados

O projeto utiliza:

- linguagem Python;
- biblioteca Pygame;
- arquivos de texto para persistência do ranking;
- imagens armazenadas na pasta `assets/imagens`;
- estruturas de dados como dicionários, listas e conjuntos;
- testes automatizados com pytest.

As referências para imagens, sons, fontes ou qualquer outro asset externo utilizado devem ser registradas na documentação do projeto ou em arquivo próprio dentro da pasta `docs/`.

---

## Checklist da entrega final - Semana 4

- [x] Jogo completo e executável.
- [x] Código-fonte organizado.
- [x] README preenchido.
- [x] Proposta inicial no arquivo `docs/proposta.md`.
- [x] Testes implementados.
- [x] Arquivos auxiliares necessários incluídos.
- [x] Sistema de ranking com leitura e escrita em arquivo.
- [x] Sistema de pontuação.
- [x] Sistema de status do jogador.
- [x] Sistema de inventário.
- [x] Condições de vitória e derrota.
- [x] História completa com 7 dias.
- [x] Suporte a imagens nas cenas.
- [x] Referências de assets externos previstas na documentação.
- [x] Projeto pronto para apresentação em sala.

---

## Conceitos da disciplina aplicados

Durante o desenvolvimento do jogo, foram aplicados conceitos trabalhados na disciplina, como:

- variáveis;
- condicionais;
- laços de repetição;
- funções;
- listas;
- dicionários;
- conjuntos;
- manipulação de arquivos;
- modularização;
- tratamento de eventos;
- testes automatizados;
- organização de projeto.

---

## Observações finais

**Seven Days of Fear** foi desenvolvido como projeto final da disciplina, com foco em narrativa interativa, tomada de decisões, controle de recursos e múltiplas possibilidades de encerramento.

A versão final permite jogar do início ao fim, visualizar status do personagem, realizar escolhas, acumular pontuação, salvar o ranking, acessar diferentes rotas e chegar a finais de vitória ou derrota conforme as decisões tomadas pelo jogador.
