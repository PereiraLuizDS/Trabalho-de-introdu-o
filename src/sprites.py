"""Funções auxiliares para localizar, carregar e redimensionar imagens."""

import os

import pygame

from .config import PASTA_ASSETS, PASTA_ASSETS_ALTERNATIVA

FORMATOS_IMAGEM = (".png", ".jpg", ".jpeg", ".bmp")


def caminho_imagem_da_cena(chave_cena, cena):
    """Retorna o caminho configurado para a imagem de uma cena."""
    return cena.get("imagem", os.path.join(PASTA_ASSETS, f"{chave_cena}.png"))


def caminhos_possiveis_imagem(chave_cena, cena):
    """Gera caminhos possíveis para localizar a imagem de uma cena."""
    caminho_configurado = caminho_imagem_da_cena(chave_cena, cena)

    if caminho_configurado:
        yield caminho_configurado

    nome_base = str(chave_cena)
    for pasta in (PASTA_ASSETS, PASTA_ASSETS_ALTERNATIVA):
        for extensao in FORMATOS_IMAGEM:
            yield os.path.join(pasta, nome_base + extensao)


def resolver_caminho(caminho, arquivo_base):
    """Transforma um caminho relativo em caminho absoluto usando o arquivo base."""
    if not caminho or os.path.isabs(caminho):
        return caminho

    pasta_base = os.path.dirname(os.path.abspath(arquivo_base))
    return os.path.join(pasta_base, caminho)


def carregar_imagem(chave_cena, cena, arquivo_base):
    """Carrega a imagem de uma cena, se ela existir."""
    ultimo_caminho = None

    for caminho in caminhos_possiveis_imagem(chave_cena, cena):
        caminho_resolvido = resolver_caminho(caminho, arquivo_base)
        ultimo_caminho = caminho_resolvido

        if not caminho_resolvido or not os.path.exists(caminho_resolvido):
            continue

        try:
            imagem = pygame.image.load(caminho_resolvido).convert_alpha()
            return imagem, caminho_resolvido

        except pygame.error:
            return None, caminho_resolvido

    return None, ultimo_caminho


def escalar_imagem_para_retangulo(imagem, retangulo, preencher=True):
    """Redimensiona uma imagem para o retângulo da interface.

    Quando ``preencher`` é True, a imagem ocupa todo o espaço do retângulo.
    Quando é False, a proporção original é preservada.
    """
    if preencher:
        imagem = pygame.transform.smoothscale(imagem, (retangulo.width, retangulo.height))
        return imagem, retangulo.x, retangulo.y

    escala = min(retangulo.width / imagem.get_width(), retangulo.height / imagem.get_height())
    nova_largura = int(imagem.get_width() * escala)
    nova_altura = int(imagem.get_height() * escala)

    imagem = pygame.transform.smoothscale(imagem, (nova_largura, nova_altura))

    x = retangulo.centerx - nova_largura // 2
    y = retangulo.centery - nova_altura // 2

    return imagem, x, y
