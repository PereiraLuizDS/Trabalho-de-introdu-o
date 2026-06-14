"""
Entrada alternativa para executar o jogo.

O jogo principal está no arquivo main.py da raiz do projeto.
Este arquivo permite iniciar o jogo a partir da pasta src sem duplicar a lógica.
"""

from pathlib import Path
import sys


def executar():
    raiz = Path(__file__).resolve().parents[1]

    if str(raiz) not in sys.path:
        sys.path.insert(0, str(raiz))

    from main import loop_principal

    loop_principal()


if __name__ == "__main__":
    executar()
