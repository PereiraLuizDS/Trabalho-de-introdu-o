# Código-fonte (`src`)

Esta pasta contém módulos de apoio do jogo **Seven Days of Fear**.

O jogo principal continua sendo executado pelo arquivo `main.py` da raiz do projeto, mas os arquivos desta pasta organizam partes importantes do código e servem como base para uma modularização maior.

## Arquivos

- `__init__.py`: identifica a pasta como um pacote Python e guarda o nome do jogo.
- `config.py`: contém as configurações principais, como tamanho da tela, FPS, cores, caminhos e retângulos da interface.
- `dados.py`: contém o estado inicial do jogador, constantes de pontuação e informações persistentes do jogo.
- `funcoes.py`: reúne funções auxiliares de regra e lógica, como pontuação, limites de status, validação de requisitos e leitura/gravação do ranking.
- `sprites.py`: reúne funções relacionadas ao carregamento e ajuste de imagens das cenas.
- `jogo.py`: permite executar o jogo chamando o `loop_principal()` definido em `main.py`.

## Execução principal

Para rodar o jogo, use o arquivo principal da raiz:

```bash
python main.py
