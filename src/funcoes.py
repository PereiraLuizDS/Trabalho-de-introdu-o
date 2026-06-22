"""Funções auxiliares de regra, pontuação, inventário e ranking."""

import os

from .dados import (
    MAX_RANKING,
    PONTOS_ESCOLHA_BOA,
    PONTOS_ESCOLHA_MEDIA,
    PONTOS_MORTE,
)


QUALIDADES_VALIDAS = {"boa", "media", "morte"}


def qualidade_automatica(opcao):
    """Classifica uma escolha como boa, média ou morte."""
    final = opcao.get("final")

    if final and final.get("tipo") == "derrota":
        return "morte"

    qualidade = opcao.get("qualidade")
    if qualidade in QUALIDADES_VALIDAS:
        return qualidade

    if final and final.get("tipo") == "vitoria":
        return "boa"

    efeitos = opcao.get("efeitos", {})
    tem_item = bool(opcao.get("itens_add"))
    moral = efeitos.get("moral", 0)
    confianca = efeitos.get("confianca", 0)
    vida = efeitos.get("vida", 0)
    comida = efeitos.get("comida", 0)
    agua = efeitos.get("agua", 0)

    if tem_item or moral >= 4 or confianca > 0 or vida > 0 or comida >= 2 or agua >= 2:
        return "boa"

    return "media"


def pontos_da_escolha(opcao):
    """Retorna a pontuação gerada por uma escolha."""
    qualidade = qualidade_automatica(opcao)

    if qualidade == "boa":
        return PONTOS_ESCOLHA_BOA

    if qualidade == "media":
        return PONTOS_ESCOLHA_MEDIA

    return PONTOS_MORTE


def limitar_status(nome, valor):
    """Mantém os status dentro dos limites usados pelo jogo."""
    if nome in ("vida", "energia", "moral"):
        return max(0, min(100, valor))

    if nome in ("comida", "agua", "municao"):
        return max(0, valor)

    if nome == "confianca":
        return max(-10, min(20, valor))

    return valor


def aplicar_efeitos(estado, efeitos=None):
    """Aplica alterações de status no jogador e devolve o próprio estado."""
    if not efeitos:
        return estado

    for chave, delta in efeitos.items():
        if chave not in estado:
            estado[chave] = 0

        estado[chave] = limitar_status(chave, estado[chave] + delta)

    return estado


def adicionar_itens(itens, novos_itens=None):
    """Adiciona itens ao inventário sem repetir."""
    if not novos_itens:
        return itens

    for item in novos_itens:
        if item not in itens:
            itens.append(item)

    return itens


def alterar_municao(estado, delta=0):
    """Altera a munição respeitando o limite mínimo zero."""
    if delta:
        estado["municao"] = limitar_status("municao", estado.get("municao", 0) + delta)

    return estado


def normalizar_lista_requisitos(requer_item):
    """Transforma requisitos de item em uma lista padronizada."""
    if not requer_item:
        return []

    if isinstance(requer_item, str):
        return [requer_item]

    if isinstance(requer_item, (list, tuple, set)):
        return [str(item) for item in requer_item]

    return [str(requer_item)]


def descrever_requisitos(opcao):
    """Monta um texto com os requisitos de uma escolha."""
    requisitos = normalizar_lista_requisitos(opcao.get("requer_item"))

    municao_minima = opcao.get("municao_minima", 0)
    if municao_minima:
        requisitos.append(f"{municao_minima} munição")

    return ", ".join(requisitos)


def opcao_disponivel(opcao, itens=None, estado=None):
    """Verifica se o jogador possui os itens ou recursos exigidos por uma escolha."""
    itens = itens or []
    estado = estado or {}

    for item in normalizar_lista_requisitos(opcao.get("requer_item")):
        if item not in itens:
            return False

    municao_minima = opcao.get("municao_minima", 0)
    if municao_minima and estado.get("municao", 0) < municao_minima:
        return False

    return True


def caminho_arquivo_pontuacoes(nome_arquivo, arquivo_base):
    """Retorna o caminho absoluto do arquivo de ranking."""
    pasta = os.path.dirname(os.path.abspath(arquivo_base))
    return os.path.join(pasta, nome_arquivo)


def extrair_valor_ranking(linha, chave, padrao=""):
    """Extrai valores de uma linha do arquivo pontuacoes.txt."""
    prefixo = chave + ":"

    for pedaco in linha.split("|"):
        pedaco = pedaco.strip()

        if pedaco.startswith(prefixo):
            return pedaco[len(prefixo):].strip()

    return padrao


def _extrair_primeiro_valor(linha, chaves, padrao=""):
    """Tenta extrair um valor usando diferentes nomes de chave."""
    for chave in chaves:
        valor = extrair_valor_ranking(linha, chave, "")
        if valor != "":
            return valor

    return padrao


def ler_pontuacoes(caminho, maximo=MAX_RANKING):
    """Lê o arquivo de pontuações e devolve o ranking ordenado."""
    ranking = []

    if not os.path.exists(caminho):
        return ranking

    try:
        with open(caminho, "r", encoding="utf-8") as arquivo:
            linhas = arquivo.readlines()

    except OSError as erro:
        print(f"Não foi possível ler o ranking: {erro}")
        return ranking

    for linha in linhas:
        nome = _extrair_primeiro_valor(linha, ["Nome"], "Sobrevivente")
        pontuacao_texto = _extrair_primeiro_valor(linha, ["Pontuacao", "Pontuação"], "0")
        dias_texto = _extrair_primeiro_valor(linha, ["Dias concluidos", "Dias concluídos"], "0")
        resultado = _extrair_primeiro_valor(linha, ["Resultado"], "final")
        final = _extrair_primeiro_valor(linha, ["Final"], "Final desconhecido")

        try:
            valor_pontuacao = int(pontuacao_texto)
        except ValueError:
            valor_pontuacao = 0

        try:
            valor_dias = int(dias_texto)
        except ValueError:
            valor_dias = 0

        ranking.append({
            "nome": nome,
            "pontuacao": valor_pontuacao,
            "dias": valor_dias,
            "resultado": resultado,
            "final": final,
        })

    ranking.sort(key=lambda item: item["pontuacao"], reverse=True)

    return ranking[:maximo]


def salvar_pontuacao_final(caminho, nome, pontuacao, dias_concluidos, tipo_final, titulo_final):
    """Salva a pontuação final no arquivo de ranking."""
    pasta = os.path.dirname(os.path.abspath(caminho))
    if pasta:
        os.makedirs(pasta, exist_ok=True)

    linha = (
        f"Nome: {nome} | "
        f"Pontuacao: {pontuacao} | "
        f"Dias concluidos: {len(dias_concluidos)} | "
        f"Resultado: {tipo_final} | "
        f"Final: {titulo_final}\n"
    )

    try:
        with open(caminho, "a", encoding="utf-8") as arquivo:
            arquivo.write(linha)

        return True

    except OSError as erro:
        print(f"Não foi possível salvar a pontuação: {erro}")
        return False
