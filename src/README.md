# Código-fonte (`src`)

Esta pasta contém os módulos principais do jogo **Seven Days of Fear**.

Os arquivos desta pasta organizam partes importantes do projeto, como configurações, dados, funções auxiliares, sprites e lógica principal do jogo.

## Arquivos

- `jogo.py`: contém o loop principal, tratamento de eventos, atualização da tela e renderização do jogo.
- `config.py`: armazena constantes globais, como tamanho da tela, cores, caminhos de arquivos e FPS.
- `funcoes.py`: reúne funções auxiliares de regra e lógica, como pontuação, controle de status, validações e ranking.
- `sprites.py`: responsável pelo carregamento, organização e uso de imagens ou sprites do jogo.
- `dados.py`: concentra a leitura e gravação de dados, como recorde, ranking e informações persistentes.
- `__init__.py`: indica que a pasta pode ser usada como um pacote Python.

## Dica de evolução

Quando o projeto crescer, mantenha os módulos pequenos e separados por responsabilidade. Isso facilita a leitura, a manutenção e a evolução do jogo.
