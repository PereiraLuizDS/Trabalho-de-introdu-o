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
    def left(self):
        return self.x

    @property
    def right(self):
        return self.x + self.width

    @property
    def top(self):
        return self.y

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

    @property
    def topleft(self):
        return (self.x, self.y)

    def collidepoint(self, pos):
        px, py = pos
        return self.left <= px <= self.right and self.top <= py <= self.bottom


class SuperficieFake:
    def __init__(self, largura=100, altura=100):
        self.largura = largura
        self.altura = altura

    def get_width(self):
        return self.largura

    def get_height(self):
        return self.altura

    def get_rect(self):
        return RectFake(0, 0, self.largura, self.altura)

    def convert_alpha(self):
        return self

    def blit(self, *args, **kwargs):
        return None

    def fill(self, *args, **kwargs):
        return None


class FonteFake:
    def __init__(self, tamanho=20):
        self.tamanho = tamanho

    def render(self, texto, antialias, cor):
        largura = max(1, len(str(texto)) * 8)
        return SuperficieFake(largura, self.tamanho)

    def size(self, texto):
        return (max(1, len(str(texto)) * 8), self.tamanho)

    def get_height(self):
        return self.tamanho


class ClockFake:
    def tick(self, fps):
        return None


def criar_pygame_fake():
    pygame_fake = types.ModuleType("pygame")

    pygame_fake.Rect = RectFake
    pygame_fake.Surface = SuperficieFake
    pygame_fake.error = Exception
    pygame_fake.init = lambda: None
    pygame_fake.quit = lambda: None

    pygame_fake.display = types.SimpleNamespace(
        set_caption=lambda titulo: None,
        set_mode=lambda tamanho: SuperficieFake(*tamanho),
        flip=lambda: None,
    )
    pygame_fake.time = types.SimpleNamespace(Clock=lambda: ClockFake())
    pygame_fake.font = types.SimpleNamespace(SysFont=lambda nome, tamanho, bold=False: FonteFake(tamanho))
    pygame_fake.image = types.SimpleNamespace(load=lambda caminho: SuperficieFake())
    pygame_fake.transform = types.SimpleNamespace(smoothscale=lambda imagem, tamanho: SuperficieFake(*tamanho))
    pygame_fake.draw = types.SimpleNamespace(rect=lambda *args, **kwargs: None)
    pygame_fake.mouse = types.SimpleNamespace(get_pos=lambda: (0, 0))
    pygame_fake.event = types.SimpleNamespace(get=lambda: [])

    # Constantes usadas no tratamento de eventos do jogo.
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


def encontrar_main_py():
    """Localiza o main.py tanto na raiz quanto ao executar os testes dentro da pasta tests."""
    arquivo_atual = Path(__file__).resolve()
    caminhos_possiveis = [
        arquivo_atual.parent / "main.py",
        arquivo_atual.parent.parent / "main.py",
        Path.cwd() / "main.py",
    ]

    for caminho in caminhos_possiveis:
        if caminho.exists():
            return caminho

    raise FileNotFoundError("Nao foi possível localizar o arquivo main.py para executar os testes.")


def carregar_jogo():
    sys.modules["pygame"] = criar_pygame_fake()
    sys.modules.pop("main", None)

    caminho = encontrar_main_py()
    spec = importlib.util.spec_from_file_location("main", caminho)
    modulo = importlib.util.module_from_spec(spec)

    assert spec.loader is not None
    spec.loader.exec_module(modulo)
    return modulo


def coletar_tipos_de_finais(jogo):
    tipos = set()

    for cena in jogo.cenas.values():
        if cena.get("final_jogo") and cena.get("tipo"):
            tipos.add(cena.get("tipo"))

        for opcao in cena.get("opcoes", []):
            final = opcao.get("final")
            if final and final.get("tipo"):
                tipos.add(final.get("tipo"))

    return tipos


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

    assert jogo.pontos_da_escolha(escolha_morte) == jogo.PONTOS_MORTE
    assert jogo.pontos_da_escolha(escolha_vitoria) == jogo.PONTOS_ESCOLHA_BOA
    assert jogo.pontos_da_escolha(escolha_media) == jogo.PONTOS_ESCOLHA_MEDIA


def test_jogo_tem_sete_dias_e_finais():
    jogo = carregar_jogo()

    dias = {cena.get("dia") for cena in jogo.cenas.values() if cena.get("dia")}
    assert dias == {1, 2, 3, 4, 5, 6, 7}

    tipos_finais = coletar_tipos_de_finais(jogo)
    assert "vitoria" in tipos_finais
    assert "derrota" in tipos_finais


def test_estrutura_basica_das_cenas():
    jogo = carregar_jogo()

    assert isinstance(jogo.cenas, dict)
    assert "inicio" in jogo.cenas
    assert jogo.cenas["inicio"].get("opcoes")

    for chave, cena in jogo.cenas.items():
        assert "titulo" in cena, f"A cena {chave} nao possui titulo."
        assert "texto" in cena, f"A cena {chave} nao possui texto."
        assert isinstance(cena["titulo"], str)
        assert isinstance(cena["texto"], str)
        assert cena["titulo"].strip()
        assert cena["texto"].strip()

        for opcao in cena.get("opcoes", []):
            assert "texto" in opcao, f"Uma opcao da cena {chave} nao possui texto."
            assert "proxima" in opcao or "final" in opcao, f"Uma opcao da cena {chave} nao possui destino."


def test_opcao_com_requisito_so_libera_com_item():
    jogo = carregar_jogo()

    jogo.itens = []
    opcao = {"texto": "Entregar o Soro Sete", "requer_item": "soro sete"}

    assert jogo.opcao_disponivel(opcao) is False

    jogo.itens.append("soro sete")
    assert jogo.opcao_disponivel(opcao) is True


def test_opcao_com_municao_minima_so_libera_com_municao():
    jogo = carregar_jogo()

    opcao = {"texto": "Atirar", "municao_minima": 2}

    jogo.estado["municao"] = 1
    assert jogo.opcao_disponivel(opcao) is False

    jogo.estado["municao"] = 2
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
    assert ranking[0]["resultado"] == "vitoria"
