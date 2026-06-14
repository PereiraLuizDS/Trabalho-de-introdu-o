"""
Primeira versao dos testes do jogo Sobrevivencia Zumbi.

Como executar:
    python -m pytest test_jogo_semana3.py

Os testes usam um pygame falso para permitir testar regras, pontuacao,
ranking e estrutura das cenas sem abrir a janela do jogo.
"""

import importlib.util
import sys
import types
from pathlib import Path


class RectFake:
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.w = width
        self.h = height

    @property
    def bottom(self):
        return self.y + self.height

    @property
    def centerx(self):
        return self.x + self.width // 2

    @property
    def centery(self):
        return self.y + self.height // 2

    @property
    def center(self):
        return (self.centerx, self.centery)

    def collidepoint(self, pos):
        px, py = pos
        return self.x <= px <= self.x + self.width and self.y <= py <= self.y + self.height


class FonteFake:
    def __init__(self, tamanho=20):
        self.tamanho = tamanho

    def render(self, texto, antialias, cor):
        return types.SimpleNamespace(get_width=lambda: len(str(texto)) * 8, get_height=lambda: self.tamanho)

    def size(self, texto):
        return (len(str(texto)) * 8, self.tamanho)

    def get_height(self):
        return self.tamanho


class TelaFake:
    def blit(self, *args, **kwargs):
        return None

    def fill(self, *args, **kwargs):
        return None


class ClockFake:
    def tick(self, fps):
        return None


def criar_pygame_fake():
    pygame_fake = types.ModuleType("pygame")
    pygame_fake.Rect = RectFake
    pygame_fake.error = Exception
    pygame_fake.init = lambda: None
    pygame_fake.quit = lambda: None
    pygame_fake.display = types.SimpleNamespace(
        set_caption=lambda titulo: None,
        set_mode=lambda tamanho: TelaFake(),
        flip=lambda: None,
    )
    pygame_fake.time = types.SimpleNamespace(Clock=lambda: ClockFake())
    pygame_fake.font = types.SimpleNamespace(SysFont=lambda nome, tamanho, bold=False: FonteFake(tamanho))
    pygame_fake.image = types.SimpleNamespace(load=lambda caminho: None)
    pygame_fake.transform = types.SimpleNamespace(smoothscale=lambda imagem, tamanho: imagem)
    pygame_fake.draw = types.SimpleNamespace(rect=lambda *args, **kwargs: None)
    pygame_fake.mouse = types.SimpleNamespace(get_pos=lambda: (0, 0))
    pygame_fake.event = types.SimpleNamespace(get=lambda: [])

    # Constantes usadas no tratamento de eventos.
    pygame_fake.QUIT = 0
    pygame_fake.KEYDOWN = 1
    pygame_fake.MOUSEBUTTONDOWN = 2
    pygame_fake.K_ESCAPE = 27
    pygame_fake.K_RETURN = 13
    pygame_fake.K_BACKSPACE = 8
    pygame_fake.K_SPACE = 32
    pygame_fake.K_F1 = 282
    pygame_fake.K_r = ord("r")
    pygame_fake.K_1 = ord("1")
    pygame_fake.K_2 = ord("2")
    pygame_fake.K_3 = ord("3")
    pygame_fake.K_4 = ord("4")
    return pygame_fake


def carregar_jogo():
    sys.modules["pygame"] = criar_pygame_fake()
    caminho = Path(__file__).with_name("main.py")
    spec = importlib.util.spec_from_file_location("main", caminho)
    modulo = importlib.util.module_from_spec(spec)
    assert spec.loader is not None
    spec.loader.exec_module(modulo)
    return modulo


def test_limitar_status_respeita_limites():
    jogo = carregar_jogo()
    assert jogo.limitar_status("vida", 150) == 100
    assert jogo.limitar_status("vida", -10) == 0
    assert jogo.limitar_status("energia", 101) == 100
    assert jogo.limitar_status("municao", -3) == 0
    assert jogo.limitar_status("confianca", 50) == 20
    assert jogo.limitar_status("confianca", -50) == -10


def test_pontuacao_por_tipo_de_escolha():
    jogo = carregar_jogo()
    escolha_morte = {"final": {"tipo": "derrota"}}
    escolha_vitoria = {"final": {"tipo": "vitoria"}}
    escolha_media = {"efeitos": {"energia": -2}}

    assert jogo.pontos_da_escolha(escolha_morte) == 0
    assert jogo.pontos_da_escolha(escolha_vitoria) == jogo.PONTOS_ESCOLHA_BOA
    assert jogo.pontos_da_escolha(escolha_media) == jogo.PONTOS_ESCOLHA_MEDIA


def test_jogo_tem_sete_dias_e_finais():
    jogo = carregar_jogo()
    dias = {cena.get("dia") for cena in jogo.cenas.values() if cena.get("dia")}
    assert dias == {1, 2, 3, 4, 5, 6, 7}

    tipos_finais = []
    for cena in jogo.cenas.values():
        for opcao in cena.get("opcoes", []):
            final = opcao.get("final")
            if final:
                tipos_finais.append(final.get("tipo"))

    assert "vitoria" in tipos_finais
    assert "derrota" in tipos_finais


def test_opcao_com_requisito_so_libera_com_item():
    jogo = carregar_jogo()
    jogo.itens = []
    opcao = {"texto": "Entregar o Soro Sete", "requer_item": "soro sete"}

    assert jogo.opcao_disponivel(opcao) is False

    jogo.itens.append("soro sete")
    assert jogo.opcao_disponivel(opcao) is True


def test_ranking_e_lido_e_ordenado(tmp_path):
    jogo = carregar_jogo()
    arquivo = tmp_path / "pontuacoes.txt"
    arquivo.write_text(
        "Nome: Ana | Pontuacao: 400 | Dias concluidos: 4 | Resultado: derrota | Final: Morte\n"
        "Nome: Bia | Pontuacao: 900 | Dias concluidos: 7 | Resultado: vitoria | Final: Sobreviveu\n"
        "Nome: Caio | Pontuacao: 700 | Dias concluidos: 6 | Resultado: derrota | Final: Porto\n",
        encoding="utf-8",
    )

    jogo.ARQUIVO_PONTUACOES = str(arquivo)
    ranking = jogo.ler_pontuacoes()

    assert [item["nome"] for item in ranking] == ["Bia", "Caio", "Ana"]
    assert ranking[0]["pontuacao"] == 900
    assert ranking[0]["dias"] == 7
