import pygame
import sys
import os

pygame.init()

# ---------------- CONFIGURACOES ----------------

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

LARGURA = 900
ALTURA = 600
TELA = pygame.display.set_mode((LARGURA, ALTURA))
pygame.display.set_caption("Jogo Zumbi - Dias 1 e 2")

FPS = 60
clock = pygame.time.Clock()

BRANCO = (240, 240, 240)
PRETO = (15, 15, 15)
CINZA_ESCURO = (25, 25, 25)
CINZA = (80, 80, 80)
AMARELO = (235, 210, 80)
VERDE = (80, 200, 100)
VERMELHO = (210, 65, 65)
AZUL_CLARO = (120, 220, 220)
VERDE_CLARO = (170, 235, 130)

fonte_titulo = pygame.font.SysFont(None, 42)
fonte_texto = pygame.font.SysFont(None, 27)
fonte_pequena = pygame.font.SysFont(None, 22)


cenas = {
    "inicio": {
        "titulo": "Dia 1 - Cidade destruída",
        "imagem": "assets/dia1_cidade.png",
        "cor_fundo": (55, 60, 65),
        "texto": (
            "Voce acorda em uma cidade destruída por zumbis. Pelos rastros nas ruas, "
            "parece que os zumbis são mais ativos durante a noite. Antes que escureça, "
            "voce precisa escolher onde vai tentar passar o primeiro dia."
        ),
        "opcoes": [
            {
                "texto": "1 - Ir para uma casa proxima",
                "resultado": "Voce corre ate uma casa aparentemente abandonada.",
                "efeitos": {"energia": -5},
                "proxima": "casa_entrada"
            },
            {
                "texto": "2 - Ir para um supermercado",
                "resultado": "Voce segue ate um supermercado em busca de abrigo e recursos.",
                "efeitos": {"energia": -8},
                "proxima": "mercado_entrada"
            },
            {
                "texto": "3 - Tentar correr para fora da cidade",
                "resultado": "Voce decide tentar escapar da cidade pela estrada.",
                "efeitos": {"energia": -18, "moral": -3},
                "proxima": "estrada_corrida"
            }
        ]
    },

    # ---------------- CAMINHO DA CASA ----------------

    "casa_entrada": {
        "titulo": "Dia 1 - Casa abandonada",
        "imagem": "assets/casa.png",
        "cor_fundo": (65, 55, 50),
        "texto": (
            "Você entra na casa e percebe que não está sozinho. Um zumbi se aproxima. "
            "Olhando rapidamente, você vê um machado ao lado do sofá e uma arma de fogo "
            "em cima da mesa."
        ),
        "opcoes": [
            {
                "texto": "1 - Correr para pegar o machado",
                "resultado": (
                    "Voce pega o machado e consegue matar o zumbi, mas acaba se sujando "
                    "com sangue durante a luta."
                ),
                "efeitos": {"energia": -12, "moral": 10},
                "itens_add": ["machado"],
                "proxima": "casa_recuperacao"
            },
            {
                "texto": "2 - Correr para pegar a arma de fogo",
                "resultado": (
                    "Voce pega a arma, mas percebe que ela esta descarregada. A municao "
                    "esta um pouco longe."
                ),
                "efeitos": {"energia": -6, "moral": 3},
                "itens_add": ["arma de fogo"],
                "municao_delta": 0,
                "proxima": "arma_descarregada"
            },
            {
                "texto": "3 - Voltar para a rua",
                "resultado": "Voce desiste da casa e volta para a rua desesperado.",
                "efeitos": {"energia": -10, "moral": -8},
                "proxima": "casa_rua_zumbis"
            }
        ]
    },

    "casa_recuperacao": {
        "titulo": "Dia 1 - Casa segura",
        "imagem": "assets/casa_segura.png",
        "cor_fundo": (60, 65, 55),
        "texto": (
            "Depois da luta, voce verifica a casa. Consegue tomar um banho, se alimentar "
            "e descansar por algumas horas. A casa servira como abrigo para esta noite."
        ),
        "efeitos_entrada": {"energia": 22, "comida": -1, "agua": -1, "moral": 8},
        "fim_dia": True,
        "dia": 1,
        "proxima_dia": "dia2_rota4"
    },

    "arma_descarregada": {
        "titulo": "Dia 1 - Arma descarregada",
        "imagem": "assets/arma_descarregada.png",
        "cor_fundo": (70, 55, 50),
        "texto": (
            "O zumbi continua avancando. Voce tem a arma em maos, mas ela esta sem municao. "
            "As balas estao em uma gaveta do outro lado da sala."
        ),
        "opcoes": [
            {
                "texto": "1 - Correr para pegar a municao e atirar no zumbi",
                "resultado": (
                    "Voce consegue pegar a municao e atirar. O zumbi cai, mas a adrenalina "
                    "e o cansaco fazem voce desmaiar."
                ),
                "efeitos": {"energia": -18, "moral": 12},
                "itens_add": ["municao"],
                "municao_delta": 5,
                "proxima": "casa_desmaio"
            },
            {
                "texto": "2 - Tentar dar uma coronhada no zumbi",
                "resultado": (
                    "A coronhada apenas retarda o zumbi por um momento. Ele avanca de novo "
                    "e voce nao consegue se defender."
                ),
                "efeitos": {"vida": -100},
                "final": {
                    "tipo": "derrota",
                    "titulo": "Final - Morto na casa",
                    "texto": (
                        "A tentativa de usar a arma descarregada como golpe nao foi suficiente. "
                        "O zumbi derrubou voce antes que conseguisse reagir."
                    )
                }
            }
        ]
    },

    "casa_desmaio": {
        "titulo": "Dia 1 - Depois do disparo",
        "imagem": "assets/casa_desmaio.png",
        "cor_fundo": (50, 55, 60),
        "texto": (
            "O tiro ecoa pela casa. Voce consegue eliminar o zumbi, mas o susto, o esforco "
            "e a adrenalina fazem voce desmaiar. Quando acorda, ja esta anoitecendo."
        ),
        "efeitos_entrada": {"energia": 12, "comida": -1, "agua": -1},
        "fim_dia": True,
        "dia": 1,
        "proxima_dia": "dia2_rota5"
    },

    "casa_rua_zumbis": {
        "titulo": "Dia 1 - Rua perigosa",
        "imagem": "assets/rua_zumbis.png",
        "cor_fundo": (80, 45, 45),
        "texto": (
            "Ao voltar para a rua, voce da de cara com um grupo de zumbis famintos. "
            "Sem abrigo e sem vantagem, voce precisa correr imediatamente."
        ),
        "proxima": "casa_morte_corrida"
    },

    "casa_morte_corrida": {
        "titulo": "Dia 1 - Exaustao",
        "imagem": "assets/morte_rua.png",
        "cor_fundo": (90, 40, 40),
        "texto": (
            "Voce corre o maximo que consegue, mas cansa rapido. Os zumbis alcancam voce."
        ),
        "efeitos_entrada": {"energia": -100, "vida": -100},
        "final": {
            "tipo": "derrota",
            "titulo": "Final - Alcancado pelos zumbis",
            "texto": "Voce cansou durante a fuga e foi morto pelos zumbis na rua."
        }
    },

    # ---------------- CAMINHO DO SUPERMERCADO ----------------

    "mercado_entrada": {
        "titulo": "Dia 1 - Supermercado",
        "imagem": "assets/supermercado.png",
        "cor_fundo": (55, 75, 60),
        "texto": (
            "Voce entra no supermercado e percebe que ainda existem itens para pegar. "
            "As janelas estão um pouco desprotegidas e existe uma porta de saída trancada "
            "por dentro."
        ),
        "opcoes": [
            {
                "texto": "1 - Procurar itens no supermercado",
                "resultado": "Voce procura entre as prateleiras e encontra comida e agua.",
                "efeitos": {"comida": 3, "agua": 2, "energia": -12, "moral": 5},
                "proxima": "mercado_alimentar_dormir"
            },
            {
                "texto": "2 - Verificar as janelas",
                "resultado": (
                    "Voce reforca as janelas e deixa o supermercado mais protegido "
                    "antes de procurar recursos."
                ),
                "efeitos": {"energia": -15, "moral": 12},
                "proxima": "mercado_procura_depois"
            },
            {
                "texto": "3 - Sair pela porta dos fundos",
                "resultado": "Voce destranca a porta dos fundos e sai sem verificar o exterior.",
                "efeitos": {"energia": -10, "moral": -8},
                "proxima": "mercado_porta_fundos"
            }
        ]
    },

    "mercado_alimentar_dormir": {
        "titulo": "Dia 1 - Descanso no mercado",
        "imagem": "assets/mercado_descanso.png",
        "cor_fundo": (50, 80, 60),
        "texto": (
            "Com os recursos encontrados, voce consegue se alimentar e beber agua. "
            "Depois, escolhe um canto escondido do supermercado para dormir."
        ),
        "efeitos_entrada": {"energia": 18, "comida": -1, "agua": -1, "moral": 5},
        "fim_dia": True,
        "dia": 1,
        "proxima_dia": "dia2_rota7"
    },

    "mercado_procura_depois": {
        "titulo": "Dia 1 - Mercado protegido",
        "imagem": "assets/mercado_janelas.png",
        "cor_fundo": (45, 80, 65),
        "texto": (
            "Com as janelas reforcadas, voce fica mais tranquilo. Agora pode procurar "
            "itens no supermercado sem se expor tanto."
        ),
        "efeitos_entrada": {"comida": 2, "agua": 2, "energia": -6},
        "proxima": "mercado_dorme_seguro"
    },

    "mercado_dorme_seguro": {
        "titulo": "Dia 1 - Noite segura",
        "imagem": "assets/mercado_noite.png",
        "cor_fundo": (40, 65, 55),
        "texto": (
            "Voce encontra comida e agua, consegue se alimentar e dorme com mais seguranca "
            "dentro do supermercado protegido."
        ),
        "efeitos_entrada": {"energia": 22, "comida": -1, "agua": -1, "moral": 8},
        "fim_dia": True,
        "dia": 1,
        "proxima_dia": "dia2_rota8"
    },

    "mercado_porta_fundos": {
        "titulo": "Dia 1 - Porta dos fundos",
        "imagem": "assets/porta_fundos.png",
        "cor_fundo": (75, 45, 45),
        "texto": (
            "Ao sair pela porta dos fundos, voce da de cara com alguns zumbis. "
            "Sem tempo para voltar, voce sai correndo."
        ),
        "proxima": "mercado_morte_zumbis"
    },

    "mercado_morte_zumbis": {
        "titulo": "Dia 1 - Sem saida",
        "imagem": "assets/morte_mercado.png",
        "cor_fundo": (90, 40, 40),
        "texto": "Voce tenta fugir, mas cansa rapidamente e e cercado pelos zumbis.",
        "efeitos_entrada": {"energia": -100, "vida": -100},
        "final": {
            "tipo": "derrota",
            "titulo": "Final - Cercado no mercado",
            "texto": "Voce saiu pela porta dos fundos e foi morto pelos zumbis."
        }
    },

    # ---------------- CAMINHO DA ESTRADA ----------------

    "estrada_corrida": {
        "titulo": "Dia 1 - Estrada para fora da cidade",
        "imagem": "assets/estrada.png",
        "cor_fundo": (65, 65, 55),
        "texto": (
            "Voce corre para fora da cidade pela estrada. Por alguns minutos, parece que "
            "a escolha foi boa. Então você escuta muitos passos vindo de longe."
        ),
        "proxima": "estrada_horda"
    },

    "estrada_horda": {
        "titulo": "Dia 1 - Horda de zumbis",
        "imagem": "assets/horda.png",
        "cor_fundo": (80, 45, 45),
        "texto": (
            "Você encontra uma horda de zumbis atravessando a estrada. Eles ainda não viram "
            "você, mas qualquer movimento errado pode ser fatal."
        ),
        "opcoes": [
            {
                "texto": "1 - Tentar se esconder da horda",
                "resultado": (
                    "Voce se joga entre arbustos e prende a respiracao enquanto a horda passa."
                ),
                "efeitos": {"energia": -12, "moral": 10},
                "proxima": "estrada_anoitecer"
            },
            {
                "texto": "2 - Enfrentar a horda",
                "resultado": "Voce tenta enfrentar a horda, mas a quantidade de zumbis e absurda.",
                "efeitos": {"vida": -100},
                "final": {
                    "tipo": "derrota",
                    "titulo": "Final - Morto pela horda",
                    "texto": "Voce foi brutalmente morto pelos zumbis ao tentar enfrentar a horda."
                }
            }
        ]
    },

    "estrada_anoitecer": {
        "titulo": "Dia 1 - Fuga ao anoitecer",
        "imagem": "assets/anoitecer.png",
        "cor_fundo": (45, 45, 75),
        "texto": (
            "Voce espera a horda passar e consegue fugir quando esta anoitecendo. "
            "Mesmo cansado, voce encontra um lugar escondido para passar a noite."
        ),
        "efeitos_entrada": {"energia": -5, "moral": 8, "agua": -1},
        "fim_dia": True,
        "dia": 1,
        "proxima_dia": "dia2_rota10"
    },

    # ---------------- DIA 2 ----------------

    "dia2_rota4": {
        "titulo": "Dia 2 - Casa sem recursos",
        "imagem": "assets/dia2_casa_sem_recursos.png",
        "cor_fundo": (58, 62, 68),
        "texto": (
            "Voce acorda mais descansado, mas percebe que a casa nao tem muitos recursos. "
            "Sera necessario tomar uma decisao antes que o dia avance."
        ),
        "opcoes": [
            {
                "texto": "1 - Tentar fugir pela rua principal",
                "resultado": "Voce encontra muitos zumbis na rua e tenta correr mesmo estando sem preparo.",
                "efeitos": {"energia": -35, "moral": -10},
                "final": {
                    "tipo": "derrota",
                    "titulo": "Final - Pego na rua principal",
                    "texto": "Voce cansou durante a fuga pela rua principal e foi pego pelos zumbis."
                }
            },
            {
                "texto": "2 - Vasculhar a casa com calma antes de sair",
                "resultado": "Voce encontra um bilhete indicando o terminal de onibus e alguns recursos esquecidos.",
                "efeitos": {"comida": 2, "agua": 2, "energia": -10, "moral": 8},
                "itens_add": ["bilhete do terminal"],
                "proxima": "dia2_rota12"
            },
            {
                "texto": "3 - Sair pela porta dos fundos",
                "resultado": "Voce passa por becos e vielas para evitar os zumbis, mas demora bastante.",
                "efeitos": {"energia": -22, "moral": -5},
                "proxima": "dia2_rota12"
            }
        ]
    },

    "dia2_rota5": {
        "titulo": "Dia 2 - Horda atraida pelo disparo",
        "imagem": "assets/dia2_horda_casa.png",
        "cor_fundo": (82, 50, 50),
        "texto": (
            "Voce acorda assustado com zumbis tentando entrar. O barulho da arma no dia anterior "
            "atraiu uma horda para perto da casa."
        ),
        "opcoes": [
            {
                "texto": "1 - Pular por uma janela do segundo andar",
                "resultado": "Voce consegue fugir, mas se machuca na queda e precisa correr pelos becos.",
                "efeitos": {"vida": -18, "energia": -25, "moral": -5},
                "proxima": "dia2_rota11"
            },
            {
                "texto": "2 - Atirar novamente",
                "resultado": "Voce mata alguns zumbis, mas acaba a municao e o restante da horda invade a casa.",
                "efeitos": {"energia": -15},
                "municao_delta": -5,
                "final": {
                    "tipo": "derrota",
                    "titulo": "Final - Sem municao",
                    "texto": "A arma segurou a horda por pouco tempo. Sem municao, voce nao conseguiu escapar."
                }
            },
            {
                "texto": "3 - Tentar segurar a porta",
                "resultado": "A horda e forte demais. A porta cede antes que voce encontre uma saida.",
                "efeitos": {"vida": -100},
                "final": {
                    "tipo": "derrota",
                    "titulo": "Final - Porta arrombada",
                    "texto": "Os zumbis eram muitos e acabaram matando voce dentro da casa."
                }
            }
        ]
    },

    "dia2_rota7": {
        "titulo": "Dia 2 - Zumbis no supermercado",
        "imagem": "assets/dia2_supermercado_invadido.png",
        "cor_fundo": (70, 70, 55),
        "texto": (
            "Voce acorda assustado com zumbis entrando no supermercado. A decisao precisa ser rapida."
        ),
        "opcoes": [
            {
                "texto": "1 - Pular pela janela",
                "resultado": "Voce se machuca ao pular a janela, mas consegue correr antes que seja cercado.",
                "efeitos": {"vida": -14, "energia": -18, "moral": -4},
                "proxima": "dia2_rota12"
            },
            {
                "texto": "2 - Enfrentar os zumbis",
                "resultado": "Os zumbis sao muitos. Voce nao consegue lutar contra todos.",
                "efeitos": {"vida": -100},
                "final": {
                    "tipo": "derrota",
                    "titulo": "Final - Cercado no supermercado",
                    "texto": "Voce tentou enfrentar os zumbis, mas foi morto dentro do supermercado."
                }
            }
        ]
    },

    "dia2_rota8": {
        "titulo": "Dia 2 - Supermercado protegido",
        "imagem": "assets/dia2_supermercado_seguro.png",
        "cor_fundo": (50, 80, 65),
        "texto": (
            "Voce esta um pouco melhor e consegue decidir sua rota com mais calma. "
            "Ainda assim, ficar parado pode ser perigoso."
        ),
        "opcoes": [
            {
                "texto": "1 - Procurar uma saida segura",
                "resultado": "Voce encontra uma rota discreta, uma saida segura e alguns suprimentos.",
                "efeitos": {"comida": 2, "agua": 1, "energia": -10, "moral": 8},
                "proxima": "dia2_rota12"
            },
            {
                "texto": "2 - Sair pela porta principal",
                "resultado": "Voce da de cara com muitos zumbis e tenta correr pela rua.",
                "efeitos": {"energia": -35, "moral": -8},
                "final": {
                    "tipo": "derrota",
                    "titulo": "Final - Pego na saida principal",
                    "texto": "Voce cansou durante a corrida e foi pego pelos zumbis."
                }
            }
        ]
    },

    "dia2_rota10": {
        "titulo": "Dia 2 - Fome e sede na estrada",
        "imagem": "assets/dia2_estrada_fome.png",
        "cor_fundo": (67, 65, 52),
        "texto": (
            "Voce acorda com fome e sede. Agora precisa encontrar comida, agua e algo que possa usar "
            "para se defender. Mais adiante, escuta barulho de agua vindo de uma floresta."
        ),
        "opcoes": [
            {
                "texto": "1 - Ir para a floresta buscar agua",
                "resultado": "Voce entra na floresta seguindo o som da agua.",
                "efeitos": {"energia": -8},
                "proxima": "dia2_rota10_1"
            },
            {
                "texto": "2 - Ignorar a floresta e voltar para a estrada",
                "resultado": "Voce volta para a estrada, bastante cansado, tentando achar algo mais seguro.",
                "efeitos": {"energia": -12, "moral": -3},
                "proxima": "dia2_rota10_2"
            }
        ]
    },

    "dia2_rota10_1": {
        "titulo": "Dia 2 - Riacho na floresta",
        "imagem": "assets/dia2_riacho.png",
        "cor_fundo": (45, 85, 65),
        "texto": (
            "Voce encontra um riacho pequeno. Perto dele, um zumbi esta preso entre galhos e se debate. "
            "Ao lado do zumbi existe uma mochila."
        ),
        "opcoes": [
            {
                "texto": "1 - Atacar o zumbi com uma pedra",
                "resultado": "Voce apenas irrita o zumbi, que consegue se soltar dos galhos.",
                "efeitos": {"energia": -20, "moral": -10},
                "final": {
                    "tipo": "derrota",
                    "titulo": "Final - Zumbi solto",
                    "texto": "Muito cansado, voce nao conseguiu se defender depois que o zumbi se soltou."
                }
            },
            {
                "texto": "2 - Tentar pegar a mochila sem fazer barulho",
                "resultado": "Voce consegue pegar uma faca na mochila, mas se machuca durante a fuga.",
                "efeitos": {"vida": -12, "agua": 1, "energia": -12, "comida": -1},
                "itens_add": ["faca"],
                "proxima": "dia2_rota13"
            },
            {
                "texto": "3 - Passar silenciosamente e beber a agua do riacho",
                "resultado": "Voce mata a sede, mas continua com fome e sem muitos recursos.",
                "efeitos": {"agua": 2, "energia": -5, "moral": 5},
                "proxima": "dia2_rota13"
            }
        ]
    },

    "dia2_rota10_2": {
        "titulo": "Dia 2 - Casa, celeiro e poco",
        "imagem": "assets/dia2_casa_celeiro_poco.png",
        "cor_fundo": (70, 62, 50),
        "texto": (
            "Chegando mais perto, voce ve uma casa, um celeiro e um poco. Ha fumaca saindo da chamine. "
            "Alguem pode estar no local."
        ),
        "opcoes": [
            {
                "texto": "1 - Ir ao celeiro procurar armas ou ferramentas",
                "resultado": "A porta do celeiro treme. Ao abrir, voce da de cara com varios zumbis.",
                "efeitos": {"energia": -25, "moral": -10},
                "final": {
                    "tipo": "derrota",
                    "titulo": "Final - Celeiro infestado",
                    "texto": "Voce estava muito cansado para fugir e acabou sendo devorado."
                }
            },
            {
                "texto": "2 - Tentar entrar escondido na casa",
                "resultado": "Voce entra pela porta dos fundos, mas faz barulho. O morador quase atira em voce.",
                "efeitos": {"energia": -10, "moral": -5},
                "proxima": "dia2_rota10_2_2"
            },
            {
                "texto": "3 - Ir ao poco beber agua",
                "resultado": "Voce recupera a sede e parte do cansaco, mas o barulho atrai o morador da casa.",
                "efeitos": {"agua": 2, "energia": 5},
                "proxima": "dia2_rota10_2_3"
            }
        ]
    },

    "dia2_rota10_2_2": {
        "titulo": "Dia 2 - Ajuda do morador",
        "imagem": "assets/dia2_morador_casa.png",
        "cor_fundo": (75, 65, 55),
        "texto": (
            "O morador se assusta e quase mata voce, mas percebe que voce esta fraco. "
            "Ele oferece agua e comida."
        ),
        "efeitos_entrada": {"comida": 2, "agua": 2, "moral": 10, "confianca": 1},
        "proxima": "dia2_rota14"
    },

    "dia2_rota10_2_3": {
        "titulo": "Dia 2 - Descanso na casa",
        "imagem": "assets/dia2_descanso_morador.png",
        "cor_fundo": (75, 70, 60),
        "texto": (
            "O morador chega armado, mas ve que voce esta vivo e maltrapilho. Ele oferece comida, "
            "um lugar para descansar e ajuda para se proteger."
        ),
        "efeitos_entrada": {"comida": 2, "agua": 1, "energia": 12, "moral": 12, "confianca": 1},
        "proxima": "dia2_rota14"
    },

    "dia2_rota11": {
        "titulo": "Dia 2 - Terminal sob perseguicao",
        "imagem": "assets/dia2_terminal_horda.png",
        "cor_fundo": (55, 58, 70),
        "texto": (
            "Voce chega a um terminal de onibus, mas ainda esta sendo perseguido por uma horda. "
            "Mesmo ferido e cansado, consegue se esconder ate a noite."
        ),
        "efeitos_entrada": {"energia": -10, "moral": 5, "agua": -1},
        "fim_dia": True,
        "dia": 2
    },

    "dia2_rota12": {
        "titulo": "Dia 2 - Terminal de onibus",
        "imagem": "assets/dia2_terminal.png",
        "cor_fundo": (55, 65, 75),
        "texto": (
            "Voce chega a um terminal de onibus. O lugar nao e perfeito, mas oferece abrigo suficiente "
            "para encerrar o segundo dia."
        ),
        "efeitos_entrada": {"energia": 8, "moral": 8, "comida": -1, "agua": -1},
        "fim_dia": True,
        "dia": 2
    },

    "dia2_rota13": {
        "titulo": "Dia 2 - Tiros ao longe",
        "imagem": "assets/dia2_tiros_longe.png",
        "cor_fundo": (45, 55, 65),
        "texto": (
            "Voce escuta tiros de longe, mas a noite esta chegando. Sem forcas para investigar, "
            "volta para uma cabana e decide descansar."
        ),
        "efeitos_entrada": {"energia": 8, "moral": 4, "comida": -1},
        "fim_dia": True,
        "dia": 2
    },

    "dia2_rota14": {
        "titulo": "Dia 2 - Agradecimento e nova decisao",
        "imagem": "assets/dia2_ajuda_morador.png",
        "cor_fundo": (65, 70, 60),
        "texto": (
            "Voce agradece a ajuda recebida, mas sabe que precisara decidir o que fazer no proximo dia. "
            "Por enquanto, sobreviveu ao Dia 2."
        ),
        "efeitos_entrada": {"energia": 8, "moral": 8},
        "fim_dia": True,
        "dia": 2
    }

}


# ---------------- ESTADO INICIAL ----------------

def criar_estado_inicial():
    return {
        "cena_atual": "inicio",
        "vida": 85,
        "comida": 4,
        "agua": 4,
        "energia": 75,
        "moral": 60,
        "confianca": 0,
        "municao": 0,
        "inventario": set(),
        "modo": "cena",
        "mensagem": "",
        "efeitos_mensagem": "",
        "final_titulo": "",
        "final_texto": "",
        "final_tipo": "",
        "efeitos_aplicados": set()
    }


estado = criar_estado_inicial()


# ---------------- FUNCOES DE TEXTO ----------------

def quebrar_texto(texto, fonte, largura_maxima):
    palavras = texto.split(" ")
    linhas = []
    linha = ""

    for palavra in palavras:
        teste = linha + palavra + " "
        if fonte.size(teste)[0] <= largura_maxima:
            linha = teste
        else:
            if linha:
                linhas.append(linha)
            linha = palavra + " "

    if linha:
        linhas.append(linha)

    return linhas


def desenhar_texto(texto, x, y, fonte, cor=BRANCO, largura_maxima=None, espacamento=28):
    if largura_maxima:
        linhas = quebrar_texto(texto, fonte, largura_maxima)
        for i, linha in enumerate(linhas):
            imagem = fonte.render(linha, True, cor)
            TELA.blit(imagem, (x, y + i * espacamento))
    else:
        imagem = fonte.render(texto, True, cor)
        TELA.blit(imagem, (x, y))


# ---------------- IMAGEM / CENARIO ----------------

def carregar_imagem(caminho_relativo):
    caminho = os.path.join(BASE_DIR, caminho_relativo)

    if os.path.exists(caminho):
        try:
            imagem = pygame.image.load(caminho).convert()
            imagem = pygame.transform.scale(imagem, (LARGURA, ALTURA))
            return imagem
        except pygame.error:
            return None

    return None


def desenhar_cenario(cena):
    imagem = carregar_imagem(cena.get("imagem", ""))

    if imagem:
        TELA.blit(imagem, (0, 0))
        return

    TELA.fill(cena.get("cor_fundo", (45, 45, 45)))

    # Fundo temporario enquanto as imagens reais nao existem.
    pygame.draw.rect(TELA, (20, 20, 20), (0, 410, LARGURA, 190))
    pygame.draw.circle(TELA, (95, 95, 95), (760, 120), 55)
    pygame.draw.rect(TELA, (75, 75, 75), (110, 230, 180, 170))
    pygame.draw.rect(TELA, (50, 50, 50), (360, 260, 220, 140))
    pygame.draw.rect(TELA, (40, 40, 40), (620, 280, 140, 120))

    desenhar_texto("Imagem temporaria do cenario", 300, 285, fonte_texto, AMARELO)


# ---------------- INTERFACE ----------------

def listar_itens():
    if not estado["inventario"]:
        return "nenhum"

    itens = sorted(estado["inventario"])
    return ", ".join(itens)


def desenhar_status():
    pygame.draw.rect(TELA, CINZA_ESCURO, (0, 0, LARGURA, 112))

    linha_1 = (
        f"Vida: {estado['vida']}   "
        f"Comida: {estado['comida']}   "
        f"Agua: {estado['agua']}   "
        f"Energia: {estado['energia']}"
    )

    linha_2 = (
        f"Moral: {estado['moral']}   "
        f"Confianca: {estado['confianca']}"
    )

    if "arma de fogo" in estado["inventario"]:
        linha_2 += f"   Municao: {estado['municao']}"

    linha_3 = f"Itens: {listar_itens()}"

    desenhar_texto(linha_1, 25, 14, fonte_pequena, BRANCO)
    desenhar_texto(linha_2, 25, 41, fonte_pequena, BRANCO)
    desenhar_texto(linha_3, 25, 68, fonte_pequena, AMARELO)


def desenhar_painel():
    pygame.draw.rect(TELA, (15, 15, 15), (40, 320, 820, 240))
    pygame.draw.rect(TELA, BRANCO, (40, 320, 820, 240), 2)


def desenhar_cena():
    cena = cenas[estado["cena_atual"]]

    desenhar_cenario(cena)
    desenhar_status()
    desenhar_painel()

    desenhar_texto(cena["titulo"], 65, 340, fonte_titulo, AMARELO)
    desenhar_texto(cena["texto"], 65, 386, fonte_texto, BRANCO, 760)

    if cena.get("opcoes"):
        desenhar_texto("Pressione ENTER para ver suas escolhas", 65, 525, fonte_texto, VERDE)
    else:
        desenhar_texto("Pressione ENTER para continuar", 65, 525, fonte_texto, VERDE)


def desenhar_escolhas():
    cena = cenas[estado["cena_atual"]]

    desenhar_cenario(cena)
    desenhar_status()
    desenhar_painel()

    desenhar_texto("Escolha sua acao:", 65, 340, fonte_titulo, AMARELO)

    y = 392
    for i, opcao in enumerate(cena["opcoes"], start=1):
        texto = opcao["texto"]
        # Se o texto ja comecar com numero, mantem como esta.
        if not texto.strip().startswith(str(i)):
            texto = f"{i} - {texto}"
        desenhar_texto(texto, 65, y, fonte_texto, BRANCO, 760, espacamento=24)
        y += 55


def desenhar_resultado():
    cena = cenas[estado["cena_atual"]]

    desenhar_cenario(cena)
    desenhar_status()
    desenhar_painel()

    desenhar_texto("Resultado", 65, 340, fonte_titulo, AMARELO)
    desenhar_texto(estado["mensagem"], 65, 390, fonte_texto, BRANCO, 760, espacamento=25)

    if estado["efeitos_mensagem"]:
        desenhar_texto(estado["efeitos_mensagem"], 65, 470, fonte_pequena, AMARELO, 760, espacamento=22)

    desenhar_texto("Pressione ENTER para continuar", 65, 525, fonte_texto, VERDE)


def desenhar_fim_dia():
    TELA.fill(PRETO)

    cena = cenas[estado["cena_atual"]]
    dia = cena.get("dia", 1)

    desenhar_texto(f"Fim do Dia {dia}", 335, 120, fonte_titulo, VERDE)
    desenhar_texto(
        f"Voce sobreviveu ao Dia {dia}. Suas escolhas definiram recursos, itens e condicoes "
        "que poderao influenciar os proximos acontecimentos.",
        150,
        190,
        fonte_texto,
        BRANCO,
        610
    )

    resumo_1 = (
        f"Vida: {estado['vida']} | Comida: {estado['comida']} | Agua: {estado['agua']} | "
        f"Energia: {estado['energia']}"
    )
    resumo_2 = f"Moral: {estado['moral']} | Confianca: {estado['confianca']}"

    if "arma de fogo" in estado["inventario"]:
        resumo_2 += f" | Municao: {estado['municao']}"

    desenhar_texto(resumo_1, 150, 310, fonte_texto, AMARELO, 650)
    desenhar_texto(resumo_2, 150, 345, fonte_texto, AMARELO, 650)
    desenhar_texto(f"Itens: {listar_itens()}", 150, 380, fonte_texto, AMARELO, 650)

    if cena.get("proxima_dia"):
        desenhar_texto("Pressione ENTER para iniciar o Dia 2", 255, 465, fonte_texto, BRANCO)
        desenhar_texto("Pressione R para reiniciar ou ESC para sair", 240, 500, fonte_pequena, BRANCO)
    else:
        desenhar_texto("Pressione R para reiniciar ou ESC para sair", 240, 465, fonte_texto, BRANCO)


def desenhar_final():
    TELA.fill(PRETO)

    cor = VERMELHO if estado["final_tipo"] == "derrota" else VERDE

    desenhar_texto(estado["final_titulo"], 250, 135, fonte_titulo, cor)
    desenhar_texto(estado["final_texto"], 150, 210, fonte_texto, BRANCO, 610)

    resumo = (
        f"Vida: {estado['vida']} | Energia: {estado['energia']} | Moral: {estado['moral']} | "
        f"Confianca: {estado['confianca']}"
    )
    desenhar_texto(resumo, 150, 340, fonte_pequena, AMARELO, 650)
    desenhar_texto(f"Itens: {listar_itens()}", 150, 370, fonte_pequena, AMARELO, 650)

    if "arma de fogo" in estado["inventario"]:
        desenhar_texto(f"Municao: {estado['municao']}", 150, 400, fonte_pequena, AMARELO)

    desenhar_texto("Pressione R para reiniciar ou ESC para sair", 240, 465, fonte_texto, BRANCO)


def desenhar_tela():
    if estado["modo"] == "cena":
        desenhar_cena()
    elif estado["modo"] == "escolhas":
        desenhar_escolhas()
    elif estado["modo"] == "resultado":
        desenhar_resultado()
    elif estado["modo"] == "fim_dia":
        desenhar_fim_dia()
    elif estado["modo"] == "final":
        desenhar_final()

    pygame.display.update()


# ---------------- LOGICA ----------------

def limitar_valores():
    estado["vida"] = max(0, min(100, estado["vida"]))
    estado["comida"] = max(0, min(10, estado["comida"]))
    estado["agua"] = max(0, min(10, estado["agua"]))
    estado["energia"] = max(0, min(100, estado["energia"]))
    estado["moral"] = max(0, min(100, estado["moral"]))
    estado["confianca"] = max(-5, min(10, estado["confianca"]))
    estado["municao"] = max(0, estado["municao"])


def aplicar_efeitos(efeitos):
    for recurso, valor in efeitos.items():
        if recurso in estado:
            estado[recurso] += valor

    limitar_valores()


def adicionar_itens(itens):
    for item in itens:
        estado["inventario"].add(item)


def formatar_alteracoes(efeitos, itens, municao_delta):
    partes = []

    for recurso, valor in efeitos.items():
        if recurso == "infeccao":
            continue
        sinal = "+" if valor > 0 else ""
        nome = recurso.capitalize()
        partes.append(f"{nome} {sinal}{valor}")

    for item in itens:
        partes.append(f"Item adquirido: {item}")

    if municao_delta != 0:
        sinal = "+" if municao_delta > 0 else ""
        partes.append(f"Municao {sinal}{municao_delta}")

    if not partes:
        return ""

    return "Alteracoes: " + " | ".join(partes)


def mostrar_final(dados_final):
    estado["final_titulo"] = dados_final["titulo"]
    estado["final_texto"] = dados_final["texto"]
    estado["final_tipo"] = dados_final.get("tipo", "derrota")
    estado["modo"] = "final"


def verificar_derrota_automatica():
    if estado["vida"] <= 0:
        mostrar_final({
            "tipo": "derrota",
            "titulo": "Final - Fim da jornada",
            "texto": "Sua vida chegou a zero. Voce nao conseguiu continuar no jogo."
        })
        return True

    if estado["energia"] <= 0:
        mostrar_final({
            "tipo": "derrota",
            "titulo": "Final - Exaustao",
            "texto": "Sua energia acabou completamente. Sem forcas para continuar, voce foi alcancado pelos zumbis."
        })
        return True

    if estado["moral"] <= 0:
        mostrar_final({
            "tipo": "derrota",
            "titulo": "Final - Desespero",
            "texto": "Sua moral chegou a zero. O medo tomou conta e voce nao conseguiu continuar."
        })
        return True

    return False


def aplicar_efeitos_de_entrada(id_cena):
    cena = cenas[id_cena]

    if id_cena in estado["efeitos_aplicados"]:
        return

    efeitos = cena.get("efeitos_entrada", {})
    if efeitos:
        aplicar_efeitos(efeitos)
        estado["efeitos_aplicados"].add(id_cena)


def entrar_cena(id_cena):
    estado["cena_atual"] = id_cena
    aplicar_efeitos_de_entrada(id_cena)

    if verificar_derrota_automatica():
        return

    cena = cenas[id_cena]

    if cena.get("final"):
        mostrar_final(cena["final"])
    else:
        estado["modo"] = "cena"


def aplicar_escolha(indice):
    cena = cenas[estado["cena_atual"]]

    if indice < 0 or indice >= len(cena["opcoes"]):
        return

    opcao = cena["opcoes"][indice]

    efeitos = opcao.get("efeitos", {})
    itens = opcao.get("itens_add", [])
    municao_delta = opcao.get("municao_delta", 0)

    aplicar_efeitos(efeitos)
    adicionar_itens(itens)
    estado["municao"] += municao_delta
    limitar_valores()

    estado["mensagem"] = opcao["resultado"]
    estado["efeitos_mensagem"] = formatar_alteracoes(efeitos, itens, municao_delta)

    if opcao.get("final"):
        mostrar_final(opcao["final"])
        return

    if verificar_derrota_automatica():
        return

    estado["proxima_cena"] = opcao.get("proxima")
    estado["modo"] = "resultado"


def avancar_cena():
    cena = cenas[estado["cena_atual"]]

    if estado["modo"] == "resultado":
        proxima = estado.get("proxima_cena")
    else:
        proxima = cena.get("proxima")

    if proxima:
        entrar_cena(proxima)


def reiniciar_jogo():
    global estado
    estado = criar_estado_inicial()


# ---------------- LOOP PRINCIPAL ----------------

def loop_principal():
    while True:
        clock.tick(FPS)

        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()

                if estado["modo"] == "cena":
                   cena = cenas[estado["cena_atual"]]

                   if evento.key == pygame.K_RETURN:
                      if cena.get("fim_dia"):
                       estado["modo"] = "fim_dia"
                      elif cena.get("opcoes"):
                       estado["modo"] = "escolhas"
                      else:
                        avancar_cena()

                elif estado["modo"] == "escolhas":
                    teclas_opcoes = [
                        pygame.K_1, pygame.K_2, pygame.K_3,
                        pygame.K_4, pygame.K_5, pygame.K_6,
                        pygame.K_7, pygame.K_8, pygame.K_9
                    ]

                    for i, tecla in enumerate(teclas_opcoes):
                        if evento.key == tecla:
                            aplicar_escolha(i)

                elif estado["modo"] == "resultado":
                    if evento.key == pygame.K_RETURN:
                        avancar_cena()

                elif estado["modo"] == "fim_dia":
                    cena = cenas[estado["cena_atual"]]
                    if evento.key == pygame.K_RETURN and cena.get("proxima_dia"):
                        entrar_cena(cena["proxima_dia"])
                    elif evento.key == pygame.K_r:
                        reiniciar_jogo()

                elif estado["modo"] == "final":
                    if evento.key == pygame.K_r:
                        reiniciar_jogo()

        desenhar_tela()


if __name__ == "__main__":
    loop_principal()
