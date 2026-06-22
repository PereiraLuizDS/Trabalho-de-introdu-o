"""Dados iniciais e constantes de regra do jogo."""

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

# =========================
# PONTUAÇÃO
# =========================
PONTOS_ESCOLHA_BOA = 75
PONTOS_ESCOLHA_MEDIA = 50
PONTOS_MORTE = 0
PONTOS_DIA_CONCLUIDO = 100
PONTOS_CENA_VISITADA = 10

# =========================
# RANKING
# =========================
ARQUIVO_PONTUACOES = "pontuacoes.txt"
MAX_RANKING = 10

# =========================
# OBSERVAÇÃO SOBRE AS CENAS
# =========================
# O dicionário completo de cenas permanece no arquivo main.py da raiz,
# porque ele concentra a versão final jogável. Este módulo guarda apenas
# dados e constantes de apoio para testes e futura modularização.
