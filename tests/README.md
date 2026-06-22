# Testes - Seven Days of Fear

Esta pasta contém os testes automatizados do jogo **Seven Days of Fear**.

Os testes foram atualizados para a entrega final da **Semana 4** e validam partes importantes da lógica do jogo sem abrir a janela real do Pygame. Para isso, o arquivo de testes usa uma versão simulada do módulo `pygame`, permitindo importar o `main.py` e testar funções, dados e regras principais de forma mais rápida e segura.

---

## Arquivo de testes

- `test_logica.py`: testa regras principais do jogo, como limites de status, pontuação, estrutura das cenas, existência dos 7 dias, finais de vitória e derrota, requisitos de itens e leitura do ranking salvo em arquivo.

---

## O que os testes verificam

- Se os status do jogador respeitam os limites definidos, como vida, energia, munição e confiança.
- Se a pontuação das escolhas está funcionando corretamente.
- Se o jogo possui cenas dos 7 dias da história.
- Se existem finais de vitória e derrota cadastrados.
- Se a cena inicial existe e possui opções de escolha.
- Se as cenas principais possuem título e texto.
- Se escolhas que exigem itens só ficam disponíveis quando o jogador possui o item necessário.
- Se o ranking é lido do arquivo `pontuacoes.txt` e ordenado pela maior pontuação.

---

## Como executar os testes

No terminal, dentro da pasta principal do projeto, execute:

```bash
python -m pytest tests/test_logica.py
```

Se o terminal já estiver dentro da pasta `tests`, execute:

```bash
python -m pytest test_logica.py
```

---

## Dependências

Os testes usam `pytest`. Caso ainda não esteja instalado, execute:

```bash
pip install pytest
```

Ou instale todas as dependências do projeto com:

```bash
pip install -r requirements.txt
```

---

## Observações

- Os testes não abrem a janela do jogo.
- O `pygame` é simulado dentro do arquivo de testes para permitir a importação do `main.py`.
- O arquivo `pontuacoes.txt` usado no teste de ranking é criado temporariamente pelo próprio `pytest`, sem alterar o ranking real do jogo.
- Estes testes ajudam a garantir que a versão final do projeto continue funcionando após alterações no código.
