# =========================
# DADOS INICIAIS DO JOGO
# =========================

estado_inicial = {
    "vida": 100,
    "energia": 100,
    "comida": 3,
    "agua": 3,
    "moral": 50,
    "confianca": 0,
    "municao": 0,
}

# Pontuação
PONTOS_ESCOLHA_BOA = 75
PONTOS_ESCOLHA_MEDIA = 50
PONTOS_MORTE = 0
PONTOS_DIA_CONCLUIDO = 100

# Arquivo de ranking
ARQUIVO_PONTUACOES = "pontuacoes.txt"
MAX_RANKING = 10

# Observação:
# O dicionário completo de cenas está atualmente no arquivo main.py,
# pois o jogo principal ainda roda centralizado nele.
# Futuramente, o dicionário "cenas" pode ser movido para este arquivo.
