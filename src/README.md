# Código-fonte auxiliar (`src`)

Esta pasta contém módulos de apoio do jogo **Seven Days of Fear**.

O arquivo principal da versão final continua sendo o `main.py`, localizado na raiz do projeto. Mesmo assim, os arquivos desta pasta ajudam a organizar constantes, dados, funções auxiliares, carregamento de imagens e uma entrada alternativa para execução.

---

## Arquivos

- `__init__.py`: identifica a pasta como pacote Python e guarda informações gerais do jogo.
- `config.py`: armazena configurações globais, como tamanho da tela, FPS, cores, caminhos de assets e retângulos da interface.
- `dados.py`: guarda o estado inicial do jogador, constantes de pontuação e configurações do ranking.
- `funcoes.py`: reúne funções auxiliares de lógica, como pontuação, limites de status, inventário, requisitos de escolhas e leitura/gravação do ranking.
- `sprites.py`: concentra funções para localizar, carregar e redimensionar imagens das cenas.
- `jogo.py`: permite executar o jogo chamando o `loop_principal()` existente no `main.py` da raiz.

---

## Execução principal

Para executar o jogo, use o arquivo principal na raiz do projeto:

```bash
python main.py
```

Também é possível executar pela entrada auxiliar, caso a pasta esteja configurada como pacote:

```bash
python -m src.jogo
```

---

## Observação

A história completa e o dicionário de cenas permanecem no `main.py`, pois essa é a versão final jogável. Os módulos desta pasta servem como apoio para organização, testes e futuras melhorias de modularização.
