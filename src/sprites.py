import os
import pygame

from .config import PASTA_ASSETS


def caminho_imagem_da_cena(chave_cena, cena):
    """Retorna o caminho da imagem configurada para uma cena."""
    return cena.get("imagem", os.path.join(PASTA_ASSETS, f"{chave_cena}.png"))


def carregar_imagem(chave_cena, cena, arquivo_base):
    """Carrega a imagem de uma cena, se ela existir."""
    caminho = caminho_imagem_da_cena(chave_cena, cena)

    if not caminho:
        return None, caminho

    if not os.path.isabs(caminho):
        caminho = os.path.join(os.path.dirname(os.path.abspath(arquivo_base)), caminho)

    if not os.path.exists(caminho):
        return None, caminho

    try:
        imagem = pygame.image.load(caminho).convert_alpha()
        return imagem, caminho

    except pygame.error:
        return None, caminho


def escalar_imagem_para_retangulo(imagem, retangulo):
    """Redimensiona uma imagem mantendo a proporção para caber em um retângulo."""
    escala = min(retangulo.width / imagem.get_width(), retangulo.height / imagem.get_height())

    nova_largura = int(imagem.get_width() * escala)
    nova_altura = int(imagem.get_height() * escala)

    imagem = pygame.transform.smoothscale(imagem, (nova_largura, nova_altura))

    x = retangulo.centerx - nova_largura // 2
    y = retangulo.centery - nova_altura // 2

    return imagem, x, y
