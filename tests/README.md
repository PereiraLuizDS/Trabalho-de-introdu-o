# Testes - Seven Days of Fear

Esta pasta contém a primeira versão dos testes automatizados do jogo **Seven Days of Fear**.

Os testes foram criados para validar partes importantes da lógica do jogo sem abrir a janela do Pygame durante a execução.

## Arquivo de testes

- `test_jogo_semana3.py`: testa regras principais do jogo, como limites de status, pontuação, finais, requisitos de itens e leitura do ranking salvo em arquivo.

## O que os testes verificam

- Se os status do jogador respeitam os limites definidos, como vida, energia, munição e confiança.
- Se a pontuação das escolhas está funcionando corretamente.
- Se o jogo possui os 7 dias da história.
- Se existem finais de vitória e derrota.
- Se escolhas que exigem itens só ficam disponíveis quando o jogador possui o item necessário.
- Se o ranking é lido do arquivo `pontuacoes.txt` e ordenado pela maior pontuação.

## Como executar os testes

No terminal, dentro da pasta principal do projeto, execute:

```bash
python -m pytest test_jogo_semana3.py
