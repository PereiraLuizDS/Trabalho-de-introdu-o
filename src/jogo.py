"""Entrada alternativa para executar Seven Days of Fear.

O jogo final continua centralizado no arquivo ``main.py`` localizado na raiz
do projeto. Este módulo permite executar o mesmo jogo a partir do pacote de
apoio, mantendo a organização da pasta ``src``.
"""

import importlib
import sys
from pathlib import Path


def caminho_raiz_projeto():
    """Retorna a pasta raiz do projeto considerando que este arquivo fica em src/."""
    return Path(__file__).resolve().parents[1]


def preparar_importacao_main():
    """Garante que a raiz do projeto esteja disponível no sys.path."""
    raiz = caminho_raiz_projeto()
    raiz_texto = str(raiz)

    if raiz_texto not in sys.path:
        sys.path.insert(0, raiz_texto)

    return raiz


def carregar_main():
    """Importa e devolve o módulo main.py da raiz do projeto."""
    preparar_importacao_main()
    return importlib.import_module("main")


def executar():
    """Executa o loop principal do jogo."""
    modulo_main = carregar_main()

    if not hasattr(modulo_main, "loop_principal"):
        raise AttributeError("O arquivo main.py precisa possuir a função loop_principal().")

    modulo_main.loop_principal()


if __name__ == "__main__":
    executar()
