# Dados

Esta pasta guarda arquivos de persistência simples em texto utilizados pelo jogo **Seven Days of Fear**.

Os arquivos desta pasta servem para armazenar informações que podem continuar existindo mesmo depois que o jogo é fechado, como ranking, recordes ou pontuações salvas pelos jogadores.

## Arquivos

- `ranking.txt`: arquivo reservado para armazenar uma base de ranking de jogadores, caso seja utilizado nesta pasta.
- `pontuacoes.txt`: arquivo utilizado pelo jogo principal para salvar automaticamente a pontuação final das partidas.
- `README.md`: documentação desta pasta e explicação sobre os arquivos de dados.

## Observação sobre o jogo atual

No código atual do jogo, a pontuação final é salva automaticamente em arquivo de texto ao final da partida.

O arquivo de ranking pode registrar informações como:

- nome do jogador;
- pontuação final;
- quantidade de dias concluídos;
- resultado da partida;
- final alcançado.

Esses dados são usados para exibir o ranking dentro do jogo.

## Observação sobre imagens e assets

As imagens utilizadas no jogo estão sendo geradas para representar as cenas de **Seven Days of Fear**.

Essas imagens não devem ser armazenadas nesta pasta de dados. Elas devem ficar na pasta de assets do projeto, preferencialmente em:

```text
assets/imagens/
```

Caso alguma imagem, fonte, som ou outro recurso externo seja utilizado, a origem deve ser registrada na documentação do projeto, especialmente na pasta `docs/`.

Se as imagens forem geradas pelo próprio grupo ou com auxílio de ferramenta de geração de imagens, isso também deve ser informado na documentação como referência dos assets utilizados.

## Cuidados

- Não versionar dados pessoais reais dos jogadores.
- Manter arquivos de ranking simples e legíveis.
- Evitar apagar o arquivo de pontuações antes da apresentação, caso o grupo queira demonstrar o ranking funcionando.
- Separar arquivos de dados, imagens e documentação em suas respectivas pastas.
