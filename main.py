import os
import sys
import pygame

# =========================
# CONFIGURACOES GERAIS
# =========================
LARGURA = 1580
ALTURA = 920
FPS = 60

TITULO_JANELA = "Seven Days of Fear"
PASTA_ASSETS = "assets/imagens"

# Cores
BRANCO = (155, 155, 155)
PRETO = (20, 20, 20)
CINZA_ESCURO = (35, 35, 35)
CINZA = (95, 95, 95)
CINZA_CLARO = (170, 170, 170)
VERDE = (42, 86, 62)
VERDE_CLARO = (92, 130, 85)
AZUL_CLARO = (92, 125, 150)
VERMELHO_ESCURO = (105, 35, 35)
AMARELO_CLARO = (220, 205, 135)

# Layout
MARGEM = 32
STATUS_LARGURA = 330
AREA_PRINCIPAL_LARGURA = LARGURA - STATUS_LARGURA - (MARGEM * 3)

RET_IMAGEM = pygame.Rect(MARGEM, 5, AREA_PRINCIPAL_LARGURA, 450)
RET_TEXTO = pygame.Rect(MARGEM, 412, AREA_PRINCIPAL_LARGURA, 120)
RET_OPCOES = pygame.Rect(MARGEM, 550, AREA_PRINCIPAL_LARGURA, 220)
RET_STATUS = pygame.Rect(MARGEM * 2 + AREA_PRINCIPAL_LARGURA, 82, STATUS_LARGURA, 688)

# =========================
# ROTEIRO / CENAS
# =========================
cenas = {
    'inicio': {
        'dia': 1,
        'titulo': 'DIA 1 - O DESPERTAR',
        'texto': (
            'O jogador acorda sozinho em um apartamento enquanto a cidade afunda no caos. Lá fora, '
            'sirenes ecoam, carros abandonados bloqueiam as ruas e gritos se misturam à fumaça. A '
            'televisão ainda está ligada, exibindo uma notícia interrompida sobre ataques violentos. '
            'A imagem falha, o som estoura, e a transmissão cai em estática.'
        ),
        'cor_fundo': BRANCO,
        'opcoes': [
            {
                'texto': 'Fugir pelo beco',
                'resultado': 'Você escolhe: Fugir pelo beco. A primeira rota começa agora.',
                'proxima': 'd1_r1_c1',
                'efeitos': {
                    'energia': -4,
                },
                'itens_add': ['mochila', 'canivete', 'água', 'comida'],
            },
            {
                'texto': 'Sair pelo prédio e seguir pela rua principal',
                'resultado': (
                    'Você escolhe: Sair pelo prédio e seguir pela rua principal. A primeira rota começa '
                    'agora.'
                ),
                'proxima': 'd1_r2_c1',
                'efeitos': {
                    'energia': -4,
                },
                'itens_add': ['mochila'],
            },
            {
                'texto': 'Procurar comida e suprimentos no prédio',
                'resultado': 'Você escolhe: Procurar comida e suprimentos no prédio. A primeira rota começa agora.',
                'proxima': 'd1_r3_c1',
                'efeitos': {
                    'energia': -4,
                    'comida': 1,
                    'agua': 1,
                },
                'itens_add': ['mochila'],
            },
            {
                'texto': 'Ajudar outros moradores',
                'resultado': 'Você escolhe: Ajudar outros moradores. A primeira rota começa agora.',
                'proxima': 'd1_r4_c1',
                'efeitos': {
                    'energia': -4,
                    'moral': 5,
                    'confianca': 2,
                },
                'itens_add': ['mochila'],
            },
        ],
    },
    'd2_r1_inicio': {
        'dia': 2,
        'titulo': 'DIA 2 - AMANHECER FORA DO APARTAMENTO',
        'texto': (
            'Quem escapou para as ruas acorda com o sol cinza refletido em vidros quebrados. A cidade '
            'não grita mais como na noite anterior; agora ela geme. Mensagens militares falhadas '
            'falam sobre isolamento, triagem e um ponto de evacuação chamado Operação Aurora.'
        ),
        'cor_fundo': BRANCO,
        'efeitos_entrada': {
            'comida': -1,
            'agua': -1,
            'energia': -4,
        },
        'proxima': 'd2_r1_c1',
    },
    'd2_r2_inicio': {
        'dia': 2,
        'titulo': 'DIA 2 - AMANHECER FORA DO APARTAMENTO',
        'texto': (
            'Quem escapou para as ruas acorda com o sol cinza refletido em vidros quebrados. A cidade '
            'não grita mais como na noite anterior; agora ela geme. Mensagens militares falhadas '
            'falam sobre isolamento, triagem e um ponto de evacuação chamado Operação Aurora.'
        ),
        'cor_fundo': BRANCO,
        'efeitos_entrada': {
            'comida': -1,
            'agua': -1,
            'energia': -4,
        },
        'proxima': 'd2_r2_c1',
    },
    'd2_r3_inicio': {
        'dia': 2,
        'titulo': 'DIA 2 - O PRÉDIO SEM ÁGUA',
        'texto': (
            'Quem permaneceu no prédio acorda com as torneiras secas. A comida encontrada no Dia 1 '
            'não servirá por muito tempo sem água. O silêncio dos andares superiores parece uma '
            'ameaça tão grande quanto a rua.'
        ),
        'cor_fundo': BRANCO,
        'efeitos_entrada': {
            'comida': -1,
            'agua': -1,
            'energia': -4,
        },
        'proxima': 'd2_r3_c1',
    },
    'd2_r4_inicio': {
        'dia': 2,
        'titulo': 'DIA 2 - AMANHECER FORA DO APARTAMENTO',
        'texto': (
            'Quem escapou para as ruas acorda com o sol cinza refletido em vidros quebrados. A cidade '
            'não grita mais como na noite anterior; agora ela geme. Mensagens militares falhadas '
            'falam sobre isolamento, triagem e um ponto de evacuação chamado Operação Aurora.'
        ),
        'cor_fundo': BRANCO,
        'efeitos_entrada': {
            'comida': -1,
            'agua': -1,
            'energia': -4,
        },
        'proxima': 'd2_r4_c1',
    },
    'd3_r1_inicio': {
        'dia': 3,
        'titulo': 'DIA 3 - A CIDADE APRENDE A CAÇAR',
        'texto': (
            'Fora do prédio, os sobreviventes entendem que os mortos não são o único perigo. '
            'Saqueadores, fome e decisões ruins começam a matar tanto quanto mordidas. No rádio, a '
            'palavra Aurora aparece de novo, sempre incompleta.'
        ),
        'cor_fundo': BRANCO,
        'efeitos_entrada': {
            'comida': -1,
            'agua': -1,
            'energia': -4,
        },
        'proxima': 'd3_r1_c1',
    },
    'd3_r2_inicio': {
        'dia': 3,
        'titulo': 'DIA 3 - A CIDADE APRENDE A CAÇAR',
        'texto': (
            'Fora do prédio, os sobreviventes entendem que os mortos não são o único perigo. '
            'Saqueadores, fome e decisões ruins começam a matar tanto quanto mordidas. No rádio, a '
            'palavra Aurora aparece de novo, sempre incompleta.'
        ),
        'cor_fundo': BRANCO,
        'efeitos_entrada': {
            'comida': -1,
            'agua': -1,
            'energia': -4,
        },
        'proxima': 'd3_r2_c1',
    },
    'd3_r3_inicio': {
        'dia': 3,
        'titulo': 'DIA 3 - FREQUÊNCIAS NO ESCURO',
        'texto': (
            'No prédio, um chiado estático acorda o personagem. Um rádio ou celular capta uma '
            'transmissão militar fraca sobre um ponto de extração, mas a mensagem corta antes das '
            'coordenadas. É preciso encontrar antena melhor.'
        ),
        'cor_fundo': BRANCO,
        'efeitos_entrada': {
            'comida': -1,
            'agua': -1,
            'energia': -4,
        },
        'proxima': 'd3_r3_c1',
    },
    'd3_r4_inicio': {
        'dia': 3,
        'titulo': 'DIA 3 - A CIDADE APRENDE A CAÇAR',
        'texto': (
            'Fora do prédio, os sobreviventes entendem que os mortos não são o único perigo. '
            'Saqueadores, fome e decisões ruins começam a matar tanto quanto mordidas. No rádio, a '
            'palavra Aurora aparece de novo, sempre incompleta.'
        ),
        'cor_fundo': BRANCO,
        'efeitos_entrada': {
            'comida': -1,
            'agua': -1,
            'energia': -4,
        },
        'proxima': 'd3_r4_c1',
    },
    'd4_r1_inicio': {
        'dia': 4,
        'titulo': 'DIA 4 - ROTAS DE EVACUAÇÃO',
        'texto': (
            'Fora do prédio, todos os caminhos apontam para fora da cidade: escola, rodovia, '
            'terminal, ponte e base militar. A Operação Aurora não é mais boato; é a única esperança.'
        ),
        'cor_fundo': BRANCO,
        'efeitos_entrada': {
            'comida': -1,
            'agua': -1,
            'energia': -4,
        },
        'proxima': 'd4_r1_c1',
    },
    'd4_r2_inicio': {
        'dia': 4,
        'titulo': 'DIA 4 - ROTAS DE EVACUAÇÃO',
        'texto': (
            'Fora do prédio, todos os caminhos apontam para fora da cidade: escola, rodovia, '
            'terminal, ponte e base militar. A Operação Aurora não é mais boato; é a única esperança.'
        ),
        'cor_fundo': BRANCO,
        'efeitos_entrada': {
            'comida': -1,
            'agua': -1,
            'energia': -4,
        },
        'proxima': 'd4_r2_c1',
    },
    'd4_r3_inicio': {
        'dia': 4,
        'titulo': 'DIA 4 - O APARTAMENTO SITIADO',
        'texto': (
            'Dentro do prédio, o estoque do personagem está bom, mas essa vantagem começa a atrair '
            'vivos desesperados. O maior perigo do Dia 4 pode bater à porta usando voz humana.'
        ),
        'cor_fundo': BRANCO,
        'efeitos_entrada': {
            'comida': -1,
            'agua': -1,
            'energia': -4,
        },
        'proxima': 'd4_r3_c1',
    },
    'd4_r4_inicio': {
        'dia': 4,
        'titulo': 'DIA 4 - ROTAS DE EVACUAÇÃO',
        'texto': (
            'Fora do prédio, todos os caminhos apontam para fora da cidade: escola, rodovia, '
            'terminal, ponte e base militar. A Operação Aurora não é mais boato; é a única esperança.'
        ),
        'cor_fundo': BRANCO,
        'efeitos_entrada': {
            'comida': -1,
            'agua': -1,
            'energia': -4,
        },
        'proxima': 'd4_r4_c1',
    },
    'd5_r1_inicio': {
        'dia': 5,
        'titulo': 'DIA 5 - ABRIGOS NÃO EXISTEM MAIS',
        'texto': (
            'Quem estava em escola, terminal, rodovia ou loja descobre a mesma verdade: todo abrigo '
            'cai quando faz barulho em excesso ou guarda recursos em excesso. Saqueadores e hordas '
            'começam a seguir rastros humanos.'
        ),
        'cor_fundo': BRANCO,
        'efeitos_entrada': {
            'comida': -1,
            'agua': -1,
            'energia': -4,
        },
        'proxima': 'd5_r1_c1',
    },
    'd5_r2_inicio': {
        'dia': 5,
        'titulo': 'DIA 5 - ABRIGOS NÃO EXISTEM MAIS',
        'texto': (
            'Quem estava em escola, terminal, rodovia ou loja descobre a mesma verdade: todo abrigo '
            'cai quando faz barulho em excesso ou guarda recursos em excesso. Saqueadores e hordas '
            'começam a seguir rastros humanos.'
        ),
        'cor_fundo': BRANCO,
        'efeitos_entrada': {
            'comida': -1,
            'agua': -1,
            'energia': -4,
        },
        'proxima': 'd5_r2_c1',
    },
    'd5_r3_inicio': {
        'dia': 5,
        'titulo': 'DIA 5 - FUMAÇA NO PRÉDIO',
        'texto': (
            'Quem ficou no prédio acorda com fumaça invadindo os cômodos. O bloco ao lado está em '
            'chamas. Ficar parado já não é opção. O prédio, antes abrigo, tornou-se armadilha.'
        ),
        'cor_fundo': BRANCO,
        'efeitos_entrada': {
            'comida': -1,
            'agua': -1,
            'energia': -4,
        },
        'proxima': 'd5_r3_c1',
    },
    'd5_r4_inicio': {
        'dia': 5,
        'titulo': 'DIA 5 - ABRIGOS NÃO EXISTEM MAIS',
        'texto': (
            'Quem estava em escola, terminal, rodovia ou loja descobre a mesma verdade: todo abrigo '
            'cai quando faz barulho em excesso ou guarda recursos em excesso. Saqueadores e hordas '
            'começam a seguir rastros humanos.'
        ),
        'cor_fundo': BRANCO,
        'efeitos_entrada': {
            'comida': -1,
            'agua': -1,
            'energia': -4,
        },
        'proxima': 'd5_r4_c1',
    },
    'd7_r1_inicio': {
        'dia': 7,
        'titulo': 'DIA 7 - PORTÕES DA BASE',
        'texto': (
            'Quem chegou pela ponte, caminhão ou ônibus encontra a base militar cercada por filas, '
            'soldados, grades e tiros. A zona segura existe, mas está à beira do colapso. Entrar não '
            'significa ser livre; significa sobreviver à triagem.'
        ),
        'cor_fundo': BRANCO,
        'efeitos_entrada': {
            'comida': -1,
            'agua': -1,
            'energia': -4,
        },
        'proxima': 'd7_r1_c1',
    },
    'd7_r2_inicio': {
        'dia': 7,
        'titulo': 'DIA 7 - PORTÕES DA BASE',
        'texto': (
            'Quem chegou pela ponte, caminhão ou ônibus encontra a base militar cercada por filas, '
            'soldados, grades e tiros. A zona segura existe, mas está à beira do colapso. Entrar não '
            'significa ser livre; significa sobreviver à triagem.'
        ),
        'cor_fundo': BRANCO,
        'efeitos_entrada': {
            'comida': -1,
            'agua': -1,
            'energia': -4,
        },
        'proxima': 'd7_r2_c1',
    },
    'd7_r3_inicio': {
        'dia': 7,
        'titulo': 'DIA 7 - ESTÁDIO DE FUTEBOL',
        'texto': (
            'Quem seguiu a rota de suprimentos vê o estádio ao longe. Helicópteros militares pousam e '
            'decolam enquanto hordas são atraídas pelo barulho. O resgate civil da Operação Aurora '
            'está terminando.'
        ),
        'cor_fundo': BRANCO,
        'efeitos_entrada': {
            'comida': -1,
            'agua': -1,
            'energia': -4,
        },
        'proxima': 'd7_r3_c1',
    },
    'd7_r4_inicio': {
        'dia': 7,
        'titulo': 'DIA 7 - PORTÕES DA BASE',
        'texto': (
            'Quem chegou pela ponte, caminhão ou ônibus encontra a base militar cercada por filas, '
            'soldados, grades e tiros. A zona segura existe, mas está à beira do colapso. Entrar não '
            'significa ser livre; significa sobreviver à triagem.'
        ),
        'cor_fundo': BRANCO,
        'efeitos_entrada': {
            'comida': -1,
            'agua': -1,
            'energia': -4,
        },
        'proxima': 'd7_r4_c1',
    },
    'd1_r1_fim_1': {
        'dia': 1,
        'titulo': 'FIM DO DIA 1 A',
        'texto': 'Abrigo com o grupo, reputação positiva, equipamentos e comida.',
        'cor_fundo': VERDE_CLARO,
        'fim_dia': True,
        'proxima_dia': 'd2_r1_inicio',
    },
    'd1_r1_fim_2': {
        'dia': 1,
        'titulo': 'FIM DO DIA 1 B',
        'texto': (
            'Abrigo sozinho no prédio interditado, com menos risco imediato, mas sem aliados para os '
            'dias seguintes.'
        ),
        'cor_fundo': VERDE_CLARO,
        'fim_dia': True,
        'proxima_dia': 'd2_r1_inicio',
    },
    'd1_r1_c1': {
        'dia': 1,
        'titulo': 'DIA 1 - FUGIR PELO BECO: O CAOS',
        'texto': (
            'O personagem desce pela escada de incêndio dos fundos levando uma mochila com água, '
            'barras de proteína, um canivete e o casaco que estava no sofá. Ao tocar o chão do beco, '
            'encontra a rua paralela tomada por sirenes, fumaça e pessoas correndo. Jorge, '
            'comerciante da vizinhança e seu amigo, grita seu nome do outro lado da rua. Antes que '
            'consiga responder, sete infectados o cercam.'
        ),
        'cor_fundo': VERDE,
        'opcoes': [
            {
                'texto': 'Tentar salvar Jorge.',
                'resultado': 'A escolha cobra seu preço antes que exista tempo para voltar atrás.',
                'final': {
                    'tipo': 'derrota',
                    'titulo': 'MORTE 1',
                    'texto': (
                        'Tentar salvar Jorge em meio aos sete infectados; o personagem é cercado e mordido antes '
                        'de alcançar o amigo.'
                    ),
                },
                'efeitos': {
                    'vida': -100,
                },
                'qualidade': 'morte',
            },
            {
                'texto': 'Proteger-se e não ajudar Jorge.',
                'resultado': 'A decisão leva ao próximo momento: Seu Amigo.',
                'proxima': 'd1_r1_c2',
                'efeitos': {
                    'energia': -4,
                    'moral': 5,
                    'confianca': 2,
                },
                'itens_add': ['canivete', 'mochila', 'aliado Jorge'],
            },
        ],
    },
    'd1_r1_c2': {
        'dia': 1,
        'titulo': 'DIA 1 - FUGIR PELO BECO: SEU AMIGO',
        'texto': (
            'Ao escolher proteger-se, o personagem assiste Jorge ser mordido brutalmente. O choque '
            'quase o paralisa, mas ele entende que qualquer grito chamará a atenção das criaturas. A '
            'culpa nasce ali, no primeiro dia, e acompanhará essa rota até o final.'
        ),
        'cor_fundo': VERDE,
        'proxima': 'd1_r1_c3',
    },
    'd1_r1_c3': {
        'dia': 1,
        'titulo': 'DIA 1 - FUGIR PELO BECO: CAMINHO DOS BECOS',
        'texto': (
            'Ele atravessa a avenida por trás de carros batidos e segue por becos estreitos. Na '
            'avenida principal, em outra direção, é possível ouvir um grupo tentando chegar ao '
            'terminal de ônibus; essa é a primeira conexão com a rota heroica, mas aqui o personagem '
            'escolhe desaparecer nas sombras.'
        ),
        'cor_fundo': VERDE,
        'opcoes': [
            {
                'texto': 'Seguir pela avenida.',
                'resultado': 'A decisão leva ao próximo momento: Desconhecidos.',
                'proxima': 'd1_r1_c4',
                'efeitos': {
                    'energia': -4,
                },
                'itens_add': ['ônibus'],
            },
            {
                'texto': 'Continuar pelos becos.',
                'resultado': 'A decisão leva ao próximo momento: Desconhecidos.',
                'proxima': 'd1_r1_c4',
                'efeitos': {
                    'energia': -4,
                },
                'itens_add': ['ônibus'],
            },
        ],
    },
    'd1_r1_c4': {
        'dia': 1,
        'titulo': 'DIA 1 - FUGIR PELO BECO: DESCONHECIDOS',
        'texto': (
            'Em um estacionamento pequeno, dois homens estão encurralados por dois infectados. Mais '
            'atrás, duas mulheres e uma criança choram sem saber o que fazer. Os homens chamam os '
            'infectados pelos nomes, como se ainda fossem amigos, mas os olhos vazios das criaturas '
            'mostram que já não há ninguém ali.'
        ),
        'cor_fundo': VERDE,
        'opcoes': [
            {
                'texto': 'Ajudar os desconhecidos.',
                'resultado': 'A decisão leva ao próximo momento: Seguindo em Frente.',
                'proxima': 'd1_r1_c5',
                'efeitos': {
                    'energia': -4,
                    'moral': 5,
                    'confianca': 2,
                },
                'itens_add': [],
            },
            {
                'texto': 'Ignorar o grupo e seguir sozinho.',
                'resultado': 'A decisão leva ao próximo momento: Seguindo em Frente.',
                'proxima': 'd1_r1_c5',
                'efeitos': {
                    'energia': -4,
                    'moral': -4,
                    'confianca': -1,
                },
                'itens_add': [],
            },
        ],
    },
    'd1_r1_c5': {
        'dia': 1,
        'titulo': 'DIA 1 - FUGIR PELO BECO: SEGUINDO EM FRENTE',
        'texto': (
            'O personagem acerta os infectados na cabeça com o canivete e pedaços de madeira '
            'encontrados no chão. Depois entrega água ao grupo e explica que viu Jorge morrer da '
            'mesma forma. José, Pedro, Lena, Joice e o pequeno Davi passam a vê-lo como alguém frio, '
            'mas útil.'
        ),
        'cor_fundo': VERDE,
        'proxima': 'd1_r1_c6',
    },
    'd1_r1_c6': {
        'dia': 1,
        'titulo': 'DIA 1 - FUGIR PELO BECO: A LOJA DE PESCA',
        'texto': (
            'Com a noite chegando, o grupo encontra uma loja de pesca. As prateleiras ainda guardam '
            'lanternas, cordas, facas, anzóis e mochilas. A loja também cria uma ponte com a rota de '
            'suprimentos, pois itens como lanterna e corda poderão ser decisivos em outros caminhos.'
        ),
        'cor_fundo': VERDE,
        'opcoes': [
            {
                'texto': 'Vasculhar a loja de pesca.',
                'resultado': 'A decisão leva ao próximo momento: O Susto.',
                'proxima': 'd1_r1_c7',
                'efeitos': {
                    'energia': -4,
                    'comida': 1,
                    'agua': 1,
                },
                'itens_add': ['mochila', 'lanterna', 'corda', 'faca de caça'],
            },
            {
                'texto': 'Passar direto para não perder tempo.',
                'resultado': 'A decisão leva ao próximo momento: O Susto.',
                'proxima': 'd1_r1_c7',
                'efeitos': {
                    'energia': -4,
                },
                'itens_add': ['mochila', 'lanterna', 'corda', 'faca de caça'],
            },
        ],
    },
    'd1_r1_c7': {
        'dia': 1,
        'titulo': 'DIA 1 - FUGIR PELO BECO: O SUSTO',
        'texto': (
            'Enquanto todos recolhem itens, alguns infectados batem contra a vitrine. Davi grita. O '
            'vidro estala. O personagem está mais perto da criança do que qualquer outro adulto.'
        ),
        'cor_fundo': VERDE,
        'opcoes': [
            {
                'texto': 'Pegar a criança.',
                'resultado': 'A decisão leva ao próximo momento: Prédio Interditado.',
                'proxima': 'd1_r1_c8',
                'efeitos': {
                    'energia': -4,
                },
                'itens_add': ['aliado Davi'],
            },
            {
                'texto': 'Correr para os fundos sozinho.',
                'resultado': 'A escolha cobra seu preço antes que exista tempo para voltar atrás.',
                'final': {
                    'tipo': 'derrota',
                    'titulo': 'MORTE 2',
                    'texto': (
                        'Correr sozinho na loja durante o ataque; a criança grita, os infectados entram e o '
                        'personagem fica preso entre a vitrine quebrada e o corredor dos fundos.'
                    ),
                },
                'efeitos': {
                    'vida': -100,
                },
                'qualidade': 'morte',
            },
        ],
    },
    'd1_r1_c8': {
        'dia': 1,
        'titulo': 'DIA 1 - FUGIR PELO BECO: PRÉDIO INTERDITADO',
        'texto': (
            'Carregando Davi, o personagem atravessa o beco com o grupo e encontra um prédio '
            'interditado. As janelas estão tampadas, os corredores estão vazios e o local parece '
            'abandonado há anos. Não é confortável, mas é melhor do que a rua.'
        ),
        'cor_fundo': VERDE,
        'opcoes': [
            {
                'texto': 'Entrar e reforçar as portas.',
                'resultado': 'A decisão leva ao próximo momento: O Abrigo.',
                'proxima': 'd1_r1_c9',
                'efeitos': {
                    'energia': -8,
                },
                'itens_add': ['aliado Davi'],
            },
            {
                'texto': 'Continuar andando durante a noite.',
                'resultado': 'A decisão leva ao próximo momento: O Abrigo.',
                'proxima': 'd1_r1_c9',
                'efeitos': {
                    'energia': -4,
                },
                'itens_add': ['aliado Davi'],
            },
        ],
    },
    'd1_r1_c9': {
        'dia': 1,
        'titulo': 'DIA 1 - FUGIR PELO BECO: O ABRIGO',
        'texto': (
            'Todos estão exaustos. O personagem sugere turnos de vigia, começando por ele mesmo. Ao '
            'fechar os olhos por poucos segundos, vê Jorge sendo cercado novamente. Ele salvou cinco '
            'pessoas, mas não consegue esquecer a primeira que deixou para trás.'
        ),
        'cor_fundo': VERDE,
        'opcoes': [
            {
                'texto': 'Revezar para dormir.',
                'resultado': 'Essa decisão encerra o caminho iniciado neste dia.',
                'proxima': 'd1_r1_fim_1',
                'efeitos': {
                    'energia': -4,
                },
                'itens_add': ['aliado Jorge'],
                'qualidade': 'media',
            },
            {
                'texto': 'Dormir todos ao mesmo tempo.',
                'resultado': 'Essa decisão encerra o caminho iniciado neste dia.',
                'proxima': 'd1_r1_fim_2',
                'efeitos': {
                    'energia': -4,
                },
                'itens_add': ['aliado Jorge'],
                'qualidade': 'media',
            },
        ],
    },
    'd1_r2_fim_1': {
        'dia': 1,
        'titulo': 'FIM DO DIA 1 A',
        'texto': 'Rua principal com grupo pequeno e barra de ferro como arma improvisada.',
        'cor_fundo': VERDE_CLARO,
        'fim_dia': True,
        'proxima_dia': 'd2_r2_inicio',
    },
    'd1_r2_fim_2': {
        'dia': 1,
        'titulo': 'FIM DO DIA 1 B',
        'texto': 'Rua principal sozinho, com barra de ferro e conhecimento dos caminhos subterrâneos.',
        'cor_fundo': VERDE_CLARO,
        'fim_dia': True,
        'proxima_dia': 'd2_r2_inicio',
    },
    'd1_r2_c1': {
        'dia': 1,
        'titulo': 'DIA 1 - SAIR PELO PRÉDIO E SEGUIR PELA RUA PRINCIPAL: O CORREDOR VAZIO',
        'texto': (
            'Ao abrir a porta, o corredor está quase totalmente escuro. Lâmpadas piscam, móveis '
            'bloqueiam parte da passagem e manchas de sangue marcam as paredes. Duas portas estão '
            'abertas, mas o silêncio é estranho em excesso para um prédio normalmente cheio de vida.'
        ),
        'cor_fundo': VERDE,
        'opcoes': [
            {
                'texto': 'Investigar apartamentos.',
                'resultado': 'A decisão leva ao próximo momento: O Elevador.',
                'proxima': 'd1_r2_c2',
                'efeitos': {
                    'energia': -4,
                },
                'itens_add': [],
            },
            {
                'texto': 'Seguir para a escada.',
                'resultado': 'A decisão leva ao próximo momento: O Elevador.',
                'proxima': 'd1_r2_c2',
                'efeitos': {
                    'energia': -4,
                },
                'itens_add': [],
            },
        ],
    },
    'd1_r2_c2': {
        'dia': 1,
        'titulo': 'DIA 1 - SAIR PELO PRÉDIO E SEGUIR PELA RUA PRINCIPAL: O ELEVADOR',
        'texto': (
            'A cabine do elevador está presa entre andares. Algo bate repetidamente contra a porta '
            'pelo lado de dentro. As pancadas aumentam quando o personagem se aproxima, como se a '
            'criatura reconhecesse o som de passos.'
        ),
        'cor_fundo': VERDE,
        'opcoes': [
            {
                'texto': 'Abrir o elevador.',
                'resultado': 'A escolha cobra seu preço antes que exista tempo para voltar atrás.',
                'final': {
                    'tipo': 'derrota',
                    'titulo': 'MORTE 1',
                    'texto': 'Abrir o elevador; uma pessoa infectada presa na cabine ataca imediatamente.',
                },
                'efeitos': {
                    'vida': -100,
                },
                'qualidade': 'morte',
            },
            {
                'texto': 'Ignorar o elevador.',
                'resultado': 'A decisão leva ao próximo momento: Escada de Emergência.',
                'proxima': 'd1_r2_c3',
                'efeitos': {
                    'energia': -4,
                    'moral': -4,
                    'confianca': -1,
                },
                'itens_add': [],
            },
        ],
    },
    'd1_r2_c3': {
        'dia': 1,
        'titulo': 'DIA 1 - SAIR PELO PRÉDIO E SEGUIR PELA RUA PRINCIPAL: ESCADA DE EMERGÊNCIA',
        'texto': (
            'A escada está abafada e escura. O cheiro de fumaça se mistura ao odor de ferrugem e '
            'sangue. Passos arrastados ecoam nos andares inferiores, mas às vezes tudo fica '
            'silencioso de uma forma ainda pior.'
        ),
        'cor_fundo': VERDE,
        'opcoes': [
            {
                'texto': 'Descer correndo.',
                'resultado': 'A decisão leva ao próximo momento: O Vizinho.',
                'proxima': 'd1_r2_c4',
                'efeitos': {
                    'energia': -4,
                },
                'itens_add': [],
            },
            {
                'texto': 'Descer devagar.',
                'resultado': 'A decisão leva ao próximo momento: O Vizinho.',
                'proxima': 'd1_r2_c4',
                'efeitos': {
                    'energia': -4,
                },
                'itens_add': [],
            },
        ],
    },
    'd1_r2_c4': {
        'dia': 1,
        'titulo': 'DIA 1 - SAIR PELO PRÉDIO E SEGUIR PELA RUA PRINCIPAL: O VIZINHO',
        'texto': (
            'No terceiro andar, um vizinho aparece correndo escada acima. O braço está coberto de '
            'sangue e a respiração é irregular. Ele pede ajuda, mas seus olhos estão perdidos, como '
            'os de Caio visto na rota dos moradores.'
        ),
        'cor_fundo': VERDE,
        'opcoes': [
            {
                'texto': 'Ajudar o vizinho ferido.',
                'resultado': 'A decisão leva ao próximo momento: A Portaria.',
                'proxima': 'd1_r2_c5',
                'efeitos': {
                    'energia': -4,
                    'moral': 5,
                    'confianca': 2,
                },
                'itens_add': ['rações'],
            },
            {
                'texto': 'Continuar descendo.',
                'resultado': 'A decisão leva ao próximo momento: A Portaria.',
                'proxima': 'd1_r2_c5',
                'efeitos': {
                    'energia': -4,
                },
                'itens_add': ['rações'],
            },
        ],
    },
    'd1_r2_c5': {
        'dia': 1,
        'titulo': 'DIA 1 - SAIR PELO PRÉDIO E SEGUIR PELA RUA PRINCIPAL: A PORTARIA',
        'texto': (
            'A portaria foi destruída. Vidros cobrem o chão, o balcão está virado e o porteiro jaz '
            'imóvel. Ao lado dele há uma barra de ferro caída, simples o bastante para ser ignorada e '
            'pesada o bastante para salvar uma vida.'
        ),
        'cor_fundo': VERDE,
        'opcoes': [
            {
                'texto': 'Pegar a barra de ferro.',
                'resultado': 'A decisão leva ao próximo momento: A Saída Bloqueada.',
                'proxima': 'd1_r2_c6',
                'efeitos': {
                    'energia': -4,
                },
                'itens_add': ['barra de ferro'],
            },
            {
                'texto': 'Sair sem pegar nada.',
                'resultado': 'A decisão leva ao próximo momento: A Saída Bloqueada.',
                'proxima': 'd1_r2_c6',
                'efeitos': {
                    'energia': -4,
                },
                'itens_add': ['barra de ferro'],
            },
        ],
    },
    'd1_r2_c6': {
        'dia': 1,
        'titulo': 'DIA 1 - SAIR PELO PRÉDIO E SEGUIR PELA RUA PRINCIPAL: A SAÍDA BLOQUEADA',
        'texto': (
            'Pela porta principal, infectados vagam pela rua. Pela lateral, uma entrada leva à '
            'garagem subterrânea. O caminho principal é mais rápido; a garagem é mais escura, porém '
            'menos exposta.'
        ),
        'cor_fundo': VERDE,
        'opcoes': [
            {
                'texto': 'Forçar a saída principal.',
                'resultado': 'A escolha cobra seu preço antes que exista tempo para voltar atrás.',
                'final': {
                    'tipo': 'derrota',
                    'titulo': 'MORTE 2',
                    'texto': (
                        'Forçar a saída principal sem arma; o personagem é cercado na calçada antes de chegar aos '
                        'carros.'
                    ),
                },
                'efeitos': {
                    'vida': -100,
                },
                'qualidade': 'morte',
            },
            {
                'texto': 'Passar pela garagem.',
                'resultado': 'A decisão leva ao próximo momento: Garagem Subterrânea.',
                'proxima': 'd1_r2_c7',
                'efeitos': {
                    'energia': -4,
                },
                'itens_add': [],
            },
        ],
    },
    'd1_r2_c7': {
        'dia': 1,
        'titulo': 'DIA 1 - SAIR PELO PRÉDIO E SEGUIR PELA RUA PRINCIPAL: GARAGEM SUBTERRÂNEA',
        'texto': (
            'Carros estão abertos, luzes piscam e um alarme toca sem parar em um veículo no canto. O '
            'som pode atrair os mortos de toda a quadra.'
        ),
        'cor_fundo': VERDE,
        'opcoes': [
            {
                'texto': 'Desligar o alarme.',
                'resultado': 'A decisão leva ao próximo momento: Rampa de Saída.',
                'proxima': 'd1_r2_c8',
                'efeitos': {
                    'energia': -4,
                },
                'itens_add': [],
            },
            {
                'texto': 'Ignorar o alarme e correr.',
                'resultado': 'A decisão leva ao próximo momento: Rampa de Saída.',
                'proxima': 'd1_r2_c8',
                'efeitos': {
                    'energia': -8,
                    'moral': -4,
                    'confianca': -1,
                },
                'itens_add': [],
            },
        ],
    },
    'd1_r2_c8': {
        'dia': 1,
        'titulo': 'DIA 1 - SAIR PELO PRÉDIO E SEGUIR PELA RUA PRINCIPAL: RAMPA DE SAÍDA',
        'texto': (
            'Ao alcançar a rampa, um infectado surge entre dois carros batidos e bloqueia a única '
            'saída. Não há espaço para fugir sem lutar.'
        ),
        'cor_fundo': VERDE,
        'opcoes': [
            {
                'texto': 'Usar a barra de ferro.',
                'resultado': 'A decisão leva ao próximo momento: A Rua.',
                'proxima': 'd1_r2_c9',
                'efeitos': {
                    'energia': -4,
                },
                'itens_add': ['barra de ferro'],
            },
            {
                'texto': 'Tentar empurrar o infectado com as mãos.',
                'resultado': 'A decisão leva ao próximo momento: A Rua.',
                'proxima': 'd1_r2_c9',
                'efeitos': {
                    'energia': -4,
                },
                'itens_add': [],
            },
        ],
    },
    'd1_r2_c9': {
        'dia': 1,
        'titulo': 'DIA 1 - SAIR PELO PRÉDIO E SEGUIR PELA RUA PRINCIPAL: A RUA',
        'texto': (
            'A cidade está em colapso. Carros abandonados bloqueiam avenidas, fumaça sobe entre '
            'prédios e sobreviventes fazem sinal ao longe. Um deles carrega um rádio quebrado que '
            'mais tarde dará pistas sobre a Operação Aurora.'
        ),
        'cor_fundo': VERDE,
        'opcoes': [
            {
                'texto': 'Seguir com os sobreviventes.',
                'resultado': 'Essa decisão encerra o caminho iniciado neste dia.',
                'proxima': 'd1_r2_fim_1',
                'efeitos': {
                    'energia': -4,
                },
                'itens_add': ['rádio', 'rações'],
                'qualidade': 'media',
            },
            {
                'texto': 'Continuar sozinho pela rua principal.',
                'resultado': 'Essa decisão encerra o caminho iniciado neste dia.',
                'proxima': 'd1_r2_fim_2',
                'efeitos': {
                    'energia': -4,
                    'moral': -4,
                    'confianca': -1,
                },
                'itens_add': ['rádio', 'rações'],
                'qualidade': 'media',
            },
        ],
    },
    'd1_r3_fim_1': {
        'dia': 1,
        'titulo': 'FIM DO DIA 1 A',
        'texto': 'Sobrevive com comida e água, mas poucos itens raros.',
        'cor_fundo': VERDE_CLARO,
        'fim_dia': True,
        'proxima_dia': 'd2_r3_inicio',
    },
    'd1_r3_fim_2': {
        'dia': 1,
        'titulo': 'FIM DO DIA 1 B',
        'texto': 'Sobrevive com item raro, porém ferido ou com menos recursos.',
        'cor_fundo': VERDE_CLARO,
        'fim_dia': True,
        'proxima_dia': 'd2_r3_inicio',
    },
    'd1_r3_c1': {
        'dia': 1,
        'titulo': 'DIA 1 - PROCURAR COMIDA E SUPRIMENTOS NO PRÉDIO: CORREDOR DO SEGUNDO ANDAR',
        'texto': (
            'O personagem decide não sair correndo. Ele fecha a porta do apartamento, pega uma '
            'mochila vazia e entra no corredor. Há três possibilidades: o apartamento vizinho à '
            'esquerda, uma porta trancada à direita com batidas e a escada que desce para o depósito.'
        ),
        'cor_fundo': VERDE,
        'opcoes': [
            {
                'texto': 'Entrar no apartamento vizinho.',
                'resultado': 'A decisão leva ao próximo momento: Apartamento Vizinho.',
                'proxima': 'd1_r3_c2',
                'efeitos': {
                    'energia': -4,
                },
                'itens_add': ['mochila'],
            },
            {
                'texto': 'Investigar a porta trancada.',
                'resultado': 'A decisão leva ao próximo momento: Apartamento Vizinho.',
                'proxima': 'd1_r3_c2',
                'efeitos': {
                    'energia': -4,
                },
                'itens_add': ['mochila'],
            },
            {
                'texto': 'Descer para o depósito.',
                'resultado': 'A decisão leva ao próximo momento: Apartamento Vizinho.',
                'proxima': 'd1_r3_c2',
                'efeitos': {
                    'energia': -4,
                },
                'itens_add': ['mochila'],
            },
        ],
    },
    'd1_r3_c2': {
        'dia': 1,
        'titulo': 'DIA 1 - PROCURAR COMIDA E SUPRIMENTOS NO PRÉDIO: APARTAMENTO VIZINHO',
        'texto': (
            'O apartamento está revirado, como se a família tivesse saído às pressas. A cozinha '
            'parece segura; o corredor dos quartos está escuro e promete itens melhores, mas também '
            'mais perigo.'
        ),
        'cor_fundo': VERDE,
        'opcoes': [
            {
                'texto': 'Procurar na cozinha.',
                'resultado': 'A decisão leva ao próximo momento: A Cozinha.',
                'proxima': 'd1_r3_c3',
                'efeitos': {
                    'energia': -4,
                    'comida': 1,
                    'agua': 1,
                },
                'itens_add': [],
            },
            {
                'texto': 'Procurar no quarto.',
                'resultado': 'A decisão leva ao próximo momento: A Cozinha.',
                'proxima': 'd1_r3_c3',
                'efeitos': {
                    'energia': -4,
                    'comida': 1,
                    'agua': 1,
                },
                'itens_add': [],
            },
        ],
    },
    'd1_r3_c3': {
        'dia': 1,
        'titulo': 'DIA 1 - PROCURAR COMIDA E SUPRIMENTOS NO PRÉDIO: A COZINHA',
        'texto': (
            'O personagem encontra comida enlatada, garrafas de água e uma pequena mochila térmica. É '
            'um ganho modesto, mas seguro. Na televisão da cozinha, outra notícia cortada menciona '
            'bairros isolados pelo exército.'
        ),
        'cor_fundo': VERDE,
        'proxima': 'd1_r3_c4',
    },
    'd1_r3_c4': {
        'dia': 1,
        'titulo': 'DIA 1 - PROCURAR COMIDA E SUPRIMENTOS NO PRÉDIO: O QUARTO',
        'texto': (
            'No guarda-roupa, há um kit de primeiros socorros. Ao abrir a gaveta, a madeira range e '
            'algo se mexe debaixo da cama. Um infectado preso ali desperta, magro, faminto e rápido o '
            'bastante para matar.'
        ),
        'cor_fundo': VERDE,
        'opcoes': [
            {
                'texto': 'Lutar se tiver arma improvisada.',
                'resultado': 'A escolha cobra seu preço antes que exista tempo para voltar atrás.',
                'final': {
                    'tipo': 'derrota',
                    'titulo': 'MORTE 1',
                    'texto': 'Lutar contra o infectado do quarto sem arma; o personagem é mordido e não resiste.',
                },
                'efeitos': {
                    'vida': -100,
                },
                'qualidade': 'morte',
            },
            {
                'texto': 'Fugir correndo.',
                'resultado': 'A decisão leva ao próximo momento: Porta Trancada.',
                'proxima': 'd1_r3_c5',
                'efeitos': {
                    'energia': -4,
                },
                'itens_add': ['kit médico'],
            },
        ],
    },
    'd1_r3_c5': {
        'dia': 1,
        'titulo': 'DIA 1 - PROCURAR COMIDA E SUPRIMENTOS NO PRÉDIO: PORTA TRANCADA',
        'texto': (
            'As batidas do lado direito continuam. Podem ser de um sobrevivente ou de alguém que '
            'deixou de ser humano. A porta está frágil, com a madeira rachada perto da fechadura.'
        ),
        'cor_fundo': VERDE,
        'opcoes': [
            {
                'texto': 'Arrombar a porta.',
                'resultado': 'A escolha cobra seu preço antes que exista tempo para voltar atrás.',
                'final': {
                    'tipo': 'derrota',
                    'titulo': 'MORTE 2',
                    'texto': (
                        'Arrombar a porta trancada e enfrentar o vizinho infectado sem arma; ele domina o '
                        'personagem no corredor.'
                    ),
                },
                'efeitos': {
                    'vida': -100,
                },
                'qualidade': 'morte',
            },
            {
                'texto': 'Ignorar e seguir para a escada.',
                'resultado': 'A decisão leva ao próximo momento: O Vizinho Infectado.',
                'proxima': 'd1_r3_c6',
                'efeitos': {
                    'energia': -4,
                    'moral': -4,
                    'confianca': -1,
                },
                'itens_add': [],
            },
        ],
    },
    'd1_r3_c6': {
        'dia': 1,
        'titulo': 'DIA 1 - PROCURAR COMIDA E SUPRIMENTOS NO PRÉDIO: O VIZINHO INFECTADO',
        'texto': (
            'A porta cede. Lá dentro, um vizinho ferido se vira com a boca cheia de sangue seco. '
            'Perto da janela há uma lanterna caída, item raro que pode salvar o personagem em dias '
            'futuros.'
        ),
        'cor_fundo': VERDE,
        'opcoes': [
            {
                'texto': 'Enfrentar se tiver arma.',
                'resultado': 'A decisão leva ao próximo momento: Escada para o Depósito.',
                'proxima': 'd1_r3_c7',
                'efeitos': {
                    'energia': -4,
                },
                'itens_add': ['lanterna'],
            },
            {
                'texto': 'Recuar e trancar a porta.',
                'resultado': 'A decisão leva ao próximo momento: Escada para o Depósito.',
                'proxima': 'd1_r3_c7',
                'efeitos': {
                    'energia': -4,
                },
                'itens_add': ['lanterna'],
            },
        ],
    },
    'd1_r3_c7': {
        'dia': 1,
        'titulo': 'DIA 1 - PROCURAR COMIDA E SUPRIMENTOS NO PRÉDIO: ESCADA PARA O DEPÓSITO',
        'texto': (
            'A escada está parcialmente escura. Sons da rua ficam mais altos aqui. A porta da frente '
            'do prédio está sendo forçada por algo do lado de fora.'
        ),
        'cor_fundo': VERDE,
        'opcoes': [
            {
                'texto': 'Usar a lanterna do celular.',
                'resultado': 'A decisão leva ao próximo momento: Depósito e Portaria.',
                'proxima': 'd1_r3_c8',
                'efeitos': {
                    'energia': -4,
                },
                'itens_add': ['lanterna'],
            },
            {
                'texto': 'Descer no escuro.',
                'resultado': 'A decisão leva ao próximo momento: Depósito e Portaria.',
                'proxima': 'd1_r3_c8',
                'efeitos': {
                    'energia': -4,
                },
                'itens_add': [],
            },
        ],
    },
    'd1_r3_c8': {
        'dia': 1,
        'titulo': 'DIA 1 - PROCURAR COMIDA E SUPRIMENTOS NO PRÉDIO: DEPÓSITO E PORTARIA',
        'texto': (
            'No depósito, o personagem encontra comida extra e uma corda enrolada atrás de caixas de '
            'manutenção. Se fez barulho em excesso, infectados começam a bater no saguão antes que '
            'ele termine de guardar tudo.'
        ),
        'cor_fundo': VERDE,
        'proxima': 'd1_r3_c9',
    },
    'd1_r3_c9': {
        'dia': 1,
        'titulo': 'DIA 1 - PROCURAR COMIDA E SUPRIMENTOS NO PRÉDIO: RETORNO AO APARTAMENTO',
        'texto': (
            'O personagem volta para o próprio apartamento com comida, água e talvez itens raros: kit '
            'médico, lanterna ou corda. Ele tranca a porta e entende que sobreviveu ao primeiro dia '
            'porque escolheu se preparar, não porque o mundo ficou menos perigoso.'
        ),
        'cor_fundo': VERDE,
        'opcoes': [
            {
                'texto': 'Trancar a porta e racionar recursos.',
                'resultado': 'Essa decisão encerra o caminho iniciado neste dia.',
                'proxima': 'd1_r3_fim_1',
                'efeitos': {
                    'energia': -4,
                    'comida': 1,
                    'agua': 1,
                },
                'itens_add': ['lanterna', 'corda', 'kit médico'],
                'qualidade': 'media',
            },
            {
                'texto': 'Tentar sair do prédio ainda à noite.',
                'resultado': 'Essa decisão encerra o caminho iniciado neste dia.',
                'proxima': 'd1_r3_fim_2',
                'efeitos': {
                    'energia': -4,
                },
                'itens_add': ['lanterna', 'corda', 'kit médico'],
                'qualidade': 'media',
            },
        ],
    },
    'd1_r4_fim_1': {
        'dia': 1,
        'titulo': 'FIM DO DIA 1 A',
        'texto': 'Terminal de ônibus com reputação positiva e confiança da mulher e da criança.',
        'cor_fundo': VERDE_CLARO,
        'fim_dia': True,
        'proxima_dia': 'd2_r4_inicio',
    },
    'd1_r4_fim_2': {
        'dia': 1,
        'titulo': 'FIM DO DIA 1 B',
        'texto': 'Chegada ao terminal separado dos moradores, sem confiança inicial, mas ainda vivo.',
        'cor_fundo': VERDE_CLARO,
        'fim_dia': True,
        'proxima_dia': 'd2_r4_inicio',
    },
    'd1_r4_c1': {
        'dia': 1,
        'titulo': 'DIA 1 - AJUDAR OUTROS MORADORES: VOZES NO CORREDOR',
        'texto': (
            'O personagem decide que não vai fugir sem verificar os pedidos de socorro. No corredor '
            'escuro, uma mulher segura uma criança contra o peito e implora por ajuda. Ao fundo, Caio '
            'continua se movendo, mas os sons que faz já não parecem humanos.'
        ),
        'cor_fundo': VERDE,
        'opcoes': [
            {
                'texto': 'Ajudar mulher e criança.',
                'resultado': 'A decisão leva ao próximo momento: Elevador Parado.',
                'proxima': 'd1_r4_c2',
                'efeitos': {
                    'energia': -4,
                    'moral': 5,
                    'confianca': 2,
                },
                'itens_add': [],
            },
            {
                'texto': 'Fechar a porta e ignorar.',
                'resultado': 'A decisão leva ao próximo momento: Elevador Parado.',
                'proxima': 'd1_r4_c2',
                'efeitos': {
                    'energia': -4,
                    'moral': -4,
                    'confianca': -1,
                },
                'itens_add': [],
            },
        ],
    },
    'd1_r4_c2': {
        'dia': 1,
        'titulo': 'DIA 1 - AJUDAR OUTROS MORADORES: ELEVADOR PARADO',
        'texto': (
            'O elevador está preso entre andares. Batidas secas vêm de dentro, como unhas arranhando '
            'metal. A escada parece mais lenta, mas o elevador parece uma armadilha.'
        ),
        'cor_fundo': VERDE,
        'opcoes': [
            {
                'texto': 'Entrar no elevador.',
                'resultado': 'A escolha cobra seu preço antes que exista tempo para voltar atrás.',
                'final': {
                    'tipo': 'derrota',
                    'titulo': 'MORTE 1',
                    'texto': 'Entrar no elevador; o infectado preso ataca antes que a porta feche.',
                },
                'efeitos': {
                    'vida': -100,
                },
                'qualidade': 'morte',
            },
            {
                'texto': 'Ir pela escada.',
                'resultado': 'A decisão leva ao próximo momento: Caio Transformado.',
                'proxima': 'd1_r4_c3',
                'efeitos': {
                    'energia': -4,
                },
                'itens_add': [],
            },
        ],
    },
    'd1_r4_c3': {
        'dia': 1,
        'titulo': 'DIA 1 - AJUDAR OUTROS MORADORES: CAIO TRANSFORMADO',
        'texto': (
            'No patamar inferior, Caio aparece cambaleando. O braço mordido está aberto, os olhos não '
            'reconhecem mais ninguém e ele bloqueia a passagem.'
        ),
        'cor_fundo': VERDE,
        'opcoes': [
            {
                'texto': 'Usar extintor contra Caio.',
                'resultado': 'A decisão leva ao próximo momento: Apartamento Vizinho.',
                'proxima': 'd1_r4_c4',
                'efeitos': {
                    'energia': -4,
                },
                'itens_add': [],
            },
            {
                'texto': 'Tentar conversar com Caio.',
                'resultado': 'A escolha cobra seu preço antes que exista tempo para voltar atrás.',
                'final': {
                    'tipo': 'derrota',
                    'titulo': 'MORTE 2',
                    'texto': 'Tentar conversar com Caio transformado; ele avança e morde o personagem na escada.',
                },
                'efeitos': {
                    'vida': -100,
                },
                'qualidade': 'morte',
            },
        ],
    },
    'd1_r4_c4': {
        'dia': 1,
        'titulo': 'DIA 1 - AJUDAR OUTROS MORADORES: APARTAMENTO VIZINHO',
        'texto': (
            'O grupo entra em um apartamento aberto. A sala está revirada, há comida sobre a mesa e '
            'uma varanda lateral que talvez leve a outro prédio. A porta atrás deles treme com '
            'batidas vindas do corredor.'
        ),
        'cor_fundo': VERDE,
        'opcoes': [
            {
                'texto': 'Acalmar a criança.',
                'resultado': 'A decisão leva ao próximo momento: Pânico e Barulho.',
                'proxima': 'd1_r4_c5',
                'efeitos': {
                    'energia': -4,
                    'moral': 5,
                    'confianca': 2,
                },
                'itens_add': [],
            },
            {
                'texto': 'Mandar todos correrem sem preparar nada.',
                'resultado': 'A decisão leva ao próximo momento: Pânico e Barulho.',
                'proxima': 'd1_r4_c5',
                'efeitos': {
                    'energia': -8,
                },
                'itens_add': [],
            },
        ],
    },
    'd1_r4_c5': {
        'dia': 1,
        'titulo': 'DIA 1 - AJUDAR OUTROS MORADORES: PÂNICO E BARULHO',
        'texto': (
            'O choro da criança diminui, mas os infectados batem nas portas do andar. A varanda '
            'lateral é estreita, molhada pela chuva e alta demais para erro.'
        ),
        'cor_fundo': VERDE,
        'opcoes': [
            {
                'texto': 'Ajudar os dois a atravessar primeiro.',
                'resultado': 'A decisão leva ao próximo momento: Varanda Lateral.',
                'proxima': 'd1_r4_c6',
                'efeitos': {
                    'energia': -8,
                    'moral': 5,
                    'confianca': 2,
                },
                'itens_add': [],
            },
            {
                'texto': 'Atravessar sozinho primeiro.',
                'resultado': 'A decisão leva ao próximo momento: Varanda Lateral.',
                'proxima': 'd1_r4_c6',
                'efeitos': {
                    'energia': -8,
                    'moral': -4,
                    'confianca': -1,
                },
                'itens_add': [],
            },
        ],
    },
    'd1_r4_c6': {
        'dia': 1,
        'titulo': 'DIA 1 - AJUDAR OUTROS MORADORES: VARANDA LATERAL',
        'texto': (
            'A travessia é lenta. O vento traz fumaça, alarmes e gritos. Abaixo, carros parados '
            'formam linhas de luzes quebradas. A criança fecha os olhos enquanto o personagem a '
            'entrega à mãe do outro lado.'
        ),
        'cor_fundo': VERDE,
        'proxima': 'd1_r4_c7',
    },
    'd1_r4_c7': {
        'dia': 1,
        'titulo': 'DIA 1 - AJUDAR OUTROS MORADORES: MORADOR COM RÁDIO',
        'texto': (
            'No outro prédio, um morador assustado segura um rádio antigo. Ele ouviu mensagens '
            'falhadas sobre pontos de encontro, evacuação e estradas bloqueadas. A transmissão '
            'menciona um terminal de ônibus.'
        ),
        'cor_fundo': VERDE,
        'opcoes': [
            {
                'texto': 'Ouvir o rádio e seguir a informação.',
                'resultado': 'A decisão leva ao próximo momento: Rua dos Fundos.',
                'proxima': 'd1_r4_c8',
                'efeitos': {
                    'energia': -4,
                },
                'itens_add': ['rádio', 'ônibus'],
            },
            {
                'texto': 'Ignorar o rádio e procurar estrada rural.',
                'resultado': 'A decisão leva ao próximo momento: Rua dos Fundos.',
                'proxima': 'd1_r4_c8',
                'efeitos': {
                    'energia': -4,
                    'moral': -4,
                    'confianca': -1,
                    'comida': 1,
                    'agua': 1,
                },
                'itens_add': ['rádio', 'ônibus'],
            },
        ],
    },
    'd1_r4_c8': {
        'dia': 1,
        'titulo': 'DIA 1 - AJUDAR OUTROS MORADORES: RUA DOS FUNDOS',
        'texto': (
            'O grupo alcança a rua dos fundos. Malas abertas e marcas de fuga espalham-se pelo chão. '
            'Ao longe, o som de uma multidão indica o caminho do terminal; pela direita, becos levam '
            'à rota de fuga solitária.'
        ),
        'cor_fundo': VERDE,
        'proxima': 'd1_r4_c9',
    },
    'd1_r4_c9': {
        'dia': 1,
        'titulo': 'DIA 1 - AJUDAR OUTROS MORADORES: ESCOLHA DE DESTINO',
        'texto': (
            'A mulher agradece pela ajuda, ainda segurando a criança com força. O personagem entende '
            'que a primeira noite fora do apartamento vai definir não apenas onde dormir, mas que '
            'tipo de pessoa ele será no fim do mundo.'
        ),
        'cor_fundo': VERDE,
        'opcoes': [
            {
                'texto': 'Ir com o grupo ao terminal.',
                'resultado': 'Essa decisão encerra o caminho iniciado neste dia.',
                'proxima': 'd1_r4_fim_1',
                'efeitos': {
                    'energia': -4,
                },
                'itens_add': [],
                'qualidade': 'media',
            },
            {
                'texto': 'Deixar a mulher e a criança seguirem sem você.',
                'resultado': 'Essa decisão encerra o caminho iniciado neste dia.',
                'proxima': 'd1_r4_fim_2',
                'efeitos': {
                    'energia': -4,
                },
                'itens_add': [],
                'qualidade': 'media',
            },
        ],
    },
    'd2_r1_fim_1': {
        'dia': 2,
        'titulo': 'FIM DO DIA 2 A',
        'texto': 'Casa segura com grupo maior, mas recursos divididos.',
        'cor_fundo': VERDE_CLARO,
        'fim_dia': True,
        'proxima_dia': 'd3_r1_inicio',
    },
    'd2_r1_fim_2': {
        'dia': 2,
        'titulo': 'FIM DO DIA 2 B',
        'texto': (
            'Abrigo improvisado com menos aliados, caso o personagem abandone parte do grupo, '
            'carregando culpa e mais recursos.'
        ),
        'cor_fundo': VERDE_CLARO,
        'fim_dia': True,
        'proxima_dia': 'd3_r1_inicio',
    },
    'd2_r1_c1': {
        'dia': 2,
        'titulo': 'DIA 2 - AMANHECER / SAIR DA CIDADE: CONVERSA NO ABRIGO',
        'texto': (
            'José, Pedro, Lena, Joice e Davi acordam no prédio interditado. O personagem conta sobre '
            'Jorge; o grupo conta que dois amigos foram mordidos no carro antes de se transformarem '
            'no estacionamento.'
        ),
        'cor_fundo': VERDE,
        'proxima': 'd2_r1_c2',
    },
    'd2_r1_c2': {
        'dia': 2,
        'titulo': 'DIA 2 - AMANHECER / SAIR DA CIDADE: JUNTOS OU NÃO',
        'texto': (
            'O grupo pede que o personagem continue com eles. Ele percebe que pessoas emotivas podem '
            'atrasá-lo, mas também que sozinho será mais vulnerável.'
        ),
        'cor_fundo': VERDE,
        'opcoes': [
            {
                'texto': 'Permanecer com o grupo.',
                'resultado': 'A decisão leva ao próximo momento: O Plano.',
                'proxima': 'd2_r1_c3',
                'efeitos': {
                    'energia': -4,
                },
                'itens_add': [],
            },
            {
                'texto': 'Abandonar o grupo antes do amanhecer.',
                'resultado': 'A decisão leva ao próximo momento: O Plano.',
                'proxima': 'd2_r1_c3',
                'efeitos': {
                    'energia': -4,
                    'moral': -4,
                    'confianca': -1,
                },
                'itens_add': [],
            },
        ],
    },
    'd2_r1_c3': {
        'dia': 2,
        'titulo': 'DIA 2 - AMANHECER / SAIR DA CIDADE: O PLANO',
        'texto': (
            'Para sair da cidade, será preciso andar quilômetros. A avenida principal tem carros '
            'batidos e mortos vagando. Os becos oferecem cobertura, mas também emboscadas.'
        ),
        'cor_fundo': VERDE,
        'opcoes': [
            {
                'texto': 'Seguir a pé em silêncio pelos becos.',
                'resultado': 'A decisão leva ao próximo momento: Uma Pausa.',
                'proxima': 'd2_r1_c4',
                'efeitos': {
                    'energia': -4,
                },
                'itens_add': [],
            },
            {
                'texto': 'Cortar caminho pela avenida principal.',
                'resultado': 'A decisão leva ao próximo momento: Uma Pausa.',
                'proxima': 'd2_r1_c4',
                'efeitos': {
                    'energia': -4,
                },
                'itens_add': [],
            },
        ],
    },
    'd2_r1_c4': {
        'dia': 2,
        'titulo': 'DIA 2 - AMANHECER / SAIR DA CIDADE: UMA PAUSA',
        'texto': (
            'Na marginal, o grupo encontra um posto de gasolina saqueado. Há sinais de luta e sangue '
            'no chão. Motores se aproximam: homens armados chegam em comboio, atirando em quem se '
            'aproxima.'
        ),
        'cor_fundo': VERDE,
        'opcoes': [
            {
                'texto': 'Sair pelos fundos em silêncio.',
                'resultado': 'A decisão leva ao próximo momento: Reencontro.',
                'proxima': 'd2_r1_c5',
                'efeitos': {
                    'energia': -4,
                },
                'itens_add': [],
            },
            {
                'texto': 'Pedir ajuda ao comboio.',
                'resultado': 'A escolha cobra seu preço antes que exista tempo para voltar atrás.',
                'final': {
                    'tipo': 'derrota',
                    'titulo': 'MORTE 1',
                    'texto': 'Pedir ajuda ao comboio do posto; os saqueadores executam o grupo para roubar recursos.',
                },
                'efeitos': {
                    'vida': -100,
                },
                'qualidade': 'morte',
            },
        ],
    },
    'd2_r1_c5': {
        'dia': 2,
        'titulo': 'DIA 2 - AMANHECER / SAIR DA CIDADE: REENCONTRO',
        'texto': (
            'Em outro beco, Joice reconhece a voz do irmão Lucas conversando com dois desconhecidos. '
            'Antes que o personagem avalie a situação, ela chama por ele.'
        ),
        'cor_fundo': VERDE,
        'proxima': 'd2_r1_c6',
    },
    'd2_r1_c6': {
        'dia': 2,
        'titulo': 'DIA 2 - AMANHECER / SAIR DA CIDADE: DESCONFIANÇA',
        'texto': (
            'Lucas apresenta os desconhecidos. Eles dizem que ajudaram a fugir de infectados, mas não '
            'têm recursos. O personagem pede que mostrem os braços para verificar mordidas.'
        ),
        'cor_fundo': VERDE,
        'opcoes': [
            {
                'texto': 'Ajudar os desconhecidos com água e comida.',
                'resultado': 'A decisão leva ao próximo momento: Anoitecendo.',
                'proxima': 'd2_r1_c7',
                'efeitos': {
                    'energia': -4,
                    'moral': 5,
                    'confianca': 2,
                    'comida': 1,
                    'agua': 1,
                },
                'itens_add': ['aliado Lucas'],
            },
            {
                'texto': 'Recusar ajuda e expulsá-los.',
                'resultado': 'A decisão leva ao próximo momento: Anoitecendo.',
                'proxima': 'd2_r1_c7',
                'efeitos': {
                    'energia': -4,
                },
                'itens_add': ['aliado Lucas'],
            },
        ],
    },
    'd2_r1_c7': {
        'dia': 2,
        'titulo': 'DIA 2 - AMANHECER / SAIR DA CIDADE: ANOITECENDO',
        'texto': (
            'O grupo cresce, mas os recursos diminuem. A noite se aproxima e todos estão cansados. '
            'Uma casa de dois andares parece segura o suficiente para a parada.'
        ),
        'cor_fundo': VERDE,
        'opcoes': [
            {
                'texto': 'Entrar na casa e limpar cômodos.',
                'resultado': 'A decisão leva ao próximo momento: Acomodações.',
                'proxima': 'd2_r1_c8',
                'efeitos': {
                    'energia': -4,
                },
                'itens_add': [],
            },
            {
                'texto': 'Continuar caminhando no escuro.',
                'resultado': 'A decisão leva ao próximo momento: Acomodações.',
                'proxima': 'd2_r1_c8',
                'efeitos': {
                    'energia': -4,
                },
                'itens_add': [],
            },
        ],
    },
    'd2_r1_c8': {
        'dia': 2,
        'titulo': 'DIA 2 - AMANHECER / SAIR DA CIDADE: ACOMODAÇÕES',
        'texto': (
            'A casa tem quartos e camas. O personagem manda apagar luzes, fechar cortinas e organizar '
            'turnos de vigia em duplas. Pela primeira vez, todos podem dormir fora do chão.'
        ),
        'cor_fundo': VERDE,
        'opcoes': [
            {
                'texto': 'Você e um desconhecido fazem a primeira vigia.',
                'resultado': 'A decisão leva ao próximo momento: Sono Inquieto.',
                'proxima': 'd2_r1_c9',
                'efeitos': {
                    'energia': -4,
                    'moral': 5,
                    'confianca': 2,
                },
                'itens_add': [],
            },
            {
                'texto': 'Deixar os desconhecidos vigiarem sozinhos.',
                'resultado': 'A escolha cobra seu preço antes que exista tempo para voltar atrás.',
                'final': {
                    'tipo': 'derrota',
                    'titulo': 'MORTE 2',
                    'texto': (
                        'Deixar os desconhecidos vigiarem sozinhos; eles roubam suprimentos e eliminam quem '
                        'acorda primeiro.'
                    ),
                },
                'efeitos': {
                    'vida': -100,
                },
                'qualidade': 'morte',
            },
        ],
    },
    'd2_r1_c9': {
        'dia': 2,
        'titulo': 'DIA 2 - AMANHECER / SAIR DA CIDADE: SONO INQUIETO',
        'texto': (
            'Durante a madrugada, passos rangem no piso. O personagem não sabe se é madeira cedendo, '
            'infectado próximo ou alguém do próprio grupo acordado quando não deveria.'
        ),
        'cor_fundo': VERDE,
        'opcoes': [
            {
                'texto': 'FIM DO DIA 2 A',
                'resultado': 'Essa decisão encerra o caminho iniciado neste dia.',
                'proxima': 'd2_r1_fim_1',
                'efeitos': {
                    'energia': -4,
                },
                'qualidade': 'media',
            },
            {
                'texto': 'FIM DO DIA 2 B',
                'resultado': 'Essa decisão encerra o caminho iniciado neste dia.',
                'proxima': 'd2_r1_fim_2',
                'efeitos': {
                    'energia': -4,
                },
                'qualidade': 'media',
            },
        ],
    },
    'd2_r2_fim_1': {
        'dia': 2,
        'titulo': 'FIM DO DIA 2 A',
        'texto': 'Loja abandonada reforçada, com água e informação sobre a zona segura.',
        'cor_fundo': VERDE_CLARO,
        'fim_dia': True,
        'proxima_dia': 'd3_r2_inicio',
    },
    'd2_r2_fim_2': {
        'dia': 2,
        'titulo': 'FIM DO DIA 2 B',
        'texto': (
            'Abrigo precário em outra loja, menos recursos, mas sem dividir comida com o sobrevivente '
            'ferido.'
        ),
        'cor_fundo': VERDE_CLARO,
        'fim_dia': True,
        'proxima_dia': 'd3_r2_inicio',
    },
    'd2_r2_c1': {
        'dia': 2,
        'titulo': 'DIA 2 - LOJA ABANDONADA: UMA NOITE DIFÍCIL',
        'texto': (
            'O grupo da rua passa a madrugada escondido atrás de veículos abandonados. Ninguém dorme '
            'direito. Quando o sol nasce, comida e água estão quase no fim.'
        ),
        'cor_fundo': VERDE,
        'opcoes': [
            {
                'texto': 'Procurar abrigo seguro.',
                'resultado': 'A decisão leva ao próximo momento: Ruas Secundárias.',
                'proxima': 'd2_r2_c2',
                'efeitos': {
                    'energia': -4,
                    'comida': 1,
                    'agua': 1,
                },
                'itens_add': [],
            },
            {
                'texto': 'Continuar vagando pela rua principal.',
                'resultado': 'A decisão leva ao próximo momento: Ruas Secundárias.',
                'proxima': 'd2_r2_c2',
                'efeitos': {
                    'energia': -4,
                },
                'itens_add': [],
            },
        ],
    },
    'd2_r2_c2': {
        'dia': 2,
        'titulo': 'DIA 2 - LOJA ABANDONADA: RUAS SECUNDÁRIAS',
        'texto': (
            'O grupo evita avenidas e segue por ruas menores. Algumas casas estão abertas; outras têm '
            'marcas de invasão. Ao longe, uma loja de conveniência parece quase intacta.'
        ),
        'cor_fundo': VERDE,
        'opcoes': [
            {
                'texto': 'Investigar a loja.',
                'resultado': 'A decisão leva ao próximo momento: A Loja.',
                'proxima': 'd2_r2_c3',
                'efeitos': {
                    'energia': -4,
                },
                'itens_add': [],
            },
            {
                'texto': 'Ignorar a loja por medo de armadilha.',
                'resultado': 'A decisão leva ao próximo momento: A Loja.',
                'proxima': 'd2_r2_c3',
                'efeitos': {
                    'energia': -4,
                    'moral': -4,
                    'confianca': -1,
                },
                'itens_add': [],
            },
        ],
    },
    'd2_r2_c3': {
        'dia': 2,
        'titulo': 'DIA 2 - LOJA ABANDONADA: A LOJA',
        'texto': (
            'O interior está escuro e as prateleiras foram saqueadas. Mesmo assim, garrafas de água '
            'permanecem escondidas atrás do balcão. A porta dos fundos está fechada por caixas.'
        ),
        'cor_fundo': VERDE,
        'opcoes': [
            {
                'texto': 'Coletar suprimentos.',
                'resultado': 'A decisão leva ao próximo momento: O Sobrevivente.',
                'proxima': 'd2_r2_c4',
                'efeitos': {
                    'energia': -4,
                    'comida': 1,
                    'agua': 1,
                },
                'itens_add': [],
            },
            {
                'texto': 'Entrar correndo sem observar.',
                'resultado': 'A decisão leva ao próximo momento: O Sobrevivente.',
                'proxima': 'd2_r2_c4',
                'efeitos': {
                    'energia': -4,
                },
                'itens_add': [],
            },
        ],
    },
    'd2_r2_c4': {
        'dia': 2,
        'titulo': 'DIA 2 - LOJA ABANDONADA: O SOBREVIVENTE',
        'texto': (
            'Nos fundos, um homem ferido aponta uma arma. Ele abaixa a mira ao perceber que não são '
            'infectados e diz ter ouvido sobre um abrigo alguns quilômetros adiante.'
        ),
        'cor_fundo': VERDE,
        'opcoes': [
            {
                'texto': 'Ouvir o sobrevivente.',
                'resultado': 'A decisão leva ao próximo momento: Barulho nos Fundos.',
                'proxima': 'd2_r2_c5',
                'efeitos': {
                    'energia': -4,
                },
                'itens_add': [],
            },
            {
                'texto': 'Tomar a arma dele à força.',
                'resultado': 'A escolha cobra seu preço antes que exista tempo para voltar atrás.',
                'final': {
                    'tipo': 'derrota',
                    'titulo': 'MORTE 1',
                    'texto': 'Tentar tomar a arma do sobrevivente; ele atira no personagem antes de perceber o erro.',
                },
                'efeitos': {
                    'vida': -100,
                },
                'qualidade': 'morte',
            },
        ],
    },
    'd2_r2_c5': {
        'dia': 2,
        'titulo': 'DIA 2 - LOJA ABANDONADA: BARULHO NOS FUNDOS',
        'texto': (
            'Pancadas ecoam na área de estoque. Algo se move atrás das caixas. O sobrevivente insiste '
            'que deixou alguém preso ali depois de uma mordida.'
        ),
        'cor_fundo': VERDE,
        'opcoes': [
            {
                'texto': 'Verificar com cuidado.',
                'resultado': 'A decisão leva ao próximo momento: O Infectado.',
                'proxima': 'd2_r2_c6',
                'efeitos': {
                    'energia': -4,
                },
                'itens_add': [],
            },
            {
                'texto': 'Abrir tudo rapidamente.',
                'resultado': 'A decisão leva ao próximo momento: O Infectado.',
                'proxima': 'd2_r2_c6',
                'efeitos': {
                    'energia': -4,
                },
                'itens_add': [],
            },
        ],
    },
    'd2_r2_c6': {
        'dia': 2,
        'titulo': 'DIA 2 - LOJA ABANDONADA: O INFECTADO',
        'texto': 'A criatura presa se liberta e avança. O espaço é apertado demais para luta prolongada.',
        'cor_fundo': VERDE,
        'opcoes': [
            {
                'texto': 'Fugir pela saída traseira.',
                'resultado': 'A decisão leva ao próximo momento: A Chuva.',
                'proxima': 'd2_r2_c7',
                'efeitos': {
                    'energia': -4,
                },
                'itens_add': [],
            },
            {
                'texto': 'Tentar lutar no corredor estreito.',
                'resultado': 'A escolha cobra seu preço antes que exista tempo para voltar atrás.',
                'final': {
                    'tipo': 'derrota',
                    'titulo': 'MORTE 2',
                    'texto': (
                        'Tentar lutar contra o infectado no corredor estreito; o grupo não consegue ajudar e o '
                        'personagem é mordido.'
                    ),
                },
                'efeitos': {
                    'vida': -100,
                },
                'qualidade': 'morte',
            },
        ],
    },
    'd2_r2_c7': {
        'dia': 2,
        'titulo': 'DIA 2 - LOJA ABANDONADA: A CHUVA',
        'texto': (
            'Uma chuva forte começa a cair. A rua fica escorregadia e a visibilidade some. A loja, '
            'mesmo perigosa, pode ser reforçada para a noite.'
        ),
        'cor_fundo': VERDE,
        'opcoes': [
            {
                'texto': 'Voltar para a loja e barricar.',
                'resultado': 'A decisão leva ao próximo momento: Vigia Noturna.',
                'proxima': 'd2_r2_c8',
                'efeitos': {
                    'energia': -4,
                },
                'itens_add': [],
            },
            {
                'texto': 'Dormir em um carro abandonado.',
                'resultado': 'A decisão leva ao próximo momento: Vigia Noturna.',
                'proxima': 'd2_r2_c8',
                'efeitos': {
                    'energia': -4,
                },
                'itens_add': [],
            },
        ],
    },
    'd2_r2_c8': {
        'dia': 2,
        'titulo': 'DIA 2 - LOJA ABANDONADA: VIGIA NOTURNA',
        'texto': (
            'Os infectados parecem mais ativos durante a noite. O personagem assume parte da vigia e '
            'vê, entre a chuva, luzes distantes que podem vir do terminal ou de um comboio hostil.'
        ),
        'cor_fundo': VERDE,
        'opcoes': [
            {
                'texto': 'Fazer guarda.',
                'resultado': 'A decisão leva ao próximo momento: Esperança.',
                'proxima': 'd2_r2_c9',
                'efeitos': {
                    'energia': -4,
                    'moral': 5,
                    'confianca': 2,
                },
                'itens_add': [],
            },
            {
                'texto': 'Dormir sem turno definido.',
                'resultado': 'A decisão leva ao próximo momento: Esperança.',
                'proxima': 'd2_r2_c9',
                'efeitos': {
                    'energia': -4,
                },
                'itens_add': [],
            },
        ],
    },
    'd2_r2_c9': {
        'dia': 2,
        'titulo': 'DIA 2 - LOJA ABANDONADA: ESPERANÇA',
        'texto': (
            'Antes de dormir, o sobrevivente ferido confirma ter ouvido transmissões militares sobre '
            'uma zona segura fora da cidade. Pela primeira vez, existe um destino.'
        ),
        'cor_fundo': VERDE,
        'opcoes': [
            {
                'texto': 'FIM DO DIA 2 A',
                'resultado': 'Essa decisão encerra o caminho iniciado neste dia.',
                'proxima': 'd2_r2_fim_1',
                'efeitos': {
                    'energia': -4,
                },
                'qualidade': 'media',
            },
            {
                'texto': 'FIM DO DIA 2 B',
                'resultado': 'Essa decisão encerra o caminho iniciado neste dia.',
                'proxima': 'd2_r2_fim_2',
                'efeitos': {
                    'energia': -4,
                },
                'qualidade': 'media',
            },
        ],
    },
    'd2_r3_fim_1': {
        'dia': 2,
        'titulo': 'FIM DO DIA 2 A',
        'texto': 'Apartamento abastecido com água, comida e possível faca de caça.',
        'cor_fundo': VERDE_CLARO,
        'fim_dia': True,
        'proxima_dia': 'd3_r3_inicio',
    },
    'd2_r3_fim_2': {
        'dia': 2,
        'titulo': 'FIM DO DIA 2 B',
        'texto': 'Apartamento abastecido com rações militares e bateria portátil, caso tenha corda.',
        'cor_fundo': VERDE_CLARO,
        'fim_dia': True,
        'proxima_dia': 'd3_r3_inicio',
    },
    'd2_r3_c1': {
        'dia': 2,
        'titulo': 'DIA 2 - O BLOQUEIO E A ÁGUA: POÇO DA ESCADA SUPERIOR',
        'texto': (
            'O personagem sobe até o quarto andar. O calor aumenta, há um rastro de sangue até o '
            'apartamento 402 e a escada para o terraço está bloqueada por móveis.'
        ),
        'cor_fundo': VERDE,
        'opcoes': [
            {
                'texto': 'Investigar o apartamento 402.',
                'resultado': 'A decisão leva ao próximo momento: Apartamento 402.',
                'proxima': 'd2_r3_c2',
                'efeitos': {
                    'energia': -4,
                },
                'itens_add': [],
            },
            {
                'texto': 'Tentar abrir caminho para o terraço.',
                'resultado': 'A decisão leva ao próximo momento: Apartamento 402.',
                'proxima': 'd2_r3_c2',
                'efeitos': {
                    'energia': -4,
                },
                'itens_add': [],
            },
        ],
    },
    'd2_r3_c2': {
        'dia': 2,
        'titulo': 'DIA 2 - O BLOQUEIO E A ÁGUA: APARTAMENTO 402',
        'texto': (
            'O apartamento cheira a antisséptico. Na cozinha há um galão de água mineral intacto. No '
            'corredor interno, um corpo está caído de bruços.'
        ),
        'cor_fundo': VERDE,
        'opcoes': [
            {
                'texto': 'Pegar a água e sair.',
                'resultado': 'A decisão leva ao próximo momento: Corpo no Corredor.',
                'proxima': 'd2_r3_c3',
                'efeitos': {
                    'energia': -4,
                    'comida': 1,
                    'agua': 1,
                },
                'itens_add': [],
            },
            {
                'texto': 'Revistar o corpo.',
                'resultado': 'A escolha cobra seu preço antes que exista tempo para voltar atrás.',
                'final': {
                    'tipo': 'derrota',
                    'titulo': 'MORTE 1',
                    'texto': 'Revistar o corpo sem arma; o infectado morde o personagem antes de ser subjugado.',
                },
                'efeitos': {
                    'vida': -100,
                },
                'qualidade': 'morte',
            },
        ],
    },
    'd2_r3_c3': {
        'dia': 2,
        'titulo': 'DIA 2 - O BLOQUEIO E A ÁGUA: CORPO NO CORREDOR',
        'texto': (
            'O corpo se mexe. É um infectado debilitado, mas ainda perigoso. Perto dele há uma faca '
            'de caça presa à mochila.'
        ),
        'cor_fundo': VERDE,
        'opcoes': [
            {
                'texto': 'Lutar se tiver arma.',
                'resultado': 'A decisão leva ao próximo momento: Barricada do Terraço.',
                'proxima': 'd2_r3_c4',
                'efeitos': {
                    'energia': -8,
                },
                'itens_add': ['mochila', 'faca de caça'],
            },
            {
                'texto': 'Tentar pegar a faca sem lutar.',
                'resultado': 'A decisão leva ao próximo momento: Barricada do Terraço.',
                'proxima': 'd2_r3_c4',
                'efeitos': {
                    'energia': -8,
                },
                'itens_add': ['mochila', 'faca de caça'],
            },
        ],
    },
    'd2_r3_c4': {
        'dia': 2,
        'titulo': 'DIA 2 - O BLOQUEIO E A ÁGUA: BARRICADA DO TERRAÇO',
        'texto': (
            'Mover móveis faz barulho. O céu está nublado e baldes vazios esperam no terraço. A chuva '
            'pode salvar o personagem, mas a demora atrai riscos.'
        ),
        'cor_fundo': VERDE,
        'opcoes': [
            {
                'texto': 'Esperar a chuva.',
                'resultado': 'A decisão leva ao próximo momento: Cabine de Manutenção.',
                'proxima': 'd2_r3_c5',
                'efeitos': {
                    'energia': -4,
                },
                'itens_add': [],
            },
            {
                'texto': 'Vasculhar a cabine de manutenção.',
                'resultado': 'A decisão leva ao próximo momento: Cabine de Manutenção.',
                'proxima': 'd2_r3_c5',
                'efeitos': {
                    'energia': -4,
                    'comida': 1,
                    'agua': 1,
                },
                'itens_add': [],
            },
        ],
    },
    'd2_r3_c5': {
        'dia': 2,
        'titulo': 'DIA 2 - O BLOQUEIO E A ÁGUA: CABINE DE MANUTENÇÃO',
        'texto': (
            'A cabine está trancada. Pela abertura, o personagem vê uma mochila militar abandonada no '
            'poço do elevador, presa em cabos antigos.'
        ),
        'cor_fundo': VERDE,
        'opcoes': [
            {
                'texto': 'Usar a corda se tiver.',
                'resultado': 'A decisão leva ao próximo momento: Água da Chuva.',
                'proxima': 'd2_r3_c6',
                'efeitos': {
                    'energia': -4,
                },
                'itens_add': ['mochila', 'corda'],
            },
            {
                'texto': 'Arrombar a cabine sem corda.',
                'resultado': 'A escolha cobra seu preço antes que exista tempo para voltar atrás.',
                'final': {
                    'tipo': 'derrota',
                    'titulo': 'MORTE 2',
                    'texto': 'Arrombar a cabine sem corda; o teto cede e o personagem cai no poço do elevador.',
                },
                'efeitos': {
                    'vida': -100,
                },
                'qualidade': 'morte',
            },
        ],
    },
    'd2_r3_c6': {
        'dia': 2,
        'titulo': 'DIA 2 - O BLOQUEIO E A ÁGUA: ÁGUA DA CHUVA',
        'texto': (
            'A chuva finalmente cai. O personagem enche baldes, mas na descida escuta portas abrindo '
            'no quarto andar. Algo foi atraído pelo barulho da barricada.'
        ),
        'cor_fundo': VERDE,
        'opcoes': [
            {
                'texto': 'Descer devagar e esconder-se.',
                'resultado': 'A decisão leva ao próximo momento: Mochila Militar.',
                'proxima': 'd2_r3_c7',
                'efeitos': {
                    'energia': -4,
                    'moral': -4,
                    'confianca': -1,
                },
                'itens_add': [],
            },
            {
                'texto': 'Correr pela escada.',
                'resultado': 'A decisão leva ao próximo momento: Mochila Militar.',
                'proxima': 'd2_r3_c7',
                'efeitos': {
                    'energia': -8,
                },
                'itens_add': [],
            },
        ],
    },
    'd2_r3_c7': {
        'dia': 2,
        'titulo': 'DIA 2 - O BLOQUEIO E A ÁGUA: MOCHILA MILITAR',
        'texto': (
            'Com a corda, o personagem alcança a mochila no poço do elevador. Dentro há rações, uma '
            'bateria portátil e um bilhete militar rasgado com a palavra AURORA.'
        ),
        'cor_fundo': VERDE,
        'proxima': 'd2_r3_c8',
    },
    'd2_r3_c8': {
        'dia': 2,
        'titulo': 'DIA 2 - O BLOQUEIO E A ÁGUA: VOLTA AO APARTAMENTO',
        'texto': (
            'Com água ou rações, o personagem retorna. Tiros ecoam de longe, talvez do terminal, '
            'talvez do posto. A cidade começa a se organizar em pequenos grupos violentos.'
        ),
        'cor_fundo': VERDE,
        'proxima': 'd2_r3_c9',
    },
    'd2_r3_c9': {
        'dia': 2,
        'titulo': 'DIA 2 - O BLOQUEIO E A ÁGUA: RACIONAMENTO',
        'texto': (
            'O personagem marca garrafas com fita e separa comida por dias. Pela primeira vez, '
            'sobreviver parece uma matemática cruel.'
        ),
        'cor_fundo': VERDE,
        'opcoes': [
            {
                'texto': 'Guardar recursos para si.',
                'resultado': 'Essa decisão encerra o caminho iniciado neste dia.',
                'proxima': 'd2_r3_fim_1',
                'efeitos': {
                    'energia': -4,
                    'comida': 1,
                    'agua': 1,
                },
                'itens_add': [],
                'qualidade': 'media',
            },
            {
                'texto': 'Deixar água no corredor para algum vizinho vivo.',
                'resultado': 'Essa decisão encerra o caminho iniciado neste dia.',
                'proxima': 'd2_r3_fim_2',
                'efeitos': {
                    'energia': -4,
                    'comida': 1,
                    'agua': 1,
                },
                'itens_add': [],
                'qualidade': 'media',
            },
        ],
    },
    'd2_r4_fim_1': {
        'dia': 2,
        'titulo': 'FIM DO DIA 2 A',
        'texto': 'Terminal seguro, portões reforçados e liderança de Helena fortalecida.',
        'cor_fundo': VERDE_CLARO,
        'fim_dia': True,
        'proxima_dia': 'd3_r4_inicio',
    },
    'd2_r4_fim_2': {
        'dia': 2,
        'titulo': 'FIM DO DIA 2 B',
        'texto': 'Terminal instável, ônibus descoberto, mas Jonas ganha influência perigosa.',
        'cor_fundo': VERDE_CLARO,
        'fim_dia': True,
        'proxima_dia': 'd3_r4_inicio',
    },
    'd2_r4_c1': {
        'dia': 2,
        'titulo': 'DIA 2 - LIDERANÇA NO TERMINAL: DISCUSSÃO NO TERMINAL',
        'texto': (
            'A manhã chega cinza. O terminal cheira a suor, poeira e medo. Helena defende regras '
            'simples; Jonas diz que regras não importam quando os mortos chegarem.'
        ),
        'cor_fundo': VERDE,
        'opcoes': [
            {
                'texto': 'Apoiar Helena.',
                'resultado': 'A decisão leva ao próximo momento: Portões Fracos.',
                'proxima': 'd2_r4_c2',
                'efeitos': {
                    'energia': -4,
                    'moral': 5,
                    'confianca': 2,
                },
                'itens_add': ['aliado Lena', 'aliado Helena', 'aliado Jonas'],
            },
            {
                'texto': 'Apoiar Jonas.',
                'resultado': 'A escolha cobra seu preço antes que exista tempo para voltar atrás.',
                'final': {
                    'tipo': 'derrota',
                    'titulo': 'MORTE 1',
                    'texto': (
                        'Apoiar Jonas e permitir controle das reservas; a disputa vira violência e o personagem é '
                        'morto em um motim.'
                    ),
                },
                'efeitos': {
                    'vida': -100,
                },
                'qualidade': 'morte',
            },
        ],
    },
    'd2_r4_c2': {
        'dia': 2,
        'titulo': 'DIA 2 - LIDERANÇA NO TERMINAL: PORTÕES FRACOS',
        'texto': (
            'As grades estão tortas, correntes frouxas e pontos frágeis podem ceder se a horda '
            'pressionar. Infectados caminham pela avenida.'
        ),
        'cor_fundo': VERDE,
        'opcoes': [
            {
                'texto': 'Reforçar portões.',
                'resultado': 'A decisão leva ao próximo momento: Comida Escondida.',
                'proxima': 'd2_r4_c3',
                'efeitos': {
                    'energia': -8,
                },
                'itens_add': [],
            },
            {
                'texto': 'Guardar energia e não mexer nas grades.',
                'resultado': 'A decisão leva ao próximo momento: Comida Escondida.',
                'proxima': 'd2_r4_c3',
                'efeitos': {
                    'energia': -4,
                },
                'itens_add': [],
            },
        ],
    },
    'd2_r4_c3': {
        'dia': 2,
        'titulo': 'DIA 2 - LIDERANÇA NO TERMINAL: COMIDA ESCONDIDA',
        'texto': (
            'O personagem vê Jonas escondendo parte da comida em uma sala lateral. Ele diz que é '
            'reserva estratégica, mas outros sobreviventes começam a discutir.'
        ),
        'cor_fundo': VERDE,
        'opcoes': [
            {
                'texto': 'Dividir comida.',
                'resultado': 'A decisão leva ao próximo momento: Lista de Ônibus.',
                'proxima': 'd2_r4_c4',
                'efeitos': {
                    'energia': -4,
                    'moral': 5,
                    'confianca': 2,
                    'comida': 1,
                    'agua': 1,
                },
                'itens_add': ['aliado Jonas'],
            },
            {
                'texto': 'Permitir que Jonas controle as reservas.',
                'resultado': 'A decisão leva ao próximo momento: Lista de Ônibus.',
                'proxima': 'd2_r4_c4',
                'efeitos': {
                    'energia': -4,
                },
                'itens_add': ['aliado Jonas'],
            },
        ],
    },
    'd2_r4_c4': {
        'dia': 2,
        'titulo': 'DIA 2 - LIDERANÇA NO TERMINAL: LISTA DE ÔNIBUS',
        'texto': (
            'Helena encontra uma lista de ônibus ainda funcionais. Um deles está na garagem do '
            'terminal. Se for consertado e abastecido, pode levar parte do grupo para fora da cidade.'
        ),
        'cor_fundo': VERDE,
        'opcoes': [
            {
                'texto': 'Contar sobre o ônibus.',
                'resultado': 'A decisão leva ao próximo momento: Infectado no Banheiro.',
                'proxima': 'd2_r4_c5',
                'efeitos': {
                    'energia': -4,
                },
                'itens_add': ['ônibus', 'aliado Lena', 'aliado Helena'],
            },
            {
                'texto': 'Esconder a informação com Helena.',
                'resultado': 'A decisão leva ao próximo momento: Infectado no Banheiro.',
                'proxima': 'd2_r4_c5',
                'efeitos': {
                    'energia': -4,
                    'moral': -4,
                    'confianca': -1,
                },
                'itens_add': ['ônibus', 'aliado Lena', 'aliado Helena'],
            },
        ],
    },
    'd2_r4_c5': {
        'dia': 2,
        'titulo': 'DIA 2 - LIDERANÇA NO TERMINAL: INFECTADO NO BANHEIRO',
        'texto': (
            'Barulhos vêm do banheiro masculino. Um infectado está preso lá dentro, batendo contra a '
            'porta. Ignorar pode custar caro durante a noite.'
        ),
        'cor_fundo': VERDE,
        'opcoes': [
            {
                'texto': 'Eliminar o infectado.',
                'resultado': 'A decisão leva ao próximo momento: Divisão dos Alimentos.',
                'proxima': 'd2_r4_c6',
                'efeitos': {
                    'energia': -4,
                },
                'itens_add': [],
            },
            {
                'texto': 'Trancar o banheiro e esquecer.',
                'resultado': 'A escolha cobra seu preço antes que exista tempo para voltar atrás.',
                'final': {
                    'tipo': 'derrota',
                    'titulo': 'MORTE 2',
                    'texto': (
                        'Trancar o banheiro e esquecer; o infectado escapa à noite e ataca o personagem durante a '
                        'vigia.'
                    ),
                },
                'efeitos': {
                    'vida': -100,
                },
                'qualidade': 'morte',
            },
        ],
    },
    'd2_r4_c6': {
        'dia': 2,
        'titulo': 'DIA 2 - LIDERANÇA NO TERMINAL: DIVISÃO DOS ALIMENTOS',
        'texto': (
            'Crianças, idosos e feridos precisam mais, mas todos estão com fome. Jonas reclama que '
            'solidariedade vai matar o grupo.'
        ),
        'cor_fundo': VERDE,
        'opcoes': [
            {
                'texto': 'Manter divisão justa.',
                'resultado': 'A decisão leva ao próximo momento: Ônibus Possível.',
                'proxima': 'd2_r4_c7',
                'efeitos': {
                    'energia': -4,
                },
                'itens_add': ['aliado Jonas'],
            },
            {
                'texto': 'Priorizar apenas os fortes.',
                'resultado': 'A decisão leva ao próximo momento: Ônibus Possível.',
                'proxima': 'd2_r4_c7',
                'efeitos': {
                    'energia': -4,
                },
                'itens_add': ['aliado Jonas'],
            },
        ],
    },
    'd2_r4_c7': {
        'dia': 2,
        'titulo': 'DIA 2 - LIDERANÇA NO TERMINAL: ÔNIBUS POSSÍVEL',
        'texto': (
            'Helena leva o personagem à garagem. O ônibus está empoeirado, mas inteiro. O problema é '
            'a bateria descarregada e a falta de combustível.'
        ),
        'cor_fundo': VERDE,
        'proxima': 'd2_r4_c8',
    },
    'd2_r4_c8': {
        'dia': 2,
        'titulo': 'DIA 2 - LIDERANÇA NO TERMINAL: BATERIA DESCARREGADA',
        'texto': (
            'Helena acredita que uma peça ou energia de outro veículo pode salvar o ônibus. O plano '
            'dá esperança ao terminal, mas também cria disputa por lugares.'
        ),
        'cor_fundo': VERDE,
        'proxima': 'd2_r4_c9',
    },
    'd2_r4_c9': {
        'dia': 2,
        'titulo': 'DIA 2 - LIDERANÇA NO TERMINAL: VIGIA NOTURNA',
        'texto': (
            'A noite cai. Infectados se movem entre ônibus abandonados. Dentro, o grupo tenta dormir '
            'sem confiar totalmente uns nos outros.'
        ),
        'cor_fundo': VERDE,
        'opcoes': [
            {
                'texto': 'Montar vigia noturna.',
                'resultado': 'Essa decisão encerra o caminho iniciado neste dia.',
                'proxima': 'd2_r4_fim_1',
                'efeitos': {
                    'energia': -4,
                    'moral': 5,
                    'confianca': 2,
                },
                'itens_add': ['ônibus'],
                'qualidade': 'media',
            },
            {
                'texto': 'Deixar cada família cuidar de si.',
                'resultado': 'Essa decisão encerra o caminho iniciado neste dia.',
                'proxima': 'd2_r4_fim_2',
                'efeitos': {
                    'energia': -4,
                },
                'itens_add': ['ônibus'],
                'qualidade': 'media',
            },
        ],
    },
    'd3_r1_fim_1': {
        'dia': 3,
        'titulo': 'FIM DO DIA 3 A',
        'texto': 'Escola segura, grupo traumatizado e novos recursos.',
        'cor_fundo': VERDE_CLARO,
        'fim_dia': True,
        'proxima_dia': 'd4_r1_inicio',
    },
    'd3_r1_fim_2': {
        'dia': 3,
        'titulo': 'FIM DO DIA 3 B',
        'texto': (
            'Escola alcançada, mas sem pistola ou com feridos adicionais, tornando o Dia 4 mais '
            'difícil.'
        ),
        'cor_fundo': VERDE_CLARO,
        'fim_dia': True,
        'proxima_dia': 'd4_r1_inicio',
    },
    'd3_r1_c1': {
        'dia': 3,
        'titulo': 'DIA 3 - ESCOLHAS RUINS: MADRUGADA',
        'texto': (
            'Quase ao amanhecer, o desconhecido que vigiava os fundos da casa desaparece. O silêncio '
            'parece planejado. O personagem sente tarde demais que acolher estranhos custou caro.'
        ),
        'cor_fundo': VERDE,
        'opcoes': [
            {
                'texto': 'Aguardar retorno.',
                'resultado': 'A decisão leva ao próximo momento: Preocupados.',
                'proxima': 'd3_r1_c2',
                'efeitos': {
                    'energia': -4,
                    'comida': 1,
                    'agua': 1,
                },
                'itens_add': [],
            },
            {
                'texto': 'Chamar por ele.',
                'resultado': 'A decisão leva ao próximo momento: Preocupados.',
                'proxima': 'd3_r1_c2',
                'efeitos': {
                    'energia': -4,
                },
                'itens_add': [],
            },
            {
                'texto': 'Avisar José em silêncio.',
                'resultado': 'A decisão leva ao próximo momento: Preocupados.',
                'proxima': 'd3_r1_c2',
                'efeitos': {
                    'energia': -4,
                    'moral': 5,
                    'confianca': 2,
                },
                'itens_add': ['aliado José'],
            },
        ],
    },
    'd3_r1_c2': {
        'dia': 3,
        'titulo': 'DIA 3 - ESCOLHAS RUINS: PREOCUPADOS',
        'texto': (
            'O personagem acorda José e repassa a notícia. O grupo desce com cautela, sem acender '
            'luzes para não chamar atenção de fora.'
        ),
        'cor_fundo': VERDE,
        'proxima': 'd3_r1_c3',
    },
    'd3_r1_c3': {
        'dia': 3,
        'titulo': 'DIA 3 - ESCOLHAS RUINS: TENSÃO',
        'texto': (
            'No banheiro, José leva uma coronhada e cai. Um dos desconhecidos aponta uma pistola para '
            'o personagem.'
        ),
        'cor_fundo': VERDE,
        'opcoes': [
            {
                'texto': 'Render-se e levantar as mãos.',
                'resultado': 'A decisão leva ao próximo momento: Tensão Continua.',
                'proxima': 'd3_r1_c4',
                'efeitos': {
                    'energia': -4,
                    'moral': -4,
                    'confianca': -1,
                },
                'itens_add': ['pistola', 'aliado José'],
            },
            {
                'texto': 'Atacar o homem armado.',
                'resultado': 'A escolha cobra seu preço antes que exista tempo para voltar atrás.',
                'final': {
                    'tipo': 'derrota',
                    'titulo': 'MORTE 1',
                    'texto': 'Atacar o homem armado na cena da rendição; o personagem leva um tiro à queima-roupa.',
                },
                'efeitos': {
                    'vida': -100,
                },
                'qualidade': 'morte',
            },
        ],
    },
    'd3_r1_c4': {
        'dia': 3,
        'titulo': 'DIA 3 - ESCOLHAS RUINS: TENSÃO CONTINUA',
        'texto': (
            'Pedro também foi derrubado. Joice, Lena e Davi estão sentados no canto enquanto o '
            'segundo desconhecido recolhe mochilas. Eles querem recursos só para eles.'
        ),
        'cor_fundo': VERDE,
        'proxima': 'd3_r1_c5',
    },
    'd3_r1_c5': {
        'dia': 3,
        'titulo': 'DIA 3 - ESCOLHAS RUINS: TIROS',
        'texto': (
            'Davi começa a chorar. Um dos criminosos ameaça matar a criança. José, enfurecido, ataca '
            'o homem armado.'
        ),
        'cor_fundo': VERDE,
        'opcoes': [
            {
                'texto': 'Ajudar José.',
                'resultado': 'A decisão leva ao próximo momento: Mais Tiros.',
                'proxima': 'd3_r1_c6',
                'efeitos': {
                    'energia': -4,
                    'moral': 5,
                    'confianca': 2,
                },
                'itens_add': ['aliado José', 'aliado Davi'],
            },
            {
                'texto': 'Atacar o outro desconhecido.',
                'resultado': 'A decisão leva ao próximo momento: Mais Tiros.',
                'proxima': 'd3_r1_c6',
                'efeitos': {
                    'energia': -8,
                },
                'itens_add': ['aliado José', 'aliado Davi'],
            },
            {
                'texto': 'Acalmar Davi.',
                'resultado': 'A decisão leva ao próximo momento: Mais Tiros.',
                'proxima': 'd3_r1_c6',
                'efeitos': {
                    'energia': -4,
                    'moral': 5,
                    'confianca': 2,
                },
                'itens_add': ['aliado José', 'aliado Davi'],
            },
        ],
    },
    'd3_r1_c6': {
        'dia': 3,
        'titulo': 'DIA 3 - ESCOLHAS RUINS: MAIS TIROS',
        'texto': (
            'Disparos quebram o silêncio. José mata um dos desconhecidos, mas o outro atira em José e '
            'Lucas. Ambos caem mortos. O atirador foge mancando com a mochila de recursos.'
        ),
        'cor_fundo': VERDE,
        'opcoes': [
            {
                'texto': 'Correr atrás dele.',
                'resultado': 'A decisão leva ao próximo momento: Eliminação.',
                'proxima': 'd3_r1_c7',
                'efeitos': {
                    'energia': -8,
                },
                'itens_add': ['mochila', 'aliado José', 'aliado Lucas'],
            },
            {
                'texto': 'Aguardar para evitar mais mortes.',
                'resultado': 'A decisão leva ao próximo momento: Eliminação.',
                'proxima': 'd3_r1_c7',
                'efeitos': {
                    'energia': -4,
                    'comida': 1,
                    'agua': 1,
                },
                'itens_add': ['mochila', 'aliado José', 'aliado Lucas'],
            },
            {
                'texto': 'Tentar salvar José e Lucas.',
                'resultado': 'A decisão leva ao próximo momento: Eliminação.',
                'proxima': 'd3_r1_c7',
                'efeitos': {
                    'energia': -4,
                    'moral': 5,
                    'confianca': 2,
                },
                'itens_add': ['mochila', 'aliado José', 'aliado Lucas'],
            },
        ],
    },
    'd3_r1_c7': {
        'dia': 3,
        'titulo': 'DIA 3 - ESCOLHAS RUINS: ELIMINAÇÃO',
        'texto': (
            'O desconhecido desce e encontra infectados atraídos pelos tiros. O vidro dos fundos '
            'quebra. Seus gritos ecoam pela casa. A morte dele vira distração.'
        ),
        'cor_fundo': VERDE,
        'opcoes': [
            {
                'texto': 'Sair imediatamente com o grupo.',
                'resultado': 'A decisão leva ao próximo momento: Recomposição.',
                'proxima': 'd3_r1_c8',
                'efeitos': {
                    'energia': -4,
                },
                'itens_add': ['rações'],
            },
            {
                'texto': 'Ficar para recuperar os recursos.',
                'resultado': 'A escolha cobra seu preço antes que exista tempo para voltar atrás.',
                'final': {
                    'tipo': 'derrota',
                    'titulo': 'MORTE 2',
                    'texto': (
                        'Ficar para recuperar recursos enquanto os infectados entram; o grupo é cercado no '
                        'térreo.'
                    ),
                },
                'efeitos': {
                    'vida': -100,
                },
                'qualidade': 'morte',
            },
        ],
    },
    'd3_r1_c8': {
        'dia': 3,
        'titulo': 'DIA 3 - ESCOLHAS RUINS: RECOMPOSIÇÃO',
        'texto': (
            'Na rua vazia, o grupo está reduzido. Lena perdeu o marido. Joice perdeu o irmão. Davi '
            'perdeu o pai. O personagem carrega uma pistola, poucos recursos e muitas culpas.'
        ),
        'cor_fundo': VERDE,
        'proxima': 'd3_r1_c9',
    },
    'd3_r1_c9': {
        'dia': 3,
        'titulo': 'DIA 3 - ESCOLHAS RUINS: ESCOLA',
        'texto': (
            'O grupo pula o portão de uma escola próxima. Há barricadas antigas, mochilas abandonadas '
            'e comida no refeitório. O lugar parece seguro, mas também sugere que há gente escondida '
            'ali.'
        ),
        'cor_fundo': VERDE,
        'opcoes': [
            {
                'texto': 'Trancar-se no refeitório.',
                'resultado': 'Essa decisão encerra o caminho iniciado neste dia.',
                'proxima': 'd3_r1_fim_1',
                'efeitos': {
                    'energia': -4,
                },
                'itens_add': ['mochila'],
                'qualidade': 'media',
            },
            {
                'texto': 'Investigar a escola ainda à noite.',
                'resultado': 'Essa decisão encerra o caminho iniciado neste dia.',
                'proxima': 'd3_r1_fim_2',
                'efeitos': {
                    'energia': -4,
                },
                'itens_add': ['mochila'],
                'qualidade': 'media',
            },
        ],
    },
    'd3_r2_fim_1': {
        'dia': 3,
        'titulo': 'FIM DO DIA 3 A',
        'texto': 'Viaduto com comida, água, combustível e coordenadas parciais.',
        'cor_fundo': VERDE_CLARO,
        'fim_dia': True,
        'proxima_dia': 'd4_r2_inicio',
    },
    'd3_r2_fim_2': {
        'dia': 3,
        'titulo': 'FIM DO DIA 3 B',
        'texto': 'Viaduto com menos recursos, mas grupo inteiro e mais rápido.',
        'cor_fundo': VERDE_CLARO,
        'fim_dia': True,
        'proxima_dia': 'd4_r2_inicio',
    },
    'd3_r2_c1': {
        'dia': 3,
        'titulo': 'DIA 3 - POSTO DE GASOLINA: RECURSOS ACABANDO',
        'texto': (
            'A manhã chega fria. A chuva da noite anterior molhou roupas e mochilas. A comida '
            'restante não será suficiente para todos.'
        ),
        'cor_fundo': VERDE,
        'opcoes': [
            {
                'texto': 'Procurar mais suprimentos.',
                'resultado': 'A decisão leva ao próximo momento: O Posto.',
                'proxima': 'd3_r2_c2',
                'efeitos': {
                    'energia': -4,
                    'comida': 1,
                    'agua': 1,
                },
                'itens_add': ['mochila'],
            },
            {
                'texto': 'Racionar e não sair.',
                'resultado': 'A decisão leva ao próximo momento: O Posto.',
                'proxima': 'd3_r2_c2',
                'efeitos': {
                    'energia': -4,
                },
                'itens_add': ['mochila'],
            },
        ],
    },
    'd3_r2_c2': {
        'dia': 3,
        'titulo': 'DIA 3 - POSTO DE GASOLINA: O POSTO',
        'texto': (
            'Após horas por ruas secundárias, o grupo encontra um posto de gasolina aparentemente '
            'abandonado. A conveniência parece intacta, mas as portas estão fechadas.'
        ),
        'cor_fundo': VERDE,
        'opcoes': [
            {
                'texto': 'Entrar na conveniência.',
                'resultado': 'A decisão leva ao próximo momento: A Conveniência.',
                'proxima': 'd3_r2_c3',
                'efeitos': {
                    'energia': -4,
                },
                'itens_add': [],
            },
            {
                'texto': 'Vasculhar bombas primeiro.',
                'resultado': 'A decisão leva ao próximo momento: A Conveniência.',
                'proxima': 'd3_r2_c3',
                'efeitos': {
                    'energia': -4,
                    'comida': 1,
                    'agua': 1,
                },
                'itens_add': [],
            },
        ],
    },
    'd3_r2_c3': {
        'dia': 3,
        'titulo': 'DIA 3 - POSTO DE GASOLINA: A CONVENIÊNCIA',
        'texto': (
            'O interior está escuro. Há alimentos espalhados, cheiro de comida estragada e uma '
            'mochila esquecida perto do caixa.'
        ),
        'cor_fundo': VERDE,
        'opcoes': [
            {
                'texto': 'Recolher suprimentos.',
                'resultado': 'A decisão leva ao próximo momento: O Gerador.',
                'proxima': 'd3_r2_c4',
                'efeitos': {
                    'energia': -4,
                    'comida': 1,
                    'agua': 1,
                },
                'itens_add': ['mochila'],
            },
            {
                'texto': 'Abrir a mochila sem olhar ao redor.',
                'resultado': 'A decisão leva ao próximo momento: O Gerador.',
                'proxima': 'd3_r2_c4',
                'efeitos': {
                    'energia': -4,
                },
                'itens_add': ['mochila'],
            },
        ],
    },
    'd3_r2_c4': {
        'dia': 3,
        'titulo': 'DIA 3 - POSTO DE GASOLINA: O GERADOR',
        'texto': (
            'Nos fundos existe um pequeno gerador desligado e galões de combustível. Levar '
            'combustível pode ser útil, mas pesa.'
        ),
        'cor_fundo': VERDE,
        'opcoes': [
            {
                'texto': 'Coletar combustível.',
                'resultado': 'A decisão leva ao próximo momento: Carro de Polícia.',
                'proxima': 'd3_r2_c5',
                'efeitos': {
                    'energia': -4,
                    'comida': 1,
                    'agua': 1,
                },
                'itens_add': ['combustível'],
            },
            {
                'texto': 'Deixar os galões para andar mais leve.',
                'resultado': 'A decisão leva ao próximo momento: Carro de Polícia.',
                'proxima': 'd3_r2_c5',
                'efeitos': {
                    'energia': -4,
                },
                'itens_add': ['combustível'],
            },
        ],
    },
    'd3_r2_c5': {
        'dia': 3,
        'titulo': 'DIA 3 - POSTO DE GASOLINA: CARRO DE POLÍCIA',
        'texto': (
            'Uma viatura abandonada ainda produz ruídos estáticos. O rádio menciona uma zona segura '
            'fora da cidade e cortes de quarentena perto da rodovia.'
        ),
        'cor_fundo': VERDE,
        'opcoes': [
            {
                'texto': 'Ouvir o rádio.',
                'resultado': 'A decisão leva ao próximo momento: O Alarme.',
                'proxima': 'd3_r2_c6',
                'efeitos': {
                    'energia': -4,
                },
                'itens_add': ['rádio'],
            },
            {
                'texto': 'Ignorar o rádio e ir embora.',
                'resultado': 'A decisão leva ao próximo momento: O Alarme.',
                'proxima': 'd3_r2_c6',
                'efeitos': {
                    'energia': -4,
                    'moral': -4,
                    'confianca': -1,
                },
                'itens_add': ['rádio'],
            },
        ],
    },
    'd3_r2_c6': {
        'dia': 3,
        'titulo': 'DIA 3 - POSTO DE GASOLINA: O ALARME',
        'texto': (
            'Um sobrevivente esbarra em prateleira metálica e ativa um alarme com bateria. O som ecoa '
            'pela região.'
        ),
        'cor_fundo': VERDE,
        'opcoes': [
            {
                'texto': 'Sair imediatamente.',
                'resultado': 'A decisão leva ao próximo momento: Movimento na Estrada.',
                'proxima': 'd3_r2_c7',
                'efeitos': {
                    'energia': -4,
                },
                'itens_add': ['bateria portátil'],
            },
            {
                'texto': 'Tentar desligar o alarme.',
                'resultado': 'A escolha cobra seu preço antes que exista tempo para voltar atrás.',
                'final': {
                    'tipo': 'derrota',
                    'titulo': 'MORTE 1',
                    'texto': (
                        'Tentar desligar o alarme com a horda chegando; o personagem fica preso entre prateleiras '
                        'e infectados.'
                    ),
                },
                'efeitos': {
                    'vida': -100,
                },
                'qualidade': 'morte',
            },
        ],
    },
    'd3_r2_c7': {
        'dia': 3,
        'titulo': 'DIA 3 - POSTO DE GASOLINA: MOVIMENTO NA ESTRADA',
        'texto': (
            'Dezenas de infectados surgem entre carros abandonados. Alguns caminham, outros parecem '
            'seguir o som diretamente.'
        ),
        'cor_fundo': VERDE,
        'opcoes': [
            {
                'texto': 'Seguir pelos fundos.',
                'resultado': 'A decisão leva ao próximo momento: Perseguição.',
                'proxima': 'd3_r2_c8',
                'efeitos': {
                    'energia': -4,
                },
                'itens_add': [],
            },
            {
                'texto': 'Cruzar a frente do posto.',
                'resultado': 'A decisão leva ao próximo momento: Perseguição.',
                'proxima': 'd3_r2_c8',
                'efeitos': {
                    'energia': -4,
                },
                'itens_add': [],
            },
        ],
    },
    'd3_r2_c8': {
        'dia': 3,
        'titulo': 'DIA 3 - POSTO DE GASOLINA: PERSEGUIÇÃO',
        'texto': 'A horda se aproxima e o grupo está cansado. Suprimentos pesam nas costas.',
        'cor_fundo': VERDE,
        'opcoes': [
            {
                'texto': 'Abandonar parte da carga.',
                'resultado': 'A escolha cobra seu preço antes que exista tempo para voltar atrás.',
                'final': {
                    'tipo': 'derrota',
                    'titulo': 'MORTE 2',
                    'texto': (
                        'Manter toda a carga durante a perseguição; o peso reduz a velocidade e o grupo é '
                        'alcançado.'
                    ),
                },
                'efeitos': {
                    'vida': -100,
                },
                'qualidade': 'morte',
            },
            {
                'texto': 'Manter tudo e correr.',
                'resultado': 'A decisão leva ao próximo momento: Viaduto e Transmissão.',
                'proxima': 'd3_r2_c9',
                'efeitos': {
                    'energia': -8,
                },
                'itens_add': [],
            },
        ],
    },
    'd3_r2_c9': {
        'dia': 3,
        'titulo': 'DIA 3 - POSTO DE GASOLINA: VIADUTO E TRANSMISSÃO',
        'texto': (
            'Ao anoitecer, o grupo se abriga sob um viaduto. O rádio da viatura capta mensagem mais '
            'clara: Operação Aurora continua recebendo sobreviventes na direção da rodovia e da base.'
        ),
        'cor_fundo': VERDE,
        'opcoes': [
            {
                'texto': 'FIM DO DIA 3 A',
                'resultado': 'Essa decisão encerra o caminho iniciado neste dia.',
                'proxima': 'd3_r2_fim_1',
                'efeitos': {
                    'energia': -4,
                },
                'qualidade': 'media',
            },
            {
                'texto': 'FIM DO DIA 3 B',
                'resultado': 'Essa decisão encerra o caminho iniciado neste dia.',
                'proxima': 'd3_r2_fim_2',
                'efeitos': {
                    'energia': -4,
                },
                'qualidade': 'media',
            },
        ],
    },
    'd3_r3_fim_1': {
        'dia': 3,
        'titulo': 'FIM DO DIA 3 A',
        'texto': 'Coordenadas completas do estádio e pé de cabra obtido.',
        'cor_fundo': VERDE_CLARO,
        'fim_dia': True,
        'proxima_dia': 'd4_r3_inicio',
    },
    'd3_r3_fim_2': {
        'dia': 3,
        'titulo': 'FIM DO DIA 3 B',
        'texto': 'Coordenadas incompletas, mas indicação de resgate no Dia 7.',
        'cor_fundo': VERDE_CLARO,
        'fim_dia': True,
        'proxima_dia': 'd4_r3_inicio',
    },
    'd3_r3_c1': {
        'dia': 3,
        'titulo': 'DIA 3 - FREQUÊNCIAS DE RÁDIO: APARTAMENTO DO SÍNDICO',
        'texto': (
            'O síndico morava na cobertura e era entusiasta de rádio amador. O corredor da cobertura '
            'está limpo em excesso, sem sangue, sem móveis, sem sinal de fuga. Isso parece mais '
            'perigoso que sujeira.'
        ),
        'cor_fundo': VERDE,
        'opcoes': [
            {
                'texto': 'Entrar direto na sala.',
                'resultado': 'A decisão leva ao próximo momento: Sala da Cobertura.',
                'proxima': 'd3_r3_c2',
                'efeitos': {
                    'energia': -4,
                },
                'itens_add': ['rádio'],
            },
            {
                'texto': 'Investigar armários de incêndio.',
                'resultado': 'A decisão leva ao próximo momento: Sala da Cobertura.',
                'proxima': 'd3_r3_c2',
                'efeitos': {
                    'energia': -4,
                },
                'itens_add': ['rádio'],
            },
        ],
    },
    'd3_r3_c2': {
        'dia': 3,
        'titulo': 'DIA 3 - FREQUÊNCIAS DE RÁDIO: SALA DA COBERTURA',
        'texto': (
            'O rádio amador está na mesa, mas os cabos foram arrancados e puxados até o quarto '
            'principal. A luz não funciona.'
        ),
        'cor_fundo': VERDE,
        'opcoes': [
            {
                'texto': 'Seguir os cabos até o quarto.',
                'resultado': 'A decisão leva ao próximo momento: Quarto Escuro.',
                'proxima': 'd3_r3_c3',
                'efeitos': {
                    'energia': -4,
                },
                'itens_add': ['rádio'],
            },
            {
                'texto': 'Tentar consertar o rádio na sala.',
                'resultado': 'A decisão leva ao próximo momento: Quarto Escuro.',
                'proxima': 'd3_r3_c3',
                'efeitos': {
                    'energia': -4,
                },
                'itens_add': ['rádio'],
            },
        ],
    },
    'd3_r3_c3': {
        'dia': 3,
        'titulo': 'DIA 3 - FREQUÊNCIAS DE RÁDIO: QUARTO ESCURO',
        'texto': (
            'No quarto, fios finos atravessam a porta. O síndico paranoico montou uma armadilha com '
            'explosivos improvisados. A lanterna pode revelar o perigo.'
        ),
        'cor_fundo': VERDE,
        'opcoes': [
            {
                'texto': 'Usar lanterna se tiver.',
                'resultado': 'A decisão leva ao próximo momento: Rádio Incompleto.',
                'proxima': 'd3_r3_c4',
                'efeitos': {
                    'energia': -4,
                },
                'itens_add': ['lanterna'],
            },
            {
                'texto': 'Entrar no escuro.',
                'resultado': 'A escolha cobra seu preço antes que exista tempo para voltar atrás.',
                'final': {
                    'tipo': 'derrota',
                    'titulo': 'MORTE 1',
                    'texto': 'Entrar no quarto escuro sem lanterna; a armadilha explode.',
                },
                'efeitos': {
                    'vida': -100,
                },
                'qualidade': 'morte',
            },
        ],
    },
    'd3_r3_c4': {
        'dia': 3,
        'titulo': 'DIA 3 - FREQUÊNCIAS DE RÁDIO: RÁDIO INCOMPLETO',
        'texto': (
            'Tentando consertar o rádio sem ferramentas, o personagem consegue apenas trechos: '
            'estádio, Dia 7, portão leste, Aurora. O resto se perde em chiado.'
        ),
        'cor_fundo': VERDE,
        'proxima': 'd3_r3_c5',
    },
    'd3_r3_c5': {
        'dia': 3,
        'titulo': 'DIA 3 - FREQUÊNCIAS DE RÁDIO: ARMÁRIO DE INCÊNDIO',
        'texto': (
            'Dentro do armário está o corpo do síndico. No bolso, uma chave da sala de comunicações '
            'no subsolo. No pulso, uma pulseira com nome de filha: Sofia.'
        ),
        'cor_fundo': VERDE,
        'opcoes': [
            {
                'texto': 'Pegar a chave.',
                'resultado': 'A decisão leva ao próximo momento: Sala de Comunicações.',
                'proxima': 'd3_r3_c6',
                'efeitos': {
                    'energia': -4,
                },
                'itens_add': ['aliado Sofia'],
            },
            {
                'texto': 'Ignorar o corpo e voltar à cobertura.',
                'resultado': 'A decisão leva ao próximo momento: Sala de Comunicações.',
                'proxima': 'd3_r3_c6',
                'efeitos': {
                    'energia': -4,
                    'moral': -4,
                    'confianca': -1,
                },
                'itens_add': ['aliado Sofia'],
            },
        ],
    },
    'd3_r3_c6': {
        'dia': 3,
        'titulo': 'DIA 3 - FREQUÊNCIAS DE RÁDIO: SALA DE COMUNICAÇÕES',
        'texto': (
            'No subsolo, a chave abre uma sala protegida. O rádio central funciona. A mensagem é '
            'clara: resgate civil no Estádio de Futebol no Dia 7; triagem militar na base.'
        ),
        'cor_fundo': VERDE,
        'opcoes': [
            {
                'texto': 'Anotar coordenadas.',
                'resultado': 'A decisão leva ao próximo momento: Pé de Cabra.',
                'proxima': 'd3_r3_c7',
                'efeitos': {
                    'energia': -4,
                },
                'itens_add': ['rádio', 'coordenadas'],
            },
            {
                'texto': 'Transmitir pedido de socorro.',
                'resultado': 'A escolha cobra seu preço antes que exista tempo para voltar atrás.',
                'final': {
                    'tipo': 'derrota',
                    'titulo': 'MORTE 2',
                    'texto': (
                        'Transmitir pedido de socorro alto em excesso; saqueadores próximos rastreiam o sinal e '
                        'invadem o prédio.'
                    ),
                },
                'efeitos': {
                    'vida': -100,
                },
                'qualidade': 'morte',
            },
        ],
    },
    'd3_r3_c7': {
        'dia': 3,
        'titulo': 'DIA 3 - FREQUÊNCIAS DE RÁDIO: PÉ DE CABRA',
        'texto': (
            'Atrás da mesa, há um pé de cabra usado para fechar armários. É ferramenta e arma ao '
            'mesmo tempo. O personagem percebe que preparo pode valer mais que coragem.'
        ),
        'cor_fundo': VERDE,
        'proxima': 'd3_r3_c8',
    },
    'd3_r3_c8': {
        'dia': 3,
        'titulo': 'DIA 3 - FREQUÊNCIAS DE RÁDIO: PASSOS NA ESCADA',
        'texto': (
            'Ao voltar, passos pesados sobem o prédio. Não parecem humanos apressados; parecem '
            'criaturas seguindo som. O personagem precisa sumir antes que cheguem ao corredor.'
        ),
        'cor_fundo': VERDE,
        'opcoes': [
            {
                'texto': 'Trancar-se no apartamento.',
                'resultado': 'A decisão leva ao próximo momento: Fim da Transmissão.',
                'proxima': 'd3_r3_c9',
                'efeitos': {
                    'energia': -4,
                },
                'itens_add': [],
            },
            {
                'texto': 'Esconder-se na sala de comunicações.',
                'resultado': 'A decisão leva ao próximo momento: Fim da Transmissão.',
                'proxima': 'd3_r3_c9',
                'efeitos': {
                    'energia': -4,
                    'moral': -4,
                    'confianca': -1,
                },
                'itens_add': [],
            },
        ],
    },
    'd3_r3_c9': {
        'dia': 3,
        'titulo': 'DIA 3 - FREQUÊNCIAS DE RÁDIO: FIM DA TRANSMISSÃO',
        'texto': (
            'Com coordenadas anotadas ou com informações incompletas, o personagem volta ao '
            'esconderijo. Pela primeira vez, o Dia 7 tem um lugar: o estádio.'
        ),
        'cor_fundo': VERDE,
        'opcoes': [
            {
                'texto': 'FIM DO DIA 3 A',
                'resultado': 'Essa decisão encerra o caminho iniciado neste dia.',
                'proxima': 'd3_r3_fim_1',
                'efeitos': {
                    'energia': -4,
                },
                'qualidade': 'media',
            },
            {
                'texto': 'FIM DO DIA 3 B',
                'resultado': 'Essa decisão encerra o caminho iniciado neste dia.',
                'proxima': 'd3_r3_fim_2',
                'efeitos': {
                    'energia': -4,
                },
                'qualidade': 'media',
            },
        ],
    },
    'd3_r4_fim_1': {
        'dia': 3,
        'titulo': 'FIM DO DIA 3 A',
        'texto': 'Ônibus reparado e criança salva, fortalecendo o final heroico.',
        'cor_fundo': VERDE_CLARO,
        'fim_dia': True,
        'proxima_dia': 'd4_r4_inicio',
    },
    'd3_r4_fim_2': {
        'dia': 3,
        'titulo': 'FIM DO DIA 3 B',
        'texto': 'Ônibus reparado sem salvar a criança, gerando culpa e perda de confiança.',
        'cor_fundo': VERDE_CLARO,
        'fim_dia': True,
        'proxima_dia': 'd4_r4_inicio',
    },
    'd3_r4_c1': {
        'dia': 3,
        'titulo': 'DIA 3 - A PEÇA DO ÔNIBUS: DEFEITO NO ÔNIBUS',
        'texto': (
            'Helena mostra que o ônibus precisa de uma peça para manter força. A garagem tem veículos '
            'abandonados e infectados presos entre carros.'
        ),
        'cor_fundo': VERDE,
        'opcoes': [
            {
                'texto': 'Ir com Helena.',
                'resultado': 'A decisão leva ao próximo momento: Veículo para Peça.',
                'proxima': 'd3_r4_c2',
                'efeitos': {
                    'energia': -4,
                },
                'itens_add': ['ônibus', 'peça do ônibus', 'aliado Lena', 'aliado Helena'],
            },
            {
                'texto': 'Mandar Jonas buscar a peça.',
                'resultado': 'A decisão leva ao próximo momento: Veículo para Peça.',
                'proxima': 'd3_r4_c2',
                'efeitos': {
                    'energia': -4,
                },
                'itens_add': ['ônibus', 'peça do ônibus', 'aliado Lena', 'aliado Helena', 'aliado Jonas'],
            },
        ],
    },
    'd3_r4_c2': {
        'dia': 3,
        'titulo': 'DIA 3 - A PEÇA DO ÔNIBUS: VEÍCULO PARA PEÇA',
        'texto': (
            'A peça pode ser retirada de outro ônibus no setor antigo da garagem. O caminho é escuro '
            'e apertado.'
        ),
        'cor_fundo': VERDE,
        'opcoes': [
            {
                'texto': 'Entrar pelos fundos.',
                'resultado': 'A decisão leva ao próximo momento: Garagem Escura.',
                'proxima': 'd3_r4_c3',
                'efeitos': {
                    'energia': -4,
                },
                'itens_add': ['ônibus', 'peça do ônibus'],
            },
            {
                'texto': 'Ir pelo centro da garagem.',
                'resultado': 'A escolha cobra seu preço antes que exista tempo para voltar atrás.',
                'final': {
                    'tipo': 'derrota',
                    'titulo': 'MORTE 1',
                    'texto': 'Ir pelo centro da garagem; o personagem é cercado entre veículos.',
                },
                'efeitos': {
                    'vida': -100,
                },
                'qualidade': 'morte',
            },
        ],
    },
    'd3_r4_c3': {
        'dia': 3,
        'titulo': 'DIA 3 - A PEÇA DO ÔNIBUS: GARAGEM ESCURA',
        'texto': (
            'O cheiro de combustível velho se mistura ao de corpos escondidos. Infectados presos '
            'batem contra portas de carros.'
        ),
        'cor_fundo': VERDE,
        'proxima': 'd3_r4_c4',
    },
    'd3_r4_c4': {
        'dia': 3,
        'titulo': 'DIA 3 - A PEÇA DO ÔNIBUS: JONAS APARECE',
        'texto': (
            'Jonas surge oferecendo ajuda, mas cobra influência sobre o ônibus. Ele diz que Helena é '
            'fraca para decidir quem vive.'
        ),
        'cor_fundo': VERDE,
        'opcoes': [
            {
                'texto': 'Recusar acordo com Jonas.',
                'resultado': 'A decisão leva ao próximo momento: Ônibus Escolar Batido.',
                'proxima': 'd3_r4_c5',
                'efeitos': {
                    'energia': -4,
                },
                'itens_add': ['ônibus', 'aliado Lena', 'aliado Helena', 'aliado Jonas'],
            },
            {
                'texto': 'Aceitar acordo com Jonas.',
                'resultado': 'A decisão leva ao próximo momento: Ônibus Escolar Batido.',
                'proxima': 'd3_r4_c5',
                'efeitos': {
                    'energia': -4,
                },
                'itens_add': ['ônibus', 'aliado Lena', 'aliado Helena', 'aliado Jonas'],
            },
        ],
    },
    'd3_r4_c5': {
        'dia': 3,
        'titulo': 'DIA 3 - A PEÇA DO ÔNIBUS: ÔNIBUS ESCOLAR BATIDO',
        'texto': 'O ônibus escolar está perto da parede externa. Há marcas de mãos no vidro embaçado.',
        'cor_fundo': VERDE,
        'proxima': 'd3_r4_c6',
    },
    'd3_r4_c6': {
        'dia': 3,
        'titulo': 'DIA 3 - A PEÇA DO ÔNIBUS: CRIANÇA ESCONDIDA',
        'texto': (
            'Dentro do ônibus, uma criança está escondida entre bancos. Helena quer salvá-la antes de '
            'mexer na peça.'
        ),
        'cor_fundo': VERDE,
        'opcoes': [
            {
                'texto': 'Salvar a criança.',
                'resultado': 'A decisão leva ao próximo momento: Peça Retirada.',
                'proxima': 'd3_r4_c7',
                'efeitos': {
                    'energia': -4,
                    'moral': 5,
                    'confianca': 2,
                },
                'itens_add': ['ônibus', 'peça do ônibus', 'aliado Lena', 'aliado Helena'],
            },
            {
                'texto': 'Pegar a peça primeiro.',
                'resultado': 'A decisão leva ao próximo momento: Peça Retirada.',
                'proxima': 'd3_r4_c7',
                'efeitos': {
                    'energia': -4,
                },
                'itens_add': ['ônibus', 'peça do ônibus', 'aliado Lena', 'aliado Helena'],
            },
        ],
    },
    'd3_r4_c7': {
        'dia': 3,
        'titulo': 'DIA 3 - A PEÇA DO ÔNIBUS: PEÇA RETIRADA',
        'texto': 'A peça está presa ao painel enferrujado. O menor barulho ecoa.',
        'cor_fundo': VERDE,
        'opcoes': [
            {
                'texto': 'Usar ferramentas.',
                'resultado': 'A decisão leva ao próximo momento: Infectados se Aproximam.',
                'proxima': 'd3_r4_c8',
                'efeitos': {
                    'energia': -4,
                },
                'itens_add': ['ferramentas', 'peça do ônibus'],
            },
            {
                'texto': 'Arrancar a peça à força.',
                'resultado': 'A escolha cobra seu preço antes que exista tempo para voltar atrás.',
                'final': {
                    'tipo': 'derrota',
                    'titulo': 'MORTE 2',
                    'texto': 'Arrancar a peça à força; o barulho atrai infectados antes que consigam sair.',
                },
                'efeitos': {
                    'vida': -100,
                },
                'qualidade': 'morte',
            },
        ],
    },
    'd3_r4_c8': {
        'dia': 3,
        'titulo': 'DIA 3 - A PEÇA DO ÔNIBUS: INFECTADOS SE APROXIMAM',
        'texto': (
            'O som metálico atrai infectados. Helena segura a criança enquanto o personagem abre '
            'caminho.'
        ),
        'cor_fundo': VERDE,
        'opcoes': [
            {
                'texto': 'Distrair infectados.',
                'resultado': 'A decisão leva ao próximo momento: Retorno ao Terminal.',
                'proxima': 'd3_r4_c9',
                'efeitos': {
                    'energia': -4,
                },
                'itens_add': ['aliado Lena', 'aliado Helena'],
            },
            {
                'texto': 'Correr pelo caminho direto.',
                'resultado': 'A decisão leva ao próximo momento: Retorno ao Terminal.',
                'proxima': 'd3_r4_c9',
                'efeitos': {
                    'energia': -8,
                },
                'itens_add': ['aliado Lena', 'aliado Helena'],
            },
        ],
    },
    'd3_r4_c9': {
        'dia': 3,
        'titulo': 'DIA 3 - A PEÇA DO ÔNIBUS: RETORNO AO TERMINAL',
        'texto': (
            'Com a peça na mochila e a criança salva, o grupo retorna. O ônibus finalmente tem chance '
            'real de funcionar.'
        ),
        'cor_fundo': VERDE,
        'opcoes': [
            {
                'texto': 'Voltar rápido.',
                'resultado': 'Essa decisão encerra o caminho iniciado neste dia.',
                'proxima': 'd3_r4_fim_1',
                'efeitos': {
                    'energia': -4,
                },
                'itens_add': ['mochila', 'ônibus', 'peça do ônibus'],
                'qualidade': 'media',
            },
            {
                'texto': 'Vasculhar outros veículos.',
                'resultado': 'Essa decisão encerra o caminho iniciado neste dia.',
                'proxima': 'd3_r4_fim_2',
                'efeitos': {
                    'energia': -4,
                    'comida': 1,
                    'agua': 1,
                },
                'itens_add': ['mochila', 'ônibus', 'peça do ônibus'],
                'qualidade': 'media',
            },
        ],
    },
    'd4_r1_fim_1': {
        'dia': 4,
        'titulo': 'FIM DO DIA 4 A',
        'texto': 'Grupo crescido, escola organizada e plano de evacuação para a base.',
        'cor_fundo': VERDE_CLARO,
        'fim_dia': True,
        'proxima_dia': 'd5_r1_inicio',
    },
    'd4_r1_fim_2': {
        'dia': 4,
        'titulo': 'FIM DO DIA 4 B',
        'texto': 'Grupo menor, mas mais silencioso, caso o jogador decida ir a pé com poucos adultos.',
        'cor_fundo': VERDE_CLARO,
        'fim_dia': True,
        'proxima_dia': 'd5_r1_inicio',
    },
    'd4_r1_c1': {
        'dia': 4,
        'titulo': 'DIA 4 - UM NOVO GRUPO: INVESTIGAÇÃO',
        'texto': (
            'O dia amanhece na escola. O personagem percebe que barricadas nos portões significam que '
            'alguém tentou proteger o lugar. Sons vêm do ginásio.'
        ),
        'cor_fundo': VERDE,
        'opcoes': [
            {
                'texto': 'Investigar o ginásio.',
                'resultado': 'A decisão leva ao próximo momento: A Diretora.',
                'proxima': 'd4_r1_c2',
                'efeitos': {
                    'energia': -4,
                },
                'itens_add': [],
            },
            {
                'texto': 'Ignorar e ficar no refeitório.',
                'resultado': 'A escolha cobra seu preço antes que exista tempo para voltar atrás.',
                'final': {
                    'tipo': 'derrota',
                    'titulo': 'MORTE 1',
                    'texto': 'Ignorar o ginásio; infectados presos em outra ala invadem o refeitório à noite.',
                },
                'efeitos': {
                    'vida': -100,
                },
                'qualidade': 'morte',
            },
        ],
    },
    'd4_r1_c2': {
        'dia': 4,
        'titulo': 'DIA 4 - UM NOVO GRUPO: A DIRETORA',
        'texto': (
            'No ginásio, há crianças, professores e funcionários. A diretora fechou a escola quando o '
            'caos começou e espera ajuda desde então.'
        ),
        'cor_fundo': VERDE,
        'opcoes': [
            {
                'texto': 'Alertar sobre os perigos.',
                'resultado': 'A decisão leva ao próximo momento: O Zelador.',
                'proxima': 'd4_r1_c3',
                'efeitos': {
                    'energia': -4,
                },
                'itens_add': ['aliado diretora'],
            },
            {
                'texto': 'Perguntar se há plano.',
                'resultado': 'A decisão leva ao próximo momento: O Zelador.',
                'proxima': 'd4_r1_c3',
                'efeitos': {
                    'energia': -4,
                },
                'itens_add': ['aliado diretora'],
            },
            {
                'texto': 'Oferecer ajuda.',
                'resultado': 'A decisão leva ao próximo momento: O Zelador.',
                'proxima': 'd4_r1_c3',
                'efeitos': {
                    'energia': -4,
                },
                'itens_add': ['aliado diretora'],
            },
        ],
    },
    'd4_r1_c3': {
        'dia': 4,
        'titulo': 'DIA 4 - UM NOVO GRUPO: O ZELADOR',
        'texto': (
            'O zelador ouviu no rádio que há uma zona segura em uma base militar. Ficar na escola é '
            'esperar comida acabar.'
        ),
        'cor_fundo': VERDE,
        'opcoes': [
            {
                'texto': 'Planejar saída da escola.',
                'resultado': 'A decisão leva ao próximo momento: Inventário da Escola.',
                'proxima': 'd4_r1_c4',
                'efeitos': {
                    'energia': -4,
                },
                'itens_add': ['rádio', 'aliado zelador'],
            },
            {
                'texto': 'Defender permanência no prédio.',
                'resultado': 'A decisão leva ao próximo momento: Inventário da Escola.',
                'proxima': 'd4_r1_c4',
                'efeitos': {
                    'energia': -4,
                    'moral': 5,
                    'confianca': 2,
                },
                'itens_add': ['rádio', 'aliado zelador'],
            },
        ],
    },
    'd4_r1_c4': {
        'dia': 4,
        'titulo': 'DIA 4 - UM NOVO GRUPO: INVENTÁRIO DA ESCOLA',
        'texto': (
            'Todos recolhem mochilas, alimentos do refeitório, remédios da enfermaria e objetos para '
            'defesa. Crianças perguntam se vão encontrar os pais na base.'
        ),
        'cor_fundo': VERDE,
        'proxima': 'd4_r1_c5',
    },
    'd4_r1_c5': {
        'dia': 4,
        'titulo': 'DIA 4 - UM NOVO GRUPO: MAPA DA CIDADE',
        'texto': (
            'A diretora abre um mapa antigo. Há três opções: buscar ônibus, ir a pé pelos bairros ou '
            'dividir grupos. Cada escolha muda quem sobreviverá ao Dia 5.'
        ),
        'cor_fundo': VERDE,
        'opcoes': [
            {
                'texto': 'Buscar ônibus.',
                'resultado': 'A decisão leva ao próximo momento: Treinamento Rápido.',
                'proxima': 'd4_r1_c6',
                'efeitos': {
                    'energia': -4,
                },
                'itens_add': ['ônibus', 'aliado diretora'],
            },
            {
                'texto': 'Ir a pé devagar.',
                'resultado': 'A decisão leva ao próximo momento: Treinamento Rápido.',
                'proxima': 'd4_r1_c6',
                'efeitos': {
                    'energia': -4,
                },
                'itens_add': ['ônibus', 'aliado diretora'],
            },
            {
                'texto': 'Dividir grupo.',
                'resultado': 'A decisão leva ao próximo momento: Treinamento Rápido.',
                'proxima': 'd4_r1_c6',
                'efeitos': {
                    'energia': -4,
                    'moral': 5,
                    'confianca': 2,
                },
                'itens_add': ['ônibus', 'aliado diretora'],
            },
        ],
    },
    'd4_r1_c6': {
        'dia': 4,
        'titulo': 'DIA 4 - UM NOVO GRUPO: TREINAMENTO RÁPIDO',
        'texto': (
            'O personagem ensina adultos a andar em silêncio, manter crianças no centro e nunca '
            'atirar sem necessidade. Alguns obedecem; outros acham exagero.'
        ),
        'cor_fundo': VERDE,
        'proxima': 'd4_r1_c7',
    },
    'd4_r1_c7': {
        'dia': 4,
        'titulo': 'DIA 4 - UM NOVO GRUPO: RUÍDO NO PÁTIO',
        'texto': (
            'À tarde, alguém vê homens armados passando pela rua. O personagem reconhece o estilo do '
            'comboio do posto de gasolina.'
        ),
        'cor_fundo': VERDE,
        'opcoes': [
            {
                'texto': 'Apagar sinais de presença.',
                'resultado': 'A decisão leva ao próximo momento: Última Refeição.',
                'proxima': 'd4_r1_c8',
                'efeitos': {
                    'energia': -4,
                },
                'itens_add': [],
            },
            {
                'texto': 'Preparar emboscada.',
                'resultado': 'A decisão leva ao próximo momento: Última Refeição.',
                'proxima': 'd4_r1_c8',
                'efeitos': {
                    'energia': -4,
                },
                'itens_add': [],
            },
        ],
    },
    'd4_r1_c8': {
        'dia': 4,
        'titulo': 'DIA 4 - UM NOVO GRUPO: ÚLTIMA REFEIÇÃO',
        'texto': (
            'O grupo divide comida antes da evacuação. Lena e Davi sentam afastados. A dor de José '
            'ainda ocupa cada silêncio.'
        ),
        'cor_fundo': VERDE,
        'proxima': 'd4_r1_c9',
    },
    'd4_r1_c9': {
        'dia': 4,
        'titulo': 'DIA 4 - UM NOVO GRUPO: NOITE NA ESCOLA',
        'texto': (
            'Todos dormem em salas próximas ao ginásio. O personagem fica inquieto: agora ele lidera '
            'gente em excesso, e gente em excesso faz barulho em excesso.'
        ),
        'cor_fundo': VERDE,
        'opcoes': [
            {
                'texto': 'Dormir em turnos.',
                'resultado': 'Essa decisão encerra o caminho iniciado neste dia.',
                'proxima': 'd4_r1_fim_1',
                'efeitos': {
                    'energia': -4,
                },
                'itens_add': [],
                'qualidade': 'media',
            },
            {
                'texto': 'Deixar todos descansarem sem vigia.',
                'resultado': 'A escolha cobra seu preço antes que exista tempo para voltar atrás.',
                'final': {
                    'tipo': 'derrota',
                    'titulo': 'MORTE 2',
                    'texto': 'Deixar todos sem vigia; saqueadores observam a escola e atacam antes do amanhecer.',
                },
                'efeitos': {
                    'vida': -100,
                },
                'qualidade': 'morte',
            },
            {
                'texto': 'FIM DO DIA 4 B',
                'resultado': 'Essa decisão encerra o caminho iniciado neste dia.',
                'proxima': 'd4_r1_fim_2',
                'efeitos': {
                    'energia': -4,
                },
                'qualidade': 'media',
            },
        ],
    },
    'd4_r2_fim_1': {
        'dia': 4,
        'titulo': 'FIM DO DIA 4 A',
        'texto': 'Rodovia alcançada, cidade deixada para trás, medicamentos encontrados.',
        'cor_fundo': VERDE_CLARO,
        'fim_dia': True,
        'proxima_dia': 'd5_r2_inicio',
    },
    'd4_r2_fim_2': {
        'dia': 4,
        'titulo': 'FIM DO DIA 4 B',
        'texto': 'Acampamento fora da cidade sem medicamentos, mas com menor exposição a infectados.',
        'cor_fundo': VERDE_CLARO,
        'fim_dia': True,
        'proxima_dia': 'd5_r2_inicio',
    },
    'd4_r2_c1': {
        'dia': 4,
        'titulo': 'DIA 4 - RODOVIA DE SAÍDA: CAMINHO PARA FORA',
        'texto': (
            'A manhã começa com meta clara: sair da cidade antes que recursos acabem. O rádio e '
            'placas indicam a rodovia principal.'
        ),
        'cor_fundo': VERDE,
        'opcoes': [
            {
                'texto': 'Seguir para a saída da cidade.',
                'resultado': 'A decisão leva ao próximo momento: Bairro Destruído.',
                'proxima': 'd4_r2_c2',
                'efeitos': {
                    'energia': -4,
                },
                'itens_add': ['rádio'],
            },
            {
                'texto': 'Voltar ao centro por mais suprimentos.',
                'resultado': 'A decisão leva ao próximo momento: Bairro Destruído.',
                'proxima': 'd4_r2_c2',
                'efeitos': {
                    'energia': -4,
                    'comida': 1,
                    'agua': 1,
                },
                'itens_add': ['rádio'],
            },
        ],
    },
    'd4_r2_c2': {
        'dia': 4,
        'titulo': 'DIA 4 - RODOVIA DE SAÍDA: BAIRRO DESTRUÍDO',
        'texto': (
            'Casas abertas, carros queimados e silêncio pesado dominam o bairro. Fumaça sobe de uma '
            'chaminé.'
        ),
        'cor_fundo': VERDE,
        'opcoes': [
            {
                'texto': 'Ignorar a casa.',
                'resultado': 'A decisão leva ao próximo momento: A Escola.',
                'proxima': 'd4_r2_c3',
                'efeitos': {
                    'energia': -4,
                    'moral': -4,
                    'confianca': -1,
                },
                'itens_add': [],
            },
            {
                'texto': 'Investigar a casa com fumaça.',
                'resultado': 'A decisão leva ao próximo momento: A Escola.',
                'proxima': 'd4_r2_c3',
                'efeitos': {
                    'energia': -4,
                },
                'itens_add': [],
            },
        ],
    },
    'd4_r2_c3': {
        'dia': 4,
        'titulo': 'DIA 4 - RODOVIA DE SAÍDA: A ESCOLA',
        'texto': (
            'Uma escola municipal aparece no caminho. O portão está aberto, mochilas infantis estão '
            'no pátio e o local parece abandonado, embora a rota do beco prove que escolas podem '
            'esconder grupos vivos.'
        ),
        'cor_fundo': VERDE,
        'opcoes': [
            {
                'texto': 'Procurar suprimentos rapidamente.',
                'resultado': 'A decisão leva ao próximo momento: O Ginásio.',
                'proxima': 'd4_r2_c4',
                'efeitos': {
                    'energia': -4,
                    'comida': 1,
                    'agua': 1,
                },
                'itens_add': ['mochila'],
            },
            {
                'texto': 'Ficar na escola por segurança.',
                'resultado': 'A decisão leva ao próximo momento: O Ginásio.',
                'proxima': 'd4_r2_c4',
                'efeitos': {
                    'energia': -4,
                },
                'itens_add': ['mochila'],
            },
        ],
    },
    'd4_r2_c4': {
        'dia': 4,
        'titulo': 'DIA 4 - RODOVIA DE SAÍDA: O GINÁSIO',
        'texto': 'Sons estranhos ecoam do ginásio. Algo arranha a porta por dentro.',
        'cor_fundo': VERDE,
        'opcoes': [
            {
                'texto': 'Não entrar.',
                'resultado': 'A decisão leva ao próximo momento: A Rodovia.',
                'proxima': 'd4_r2_c5',
                'efeitos': {
                    'energia': -4,
                },
                'itens_add': [],
            },
            {
                'texto': 'Investigar o ginásio.',
                'resultado': 'A escolha cobra seu preço antes que exista tempo para voltar atrás.',
                'final': {
                    'tipo': 'derrota',
                    'titulo': 'MORTE 1',
                    'texto': 'Investigar o ginásio; dezenas de infectados presos cercam o personagem.',
                },
                'efeitos': {
                    'vida': -100,
                },
                'qualidade': 'morte',
            },
        ],
    },
    'd4_r2_c5': {
        'dia': 4,
        'titulo': 'DIA 4 - RODOVIA DE SAÍDA: A RODOVIA',
        'texto': (
            'Centenas de veículos abandonados bloqueiam pistas. Motoristas tentaram fugir e ficaram '
            'presos. A rodovia parece um cemitério de metal.'
        ),
        'cor_fundo': VERDE,
        'opcoes': [
            {
                'texto': 'Avançar entre os veículos.',
                'resultado': 'A decisão leva ao próximo momento: O Acidente.',
                'proxima': 'd4_r2_c6',
                'efeitos': {
                    'energia': -8,
                },
                'itens_add': [],
            },
            {
                'texto': 'Voltar para ruas internas.',
                'resultado': 'A decisão leva ao próximo momento: O Acidente.',
                'proxima': 'd4_r2_c6',
                'efeitos': {
                    'energia': -4,
                },
                'itens_add': [],
            },
        ],
    },
    'd4_r2_c6': {
        'dia': 4,
        'titulo': 'DIA 4 - RODOVIA DE SAÍDA: O ACIDENTE',
        'texto': 'Um caminhão tombado bloqueia passagem. Próximo dele há uma ambulância destruída.',
        'cor_fundo': VERDE,
        'opcoes': [
            {
                'texto': 'Vasculhar a ambulância.',
                'resultado': 'A decisão leva ao próximo momento: Som de Helicóptero.',
                'proxima': 'd4_r2_c7',
                'efeitos': {
                    'energia': -4,
                    'comida': 1,
                    'agua': 1,
                },
                'itens_add': ['caminhão'],
            },
            {
                'texto': 'Evitar ambulância por medo de infectados.',
                'resultado': 'A decisão leva ao próximo momento: Som de Helicóptero.',
                'proxima': 'd4_r2_c7',
                'efeitos': {
                    'energia': -4,
                },
                'itens_add': ['caminhão'],
            },
        ],
    },
    'd4_r2_c7': {
        'dia': 4,
        'titulo': 'DIA 4 - RODOVIA DE SAÍDA: SOM DE HELICÓPTERO',
        'texto': (
            'Um helicóptero militar cruza o céu em direção ao interior. O rádio confirma que a zona '
            'segura ainda opera.'
        ),
        'cor_fundo': VERDE,
        'opcoes': [
            {
                'texto': 'Seguir coordenadas.',
                'resultado': 'A decisão leva ao próximo momento: A Ponte.',
                'proxima': 'd4_r2_c8',
                'efeitos': {
                    'energia': -4,
                },
                'itens_add': ['rádio', 'coordenadas'],
            },
            {
                'texto': 'Tentar sinalizar para o helicóptero.',
                'resultado': 'A escolha cobra seu preço antes que exista tempo para voltar atrás.',
                'final': {
                    'tipo': 'derrota',
                    'titulo': 'MORTE 2',
                    'texto': (
                        'Tentar sinalizar ao helicóptero no meio da rodovia; o barulho atrai horda e o grupo é '
                        'esmagado entre carros.'
                    ),
                },
                'efeitos': {
                    'vida': -100,
                },
                'qualidade': 'morte',
            },
        ],
    },
    'd4_r2_c8': {
        'dia': 4,
        'titulo': 'DIA 4 - RODOVIA DE SAÍDA: A PONTE',
        'texto': (
            'O grupo encontra ponte parcialmente destruída. A travessia é perigosa, mas economiza '
            'horas.'
        ),
        'cor_fundo': VERDE,
        'opcoes': [
            {
                'texto': 'Atravessar com cuidado.',
                'resultado': 'A decisão leva ao próximo momento: O Cerco e o Anoitecer.',
                'proxima': 'd4_r2_c9',
                'efeitos': {
                    'energia': -8,
                },
                'itens_add': [],
            },
            {
                'texto': 'Procurar rota longa.',
                'resultado': 'A decisão leva ao próximo momento: O Cerco e o Anoitecer.',
                'proxima': 'd4_r2_c9',
                'efeitos': {
                    'energia': -4,
                    'comida': 1,
                    'agua': 1,
                },
                'itens_add': [],
            },
        ],
    },
    'd4_r2_c9': {
        'dia': 4,
        'titulo': 'DIA 4 - RODOVIA DE SAÍDA: O CERCO E O ANOITECER',
        'texto': (
            'Infectados surgem dos dois lados da pista. O grupo corre para o acostamento e acampa '
            'próximo à rodovia quando campos abertos substituem prédios.'
        ),
        'cor_fundo': VERDE,
        'opcoes': [
            {
                'texto': 'FIM DO DIA 4 A',
                'resultado': 'Essa decisão encerra o caminho iniciado neste dia.',
                'proxima': 'd4_r2_fim_1',
                'efeitos': {
                    'energia': -4,
                },
                'qualidade': 'media',
            },
            {
                'texto': 'FIM DO DIA 4 B',
                'resultado': 'Essa decisão encerra o caminho iniciado neste dia.',
                'proxima': 'd4_r2_fim_2',
                'efeitos': {
                    'energia': -4,
                },
                'qualidade': 'media',
            },
        ],
    },
    'd4_r3_fim_1': {
        'dia': 4,
        'titulo': 'FIM DO DIA 4 A',
        'texto': 'Sobrevive com medicamentos e isqueiro após vencer o saqueador.',
        'cor_fundo': VERDE_CLARO,
        'fim_dia': True,
        'proxima_dia': 'd5_r3_inicio',
    },
    'd4_r3_fim_2': {
        'dia': 4,
        'titulo': 'FIM DO DIA 4 B',
        'texto': (
            'Sobrevive no apartamento inferior com enlatados, mas perde parte do esconderijo '
            'original.'
        ),
        'cor_fundo': VERDE_CLARO,
        'fim_dia': True,
        'proxima_dia': 'd5_r3_inicio',
    },
    'd4_r3_c1': {
        'dia': 4,
        'titulo': 'DIA 4 - O SAQUEADOR: CONFRONTO NA PORTA',
        'texto': (
            'A porta do apartamento começa a ceder. Um saqueador solitário grita que sabe que há '
            'comida ali dentro.'
        ),
        'cor_fundo': VERDE,
        'opcoes': [
            {
                'texto': 'Abrir e confrontar.',
                'resultado': 'A escolha cobra seu preço antes que exista tempo para voltar atrás.',
                'final': {
                    'tipo': 'derrota',
                    'titulo': 'MORTE 1',
                    'texto': 'Confrontar o saqueador sem arma; ele espanca o personagem até roubar tudo.',
                },
                'efeitos': {
                    'vida': -100,
                },
                'qualidade': 'morte',
            },
            {
                'texto': 'Segurar a porta.',
                'resultado': 'A decisão leva ao próximo momento: Barra de Ferro.',
                'proxima': 'd4_r3_c2',
                'efeitos': {
                    'energia': -4,
                },
                'itens_add': [],
            },
            {
                'texto': 'Fugir pela varanda se tiver corda.',
                'resultado': 'A escolha cobra seu preço antes que exista tempo para voltar atrás.',
                'final': {
                    'tipo': 'derrota',
                    'titulo': 'MORTE 2',
                    'texto': 'Tentar descer pela varanda sem corda; o personagem escorrega e cai.',
                },
                'efeitos': {
                    'vida': -100,
                },
                'qualidade': 'morte',
            },
        ],
    },
    'd4_r3_c2': {
        'dia': 4,
        'titulo': 'DIA 4 - O SAQUEADOR: BARRA DE FERRO',
        'texto': (
            'O saqueador está armado com uma barra de ferro. Ele não parece infectado; parece '
            'faminto, cansado e disposto a matar por enlatados.'
        ),
        'cor_fundo': VERDE,
        'opcoes': [
            {
                'texto': 'Usar faca ou pé de cabra.',
                'resultado': 'A decisão leva ao próximo momento: Porta Quebrada.',
                'proxima': 'd4_r3_c3',
                'efeitos': {
                    'energia': -4,
                },
                'itens_add': ['barra de ferro', 'faca de caça', 'pé de cabra'],
            },
            {
                'texto': 'Enfrentar sem arma.',
                'resultado': 'A decisão leva ao próximo momento: Porta Quebrada.',
                'proxima': 'd4_r3_c3',
                'efeitos': {
                    'energia': -4,
                },
                'itens_add': ['barra de ferro'],
            },
        ],
    },
    'd4_r3_c3': {
        'dia': 4,
        'titulo': 'DIA 4 - O SAQUEADOR: PORTA QUEBRADA',
        'texto': (
            'Se o personagem segura a porta, a madeira parte e ele é jogado para trás. O barulho '
            'atrai um infectado do corredor, que ataca o saqueador.'
        ),
        'cor_fundo': VERDE,
        'opcoes': [
            {
                'texto': 'Trancar a porta quebrada.',
                'resultado': 'A decisão leva ao próximo momento: Varanda.',
                'proxima': 'd4_r3_c4',
                'efeitos': {
                    'energia': -4,
                },
                'itens_add': [],
            },
            {
                'texto': 'Sair enquanto os dois lutam.',
                'resultado': 'A decisão leva ao próximo momento: Varanda.',
                'proxima': 'd4_r3_c4',
                'efeitos': {
                    'energia': -4,
                },
                'itens_add': [],
            },
        ],
    },
    'd4_r3_c4': {
        'dia': 4,
        'titulo': 'DIA 4 - O SAQUEADOR: VARANDA',
        'texto': (
            'A rota pela varanda leva ao apartamento de baixo. Sem corda, a queda é quase certa. Com '
            'corda, o personagem desce para o primeiro andar.'
        ),
        'cor_fundo': VERDE,
        'opcoes': [
            {
                'texto': 'Usar corda.',
                'resultado': 'A decisão leva ao próximo momento: Apartamento Inferior.',
                'proxima': 'd4_r3_c5',
                'efeitos': {
                    'energia': -4,
                },
                'itens_add': ['corda'],
            },
            {
                'texto': 'Tentar descer pendurado sem corda.',
                'resultado': 'A decisão leva ao próximo momento: Apartamento Inferior.',
                'proxima': 'd4_r3_c5',
                'efeitos': {
                    'energia': -4,
                },
                'itens_add': ['corda'],
            },
        ],
    },
    'd4_r3_c5': {
        'dia': 4,
        'titulo': 'DIA 4 - O SAQUEADOR: APARTAMENTO INFERIOR',
        'texto': (
            'No primeiro andar, há enlatados e um rádio velho. Pela janela, o personagem vê pessoas '
            'correndo em direção ao terminal.'
        ),
        'cor_fundo': VERDE,
        'proxima': 'd4_r3_c6',
    },
    'd4_r3_c6': {
        'dia': 4,
        'titulo': 'DIA 4 - O SAQUEADOR: MOCHILA DO SAQUEADOR',
        'texto': (
            'Caso vença o confronto, o saqueador foge deixando medicamentos e um isqueiro. O item '
            'parece pequeno, mas fogo e remédios serão importantes no Dia 5.'
        ),
        'cor_fundo': VERDE,
        'proxima': 'd4_r3_c7',
    },
    'd4_r3_c7': {
        'dia': 4,
        'titulo': 'DIA 4 - O SAQUEADOR: PORTA DANIFICADA',
        'texto': (
            'Mesmo sobrevivendo, o esconderijo original está comprometido. O personagem precisa '
            'reforçar a entrada ou mudar de apartamento.'
        ),
        'cor_fundo': VERDE,
        'opcoes': [
            {
                'texto': 'Reforçar a porta.',
                'resultado': 'A decisão leva ao próximo momento: Pesadelos.',
                'proxima': 'd4_r3_c8',
                'efeitos': {
                    'energia': -8,
                },
                'itens_add': [],
            },
            {
                'texto': 'Mudar para outro apartamento.',
                'resultado': 'A decisão leva ao próximo momento: Pesadelos.',
                'proxima': 'd4_r3_c8',
                'efeitos': {
                    'energia': -4,
                },
                'itens_add': [],
            },
        ],
    },
    'd4_r3_c8': {
        'dia': 4,
        'titulo': 'DIA 4 - O SAQUEADOR: PESADELOS',
        'texto': (
            'À noite, ele ouve o saqueador gritando em algum andar. Não sabe se foi mordido ou morto '
            'por outro humano. A cidade está transformando vivos em predadores.'
        ),
        'cor_fundo': VERDE,
        'proxima': 'd4_r3_c9',
    },
    'd4_r3_c9': {
        'dia': 4,
        'titulo': 'DIA 4 - O SAQUEADOR: SONO LEVE',
        'texto': (
            'Com porta danificada ou novo esconderijo, o personagem dorme pouco. A fumaça no '
            'horizonte anuncia o incêndio que chegará no Dia 5.'
        ),
        'cor_fundo': VERDE,
        'opcoes': [
            {
                'texto': 'Dormir perto da saída.',
                'resultado': 'Essa decisão encerra o caminho iniciado neste dia.',
                'proxima': 'd4_r3_fim_1',
                'efeitos': {
                    'energia': -4,
                },
                'itens_add': [],
                'qualidade': 'media',
            },
            {
                'texto': 'Dormir no quarto mais protegido.',
                'resultado': 'Essa decisão encerra o caminho iniciado neste dia.',
                'proxima': 'd4_r3_fim_2',
                'efeitos': {
                    'energia': -4,
                },
                'itens_add': [],
                'qualidade': 'media',
            },
        ],
    },
    'd4_r4_fim_1': {
        'dia': 4,
        'titulo': 'FIM DO DIA 4 A',
        'texto': 'Ônibus pronto, lista definida e grupo ainda unido.',
        'cor_fundo': VERDE_CLARO,
        'fim_dia': True,
        'proxima_dia': 'd5_r4_inicio',
    },
    'd4_r4_fim_2': {
        'dia': 4,
        'titulo': 'FIM DO DIA 4 B',
        'texto': 'Ônibus pronto, mas grupo dividido e Jonas com apoio perigoso.',
        'cor_fundo': VERDE_CLARO,
        'fim_dia': True,
        'proxima_dia': 'd5_r4_inicio',
    },
    'd4_r4_c1': {
        'dia': 4,
        'titulo': 'DIA 4 - QUEM MERECE UM LUGAR NO ÔNIBUS: LUGARES LIMITADOS',
        'texto': (
            'O ônibus não comporta todos com segurança. Crianças, idosos, feridos e recém-chegados '
            'esperam uma decisão.'
        ),
        'cor_fundo': VERDE,
        'opcoes': [
            {
                'texto': 'Apoiar Helena.',
                'resultado': 'A decisão leva ao próximo momento: Proposta de Jonas.',
                'proxima': 'd4_r4_c2',
                'efeitos': {
                    'energia': -4,
                    'moral': 5,
                    'confianca': 2,
                },
                'itens_add': ['ônibus', 'aliado Lena', 'aliado Helena'],
            },
            {
                'texto': 'Permitir votação caótica.',
                'resultado': 'A decisão leva ao próximo momento: Proposta de Jonas.',
                'proxima': 'd4_r4_c2',
                'efeitos': {
                    'energia': -4,
                },
                'itens_add': ['ônibus'],
            },
        ],
    },
    'd4_r4_c2': {
        'dia': 4,
        'titulo': 'DIA 4 - QUEM MERECE UM LUGAR NO ÔNIBUS: PROPOSTA DE JONAS',
        'texto': (
            'Jonas propõe abandonar feridos para aumentar chances dos fortes. Alguns sobreviventes, '
            'apavorados, concordam.'
        ),
        'cor_fundo': VERDE,
        'opcoes': [
            {
                'texto': 'Defender os feridos.',
                'resultado': 'A decisão leva ao próximo momento: Prioridade das Crianças.',
                'proxima': 'd4_r4_c3',
                'efeitos': {
                    'energia': -4,
                    'moral': 5,
                    'confianca': 2,
                },
                'itens_add': ['corda', 'aliado Jonas'],
            },
            {
                'texto': 'Aceitar proposta de Jonas.',
                'resultado': 'A decisão leva ao próximo momento: Prioridade das Crianças.',
                'proxima': 'd4_r4_c3',
                'efeitos': {
                    'energia': -4,
                },
                'itens_add': ['corda', 'aliado Jonas'],
            },
        ],
    },
    'd4_r4_c3': {
        'dia': 4,
        'titulo': 'DIA 4 - QUEM MERECE UM LUGAR NO ÔNIBUS: PRIORIDADE DAS CRIANÇAS',
        'texto': (
            'Helena quer levar crianças e idosos primeiro. A mulher e a criança salvas no Dia 1 '
            'observam o personagem, temendo serem deixadas.'
        ),
        'cor_fundo': VERDE,
        'opcoes': [
            {
                'texto': 'Proteger crianças e idosos.',
                'resultado': 'A decisão leva ao próximo momento: Mordida Escondida.',
                'proxima': 'd4_r4_c4',
                'efeitos': {
                    'energia': -4,
                    'moral': 5,
                    'confianca': 2,
                },
                'itens_add': ['aliado Lena', 'aliado Helena'],
            },
            {
                'texto': 'Priorizar quem sabe lutar.',
                'resultado': 'A decisão leva ao próximo momento: Mordida Escondida.',
                'proxima': 'd4_r4_c4',
                'efeitos': {
                    'energia': -8,
                },
                'itens_add': ['aliado Lena', 'aliado Helena'],
            },
        ],
    },
    'd4_r4_c4': {
        'dia': 4,
        'titulo': 'DIA 4 - QUEM MERECE UM LUGAR NO ÔNIBUS: MORDIDA ESCONDIDA',
        'texto': (
            'Um sobrevivente tenta esconder mordida no braço. A febre já começou, mas ele implora '
            'para não ser expulso.'
        ),
        'cor_fundo': VERDE,
        'opcoes': [
            {
                'texto': 'Revelar a mordida e isolar.',
                'resultado': 'A decisão leva ao próximo momento: Lista de Embarque.',
                'proxima': 'd4_r4_c5',
                'efeitos': {
                    'energia': -4,
                    'moral': 5,
                    'confianca': 2,
                },
                'itens_add': [],
            },
            {
                'texto': 'Esconder para evitar pânico.',
                'resultado': 'A decisão leva ao próximo momento: Lista de Embarque.',
                'proxima': 'd4_r4_c5',
                'efeitos': {
                    'energia': -4,
                    'moral': -4,
                    'confianca': -1,
                },
                'itens_add': [],
            },
        ],
    },
    'd4_r4_c5': {
        'dia': 4,
        'titulo': 'DIA 4 - QUEM MERECE UM LUGAR NO ÔNIBUS: LISTA DE EMBARQUE',
        'texto': (
            'A lista divide o grupo. Quem fica fora acusa Helena de favoritismo. Jonas usa a raiva '
            'como arma política.'
        ),
        'cor_fundo': VERDE,
        'opcoes': [
            {
                'texto': 'Usar diálogo.',
                'resultado': 'A decisão leva ao próximo momento: Ameaça Aberta.',
                'proxima': 'd4_r4_c6',
                'efeitos': {
                    'energia': -4,
                },
                'itens_add': ['aliado Lena', 'aliado Helena', 'aliado Jonas'],
            },
            {
                'texto': 'Responder com ameaça.',
                'resultado': 'A decisão leva ao próximo momento: Ameaça Aberta.',
                'proxima': 'd4_r4_c6',
                'efeitos': {
                    'energia': -4,
                },
                'itens_add': ['aliado Lena', 'aliado Helena', 'aliado Jonas'],
            },
        ],
    },
    'd4_r4_c6': {
        'dia': 4,
        'titulo': 'DIA 4 - QUEM MERECE UM LUGAR NO ÔNIBUS: AMEAÇA ABERTA',
        'texto': (
            'Jonas ameaça tomar o ônibus. Alguns o seguem, mas outros recuam ao ver que Helena e o '
            'personagem não querem violência.'
        ),
        'cor_fundo': VERDE,
        'proxima': 'd4_r4_c7',
    },
    'd4_r4_c7': {
        'dia': 4,
        'titulo': 'DIA 4 - QUEM MERECE UM LUGAR NO ÔNIBUS: INFECTADOS NAS GRADES',
        'texto': (
            'O barulho da discussão atrai infectados. Eles batem nas grades reforçadas e forçam o '
            'grupo a agir junto.'
        ),
        'cor_fundo': VERDE,
        'opcoes': [
            {
                'texto': 'Reforçar terminal.',
                'resultado': 'A escolha cobra seu preço antes que exista tempo para voltar atrás.',
                'final': {
                    'tipo': 'derrota',
                    'titulo': 'MORTE 1',
                    'texto': (
                        'Esconder a mordida; o infectado se transforma dentro do terminal durante a noite e mata '
                        'o personagem.'
                    ),
                },
                'efeitos': {
                    'vida': -100,
                },
                'qualidade': 'morte',
            },
            {
                'texto': 'Deixar Jonas cuidar do portão.',
                'resultado': 'A decisão leva ao próximo momento: Motor Ligado.',
                'proxima': 'd4_r4_c8',
                'efeitos': {
                    'energia': -4,
                },
                'itens_add': ['aliado Jonas'],
            },
        ],
    },
    'd4_r4_c8': {
        'dia': 4,
        'titulo': 'DIA 4 - QUEM MERECE UM LUGAR NO ÔNIBUS: MOTOR LIGADO',
        'texto': 'Helena liga o ônibus. O som atrai horda distante, mas prova que a fuga é possível.',
        'cor_fundo': VERDE,
        'opcoes': [
            {
                'texto': 'Esperar a noite.',
                'resultado': 'A decisão leva ao próximo momento: Horda Distante.',
                'proxima': 'd4_r4_c9',
                'efeitos': {
                    'energia': -4,
                },
                'itens_add': ['ônibus', 'aliado Lena', 'aliado Helena'],
            },
            {
                'texto': 'Sair imediatamente.',
                'resultado': 'A escolha cobra seu preço antes que exista tempo para voltar atrás.',
                'final': {
                    'tipo': 'derrota',
                    'titulo': 'MORTE 2',
                    'texto': (
                        'Sair imediatamente com o motor alto; a horda intercepta o ônibus antes de todos '
                        'embarcarem.'
                    ),
                },
                'efeitos': {
                    'vida': -100,
                },
                'qualidade': 'morte',
            },
        ],
    },
    'd4_r4_c9': {
        'dia': 4,
        'titulo': 'DIA 4 - QUEM MERECE UM LUGAR NO ÔNIBUS: HORDA DISTANTE',
        'texto': (
            'Ao anoitecer, sombras se acumulam na avenida. O terminal não será seguro por muito mais '
            'tempo.'
        ),
        'cor_fundo': VERDE,
        'opcoes': [
            {
                'texto': 'FIM DO DIA 4 A',
                'resultado': 'Essa decisão encerra o caminho iniciado neste dia.',
                'proxima': 'd4_r4_fim_1',
                'efeitos': {
                    'energia': -4,
                },
                'qualidade': 'media',
            },
            {
                'texto': 'FIM DO DIA 4 B',
                'resultado': 'Essa decisão encerra o caminho iniciado neste dia.',
                'proxima': 'd4_r4_fim_2',
                'efeitos': {
                    'energia': -4,
                },
                'qualidade': 'media',
            },
        ],
    },
    'd5_r1_fim_1': {
        'dia': 5,
        'titulo': 'FIM DO DIA 5',
        'texto': 'Escondidos na casa arrombada, com grupo reduzido, feridos e poucos recursos.',
        'cor_fundo': VERDE_CLARO,
        'fim_dia': True,
        'proxima_dia': 'd6_r1_c1',
    },
    'd5_r1_c1': {
        'dia': 5,
        'titulo': 'DIA 5 - DE NOVO NÃO / FUJAM: DESESPERO',
        'texto': (
            'Todos estão prontos para sair da escola quando um estrondo vem do portão. Um caminhão o '
            'derruba e outros carros entram atrás. São os homens armados do posto de gasolina.'
        ),
        'cor_fundo': VERDE,
        'opcoes': [
            {
                'texto': 'Alertar todos para fugir.',
                'resultado': 'A decisão leva ao próximo momento: Fujam.',
                'proxima': 'd5_r1_c2',
                'efeitos': {
                    'energia': -4,
                },
                'itens_add': ['caminhão'],
            },
            {
                'texto': 'Ficar e lutar.',
                'resultado': 'A decisão leva ao próximo momento: Fujam.',
                'proxima': 'd5_r1_c2',
                'efeitos': {
                    'energia': -8,
                },
                'itens_add': ['caminhão'],
            },
            {
                'texto': 'Dividir o grupo.',
                'resultado': 'A decisão leva ao próximo momento: Fujam.',
                'proxima': 'd5_r1_c2',
                'efeitos': {
                    'energia': -4,
                    'moral': 5,
                    'confianca': 2,
                },
                'itens_add': ['caminhão'],
            },
        ],
    },
    'd5_r1_c2': {
        'dia': 5,
        'titulo': 'DIA 5 - DE NOVO NÃO / FUJAM: FUJAM',
        'texto': (
            'Homens assoviam ao encontrar o ginásio. A diretora tenta manter crianças juntas. O '
            'zelador mostra a chave do fundo da escola.'
        ),
        'cor_fundo': VERDE,
        'opcoes': [
            {
                'texto': 'Lutar para dar tempo ao grupo.',
                'resultado': 'A decisão leva ao próximo momento: Confronto.',
                'proxima': 'd5_r1_c3',
                'efeitos': {
                    'energia': -8,
                },
                'itens_add': ['aliado diretora', 'aliado zelador'],
            },
            {
                'texto': 'Correr primeiro com Lena e Davi.',
                'resultado': 'A decisão leva ao próximo momento: Confronto.',
                'proxima': 'd5_r1_c3',
                'efeitos': {
                    'energia': -8,
                },
                'itens_add': ['aliado Lena', 'aliado Davi', 'aliado diretora', 'aliado zelador'],
            },
        ],
    },
    'd5_r1_c3': {
        'dia': 5,
        'titulo': 'DIA 5 - DE NOVO NÃO / FUJAM: CONFRONTO',
        'texto': (
            'Os saqueadores disparam sem piedade. O personagem usa a pistola da casa e elimina dois '
            'homens antes da munição acabar.'
        ),
        'cor_fundo': VERDE,
        'opcoes': [
            {
                'texto': 'Pedir cobertura para pegar outra arma.',
                'resultado': 'A decisão leva ao próximo momento: Aliado Caído.',
                'proxima': 'd5_r1_c4',
                'efeitos': {
                    'energia': -4,
                },
                'itens_add': ['pistola', 'munição'],
            },
            {
                'texto': 'Avançar sem munição.',
                'resultado': 'A escolha cobra seu preço antes que exista tempo para voltar atrás.',
                'final': {
                    'tipo': 'derrota',
                    'titulo': 'MORTE 1',
                    'texto': 'Avançar sem munição no confronto; o personagem é executado pelos saqueadores.',
                },
                'efeitos': {
                    'vida': -100,
                },
                'qualidade': 'morte',
            },
        ],
    },
    'd5_r1_c4': {
        'dia': 5,
        'titulo': 'DIA 5 - DE NOVO NÃO / FUJAM: ALIADO CAÍDO',
        'texto': (
            'Um funcionário da escola pula em um saqueador e salva o personagem, mas é baleado. O '
            'sangue dele se espalha no piso do ginásio.'
        ),
        'cor_fundo': VERDE,
        'proxima': 'd5_r1_c5',
    },
    'd5_r1_c5': {
        'dia': 5,
        'titulo': 'DIA 5 - DE NOVO NÃO / FUJAM: CONFRONTO CONTINUA',
        'texto': (
            'Os saqueadores gritam que a cidade agora é deles. Prometem poupar quem se render e '
            'entregar crianças, comida e mulheres.'
        ),
        'cor_fundo': VERDE,
        'opcoes': [
            {
                'texto': 'Continuar atirando.',
                'resultado': 'A decisão leva ao próximo momento: Chacina.',
                'proxima': 'd5_r1_c6',
                'efeitos': {
                    'energia': -4,
                },
                'itens_add': [],
            },
            {
                'texto': 'Render-se.',
                'resultado': 'A escolha cobra seu preço antes que exista tempo para voltar atrás.',
                'final': {
                    'tipo': 'derrota',
                    'titulo': 'MORTE 2',
                    'texto': (
                        'Render-se; os saqueadores matam os adultos e levam recursos, deixando o personagem para '
                        'a horda.'
                    ),
                },
                'efeitos': {
                    'vida': -100,
                },
                'qualidade': 'morte',
            },
        ],
    },
    'd5_r1_c6': {
        'dia': 5,
        'titulo': 'DIA 5 - DE NOVO NÃO / FUJAM: CHACINA',
        'texto': (
            'Fica claro que não há vitória possível. Os saqueadores são muitos e estão armados. '
            'Adultos caem tentando proteger crianças.'
        ),
        'cor_fundo': VERDE,
        'opcoes': [
            {
                'texto': 'Recuar com sobreviventes.',
                'resultado': 'A decisão leva ao próximo momento: Pânico na Rua.',
                'proxima': 'd5_r1_c7',
                'efeitos': {
                    'energia': -4,
                },
                'itens_add': [],
            },
            {
                'texto': 'Insistir na luta.',
                'resultado': 'A escolha cobra seu preço antes que exista tempo para voltar atrás.',
                'final': {
                    'tipo': 'derrota',
                    'titulo': 'MORTE 3',
                    'texto': (
                        'Insistir na luta quando todos recuam; o ginásio é cercado e o personagem morre '
                        'protegendo a saída.'
                    ),
                },
                'efeitos': {
                    'vida': -100,
                },
                'qualidade': 'morte',
            },
        ],
    },
    'd5_r1_c7': {
        'dia': 5,
        'titulo': 'DIA 5 - DE NOVO NÃO / FUJAM: PÂNICO NA RUA',
        'texto': (
            'Do lado de fora, uma horda aparece na esquina atraída pelos tiros. Muitos membros da '
            'escola se espalham.'
        ),
        'cor_fundo': VERDE,
        'opcoes': [
            {
                'texto': 'Gritar para seguirem o zelador.',
                'resultado': 'A decisão leva ao próximo momento: Pedro e Joice.',
                'proxima': 'd5_r1_c8',
                'efeitos': {
                    'energia': -4,
                },
                'itens_add': ['aliado zelador'],
            },
            {
                'texto': 'Mandar cada um correr por si.',
                'resultado': 'A decisão leva ao próximo momento: Pedro e Joice.',
                'proxima': 'd5_r1_c8',
                'efeitos': {
                    'energia': -8,
                },
                'itens_add': [],
            },
        ],
    },
    'd5_r1_c8': {
        'dia': 5,
        'titulo': 'DIA 5 - DE NOVO NÃO / FUJAM: PEDRO E JOICE',
        'texto': (
            'Na confusão, Pedro e Joice somem pelos becos. O personagem não sabe se morreram. Essa '
            'ausência permite que reapareçam no Dia 7.'
        ),
        'cor_fundo': VERDE,
        'proxima': 'd5_r1_c9',
    },
    'd5_r1_c9': {
        'dia': 5,
        'titulo': 'DIA 5 - DE NOVO NÃO / FUJAM: CASA ARROMBADA',
        'texto': (
            'O zelador abre uma casa próxima. Menos da metade do grupo entra. Feridos gemem, crianças '
            'tremem e Lena abraça Davi no chão.'
        ),
        'cor_fundo': VERDE,
        'opcoes': [
            {
                'texto': 'Aguardar a horda passar.',
                'resultado': 'A decisão leva ao próximo momento: Contagem dos Vivos.',
                'proxima': 'd5_r1_c10',
                'efeitos': {
                    'energia': -4,
                    'comida': 1,
                    'agua': 1,
                },
                'itens_add': ['aliado Lena', 'aliado Davi', 'aliado zelador'],
            },
            {
                'texto': 'Continuar fugindo mesmo exaustos.',
                'resultado': 'A decisão leva ao próximo momento: Contagem dos Vivos.',
                'proxima': 'd5_r1_c10',
                'efeitos': {
                    'energia': -4,
                },
                'itens_add': ['aliado Lena', 'aliado Davi', 'aliado zelador'],
            },
        ],
    },
    'd5_r1_c10': {
        'dia': 5,
        'titulo': 'DIA 5 - DE NOVO NÃO / FUJAM: CONTAGEM DOS VIVOS',
        'texto': (
            'A diretora lista quem sobreviveu. Cada nome ausente corta mais fundo. O personagem '
            'percebe que liderança não impede perdas; só organiza a culpa.'
        ),
        'cor_fundo': VERDE,
        'proxima': 'd5_r1_c11',
    },
    'd5_r1_c11': {
        'dia': 5,
        'titulo': 'DIA 5 - DE NOVO NÃO / FUJAM: FERIDOS',
        'texto': (
            'Há poucos curativos. Alguém pede para usar tudo em uma criança. Outro adulto está '
            'sangrando muito.'
        ),
        'cor_fundo': VERDE,
        'opcoes': [
            {
                'texto': 'Priorizar quem pode ser salvo.',
                'resultado': 'A decisão leva ao próximo momento: Saqueadores na Rua.',
                'proxima': 'd5_r1_c12',
                'efeitos': {
                    'energia': -4,
                },
                'itens_add': [],
            },
            {
                'texto': 'Dividir igualmente mesmo sem eficácia.',
                'resultado': 'A decisão leva ao próximo momento: Saqueadores na Rua.',
                'proxima': 'd5_r1_c12',
                'efeitos': {
                    'energia': -4,
                    'moral': 5,
                    'confianca': 2,
                },
                'itens_add': [],
            },
        ],
    },
    'd5_r1_c12': {
        'dia': 5,
        'titulo': 'DIA 5 - DE NOVO NÃO / FUJAM: SAQUEADORES NA RUA',
        'texto': (
            'Pela janela, homens armados passam procurando sobreviventes. Eles riem enquanto arrastam '
            'mochilas da escola.'
        ),
        'cor_fundo': VERDE,
        'opcoes': [
            {
                'texto': 'Apagar qualquer sinal dentro da casa.',
                'resultado': 'A decisão leva ao próximo momento: Horda Passando.',
                'proxima': 'd5_r1_c13',
                'efeitos': {
                    'energia': -4,
                },
                'itens_add': ['mochila'],
            },
            {
                'texto': 'Atacar pela janela.',
                'resultado': 'A escolha cobra seu preço antes que exista tempo para voltar atrás.',
                'final': {
                    'tipo': 'derrota',
                    'titulo': 'MORTE 4',
                    'texto': 'Atacar os saqueadores pela janela; tiros revelam a casa e todos são invadidos.',
                },
                'efeitos': {
                    'vida': -100,
                },
                'qualidade': 'morte',
            },
        ],
    },
    'd5_r1_c13': {
        'dia': 5,
        'titulo': 'DIA 5 - DE NOVO NÃO / FUJAM: HORDA PASSANDO',
        'texto': (
            'Infectados seguem atrás do barulho dos carros. Um deles para diante da porta, farejando. '
            'Davi prende o choro.'
        ),
        'cor_fundo': VERDE,
        'proxima': 'd5_r1_c14',
    },
    'd5_r1_c14': {
        'dia': 5,
        'titulo': 'DIA 5 - DE NOVO NÃO / FUJAM: SILÊNCIO PÓS-MASSACRE',
        'texto': (
            'Quando o barulho diminui, resta apenas o peso do que aconteceu. O personagem sabe que a '
            'base militar precisa ser alcançada no Dia 6.'
        ),
        'cor_fundo': VERDE,
        'opcoes': [
            {
                'texto': 'Dormir em turnos.',
                'resultado': 'A decisão leva ao próximo momento: Escondidos.',
                'proxima': 'd5_r1_c15',
                'efeitos': {
                    'energia': -4,
                },
                'itens_add': [],
            },
            {
                'texto': 'Ficar acordado sozinho a noite toda.',
                'resultado': 'A decisão leva ao próximo momento: Escondidos.',
                'proxima': 'd5_r1_c15',
                'efeitos': {
                    'energia': -4,
                    'moral': -4,
                    'confianca': -1,
                },
                'itens_add': ['corda'],
            },
        ],
    },
    'd5_r1_c15': {
        'dia': 5,
        'titulo': 'DIA 5 - DE NOVO NÃO / FUJAM: ESCONDIDOS',
        'texto': (
            'O grupo se acomoda no escuro. Não há vitória; há apenas sobrevivência temporária. Amanhã '
            'a ponte para a base será a última chance.'
        ),
        'cor_fundo': VERDE,
        'proxima': 'd5_r1_fim_1',
    },
    'd5_r2_fim_1': {
        'dia': 5,
        'titulo': 'FIM DO DIA 5',
        'texto': 'Fazenda isolada com comida, água, caminhão quase funcional e perigo crescente.',
        'cor_fundo': VERDE_CLARO,
        'fim_dia': True,
        'proxima_dia': 'd6_r2_c1',
    },
    'd5_r2_c1': {
        'dia': 5,
        'titulo': 'DIA 5 - FAZENDA ISOLADA: CAMPOS ABANDONADOS',
        'texto': (
            'O grupo acorda próximo à rodovia. A cidade ficou para trás, mas o silêncio dos campos '
            'abertos parece artificial. O rádio ainda transmite Aurora, com sinal fraco.'
        ),
        'cor_fundo': VERDE,
        'opcoes': [
            {
                'texto': 'Continuar pela estrada rural.',
                'resultado': 'A decisão leva ao próximo momento: A Fazenda.',
                'proxima': 'd5_r2_c2',
                'efeitos': {
                    'energia': -4,
                },
                'itens_add': ['corda', 'rádio'],
            },
            {
                'texto': 'Voltar à rodovia principal.',
                'resultado': 'A decisão leva ao próximo momento: A Fazenda.',
                'proxima': 'd5_r2_c2',
                'efeitos': {
                    'energia': -4,
                },
                'itens_add': ['corda', 'rádio'],
            },
        ],
    },
    'd5_r2_c2': {
        'dia': 5,
        'titulo': 'DIA 5 - FAZENDA ISOLADA: A FAZENDA',
        'texto': (
            'Uma fazenda aparece ao longe, com celeiro vermelho, casa principal e fumaça na chaminé. '
            'Pode haver recursos, moradores ou armadilha.'
        ),
        'cor_fundo': VERDE,
        'opcoes': [
            {
                'texto': 'Investigar a fazenda.',
                'resultado': 'A escolha cobra seu preço antes que exista tempo para voltar atrás.',
                'final': {
                    'tipo': 'derrota',
                    'titulo': 'MORTE 4',
                    'texto': 'Deixar o fazendeiro; no Dia 6 ninguém conclui o reparo e a fazenda cai antes da partida.',
                },
                'efeitos': {
                    'vida': -100,
                },
                'qualidade': 'morte',
            },
            {
                'texto': 'Evitar a fazenda.',
                'resultado': 'A decisão leva ao próximo momento: O Fazendeiro.',
                'proxima': 'd5_r2_c3',
                'efeitos': {
                    'energia': -4,
                },
                'itens_add': [],
            },
        ],
    },
    'd5_r2_c3': {
        'dia': 5,
        'titulo': 'DIA 5 - FAZENDA ISOLADA: O FAZENDEIRO',
        'texto': (
            'Um homem idoso aponta uma espingarda. Ele baixa a arma quando percebe que não são '
            'infectados. Diz estar sozinho desde o surto.'
        ),
        'cor_fundo': VERDE,
        'opcoes': [
            {
                'texto': 'Conversar com o fazendeiro.',
                'resultado': 'A decisão leva ao próximo momento: Estoque de Comida.',
                'proxima': 'd5_r2_c4',
                'efeitos': {
                    'energia': -4,
                },
                'itens_add': ['aliado fazendeiro'],
            },
            {
                'texto': 'Tomar a casa à força.',
                'resultado': 'A escolha cobra seu preço antes que exista tempo para voltar atrás.',
                'final': {
                    'tipo': 'derrota',
                    'titulo': 'MORTE 1',
                    'texto': 'Tomar a casa à força; o fazendeiro atira e o barulho atrai infectados.',
                },
                'efeitos': {
                    'vida': -100,
                },
                'qualidade': 'morte',
            },
        ],
    },
    'd5_r2_c4': {
        'dia': 5,
        'titulo': 'DIA 5 - FAZENDA ISOLADA: ESTOQUE DE COMIDA',
        'texto': (
            'O porão guarda alimentos enlatados, arroz e galões de água. É o maior estoque que o '
            'grupo viu desde o início.'
        ),
        'cor_fundo': VERDE,
        'opcoes': [
            {
                'texto': 'Reabastecer mochilas.',
                'resultado': 'A decisão leva ao próximo momento: O Celeiro.',
                'proxima': 'd5_r2_c5',
                'efeitos': {
                    'energia': -4,
                    'comida': 1,
                    'agua': 1,
                },
                'itens_add': ['mochila'],
            },
            {
                'texto': 'Pegar tudo sem deixar nada.',
                'resultado': 'A decisão leva ao próximo momento: O Celeiro.',
                'proxima': 'd5_r2_c5',
                'efeitos': {
                    'energia': -4,
                },
                'itens_add': [],
            },
        ],
    },
    'd5_r2_c5': {
        'dia': 5,
        'titulo': 'DIA 5 - FAZENDA ISOLADA: O CELEIRO',
        'texto': (
            'Sons estranhos vêm do celeiro. A porta está presa por correntes improvisadas. O '
            'fazendeiro fica nervoso.'
        ),
        'cor_fundo': VERDE,
        'opcoes': [
            {
                'texto': 'Verificar o celeiro.',
                'resultado': 'A decisão leva ao próximo momento: A Descoberta.',
                'proxima': 'd5_r2_c6',
                'efeitos': {
                    'energia': -4,
                },
                'itens_add': ['aliado fazendeiro'],
            },
            {
                'texto': 'Ignorar o celeiro.',
                'resultado': 'A escolha cobra seu preço antes que exista tempo para voltar atrás.',
                'final': {
                    'tipo': 'derrota',
                    'titulo': 'MORTE 2',
                    'texto': 'Ignorar o celeiro; os infectados escapam à noite e atacam durante o sono.',
                },
                'efeitos': {
                    'vida': -100,
                },
                'qualidade': 'morte',
            },
        ],
    },
    'd5_r2_c6': {
        'dia': 5,
        'titulo': 'DIA 5 - FAZENDA ISOLADA: A DESCOBERTA',
        'texto': (
            'Três infectados estão presos no interior; eram trabalhadores da fazenda. As correntes '
            'estão cedendo.'
        ),
        'cor_fundo': VERDE,
        'opcoes': [
            {
                'texto': 'Reforçar o bloqueio.',
                'resultado': 'A decisão leva ao próximo momento: Barulhos na Estrada.',
                'proxima': 'd5_r2_c7',
                'efeitos': {
                    'energia': -8,
                },
                'itens_add': [],
            },
            {
                'texto': 'Eliminar todos lá dentro.',
                'resultado': 'A decisão leva ao próximo momento: Barulhos na Estrada.',
                'proxima': 'd5_r2_c7',
                'efeitos': {
                    'energia': -4,
                },
                'itens_add': [],
            },
        ],
    },
    'd5_r2_c7': {
        'dia': 5,
        'titulo': 'DIA 5 - FAZENDA ISOLADA: BARULHOS NA ESTRADA',
        'texto': (
            'Motores são ouvidos ao longe. Veículos ainda funcionam em algum lugar. O grupo sobe em '
            'um silo para observar.'
        ),
        'cor_fundo': VERDE,
        'opcoes': [
            {
                'texto': 'Investigar a origem do som.',
                'resultado': 'A decisão leva ao próximo momento: O Caminhão.',
                'proxima': 'd5_r2_c8',
                'efeitos': {
                    'energia': -4,
                },
                'itens_add': [],
            },
            {
                'texto': 'Esconder-se dentro da casa.',
                'resultado': 'A decisão leva ao próximo momento: O Caminhão.',
                'proxima': 'd5_r2_c8',
                'efeitos': {
                    'energia': -4,
                    'moral': -4,
                    'confianca': -1,
                },
                'itens_add': [],
            },
        ],
    },
    'd5_r2_c8': {
        'dia': 5,
        'titulo': 'DIA 5 - FAZENDA ISOLADA: O CAMINHÃO',
        'texto': (
            'Em um galpão secundário há um caminhão de carga antigo. O motor parece inteiro, mas não '
            'liga.'
        ),
        'cor_fundo': VERDE,
        'opcoes': [
            {
                'texto': 'Tentar ligar o caminhão.',
                'resultado': 'A decisão leva ao próximo momento: O Problema.',
                'proxima': 'd5_r2_c9',
                'efeitos': {
                    'energia': -4,
                },
                'itens_add': ['caminhão'],
            },
            {
                'texto': 'Desistir do veículo.',
                'resultado': 'A decisão leva ao próximo momento: O Problema.',
                'proxima': 'd5_r2_c9',
                'efeitos': {
                    'energia': -4,
                },
                'itens_add': ['caminhão'],
            },
        ],
    },
    'd5_r2_c9': {
        'dia': 5,
        'titulo': 'DIA 5 - FAZENDA ISOLADA: O PROBLEMA',
        'texto': (
            'O caminhão precisa de combustível e reparos simples. As peças podem estar espalhadas '
            'pela fazenda. O combustível do posto finalmente faz sentido.'
        ),
        'cor_fundo': VERDE,
        'opcoes': [
            {
                'texto': 'Procurar peças.',
                'resultado': 'A decisão leva ao próximo momento: Ataque ao Anoitecer.',
                'proxima': 'd5_r2_c10',
                'efeitos': {
                    'energia': -4,
                    'comida': 1,
                    'agua': 1,
                },
                'itens_add': ['combustível', 'caminhão', 'peça do ônibus'],
            },
            {
                'texto': 'Esperar até amanhã sem procurar.',
                'resultado': 'A decisão leva ao próximo momento: Ataque ao Anoitecer.',
                'proxima': 'd5_r2_c10',
                'efeitos': {
                    'energia': -4,
                    'comida': 1,
                    'agua': 1,
                },
                'itens_add': ['combustível', 'caminhão', 'peça do ônibus'],
            },
        ],
    },
    'd5_r2_c10': {
        'dia': 5,
        'titulo': 'DIA 5 - FAZENDA ISOLADA: ATAQUE AO ANOITECER',
        'texto': (
            'Os infectados do celeiro rompem parte do bloqueio. O barulho atrai outros que vagavam '
            'pelos campos.'
        ),
        'cor_fundo': VERDE,
        'opcoes': [
            {
                'texto': 'Defender a propriedade.',
                'resultado': 'A decisão leva ao próximo momento: Galpão de Ferramentas.',
                'proxima': 'd5_r2_c11',
                'efeitos': {
                    'energia': -4,
                    'moral': 5,
                    'confianca': 2,
                },
                'itens_add': [],
            },
            {
                'texto': 'Fugir pelos fundos.',
                'resultado': 'A decisão leva ao próximo momento: Galpão de Ferramentas.',
                'proxima': 'd5_r2_c11',
                'efeitos': {
                    'energia': -4,
                },
                'itens_add': [],
            },
        ],
    },
    'd5_r2_c11': {
        'dia': 5,
        'titulo': 'DIA 5 - FAZENDA ISOLADA: GALPÃO DE FERRAMENTAS',
        'texto': (
            'Ferramentas antigas permitem reparar parte do caminhão. O fazendeiro ensina o básico '
            'enquanto segura a espingarda perto da porta.'
        ),
        'cor_fundo': VERDE,
        'proxima': 'd5_r2_c12',
    },
    'd5_r2_c12': {
        'dia': 5,
        'titulo': 'DIA 5 - FAZENDA ISOLADA: O PREÇO DA AJUDA',
        'texto': (
            'O fazendeiro pede para ir junto. Alguns do grupo temem que ele atrase a fuga; outros '
            'sabem que sem ele o caminhão talvez não funcione.'
        ),
        'cor_fundo': VERDE,
        'opcoes': [
            {
                'texto': 'Levar o fazendeiro.',
                'resultado': 'A decisão leva ao próximo momento: Última Cerca.',
                'proxima': 'd5_r2_c13',
                'efeitos': {
                    'energia': -4,
                },
                'itens_add': ['caminhão', 'aliado fazendeiro'],
            },
            {
                'texto': 'Deixá-lo na propriedade.',
                'resultado': 'A decisão leva ao próximo momento: Última Cerca.',
                'proxima': 'd5_r2_c13',
                'efeitos': {
                    'energia': -4,
                },
                'itens_add': ['caminhão', 'aliado fazendeiro'],
            },
        ],
    },
    'd5_r2_c13': {
        'dia': 5,
        'titulo': 'DIA 5 - FAZENDA ISOLADA: ÚLTIMA CERCA',
        'texto': 'A horda pressiona a cerca lateral. Se ela cair, a casa será invadida em minutos.',
        'cor_fundo': VERDE,
        'opcoes': [
            {
                'texto': 'Reforçar a cerca.',
                'resultado': 'A decisão leva ao próximo momento: Plano de Fuga.',
                'proxima': 'd5_r2_c14',
                'efeitos': {
                    'energia': -8,
                },
                'itens_add': [],
            },
            {
                'texto': 'Correr para o caminhão ainda incompleto.',
                'resultado': 'A escolha cobra seu preço antes que exista tempo para voltar atrás.',
                'final': {
                    'tipo': 'derrota',
                    'titulo': 'MORTE 3',
                    'texto': 'Correr para o caminhão incompleto; o motor não pega e o grupo é cercado.',
                },
                'efeitos': {
                    'vida': -100,
                },
                'qualidade': 'morte',
            },
        ],
    },
    'd5_r2_c14': {
        'dia': 5,
        'titulo': 'DIA 5 - FAZENDA ISOLADA: PLANO DE FUGA',
        'texto': (
            'O caminhão não está totalmente pronto, mas há esperança. Todos concordam em terminar '
            'reparos ao amanhecer.'
        ),
        'cor_fundo': VERDE,
        'proxima': 'd5_r2_c15',
    },
    'd5_r2_c15': {
        'dia': 5,
        'titulo': 'DIA 5 - FAZENDA ISOLADA: FAZENDA CERCADA',
        'texto': (
            'À noite, a fazenda deixa de parecer lar e vira ilha cercada por mortos. O grupo dorme '
            'perto do caminhão, pronto para fugir.'
        ),
        'cor_fundo': VERDE,
        'proxima': 'd5_r2_fim_1',
    },
    'd5_r3_fim_1': {
        'dia': 5,
        'titulo': 'FIM DO DIA 5',
        'texto': 'Estacionamento subterrâneo alcançado, prédio destruído e rua obrigatória no Dia 6.',
        'cor_fundo': VERDE_CLARO,
        'fim_dia': True,
        'proxima_dia': 'd6_r3_c1',
    },
    'd5_r3_c1': {
        'dia': 5,
        'titulo': 'DIA 5 - O INCÊNDIO: CORREDOR EM CHAMAS',
        'texto': (
            'O prédio ao lado queima e a fumaça entra no apartamento. O saguão está infestado. Para '
            'sair, o personagem precisa descer pelo corredor tomado por fumaça.'
        ),
        'cor_fundo': VERDE,
        'opcoes': [
            {
                'texto': 'Atravessar fumaça para a saída de emergência.',
                'resultado': 'A decisão leva ao próximo momento: Fumaça Preta.',
                'proxima': 'd5_r3_c2',
                'efeitos': {
                    'energia': -8,
                },
                'itens_add': [],
            },
            {
                'texto': 'Entrar na farmácia de manipulação do térreo.',
                'resultado': 'A decisão leva ao próximo momento: Fumaça Preta.',
                'proxima': 'd5_r3_c2',
                'efeitos': {
                    'energia': -4,
                },
                'itens_add': [],
            },
        ],
    },
    'd5_r3_c2': {
        'dia': 5,
        'titulo': 'DIA 5 - O INCÊNDIO: FUMAÇA PRETA',
        'texto': (
            'A visão desaparece. Se o personagem tiver lanterna, vê vigas caindo. Sem lanterna, cada '
            'passo é aposta.'
        ),
        'cor_fundo': VERDE,
        'opcoes': [
            {
                'texto': 'Usar lanterna.',
                'resultado': 'A decisão leva ao próximo momento: Farmácia Trancada.',
                'proxima': 'd5_r3_c3',
                'efeitos': {
                    'energia': -4,
                },
                'itens_add': ['lanterna'],
            },
            {
                'texto': 'Correr às cegas.',
                'resultado': 'A decisão leva ao próximo momento: Farmácia Trancada.',
                'proxima': 'd5_r3_c3',
                'efeitos': {
                    'energia': -8,
                },
                'itens_add': ['lanterna'],
            },
        ],
    },
    'd5_r3_c3': {
        'dia': 5,
        'titulo': 'DIA 5 - O INCÊNDIO: FARMÁCIA TRANCADA',
        'texto': (
            'A porta de vidro reforçado bloqueia medicamentos valiosos. O pé de cabra pode abrir '
            'caminho rapidamente.'
        ),
        'cor_fundo': VERDE,
        'opcoes': [
            {
                'texto': 'Usar pé de cabra.',
                'resultado': 'A escolha cobra seu preço antes que exista tempo para voltar atrás.',
                'final': {
                    'tipo': 'derrota',
                    'titulo': 'MORTE 1',
                    'texto': 'Tentar quebrar o vidro da farmácia sem pé de cabra; inala fumaça tóxica e desmaia.',
                },
                'efeitos': {
                    'vida': -100,
                },
                'qualidade': 'morte',
            },
            {
                'texto': 'Tentar quebrar no chute.',
                'resultado': 'A decisão leva ao próximo momento: Kit Médico Avançado.',
                'proxima': 'd5_r3_c4',
                'efeitos': {
                    'energia': -4,
                },
                'itens_add': ['pé de cabra', 'medicamentos'],
            },
        ],
    },
    'd5_r3_c4': {
        'dia': 5,
        'titulo': 'DIA 5 - O INCÊNDIO: KIT MÉDICO AVANÇADO',
        'texto': (
            'Dentro da farmácia há curativos, antibióticos e pastilhas de cloro. A demora, porém, '
            'deixa a saída principal cercada por chamas.'
        ),
        'cor_fundo': VERDE,
        'opcoes': [
            {
                'texto': 'Pegar kit e sair pelos dutos.',
                'resultado': 'A decisão leva ao próximo momento: Dutos de Ventilação.',
                'proxima': 'd5_r3_c5',
                'efeitos': {
                    'energia': -4,
                    'vida': 5,
                },
                'itens_add': ['kit médico'],
            },
            {
                'texto': 'Continuar procurando mais remédios.',
                'resultado': 'A escolha cobra seu preço antes que exista tempo para voltar atrás.',
                'final': {
                    'tipo': 'derrota',
                    'titulo': 'MORTE 2',
                    'texto': 'Continuar procurando remédios; o teto cede e bloqueia a saída.',
                },
                'efeitos': {
                    'vida': -100,
                },
                'qualidade': 'morte',
            },
        ],
    },
    'd5_r3_c5': {
        'dia': 5,
        'titulo': 'DIA 5 - O INCÊNDIO: DUTOS DE VENTILAÇÃO',
        'texto': (
            'Os dutos levam ao estacionamento subterrâneo. O metal aquece e rangidos indicam que '
            'parte do prédio pode desabar.'
        ),
        'cor_fundo': VERDE,
        'opcoes': [
            {
                'texto': 'Rastejar devagar.',
                'resultado': 'A decisão leva ao próximo momento: Escada de Emergência.',
                'proxima': 'd5_r3_c6',
                'efeitos': {
                    'energia': -4,
                },
                'itens_add': [],
            },
            {
                'texto': 'Forçar passagem rápida.',
                'resultado': 'A decisão leva ao próximo momento: Escada de Emergência.',
                'proxima': 'd5_r3_c6',
                'efeitos': {
                    'energia': -8,
                },
                'itens_add': [],
            },
        ],
    },
    'd5_r3_c6': {
        'dia': 5,
        'titulo': 'DIA 5 - O INCÊNDIO: ESCADA DE EMERGÊNCIA',
        'texto': (
            'A escada está cheia de fumaça. Um infectado em chamas tropeça degraus abaixo, espalhando '
            'fogo.'
        ),
        'cor_fundo': VERDE,
        'opcoes': [
            {
                'texto': 'Esperar ele cair.',
                'resultado': 'A decisão leva ao próximo momento: Subsolo.',
                'proxima': 'd5_r3_c7',
                'efeitos': {
                    'energia': -4,
                },
                'itens_add': ['peça do ônibus'],
            },
            {
                'texto': 'Passar por cima dele.',
                'resultado': 'A decisão leva ao próximo momento: Subsolo.',
                'proxima': 'd5_r3_c7',
                'efeitos': {
                    'energia': -4,
                },
                'itens_add': ['peça do ônibus'],
            },
        ],
    },
    'd5_r3_c7': {
        'dia': 5,
        'titulo': 'DIA 5 - O INCÊNDIO: SUBSOLO',
        'texto': (
            'O personagem chega ao estacionamento. Acima, o apartamento que servia de abrigo '
            'desaparece nas chamas.'
        ),
        'cor_fundo': VERDE,
        'proxima': 'd5_r3_c8',
    },
    'd5_r3_c8': {
        'dia': 5,
        'titulo': 'DIA 5 - O INCÊNDIO: PORTÃO FECHADO',
        'texto': (
            'O portão da garagem está travado. Há controles queimados e uma corrente grossa. Talvez o '
            'pé de cabra abra, talvez seja preciso achar outro caminho.'
        ),
        'cor_fundo': VERDE,
        'opcoes': [
            {
                'texto': 'Forçar portão.',
                'resultado': 'A decisão leva ao próximo momento: Saída de Serviço.',
                'proxima': 'd5_r3_c9',
                'efeitos': {
                    'energia': -8,
                },
                'itens_add': ['pé de cabra'],
            },
            {
                'texto': 'Procurar saída de serviço.',
                'resultado': 'A decisão leva ao próximo momento: Saída de Serviço.',
                'proxima': 'd5_r3_c9',
                'efeitos': {
                    'energia': -4,
                    'comida': 1,
                    'agua': 1,
                },
                'itens_add': ['pé de cabra'],
            },
        ],
    },
    'd5_r3_c9': {
        'dia': 5,
        'titulo': 'DIA 5 - O INCÊNDIO: SAÍDA DE SERVIÇO',
        'texto': (
            'A saída de serviço leva a um beco tomado por fumaça. Carros batidos bloqueiam a rua. Um '
            'som de helicóptero passa longe, rumo ao estádio.'
        ),
        'cor_fundo': VERDE,
        'proxima': 'd5_r3_c10',
    },
    'd5_r3_c10': {
        'dia': 5,
        'titulo': 'DIA 5 - O INCÊNDIO: CHAMAS NO TETO',
        'texto': (
            'Parte da laje cede. O personagem precisa escolher entre salvar a mochila ou sair '
            'imediatamente.'
        ),
        'cor_fundo': VERDE,
        'opcoes': [
            {
                'texto': 'Salvar mochila.',
                'resultado': 'A escolha cobra seu preço antes que exista tempo para voltar atrás.',
                'final': {
                    'tipo': 'derrota',
                    'titulo': 'MORTE 4',
                    'texto': (
                        'Salvar a mochila durante o desabamento; o atraso prende o personagem no corredor em '
                        'chamas.'
                    ),
                },
                'efeitos': {
                    'vida': -100,
                },
                'qualidade': 'morte',
            },
            {
                'texto': 'Abandonar parte dos recursos.',
                'resultado': 'A decisão leva ao próximo momento: Saqueadores Atraídos.',
                'proxima': 'd5_r3_c11',
                'efeitos': {
                    'energia': -4,
                    'moral': -4,
                    'confianca': -1,
                    'comida': 1,
                    'agua': 1,
                },
                'itens_add': ['mochila'],
            },
        ],
    },
    'd5_r3_c11': {
        'dia': 5,
        'titulo': 'DIA 5 - O INCÊNDIO: SAQUEADORES ATRAÍDOS',
        'texto': 'Homens gritam na rua, atraídos pelo incêndio. Eles procuram prédios vazios para saquear.',
        'cor_fundo': VERDE,
        'opcoes': [
            {
                'texto': 'Esconder-se no subsolo.',
                'resultado': 'A decisão leva ao próximo momento: Respiração Difícil.',
                'proxima': 'd5_r3_c12',
                'efeitos': {
                    'energia': -4,
                    'moral': -4,
                    'confianca': -1,
                },
                'itens_add': [],
            },
            {
                'texto': 'Pedir ajuda.',
                'resultado': 'A escolha cobra seu preço antes que exista tempo para voltar atrás.',
                'final': {
                    'tipo': 'derrota',
                    'titulo': 'MORTE 3',
                    'texto': (
                        'Pedir ajuda aos saqueadores; eles roubam recursos e deixam o personagem para morrer no '
                        'fogo.'
                    ),
                },
                'efeitos': {
                    'vida': -100,
                },
                'qualidade': 'morte',
            },
        ],
    },
    'd5_r3_c12': {
        'dia': 5,
        'titulo': 'DIA 5 - O INCÊNDIO: RESPIRAÇÃO DIFÍCIL',
        'texto': (
            'A fumaça cobra preço. Sem kit médico ou água, o personagem tosse sangue. Com preparo, '
            'estabiliza a respiração.'
        ),
        'cor_fundo': VERDE,
        'proxima': 'd5_r3_c13',
    },
    'd5_r3_c13': {
        'dia': 5,
        'titulo': 'DIA 5 - O INCÊNDIO: GARAGEM COMO NOVO ABRIGO',
        'texto': (
            'O estacionamento vira abrigo temporário. Há carros, corpos e escuridão, mas pelo menos '
            'não há fogo imediato.'
        ),
        'cor_fundo': VERDE,
        'opcoes': [
            {
                'texto': 'Dormir dentro de um carro.',
                'resultado': 'A decisão leva ao próximo momento: Sem Volta.',
                'proxima': 'd5_r3_c14',
                'efeitos': {
                    'energia': -4,
                },
                'itens_add': [],
            },
            {
                'texto': 'Dormir na guarita.',
                'resultado': 'A decisão leva ao próximo momento: Sem Volta.',
                'proxima': 'd5_r3_c14',
                'efeitos': {
                    'energia': -4,
                },
                'itens_add': [],
            },
        ],
    },
    'd5_r3_c14': {
        'dia': 5,
        'titulo': 'DIA 5 - O INCÊNDIO: SEM VOLTA',
        'texto': (
            'O prédio está perdido. A rota de sobrevivência deixa de ser vertical e passa a ser a '
            'rua.'
        ),
        'cor_fundo': VERDE,
        'proxima': 'd5_r3_c15',
    },
    'd5_r3_c15': {
        'dia': 5,
        'titulo': 'DIA 5 - O INCÊNDIO: FIM NO SUBSOLO',
        'texto': (
            'O personagem fecha a noite no estacionamento, segurando itens raros. O Dia 6 será a '
            'busca por veículo ou saída segura.'
        ),
        'cor_fundo': VERDE,
        'proxima': 'd5_r3_fim_1',
    },
    'd5_r4_fim_1': {
        'dia': 5,
        'titulo': 'FIM DO DIA 5',
        'texto': 'Comboio na estrada, terminal destruído e grupo ainda unido.',
        'cor_fundo': VERDE_CLARO,
        'fim_dia': True,
        'proxima_dia': 'd6_r4_c1',
    },
    'd5_r4_c1': {
        'dia': 5,
        'titulo': 'DIA 5 - FUGA DE ÔNIBUS: PORTÃO CEDENDO',
        'texto': (
            'O amanhecer chega com pancadas no portão principal do terminal. A horda encontrou o '
            'abrigo. Sobreviventes reúnem mochilas, crianças e feridos.'
        ),
        'cor_fundo': VERDE,
        'opcoes': [
            {
                'texto': 'Esperar sobreviventes da lista.',
                'resultado': 'A decisão leva ao próximo momento: Helena Liga o Ônibus.',
                'proxima': 'd5_r4_c2',
                'efeitos': {
                    'energia': -4,
                },
                'itens_add': ['mochila'],
            },
            {
                'texto': 'Sair antes de todos embarcarem.',
                'resultado': 'A decisão leva ao próximo momento: Helena Liga o Ônibus.',
                'proxima': 'd5_r4_c2',
                'efeitos': {
                    'energia': -4,
                },
                'itens_add': ['mochila'],
            },
        ],
    },
    'd5_r4_c2': {
        'dia': 5,
        'titulo': 'DIA 5 - FUGA DE ÔNIBUS: HELENA LIGA O ÔNIBUS',
        'texto': (
            'Helena gira a chave. O motor reclama, falha e finalmente liga. O som alto atrai ainda '
            'mais infectados.'
        ),
        'cor_fundo': VERDE,
        'proxima': 'd5_r4_c3',
    },
    'd5_r4_c3': {
        'dia': 5,
        'titulo': 'DIA 5 - FUGA DE ÔNIBUS: JONAS TENTA TOMAR O VOLANTE',
        'texto': (
            'Jonas avança para a cabine dizendo que Helena vai matar todos por esperar. O ônibus '
            'inteiro prende a respiração.'
        ),
        'cor_fundo': VERDE,
        'opcoes': [
            {
                'texto': 'Apoiar Helena.',
                'resultado': 'A decisão leva ao próximo momento: Corrida para Embarcar.',
                'proxima': 'd5_r4_c4',
                'efeitos': {
                    'energia': -4,
                    'moral': 5,
                    'confianca': 2,
                },
                'itens_add': ['rações', 'ônibus', 'aliado Lena', 'aliado Helena', 'aliado Jonas'],
            },
            {
                'texto': 'Deixar Jonas assumir.',
                'resultado': 'A escolha cobra seu preço antes que exista tempo para voltar atrás.',
                'final': {
                    'tipo': 'derrota',
                    'titulo': 'MORTE 1',
                    'texto': 'Deixar Jonas assumir; ele acelera cedo em excesso e bate o ônibus contra a barricada.',
                },
                'efeitos': {
                    'vida': -100,
                },
                'qualidade': 'morte',
            },
        ],
    },
    'd5_r4_c4': {
        'dia': 5,
        'titulo': 'DIA 5 - FUGA DE ÔNIBUS: CORRIDA PARA EMBARCAR',
        'texto': (
            'Pessoas correm pela plataforma. Mochilas caem, nomes de familiares são gritados e as '
            'primeiras brechas se abrem nos portões.'
        ),
        'cor_fundo': VERDE,
        'proxima': 'd5_r4_c5',
    },
    'd5_r4_c5': {
        'dia': 5,
        'titulo': 'DIA 5 - FUGA DE ÔNIBUS: CRIANÇA PRESA',
        'texto': (
            'Uma criança fica presa entre malas e bancos virados. A mulher salva no Dia 1 grita '
            'pedindo ajuda.'
        ),
        'cor_fundo': VERDE,
        'opcoes': [
            {
                'texto': 'Salvar a criança.',
                'resultado': 'A decisão leva ao próximo momento: Motor Falha.',
                'proxima': 'd5_r4_c6',
                'efeitos': {
                    'energia': -4,
                    'moral': 5,
                    'confianca': 2,
                },
                'itens_add': [],
            },
            {
                'texto': 'Fechar a porta e partir.',
                'resultado': 'A decisão leva ao próximo momento: Motor Falha.',
                'proxima': 'd5_r4_c6',
                'efeitos': {
                    'energia': -4,
                },
                'itens_add': [],
            },
        ],
    },
    'd5_r4_c6': {
        'dia': 5,
        'titulo': 'DIA 5 - FUGA DE ÔNIBUS: MOTOR FALHA',
        'texto': (
            'O ônibus tenta avançar, mas o motor falha. Helena pede uma ferramenta específica para '
            'ajustar o painel.'
        ),
        'cor_fundo': VERDE,
        'opcoes': [
            {
                'texto': 'Buscar ferramenta.',
                'resultado': 'A decisão leva ao próximo momento: Ferramenta na Mão.',
                'proxima': 'd5_r4_c7',
                'efeitos': {
                    'energia': -4,
                },
                'itens_add': ['ferramentas', 'ônibus', 'aliado Lena', 'aliado Helena'],
            },
            {
                'texto': 'Forçar o motor no acelerador.',
                'resultado': 'A escolha cobra seu preço antes que exista tempo para voltar atrás.',
                'final': {
                    'tipo': 'derrota',
                    'titulo': 'MORTE 2',
                    'texto': 'Forçar o motor no acelerador; o ônibus apaga no meio da horda.',
                },
                'efeitos': {
                    'vida': -100,
                },
                'qualidade': 'morte',
            },
        ],
    },
    'd5_r4_c7': {
        'dia': 5,
        'titulo': 'DIA 5 - FUGA DE ÔNIBUS: FERRAMENTA NA MÃO',
        'texto': 'Com a ferramenta, Helena faz o motor responder. O portão lateral começa a cair.',
        'cor_fundo': VERDE,
        'proxima': 'd5_r4_c8',
    },
    'd5_r4_c8': {
        'dia': 5,
        'titulo': 'DIA 5 - FUGA DE ÔNIBUS: INFECTADOS NO TERMINAL',
        'texto': 'Os mortos invadem, tropeçando em bancos, grades e malas. O ônibus precisa sair agora.',
        'cor_fundo': VERDE,
        'opcoes': [
            {
                'texto': 'Fechar a porta.',
                'resultado': 'A decisão leva ao próximo momento: Barricada Rompida.',
                'proxima': 'd5_r4_c9',
                'efeitos': {
                    'energia': -4,
                },
                'itens_add': ['ônibus', 'peça do ônibus'],
            },
            {
                'texto': 'Esperar mais sobreviventes distantes.',
                'resultado': 'A escolha cobra seu preço antes que exista tempo para voltar atrás.',
                'final': {
                    'tipo': 'derrota',
                    'titulo': 'MORTE 3',
                    'texto': 'Esperar sobreviventes distantes com infectados dentro do terminal; a porta é tomada.',
                },
                'efeitos': {
                    'vida': -100,
                },
                'qualidade': 'morte',
            },
        ],
    },
    'd5_r4_c9': {
        'dia': 5,
        'titulo': 'DIA 5 - FUGA DE ÔNIBUS: BARRICADA ROMPIDA',
        'texto': (
            'Helena acelera. O ônibus bate na barricada, arrasta grades e passa por cima de '
            'destroços.'
        ),
        'cor_fundo': VERDE,
        'proxima': 'd5_r4_c10',
    },
    'd5_r4_c10': {
        'dia': 5,
        'titulo': 'DIA 5 - FUGA DE ÔNIBUS: RUA PRINCIPAL BLOQUEADA',
        'texto': (
            'A rua está tomada por veículos abandonados. Helena precisa escolher uma rota '
            'alternativa.'
        ),
        'cor_fundo': VERDE,
        'opcoes': [
            {
                'texto': 'Usar rua lateral.',
                'resultado': 'A decisão leva ao próximo momento: Rota do Desvio.',
                'proxima': 'd5_r4_c11',
                'efeitos': {
                    'energia': -4,
                },
                'itens_add': ['aliado Lena', 'aliado Helena'],
            },
            {
                'texto': 'Forçar pela avenida.',
                'resultado': 'A decisão leva ao próximo momento: Rota do Desvio.',
                'proxima': 'd5_r4_c11',
                'efeitos': {
                    'energia': -8,
                },
                'itens_add': ['aliado Lena', 'aliado Helena'],
            },
        ],
    },
    'd5_r4_c11': {
        'dia': 5,
        'titulo': 'DIA 5 - FUGA DE ÔNIBUS: ROTA DO DESVIO',
        'texto': (
            'O ônibus cruza becos largos e passa perto do posto de gasolina saqueado, onde sinais do '
            'comboio armado aparecem.'
        ),
        'cor_fundo': VERDE,
        'proxima': 'd5_r4_c12',
    },
    'd5_r4_c12': {
        'dia': 5,
        'titulo': 'DIA 5 - FUGA DE ÔNIBUS: JONAS AMEAÇA PASSAGEIROS',
        'texto': 'Jonas, furioso, ameaça passageiros e diz que salvar crianças atrasou todos.',
        'cor_fundo': VERDE,
        'opcoes': [
            {
                'texto': 'Conter Jonas com apoio do grupo.',
                'resultado': 'A decisão leva ao próximo momento: Ponte Congestionada.',
                'proxima': 'd5_r4_c13',
                'efeitos': {
                    'energia': -4,
                },
                'itens_add': ['aliado Jonas'],
            },
            {
                'texto': 'Expulsá-lo do ônibus em movimento.',
                'resultado': 'A decisão leva ao próximo momento: Ponte Congestionada.',
                'proxima': 'd5_r4_c13',
                'efeitos': {
                    'energia': -4,
                },
                'itens_add': ['ônibus', 'aliado Jonas'],
            },
        ],
    },
    'd5_r4_c13': {
        'dia': 5,
        'titulo': 'DIA 5 - FUGA DE ÔNIBUS: PONTE CONGESTIONADA',
        'texto': 'Uma ponte cheia de carros bloqueia a saída da cidade. Infectados surgem atrás.',
        'cor_fundo': VERDE,
        'opcoes': [
            {
                'texto': 'Empurrar carros com o ônibus.',
                'resultado': 'A decisão leva ao próximo momento: Fora da Cidade.',
                'proxima': 'd5_r4_c14',
                'efeitos': {
                    'energia': -4,
                },
                'itens_add': ['ônibus'],
            },
            {
                'texto': 'Abandonar o ônibus e correr.',
                'resultado': 'A escolha cobra seu preço antes que exista tempo para voltar atrás.',
                'final': {
                    'tipo': 'derrota',
                    'titulo': 'MORTE 4',
                    'texto': 'Abandonar o ônibus na ponte; a multidão se dispersa e o personagem é alcançado.',
                },
                'efeitos': {
                    'vida': -100,
                },
                'qualidade': 'morte',
            },
        ],
    },
    'd5_r4_c14': {
        'dia': 5,
        'titulo': 'DIA 5 - FUGA DE ÔNIBUS: FORA DA CIDADE',
        'texto': 'O ônibus consegue sair da área urbana. Campos e rodovia aparecem no horizonte.',
        'cor_fundo': VERDE,
        'proxima': 'd5_r4_c15',
    },
    'd5_r4_c15': {
        'dia': 5,
        'titulo': 'DIA 5 - FUGA DE ÔNIBUS: NOITE NO ÔNIBUS',
        'texto': (
            'O grupo dorme dentro do veículo parado. Helena segura o volante mesmo com o motor '
            'desligado, como se soltá-lo fosse perder a esperança.'
        ),
        'cor_fundo': VERDE,
        'opcoes': [
            {
                'texto': 'Fazer guarda.',
                'resultado': 'Essa decisão encerra o caminho iniciado neste dia.',
                'proxima': 'd5_r4_fim_1',
                'efeitos': {
                    'energia': -4,
                    'moral': 5,
                    'confianca': 2,
                },
                'itens_add': ['aliado Lena', 'aliado Helena'],
                'qualidade': 'media',
            },
            {
                'texto': 'Dormir sem vigia.',
                'resultado': 'Essa decisão encerra o caminho iniciado neste dia.',
                'proxima': 'd5_r4_fim_1',
                'efeitos': {
                    'energia': -4,
                    'moral': 5,
                    'confianca': 2,
                },
                'itens_add': ['aliado Lena', 'aliado Helena'],
                'qualidade': 'media',
            },
        ],
    },
    'd6_r1_fim_1': {
        'dia': 6,
        'titulo': 'FIM DO DIA 6 A',
        'texto': 'Na mira da base, vivos, mas tratados como ameaça.',
        'cor_fundo': VERDE_CLARO,
        'fim_dia': True,
        'proxima_dia': 'd7_r1_inicio',
    },
    'd6_r1_fim_2': {
        'dia': 6,
        'titulo': 'FIM DO DIA 6 B',
        'texto': 'Quarentena externa, com menos feridos se o jogador abandonou parte do grupo.',
        'cor_fundo': VERDE_CLARO,
        'fim_dia': True,
        'proxima_dia': 'd7_r1_inicio',
    },
    'd6_r1_c1': {
        'dia': 6,
        'titulo': 'DIA 6 - FRONTEIRA DO MEDO: O SILÊNCIO',
        'texto': (
            'O grupo acorda na casa arrombada. Feridos gemem, a diretora organiza crianças e o '
            'zelador aponta a base militar como única chance.'
        ),
        'cor_fundo': VERDE,
        'opcoes': [
            {
                'texto': 'Sair imediatamente antes que a horda volte.',
                'resultado': 'A decisão leva ao próximo momento: Rastros de Destruição.',
                'proxima': 'd6_r1_c2',
                'efeitos': {
                    'energia': -4,
                },
                'itens_add': ['corda', 'aliado diretora', 'aliado zelador'],
            },
            {
                'texto': 'Esperar os feridos melhorarem.',
                'resultado': 'A decisão leva ao próximo momento: Rastros de Destruição.',
                'proxima': 'd6_r1_c2',
                'efeitos': {
                    'energia': -4,
                },
                'itens_add': ['corda', 'aliado diretora', 'aliado zelador'],
            },
        ],
    },
    'd6_r1_c2': {
        'dia': 6,
        'titulo': 'DIA 6 - FRONTEIRA DO MEDO: RASTROS DE DESTRUIÇÃO',
        'texto': (
            'Comboios militares destruídos, barricadas capotadas e corpos de soldados aparecem no '
            'limite da cidade.'
        ),
        'cor_fundo': VERDE,
        'opcoes': [
            {
                'texto': 'Vasculhar corpos por munição.',
                'resultado': 'A decisão leva ao próximo momento: Ponte da Morte.',
                'proxima': 'd6_r1_c3',
                'efeitos': {
                    'energia': -4,
                    'comida': 1,
                    'agua': 1,
                },
                'itens_add': ['munição'],
            },
            {
                'texto': 'Apertar passo até a ponte.',
                'resultado': 'A decisão leva ao próximo momento: Ponte da Morte.',
                'proxima': 'd6_r1_c3',
                'efeitos': {
                    'energia': -4,
                },
                'itens_add': [],
            },
        ],
    },
    'd6_r1_c3': {
        'dia': 6,
        'titulo': 'DIA 6 - FRONTEIRA DO MEDO: PONTE DA MORTE',
        'texto': (
            'A ponte para a área militar está tomada por carros do antigo posto de quarentena e '
            'infectados presos.'
        ),
        'cor_fundo': VERDE,
        'opcoes': [
            {
                'texto': 'Passar pela passarela lateral.',
                'resultado': 'A decisão leva ao próximo momento: O Deslize.',
                'proxima': 'd6_r1_c4',
                'efeitos': {
                    'energia': -4,
                },
                'itens_add': [],
            },
            {
                'texto': 'Cruzar pelo centro da ponte.',
                'resultado': 'A escolha cobra seu preço antes que exista tempo para voltar atrás.',
                'final': {
                    'tipo': 'derrota',
                    'titulo': 'MORTE 1',
                    'texto': 'Cruzar pelo centro da ponte; o grupo é cercado entre veículos.',
                },
                'efeitos': {
                    'vida': -100,
                },
                'qualidade': 'morte',
            },
        ],
    },
    'd6_r1_c4': {
        'dia': 6,
        'titulo': 'DIA 6 - FRONTEIRA DO MEDO: O DESLIZE',
        'texto': (
            'Um ferido escorrega na grade úmida. O metal ecoa. Infectados quebram vidros de carros e '
            'despertam em massa.'
        ),
        'cor_fundo': VERDE,
        'opcoes': [
            {
                'texto': 'Puxar o sobrevivente e mandar todos correrem.',
                'resultado': 'A decisão leva ao próximo momento: Encurralados.',
                'proxima': 'd6_r1_c5',
                'efeitos': {
                    'energia': -8,
                },
                'itens_add': [],
            },
            {
                'texto': 'Abandoná-lo para manter silêncio.',
                'resultado': 'A decisão leva ao próximo momento: Encurralados.',
                'proxima': 'd6_r1_c5',
                'efeitos': {
                    'energia': -4,
                },
                'itens_add': [],
            },
        ],
    },
    'd6_r1_c5': {
        'dia': 6,
        'titulo': 'DIA 6 - FRONTEIRA DO MEDO: ENCURRALADOS',
        'texto': 'No fim da ponte há muro de concreto e portões fechados. A horda vem pelas costas.',
        'cor_fundo': VERDE,
        'proxima': 'd6_r1_c6',
    },
    'd6_r1_c6': {
        'dia': 6,
        'titulo': 'DIA 6 - FRONTEIRA DO MEDO: NA MIRA',
        'texto': 'Holofotes acendem. Soldados gritam por alto-falantes: todos no chão ou abrirão fogo.',
        'cor_fundo': VERDE,
        'opcoes': [
            {
                'texto': 'Jogar-se no chão com o grupo.',
                'resultado': 'A decisão leva ao próximo momento: Rajadas.',
                'proxima': 'd6_r1_c7',
                'efeitos': {
                    'energia': -4,
                },
                'itens_add': [],
            },
            {
                'texto': 'Correr para o portão.',
                'resultado': 'A escolha cobra seu preço antes que exista tempo para voltar atrás.',
                'final': {
                    'tipo': 'derrota',
                    'titulo': 'MORTE 2',
                    'texto': 'Correr para o portão sob ordem militar; soldados atiram antes de identificar civis.',
                },
                'efeitos': {
                    'vida': -100,
                },
                'qualidade': 'morte',
            },
        ],
    },
    'd6_r1_c7': {
        'dia': 6,
        'titulo': 'DIA 6 - FRONTEIRA DO MEDO: RAJADAS',
        'texto': (
            'Metralhadoras cortam a primeira linha de infectados centímetros acima das cabeças do '
            'grupo.'
        ),
        'cor_fundo': VERDE,
        'proxima': 'd6_r1_c8',
    },
    'd6_r1_c8': {
        'dia': 6,
        'titulo': 'DIA 6 - FRONTEIRA DO MEDO: PORTÃO PESADO',
        'texto': (
            'O portão range e começa a abrir. Soldados mascarados apontam fuzis para sobreviventes e '
            'feridos.'
        ),
        'cor_fundo': VERDE,
        'proxima': 'd6_r1_c9',
    },
    'd6_r1_c9': {
        'dia': 6,
        'titulo': 'DIA 6 - FRONTEIRA DO MEDO: QUARENTENA EXTERNA',
        'texto': (
            'O grupo é levado para área de triagem fora dos muros principais. Chegaram, mas segurança '
            'e liberdade não são a mesma coisa.'
        ),
        'cor_fundo': VERDE,
        'opcoes': [
            {
                'texto': 'FIM DO DIA 6 A',
                'resultado': 'Essa decisão encerra o caminho iniciado neste dia.',
                'proxima': 'd6_r1_fim_1',
                'efeitos': {
                    'energia': -4,
                },
                'qualidade': 'media',
            },
            {
                'texto': 'FIM DO DIA 6 B',
                'resultado': 'Essa decisão encerra o caminho iniciado neste dia.',
                'proxima': 'd6_r1_fim_2',
                'efeitos': {
                    'energia': -4,
                },
                'qualidade': 'media',
            },
        ],
    },
    'd6_r2_fim_1': {
        'dia': 6,
        'titulo': 'FIM DO DIA 6 A',
        'texto': 'Perto da base com caminhão funcional e grupo abastecido.',
        'cor_fundo': VERDE_CLARO,
        'fim_dia': True,
        'proxima_dia': 'd7_r2_inicio',
    },
    'd6_r2_fim_2': {
        'dia': 6,
        'titulo': 'FIM DO DIA 6 B',
        'texto': 'Perto da base a pé, sem caminhão, mas com menos barulho.',
        'cor_fundo': VERDE_CLARO,
        'fim_dia': True,
        'proxima_dia': 'd7_r2_inicio',
    },
    'd6_r2_c1': {
        'dia': 6,
        'titulo': 'DIA 6 - O CAMINHÃO: REPAROS',
        'texto': (
            'Ao amanhecer, o grupo trabalha no caminhão. O fazendeiro identifica problemas e o '
            'combustível do posto é usado.'
        ),
        'cor_fundo': VERDE,
        'opcoes': [
            {
                'texto': 'Consertar o caminhão.',
                'resultado': 'A escolha cobra seu preço antes que exista tempo para voltar atrás.',
                'final': {
                    'tipo': 'derrota',
                    'titulo': 'MORTE 2',
                    'texto': 'Acelerar na estrada esburacada; o caminhão capota.',
                },
                'efeitos': {
                    'vida': -100,
                },
                'qualidade': 'morte',
            },
            {
                'texto': 'Fugir a pé antes da horda voltar.',
                'resultado': 'A decisão leva ao próximo momento: Oficina Improvisada.',
                'proxima': 'd6_r2_c2',
                'efeitos': {
                    'energia': -4,
                },
                'itens_add': ['combustível', 'caminhão', 'aliado fazendeiro'],
            },
        ],
    },
    'd6_r2_c2': {
        'dia': 6,
        'titulo': 'DIA 6 - O CAMINHÃO: OFICINA IMPROVISADA',
        'texto': 'Ferramentas antigas estão espalhadas. Peças enferrujadas ainda servem.',
        'cor_fundo': VERDE,
        'opcoes': [
            {
                'texto': 'Continuar reparos.',
                'resultado': 'A decisão leva ao próximo momento: Primeira Tentativa.',
                'proxima': 'd6_r2_c3',
                'efeitos': {
                    'energia': -4,
                },
                'itens_add': ['ferramentas', 'peça do ônibus'],
            },
            {
                'texto': 'Forçar partida sem terminar reparo.',
                'resultado': 'A escolha cobra seu preço antes que exista tempo para voltar atrás.',
                'final': {
                    'tipo': 'derrota',
                    'titulo': 'MORTE 1',
                    'texto': 'Forçar partida sem reparo; o caminhão morre cercado por infectados.',
                },
                'efeitos': {
                    'vida': -100,
                },
                'qualidade': 'morte',
            },
        ],
    },
    'd6_r2_c3': {
        'dia': 6,
        'titulo': 'DIA 6 - O CAMINHÃO: PRIMEIRA TENTATIVA',
        'texto': 'O motor gira lentamente e finalmente liga. O som ecoa pela fazenda.',
        'cor_fundo': VERDE,
        'proxima': 'd6_r2_c4',
    },
    'd6_r2_c4': {
        'dia': 6,
        'titulo': 'DIA 6 - O CAMINHÃO: INFECTADOS ATRAÍDOS',
        'texto': 'O barulho do motor atrai infectados dos campos e do celeiro.',
        'cor_fundo': VERDE,
        'opcoes': [
            {
                'texto': 'Carregar todos rapidamente.',
                'resultado': 'A decisão leva ao próximo momento: Deixando a Fazenda.',
                'proxima': 'd6_r2_c5',
                'efeitos': {
                    'energia': -4,
                },
                'itens_add': [],
            },
            {
                'texto': 'Esperar recolher mais comida.',
                'resultado': 'A decisão leva ao próximo momento: Deixando a Fazenda.',
                'proxima': 'd6_r2_c5',
                'efeitos': {
                    'energia': -4,
                    'comida': 1,
                    'agua': 1,
                },
                'itens_add': [],
            },
        ],
    },
    'd6_r2_c5': {
        'dia': 6,
        'titulo': 'DIA 6 - O CAMINHÃO: DEIXANDO A FAZENDA',
        'texto': 'O caminhão atravessa a cerca lateral. O fazendeiro olha para trás uma última vez.',
        'cor_fundo': VERDE,
        'proxima': 'd6_r2_c6',
    },
    'd6_r2_c6': {
        'dia': 6,
        'titulo': 'DIA 6 - O CAMINHÃO: ESTRADAS SECUNDÁRIAS',
        'texto': 'A estrada rural tem buracos, lama e corpos. O veículo balança como se fosse desmontar.',
        'cor_fundo': VERDE,
        'opcoes': [
            {
                'texto': 'Seguir devagar.',
                'resultado': 'A decisão leva ao próximo momento: Posto Militar.',
                'proxima': 'd6_r2_c7',
                'efeitos': {
                    'energia': -4,
                },
                'itens_add': [],
            },
            {
                'texto': 'Acelerar para ganhar tempo.',
                'resultado': 'A decisão leva ao próximo momento: Posto Militar.',
                'proxima': 'd6_r2_c7',
                'efeitos': {
                    'energia': -4,
                },
                'itens_add': [],
            },
        ],
    },
    'd6_r2_c7': {
        'dia': 6,
        'titulo': 'DIA 6 - O CAMINHÃO: POSTO MILITAR',
        'texto': (
            'Um posto militar destruído bloqueia a estrada. Há placas de triagem e uma mensagem '
            'repetindo Aurora.'
        ),
        'cor_fundo': VERDE,
        'opcoes': [
            {
                'texto': 'Parar para ouvir rádio.',
                'resultado': 'A decisão leva ao próximo momento: Problema Mecânico.',
                'proxima': 'd6_r2_c8',
                'efeitos': {
                    'energia': -4,
                },
                'itens_add': ['rádio'],
            },
            {
                'texto': 'Passar direto.',
                'resultado': 'A decisão leva ao próximo momento: Problema Mecânico.',
                'proxima': 'd6_r2_c8',
                'efeitos': {
                    'energia': -4,
                },
                'itens_add': [],
            },
        ],
    },
    'd6_r2_c8': {
        'dia': 6,
        'titulo': 'DIA 6 - O CAMINHÃO: PROBLEMA MECÂNICO',
        'texto': (
            'O motor esquenta. É preciso parar alguns minutos ou arriscar quebrar antes da zona '
            'segura.'
        ),
        'cor_fundo': VERDE,
        'proxima': 'd6_r2_c9',
    },
    'd6_r2_c9': {
        'dia': 6,
        'titulo': 'DIA 6 - O CAMINHÃO: AS LUZES',
        'texto': (
            'Ao anoitecer, luzes da base aparecem no horizonte. O grupo estaciona escondido para a '
            'última noite.'
        ),
        'cor_fundo': VERDE,
        'opcoes': [
            {
                'texto': 'FIM DO DIA 6 A',
                'resultado': 'Essa decisão encerra o caminho iniciado neste dia.',
                'proxima': 'd6_r2_fim_1',
                'efeitos': {
                    'energia': -4,
                },
                'qualidade': 'media',
            },
            {
                'texto': 'FIM DO DIA 6 B',
                'resultado': 'Essa decisão encerra o caminho iniciado neste dia.',
                'proxima': 'd6_r2_fim_2',
                'efeitos': {
                    'energia': -4,
                },
                'qualidade': 'media',
            },
        ],
    },
    'd6_r3_fim_1': {
        'dia': 6,
        'titulo': 'FIM DO DIA 6 A',
        'texto': 'Guarita próxima ao estádio, com colete e suprimentos.',
        'cor_fundo': VERDE_CLARO,
        'fim_dia': True,
        'proxima_dia': 'd7_r3_inicio',
    },
    'd6_r3_fim_2': {
        'dia': 6,
        'titulo': 'FIM DO DIA 6 B',
        'texto': 'Caminhonete obtida, permitindo rota de impacto até o estádio.',
        'cor_fundo': VERDE_CLARO,
        'fim_dia': True,
        'proxima_dia': 'd7_r3_inicio',
    },
    'd6_r3_c1': {
        'dia': 6,
        'titulo': 'DIA 6 - GARAGEM SUBTERRÂNEA: ENTRE OS CARROS',
        'texto': (
            'O estacionamento está escuro. Há uma caminhonete com painel aceso e uma van de entregas '
            'trancada nos fundos.'
        ),
        'cor_fundo': VERDE,
        'opcoes': [
            {
                'texto': 'Entrar na caminhonete.',
                'resultado': 'A decisão leva ao próximo momento: Alarme.',
                'proxima': 'd6_r3_c2',
                'efeitos': {
                    'energia': -4,
                },
                'itens_add': ['caminhonete'],
            },
            {
                'texto': 'Investigar a van.',
                'resultado': 'A decisão leva ao próximo momento: Alarme.',
                'proxima': 'd6_r3_c2',
                'efeitos': {
                    'energia': -4,
                },
                'itens_add': ['caminhonete'],
            },
        ],
    },
    'd6_r3_c2': {
        'dia': 6,
        'titulo': 'DIA 6 - GARAGEM SUBTERRÂNEA: ALARME',
        'texto': 'Ao tocar no volante, o alarme dispara. Rosnados ecoam entre pilares.',
        'cor_fundo': VERDE,
        'opcoes': [
            {
                'texto': 'Cortar fios com faca de caça.',
                'resultado': 'A decisão leva ao próximo momento: Tanque Cheio.',
                'proxima': 'd6_r3_c3',
                'efeitos': {
                    'energia': -4,
                },
                'itens_add': ['faca de caça'],
            },
            {
                'texto': 'Abandonar veículo e correr.',
                'resultado': 'A decisão leva ao próximo momento: Tanque Cheio.',
                'proxima': 'd6_r3_c3',
                'efeitos': {
                    'energia': -8,
                    'moral': -4,
                    'confianca': -1,
                },
                'itens_add': [],
            },
        ],
    },
    'd6_r3_c3': {
        'dia': 6,
        'titulo': 'DIA 6 - GARAGEM SUBTERRÂNEA: TANQUE CHEIO',
        'texto': 'Se o alarme é cortado, o painel mostra tanque cheio. A caminhonete pode romper o portão.',
        'cor_fundo': VERDE,
        'proxima': 'd6_r3_c4',
    },
    'd6_r3_c4': {
        'dia': 6,
        'titulo': 'DIA 6 - GARAGEM SUBTERRÂNEA: VAN DE SEGURANÇA',
        'texto': 'A van pertence a uma empresa de segurança privada. A porta traseira está travada.',
        'cor_fundo': VERDE,
        'opcoes': [
            {
                'texto': 'Usar pé de cabra.',
                'resultado': 'A decisão leva ao próximo momento: Colete Balístico.',
                'proxima': 'd6_r3_c5',
                'efeitos': {
                    'energia': -4,
                },
                'itens_add': ['pé de cabra'],
            },
            {
                'texto': 'Procurar chaves no chão.',
                'resultado': 'A escolha cobra seu preço antes que exista tempo para voltar atrás.',
                'final': {
                    'tipo': 'derrota',
                    'titulo': 'MORTE 1',
                    'texto': (
                        'Procurar chaves no chão; um infectado escondido debaixo da van puxa a perna do '
                        'personagem.'
                    ),
                },
                'efeitos': {
                    'vida': -100,
                },
                'qualidade': 'morte',
            },
        ],
    },
    'd6_r3_c5': {
        'dia': 6,
        'titulo': 'DIA 6 - GARAGEM SUBTERRÂNEA: COLETE BALÍSTICO',
        'texto': (
            'Dentro da van há água e um colete balístico. O item pode anular um tiro ou impacto no '
            'Dia 7.'
        ),
        'cor_fundo': VERDE,
        'proxima': 'd6_r3_c6',
    },
    'd6_r3_c6': {
        'dia': 6,
        'titulo': 'DIA 6 - GARAGEM SUBTERRÂNEA: ESCADA CORTA-FOGO',
        'texto': 'Se abandonar o carro, o personagem sobe a escada perseguido e fecha a porta atrás de si.',
        'cor_fundo': VERDE,
        'opcoes': [
            {
                'texto': 'Trancar a porta com corrente.',
                'resultado': 'A escolha cobra seu preço antes que exista tempo para voltar atrás.',
                'final': {
                    'tipo': 'derrota',
                    'titulo': 'MORTE 2',
                    'texto': 'Não travar a porta corta-fogo; infectados alcançam a escada antes da saída.',
                },
                'efeitos': {
                    'vida': -100,
                },
                'qualidade': 'morte',
            },
            {
                'texto': 'Continuar correndo sem travar nada.',
                'resultado': 'A decisão leva ao próximo momento: Portão da Garagem.',
                'proxima': 'd6_r3_c7',
                'efeitos': {
                    'energia': -4,
                },
                'itens_add': [],
            },
        ],
    },
    'd6_r3_c7': {
        'dia': 6,
        'titulo': 'DIA 6 - GARAGEM SUBTERRÂNEA: PORTÃO DA GARAGEM',
        'texto': (
            'A caminhonete acelera contra o portão. Metal se dobra, vidro estilhaça e a rua aparece '
            'além da fumaça.'
        ),
        'cor_fundo': VERDE,
        'opcoes': [
            {
                'texto': 'Acelerar para a avenida.',
                'resultado': 'A decisão leva ao próximo momento: Guarita Abandonada.',
                'proxima': 'd6_r3_c8',
                'efeitos': {
                    'energia': -4,
                },
                'itens_add': ['caminhonete'],
            },
            {
                'texto': 'Sair devagar para não chamar atenção.',
                'resultado': 'A decisão leva ao próximo momento: Guarita Abandonada.',
                'proxima': 'd6_r3_c8',
                'efeitos': {
                    'energia': -4,
                },
                'itens_add': ['caminhonete'],
            },
        ],
    },
    'd6_r3_c8': {
        'dia': 6,
        'titulo': 'DIA 6 - GARAGEM SUBTERRÂNEA: GUARITA ABANDONADA',
        'texto': (
            'O personagem encontra uma guarita de segurança. De lá, vê holofotes do estádio acendendo '
            'ao longe.'
        ),
        'cor_fundo': VERDE,
        'proxima': 'd6_r3_c9',
    },
    'd6_r3_c9': {
        'dia': 6,
        'titulo': 'DIA 6 - GARAGEM SUBTERRÂNEA: NOITE ANTES DO RESGATE',
        'texto': (
            'Dentro da caminhonete ou trancado na guarita, ele entende que amanhã é tudo ou nada. O '
            'estádio fica a quatro quarteirões.'
        ),
        'cor_fundo': VERDE,
        'opcoes': [
            {
                'texto': 'FIM DO DIA 6 A',
                'resultado': 'Essa decisão encerra o caminho iniciado neste dia.',
                'proxima': 'd6_r3_fim_1',
                'efeitos': {
                    'energia': -4,
                },
                'qualidade': 'media',
            },
            {
                'texto': 'FIM DO DIA 6 B',
                'resultado': 'Essa decisão encerra o caminho iniciado neste dia.',
                'proxima': 'd6_r3_fim_2',
                'efeitos': {
                    'energia': -4,
                },
                'qualidade': 'media',
            },
        ],
    },
    'd6_r4_fim_1': {
        'dia': 6,
        'titulo': 'FIM DO DIA 6 A',
        'texto': 'Perto da base com comboio unido.',
        'cor_fundo': VERDE_CLARO,
        'fim_dia': True,
        'proxima_dia': 'd7_r4_inicio',
    },
    'd6_r4_fim_2': {
        'dia': 6,
        'titulo': 'FIM DO DIA 6 B',
        'texto': 'Perto da base com menos passageiros, mais combustível e moral abalada.',
        'cor_fundo': VERDE_CLARO,
        'fim_dia': True,
        'proxima_dia': 'd7_r4_inicio',
    },
    'd6_r4_c1': {
        'dia': 6,
        'titulo': 'DIA 6 - COMBOIO NA ESTRADA: RODOVIA CONGESTIONADA',
        'texto': (
            'O ônibus segue por rodovia cheia de veículos abandonados. A zona segura aparece no rádio '
            'como promessa distante.'
        ),
        'cor_fundo': VERDE,
        'opcoes': [
            {
                'texto': 'Parar para ajudar grupo na estrada.',
                'resultado': 'A decisão leva ao próximo momento: Combustível Acabando.',
                'proxima': 'd6_r4_c2',
                'efeitos': {
                    'energia': -4,
                    'moral': 5,
                    'confianca': 2,
                },
                'itens_add': ['rádio', 'ônibus'],
            },
            {
                'texto': 'Não parar por segurança.',
                'resultado': 'A decisão leva ao próximo momento: Combustível Acabando.',
                'proxima': 'd6_r4_c2',
                'efeitos': {
                    'energia': -4,
                },
                'itens_add': ['rádio', 'ônibus'],
            },
        ],
    },
    'd6_r4_c2': {
        'dia': 6,
        'titulo': 'DIA 6 - COMBOIO NA ESTRADA: COMBUSTÍVEL ACABANDO',
        'texto': 'O marcador está baixo. Se parar no lugar errado, todos ficarão presos.',
        'cor_fundo': VERDE,
        'opcoes': [
            {
                'texto': 'Procurar combustível.',
                'resultado': 'A decisão leva ao próximo momento: Bloqueio na Pista.',
                'proxima': 'd6_r4_c3',
                'efeitos': {
                    'energia': -4,
                    'comida': 1,
                    'agua': 1,
                },
                'itens_add': ['combustível'],
            },
            {
                'texto': 'Economizar desligando o motor por trechos.',
                'resultado': 'A decisão leva ao próximo momento: Bloqueio na Pista.',
                'proxima': 'd6_r4_c3',
                'efeitos': {
                    'energia': -4,
                },
                'itens_add': [],
            },
        ],
    },
    'd6_r4_c3': {
        'dia': 6,
        'titulo': 'DIA 6 - COMBOIO NA ESTRADA: BLOQUEIO NA PISTA',
        'texto': 'Carros batidos fecham passagem e infectados vagam entre veículos.',
        'cor_fundo': VERDE,
        'opcoes': [
            {
                'texto': 'Desviar pelo acostamento.',
                'resultado': 'A decisão leva ao próximo momento: Grupo na Estrada.',
                'proxima': 'd6_r4_c4',
                'efeitos': {
                    'energia': -4,
                },
                'itens_add': [],
            },
            {
                'texto': 'Forçar o ônibus pelo bloqueio.',
                'resultado': 'A escolha cobra seu preço antes que exista tempo para voltar atrás.',
                'final': {
                    'tipo': 'derrota',
                    'titulo': 'MORTE 2',
                    'texto': 'Acelerar demais no bloqueio; o ônibus quebra e a horda alcança todos.',
                },
                'efeitos': {
                    'vida': -100,
                },
                'qualidade': 'morte',
            },
        ],
    },
    'd6_r4_c4': {
        'dia': 6,
        'titulo': 'DIA 6 - COMBOIO NA ESTRADA: GRUPO NA ESTRADA',
        'texto': (
            'Os desconhecidos pedem água e lugar no comboio. Alguns parecem saudáveis; outros '
            'escondem ferimentos.'
        ),
        'cor_fundo': VERDE,
        'proxima': 'd6_r4_c5',
    },
    'd6_r4_c5': {
        'dia': 6,
        'titulo': 'DIA 6 - COMBOIO NA ESTRADA: HELENA E JONAS DISCORDAM',
        'texto': (
            'Helena quer triagem rápida. Jonas quer abandonar todos. A discussão ameaça dividir o '
            'ônibus.'
        ),
        'cor_fundo': VERDE,
        'opcoes': [
            {
                'texto': 'Unir grupo com triagem simples.',
                'resultado': 'A decisão leva ao próximo momento: Infectados entre Veículos.',
                'proxima': 'd6_r4_c6',
                'efeitos': {
                    'energia': -4,
                    'moral': 5,
                    'confianca': 2,
                },
                'itens_add': ['ônibus', 'aliado Lena', 'aliado Helena', 'aliado Jonas'],
            },
            {
                'texto': 'Deixar Jonas decidir.',
                'resultado': 'A escolha cobra seu preço antes que exista tempo para voltar atrás.',
                'final': {
                    'tipo': 'derrota',
                    'titulo': 'MORTE 1',
                    'texto': (
                        'Deixar Jonas decidir; ele abandona feridos que bloqueiam a estrada, gerando confronto e '
                        'morte do personagem.'
                    ),
                },
                'efeitos': {
                    'vida': -100,
                },
                'qualidade': 'morte',
            },
        ],
    },
    'd6_r4_c6': {
        'dia': 6,
        'titulo': 'DIA 6 - COMBOIO NA ESTRADA: INFECTADOS ENTRE VEÍCULOS',
        'texto': 'Enquanto reorganizam o comboio, infectados surgem entre caminhões abandonados.',
        'cor_fundo': VERDE,
        'proxima': 'd6_r4_c7',
    },
    'd6_r4_c7': {
        'dia': 6,
        'titulo': 'DIA 6 - COMBOIO NA ESTRADA: ABRINDO CAMINHO',
        'texto': 'O ônibus força passagem pelo acostamento, desviando de placas caídas.',
        'cor_fundo': VERDE,
        'opcoes': [
            {
                'texto': 'Manter velocidade baixa.',
                'resultado': 'A decisão leva ao próximo momento: Base no Rádio.',
                'proxima': 'd6_r4_c8',
                'efeitos': {
                    'energia': -4,
                },
                'itens_add': ['ônibus'],
            },
            {
                'texto': 'Acelerar e arriscar quebrar motor.',
                'resultado': 'A decisão leva ao próximo momento: Base no Rádio.',
                'proxima': 'd6_r4_c8',
                'efeitos': {
                    'energia': -4,
                },
                'itens_add': ['ônibus'],
            },
        ],
    },
    'd6_r4_c8': {
        'dia': 6,
        'titulo': 'DIA 6 - COMBOIO NA ESTRADA: BASE NO RÁDIO',
        'texto': (
            'A mensagem fica clara: a base ainda recebe sobreviventes, mas portões podem fechar a '
            'qualquer momento.'
        ),
        'cor_fundo': VERDE,
        'proxima': 'd6_r4_c9',
    },
    'd6_r4_c9': {
        'dia': 6,
        'titulo': 'DIA 6 - COMBOIO NA ESTRADA: ACAMPAMENTO PERTO DA RODOVIA',
        'texto': (
            'O comboio para em área afastada. Luzes da base aparecem no horizonte, junto com tiros e '
            'helicópteros.'
        ),
        'cor_fundo': VERDE,
        'opcoes': [
            {
                'texto': 'FIM DO DIA 6 A',
                'resultado': 'Essa decisão encerra o caminho iniciado neste dia.',
                'proxima': 'd6_r4_fim_1',
                'efeitos': {
                    'energia': -4,
                },
                'qualidade': 'media',
            },
            {
                'texto': 'FIM DO DIA 6 B',
                'resultado': 'Essa decisão encerra o caminho iniciado neste dia.',
                'proxima': 'd6_r4_fim_2',
                'efeitos': {
                    'energia': -4,
                },
                'qualidade': 'media',
            },
        ],
    },
    'd7_r1_fim_1': {
        'dia': 7,
        'titulo': 'FIM DO DIA 7',
        'texto': 'Final Lobo Solitário — sobrevive, mas abandona o grupo e escolhe a solidão.',
        'tipo': 'vitoria',
        'final_jogo': True,
        'cor_fundo': VERDE_CLARO,
    },
    'd7_r1_c1': {
        'dia': 7,
        'titulo': 'DIA 7 - O PESO DA SOBREVIVÊNCIA / LOBO SOLITÁRIO: TRIAGEM HOSTIL',
        'texto': (
            'Soldados revistam o grupo violentamente. A diretora tenta explicar que há crianças, mas '
            'é silenciada. O comandante trata todos como ameaça infecciosa.'
        ),
        'cor_fundo': VERDE,
        'opcoes': [
            {
                'texto': 'Acalmar a diretora.',
                'resultado': 'A decisão leva ao próximo momento: Cela de Quarentena.',
                'proxima': 'd7_r1_c2',
                'efeitos': {
                    'energia': -4,
                    'moral': 5,
                    'confianca': 2,
                },
                'itens_add': ['aliado diretora'],
            },
            {
                'texto': 'Ficar em silêncio.',
                'resultado': 'A decisão leva ao próximo momento: Cela de Quarentena.',
                'proxima': 'd7_r1_c2',
                'efeitos': {
                    'energia': -4,
                },
                'itens_add': ['aliado diretora'],
            },
            {
                'texto': 'Questionar o comandante.',
                'resultado': 'A escolha cobra seu preço antes que exista tempo para voltar atrás.',
                'final': {
                    'tipo': 'derrota',
                    'titulo': 'MORTE 1',
                    'texto': 'Questionar o comandante agressivamente; soldados o consideram ameaça e disparam.',
                },
                'efeitos': {
                    'vida': -100,
                },
                'qualidade': 'morte',
            },
        ],
    },
    'd7_r1_c2': {
        'dia': 7,
        'titulo': 'DIA 7 - O PESO DA SOBREVIVÊNCIA / LOBO SOLITÁRIO: CELA DE QUARENTENA',
        'texto': (
            'O grupo seria levado para uma área externa desprotegida. Se a horda voltar, morrerão do '
            'lado de fora dos muros.'
        ),
        'cor_fundo': VERDE,
        'proxima': 'd7_r1_c3',
    },
    'd7_r1_c3': {
        'dia': 7,
        'titulo': 'DIA 7 - O PESO DA SOBREVIVÊNCIA / LOBO SOLITÁRIO: AJUDA INESPERADA',
        'texto': (
            'Gritos vêm de dentro: Joice e Pedro estão vivos. Eles chegaram à base no Dia 6 após se '
            'separarem na confusão da escola.'
        ),
        'cor_fundo': VERDE,
        'opcoes': [
            {
                'texto': 'Confirmar a história deles.',
                'resultado': 'A decisão leva ao próximo momento: Portão Interno.',
                'proxima': 'd7_r1_c4',
                'efeitos': {
                    'energia': -4,
                },
                'itens_add': ['aliado Pedro', 'aliado Joice'],
            },
            {
                'texto': 'Fingir que não os conhece.',
                'resultado': 'A decisão leva ao próximo momento: Portão Interno.',
                'proxima': 'd7_r1_c4',
                'efeitos': {
                    'energia': -4,
                },
                'itens_add': ['aliado Pedro', 'aliado Joice'],
            },
        ],
    },
    'd7_r1_c4': {
        'dia': 7,
        'titulo': 'DIA 7 - O PESO DA SOBREVIVÊNCIA / LOBO SOLITÁRIO: PORTÃO INTERNO',
        'texto': (
            'Com relutância, o comandante permite triagem médica final. Joice e Pedro salvam o grupo '
            'como o grupo tentou salvá-los antes.'
        ),
        'cor_fundo': VERDE,
        'proxima': 'd7_r1_c5',
    },
    'd7_r1_c5': {
        'dia': 7,
        'titulo': 'DIA 7 - O PESO DA SOBREVIVÊNCIA / LOBO SOLITÁRIO: ROSTOS DO PASSADO',
        'texto': (
            'Na tenda principal, o personagem vê Ana, Sofia e Luís, família de Jorge, o amigo morto '
            'no Dia 1.'
        ),
        'cor_fundo': VERDE,
        'opcoes': [
            {
                'texto': 'Desviar o olhar.',
                'resultado': 'A decisão leva ao próximo momento: Pergunta de Ana.',
                'proxima': 'd7_r1_c6',
                'efeitos': {
                    'energia': -4,
                },
                'itens_add': ['aliado Jorge', 'aliado Ana', 'aliado Sofia', 'aliado Luís'],
            },
            {
                'texto': 'Acenar de longe.',
                'resultado': 'A decisão leva ao próximo momento: Pergunta de Ana.',
                'proxima': 'd7_r1_c6',
                'efeitos': {
                    'energia': -4,
                },
                'itens_add': ['aliado Jorge', 'aliado Ana', 'aliado Sofia', 'aliado Luís'],
            },
            {
                'texto': 'Ir até eles.',
                'resultado': 'A decisão leva ao próximo momento: Pergunta de Ana.',
                'proxima': 'd7_r1_c6',
                'efeitos': {
                    'energia': -4,
                },
                'itens_add': ['aliado Jorge', 'aliado Ana', 'aliado Sofia', 'aliado Luís'],
            },
        ],
    },
    'd7_r1_c6': {
        'dia': 7,
        'titulo': 'DIA 7 - O PESO DA SOBREVIVÊNCIA / LOBO SOLITÁRIO: PERGUNTA DE ANA',
        'texto': (
            'Ana pergunta se Jorge conseguiu sair da cidade. O personagem vê novamente o amigo sendo '
            'devorado.'
        ),
        'cor_fundo': VERDE,
        'opcoes': [
            {
                'texto': 'Contar a verdade completa.',
                'resultado': 'A escolha cobra seu preço antes que exista tempo para voltar atrás.',
                'final': {
                    'tipo': 'derrota',
                    'titulo': 'MORTE 2',
                    'texto': (
                        'Contar a verdade brutal sobre Jorge diante da família; Ana entra em pânico, atrai '
                        'confusão na triagem e o grupo é expulso para a horda.'
                    ),
                },
                'efeitos': {
                    'vida': -100,
                },
                'qualidade': 'morte',
            },
            {
                'texto': 'Omitir detalhes cruéis.',
                'resultado': 'A decisão leva ao próximo momento: Peso dos Mortos.',
                'proxima': 'd7_r1_c7',
                'efeitos': {
                    'energia': -4,
                },
                'itens_add': ['aliado Jorge', 'aliado Ana'],
            },
        ],
    },
    'd7_r1_c7': {
        'dia': 7,
        'titulo': 'DIA 7 - O PESO DA SOBREVIVÊNCIA / LOBO SOLITÁRIO: PESO DOS MORTOS',
        'texto': (
            'À noite, ele vê Lena e Davi dormindo, a diretora ajudando crianças e Joice abraçando '
            'Pedro. Todos estão vivos, mas a lembrança dos que morreram grita mais alto.'
        ),
        'cor_fundo': VERDE,
        'proxima': 'd7_r1_c8',
    },
    'd7_r1_c8': {
        'dia': 7,
        'titulo': 'DIA 7 - O PESO DA SOBREVIVÊNCIA / LOBO SOLITÁRIO: DECISÃO',
        'texto': (
            'O personagem percebe que não suportará perder mais ninguém. Laços se tornaram peso, e o '
            'peso virou medo.'
        ),
        'cor_fundo': VERDE,
        'opcoes': [
            {
                'texto': 'Afastar-se do grupo em silêncio.',
                'resultado': 'A decisão leva ao próximo momento: Suprimentos Finais.',
                'proxima': 'd7_r1_c9',
                'efeitos': {
                    'energia': -4,
                },
                'itens_add': [],
            },
            {
                'texto': 'Ficar com o grupo.',
                'resultado': 'A decisão leva ao próximo momento: Suprimentos Finais.',
                'proxima': 'd7_r1_c9',
                'efeitos': {
                    'energia': -4,
                },
                'itens_add': [],
            },
        ],
    },
    'd7_r1_c9': {
        'dia': 7,
        'titulo': 'DIA 7 - O PESO DA SOBREVIVÊNCIA / LOBO SOLITÁRIO: SUPRIMENTOS FINAIS',
        'texto': (
            'Ele prepara a mochila, confere o canivete e decide se deixará parte da comida para Lena '
            'e Davi.'
        ),
        'cor_fundo': VERDE,
        'opcoes': [
            {
                'texto': 'Deixar últimos suprimentos na tenda.',
                'resultado': 'A decisão leva ao próximo momento: Patrulha dos Fundos.',
                'proxima': 'd7_r1_c10',
                'efeitos': {
                    'energia': -4,
                    'comida': 1,
                    'agua': 1,
                },
                'itens_add': ['canivete', 'mochila', 'aliado Lena', 'aliado Davi'],
            },
            {
                'texto': 'Levar tudo consigo.',
                'resultado': 'A decisão leva ao próximo momento: Patrulha dos Fundos.',
                'proxima': 'd7_r1_c10',
                'efeitos': {
                    'energia': -4,
                },
                'itens_add': ['canivete', 'mochila', 'aliado Lena', 'aliado Davi'],
            },
        ],
    },
    'd7_r1_c10': {
        'dia': 7,
        'titulo': 'DIA 7 - O PESO DA SOBREVIVÊNCIA / LOBO SOLITÁRIO: PATRULHA DOS FUNDOS',
        'texto': (
            'Por ser calculista, observa a rota dos soldados no muro dos fundos, onde caixas vazias '
            'são descartadas.'
        ),
        'cor_fundo': VERDE,
        'opcoes': [
            {
                'texto': 'Esperar troca de turno.',
                'resultado': 'A decisão leva ao próximo momento: Fuga Silenciosa.',
                'proxima': 'd7_r1_c11',
                'efeitos': {
                    'energia': -4,
                },
                'itens_add': [],
            },
            {
                'texto': 'Correr imediatamente.',
                'resultado': 'A escolha cobra seu preço antes que exista tempo para voltar atrás.',
                'final': {
                    'tipo': 'derrota',
                    'titulo': 'MORTE 3',
                    'texto': 'Correr imediatamente durante a patrulha; o personagem é alvejado ao tentar pular o muro.',
                },
                'efeitos': {
                    'vida': -100,
                },
                'qualidade': 'morte',
            },
        ],
    },
    'd7_r1_c11': {
        'dia': 7,
        'titulo': 'DIA 7 - O PESO DA SOBREVIVÊNCIA / LOBO SOLITÁRIO: FUGA SILENCIOSA',
        'texto': (
            'Ele escala caixas e pula a cerca. Atrás, a base oferece segurança; à frente, a floresta '
            'oferece solidão.'
        ),
        'cor_fundo': VERDE,
        'proxima': 'd7_r1_c12',
    },
    'd7_r1_c12': {
        'dia': 7,
        'titulo': 'DIA 7 - O PESO DA SOBREVIVÊNCIA / LOBO SOLITÁRIO: ÚLTIMO OLHAR',
        'texto': (
            'Do lado de fora, ele vê holofotes varrendo a estrada e ouve tiros no portão principal. O '
            'mundo ainda está em guerra.'
        ),
        'cor_fundo': VERDE,
        'opcoes': [
            {
                'texto': 'Voltar para ajudar.',
                'resultado': 'A escolha cobra seu preço antes que exista tempo para voltar atrás.',
                'final': {
                    'tipo': 'derrota',
                    'titulo': 'MORTE 4',
                    'texto': 'Voltar para ajudar no portão principal sozinho; é cercado fora dos muros.',
                },
                'efeitos': {
                    'vida': -100,
                },
                'qualidade': 'morte',
            },
            {
                'texto': 'Continuar andando.',
                'resultado': 'A decisão leva ao próximo momento: A Floresta.',
                'proxima': 'd7_r1_c13',
                'efeitos': {
                    'energia': -4,
                },
                'itens_add': [],
            },
        ],
    },
    'd7_r1_c13': {
        'dia': 7,
        'titulo': 'DIA 7 - O PESO DA SOBREVIVÊNCIA / LOBO SOLITÁRIO: A FLORESTA',
        'texto': 'A mata engole os sons da base. Pela primeira vez em sete dias, ninguém chama seu nome.',
        'cor_fundo': VERDE,
        'proxima': 'd7_r1_c14',
    },
    'd7_r1_c14': {
        'dia': 7,
        'titulo': 'DIA 7 - O PESO DA SOBREVIVÊNCIA / LOBO SOLITÁRIO: FANTASMA',
        'texto': (
            'Ele entende que sobreviver sozinho evita novas culpas, mas também mata algo humano '
            'dentro dele.'
        ),
        'cor_fundo': VERDE,
        'proxima': 'd7_r1_c15',
    },
    'd7_r1_c15': {
        'dia': 7,
        'titulo': 'DIA 7 - O PESO DA SOBREVIVÊNCIA / LOBO SOLITÁRIO: LOBO SOLITÁRIO',
        'texto': (
            'O personagem desaparece na noite. Sem falhas, sem laços, sem dor compartilhada. Vivo, '
            'mas transformado pelo medo.'
        ),
        'cor_fundo': VERDE,
        'proxima': 'd7_r1_fim_1',
    },
    'd7_r2_fim_1': {
        'dia': 7,
        'titulo': 'FIM DO DIA 7',
        'texto': (
            'Final Sobrevivente — entra na base vivo, ferido emocionalmente, mas com chance de '
            'recomeço.'
        ),
        'tipo': 'vitoria',
        'final_jogo': True,
        'cor_fundo': VERDE_CLARO,
    },
    'd7_r2_c1': {
        'dia': 7,
        'titulo': 'DIA 7 - ENTRADA NA BASE / FINAL SOBREVIVENTE: ÚLTIMO TRECHO',
        'texto': (
            'O caminhão ou grupo a pé segue até a base. A estrada está cheia de sobreviventes, fumaça '
            'e soldados gritando ordens.'
        ),
        'cor_fundo': VERDE,
        'opcoes': [
            {
                'texto': 'Entrar na fila de triagem.',
                'resultado': 'A decisão leva ao próximo momento: Fila de Sobreviventes.',
                'proxima': 'd7_r2_c2',
                'efeitos': {
                    'energia': -4,
                    'moral': 5,
                    'confianca': 2,
                },
                'itens_add': ['caminhão'],
            },
            {
                'texto': 'Tentar cortar caminho pelos fundos.',
                'resultado': 'A escolha cobra seu preço antes que exista tempo para voltar atrás.',
                'final': {
                    'tipo': 'derrota',
                    'titulo': 'MORTE 1',
                    'texto': 'Tentar cortar caminho pelos fundos; minas e sentinelas impedem a entrada.',
                },
                'efeitos': {
                    'vida': -100,
                },
                'qualidade': 'morte',
            },
        ],
    },
    'd7_r2_c2': {
        'dia': 7,
        'titulo': 'DIA 7 - ENTRADA NA BASE / FINAL SOBREVIVENTE: FILA DE SOBREVIVENTES',
        'texto': (
            'Centenas esperam. Alguns rezam, outros escondem ferimentos. O grupo precisa manter '
            'calma.'
        ),
        'cor_fundo': VERDE,
        'opcoes': [
            {
                'texto': 'Manter posição na fila.',
                'resultado': 'A decisão leva ao próximo momento: Movimento Estranho.',
                'proxima': 'd7_r2_c3',
                'efeitos': {
                    'energia': -4,
                },
                'itens_add': [],
            },
            {
                'texto': 'Empurrar para avançar.',
                'resultado': 'A decisão leva ao próximo momento: Movimento Estranho.',
                'proxima': 'd7_r2_c3',
                'efeitos': {
                    'energia': -8,
                },
                'itens_add': [],
            },
        ],
    },
    'd7_r2_c3': {
        'dia': 7,
        'titulo': 'DIA 7 - ENTRADA NA BASE / FINAL SOBREVIVENTE: MOVIMENTO ESTRANHO',
        'texto': 'Um homem ferido treme perto das grades. Os olhos dele estão começando a mudar.',
        'cor_fundo': VERDE,
        'opcoes': [
            {
                'texto': 'Avisar os soldados.',
                'resultado': 'A decisão leva ao próximo momento: Triagem.',
                'proxima': 'd7_r2_c4',
                'efeitos': {
                    'energia': -4,
                    'moral': 5,
                    'confianca': 2,
                },
                'itens_add': [],
            },
            {
                'texto': 'Ignorar para não atrasar.',
                'resultado': 'A decisão leva ao próximo momento: Triagem.',
                'proxima': 'd7_r2_c4',
                'efeitos': {
                    'energia': -4,
                    'moral': -4,
                    'confianca': -1,
                },
                'itens_add': [],
            },
        ],
    },
    'd7_r2_c4': {
        'dia': 7,
        'titulo': 'DIA 7 - ENTRADA NA BASE / FINAL SOBREVIVENTE: TRIAGEM',
        'texto': (
            'Soldados medem febre, procuram mordidas e separam quem está instável. O processo é frio, '
            'mas impede desastre.'
        ),
        'cor_fundo': VERDE,
        'proxima': 'd7_r2_c5',
    },
    'd7_r2_c5': {
        'dia': 7,
        'titulo': 'DIA 7 - ENTRADA NA BASE / FINAL SOBREVIVENTE: HOMEM FERIDO',
        'texto': (
            'O homem da fila tenta atravessar escondido. O personagem nota sangue escorrendo por '
            'baixo da manga.'
        ),
        'cor_fundo': VERDE,
        'opcoes': [
            {
                'texto': 'Revelar ferimento.',
                'resultado': 'A escolha cobra seu preço antes que exista tempo para voltar atrás.',
                'final': {
                    'tipo': 'derrota',
                    'titulo': 'MORTE 2',
                    'texto': (
                        'Ajudar o homem mordido a esconder ferimento; ele se transforma dentro da fila e mata o '
                        'personagem.'
                    ),
                },
                'efeitos': {
                    'vida': -100,
                },
                'qualidade': 'morte',
            },
            {
                'texto': 'Ajudá-lo a esconder.',
                'resultado': 'A decisão leva ao próximo momento: Pânico na Fila.',
                'proxima': 'd7_r2_c6',
                'efeitos': {
                    'energia': -4,
                    'moral': -4,
                    'confianca': -1,
                },
                'itens_add': [],
            },
        ],
    },
    'd7_r2_c6': {
        'dia': 7,
        'titulo': 'DIA 7 - ENTRADA NA BASE / FINAL SOBREVIVENTE: PÂNICO NA FILA',
        'texto': (
            'A revelação causa gritos. O homem se transforma antes de ser retirado, mordendo um '
            'soldado.'
        ),
        'cor_fundo': VERDE,
        'opcoes': [
            {
                'texto': 'Ajudar a conter.',
                'resultado': 'A decisão leva ao próximo momento: A Horda.',
                'proxima': 'd7_r2_c7',
                'efeitos': {
                    'energia': -4,
                    'moral': 5,
                    'confianca': 2,
                },
                'itens_add': [],
            },
            {
                'texto': 'Correr para o portão.',
                'resultado': 'A decisão leva ao próximo momento: A Horda.',
                'proxima': 'd7_r2_c7',
                'efeitos': {
                    'energia': -8,
                },
                'itens_add': [],
            },
        ],
    },
    'd7_r2_c7': {
        'dia': 7,
        'titulo': 'DIA 7 - ENTRADA NA BASE / FINAL SOBREVIVENTE: A HORDA',
        'texto': 'O barulho atrai infectados da estrada. A fila se quebra em empurrões.',
        'cor_fundo': VERDE,
        'opcoes': [
            {
                'texto': 'Proteger o grupo.',
                'resultado': 'A decisão leva ao próximo momento: Criança Perdida.',
                'proxima': 'd7_r2_c8',
                'efeitos': {
                    'energia': -4,
                    'moral': 5,
                    'confianca': 2,
                },
                'itens_add': [],
            },
            {
                'texto': 'Correr sozinho.',
                'resultado': 'A escolha cobra seu preço antes que exista tempo para voltar atrás.',
                'final': {
                    'tipo': 'derrota',
                    'titulo': 'MORTE 3',
                    'texto': 'Correr sozinho durante pânico; o personagem é esmagado entre grades e multidão.',
                },
                'efeitos': {
                    'vida': -100,
                },
                'qualidade': 'morte',
            },
        ],
    },
    'd7_r2_c8': {
        'dia': 7,
        'titulo': 'DIA 7 - ENTRADA NA BASE / FINAL SOBREVIVENTE: CRIANÇA PERDIDA',
        'texto': 'Uma criança se separa da mãe perto de carros abandonados.',
        'cor_fundo': VERDE,
        'opcoes': [
            {
                'texto': 'Salvar a criança.',
                'resultado': 'A decisão leva ao próximo momento: Portão Secundário.',
                'proxima': 'd7_r2_c9',
                'efeitos': {
                    'energia': -4,
                    'moral': 5,
                    'confianca': 2,
                },
                'itens_add': [],
            },
            {
                'texto': 'Continuar para o portão.',
                'resultado': 'A decisão leva ao próximo momento: Portão Secundário.',
                'proxima': 'd7_r2_c9',
                'efeitos': {
                    'energia': -4,
                },
                'itens_add': [],
            },
        ],
    },
    'd7_r2_c9': {
        'dia': 7,
        'titulo': 'DIA 7 - ENTRADA NA BASE / FINAL SOBREVIVENTE: PORTÃO SECUNDÁRIO',
        'texto': (
            'Um soldado aponta para um portão menor. É caminho de emergência, mas pode fechar a '
            'qualquer momento.'
        ),
        'cor_fundo': VERDE,
        'opcoes': [
            {
                'texto': 'Seguir para o portão secundário.',
                'resultado': 'A decisão leva ao próximo momento: Última Corrida.',
                'proxima': 'd7_r2_c10',
                'efeitos': {
                    'energia': -4,
                },
                'itens_add': [],
            },
            {
                'texto': 'Ficar no principal.',
                'resultado': 'A escolha cobra seu preço antes que exista tempo para voltar atrás.',
                'final': {
                    'tipo': 'derrota',
                    'titulo': 'MORTE 4',
                    'texto': 'Ficar no portão principal; ele fecha antes do grupo atravessar e a horda chega.',
                },
                'efeitos': {
                    'vida': -100,
                },
                'qualidade': 'morte',
            },
        ],
    },
    'd7_r2_c10': {
        'dia': 7,
        'titulo': 'DIA 7 - ENTRADA NA BASE / FINAL SOBREVIVENTE: ÚLTIMA CORRIDA',
        'texto': 'O grupo corre enquanto tiros rasgam o ar acima. A horda está próxima.',
        'cor_fundo': VERDE,
        'proxima': 'd7_r2_c11',
    },
    'd7_r2_c11': {
        'dia': 7,
        'titulo': 'DIA 7 - ENTRADA NA BASE / FINAL SOBREVIVENTE: FECHANDO OS PORTÕES',
        'texto': 'Soldados começam a fechar o portão secundário. Ainda há sobreviventes fora.',
        'cor_fundo': VERDE,
        'opcoes': [
            {
                'texto': 'Entrar agora.',
                'resultado': 'A decisão leva ao próximo momento: O Impacto.',
                'proxima': 'd7_r2_c12',
                'efeitos': {
                    'energia': -4,
                },
                'itens_add': [],
            },
            {
                'texto': 'Segurar alguns segundos para o grupo passar.',
                'resultado': 'A decisão leva ao próximo momento: O Impacto.',
                'proxima': 'd7_r2_c12',
                'efeitos': {
                    'energia': -4,
                },
                'itens_add': [],
            },
        ],
    },
    'd7_r2_c12': {
        'dia': 7,
        'titulo': 'DIA 7 - ENTRADA NA BASE / FINAL SOBREVIVENTE: O IMPACTO',
        'texto': (
            'Infectados batem contra as grades no momento em que elas fecham. Dedos mortos atravessam '
            'vãos de metal.'
        ),
        'cor_fundo': VERDE,
        'proxima': 'd7_r2_c13',
    },
    'd7_r2_c13': {
        'dia': 7,
        'titulo': 'DIA 7 - ENTRADA NA BASE / FINAL SOBREVIVENTE: DENTRO DOS MUROS',
        'texto': 'O grupo entra exausto. Ninguém comemora; apenas respira.',
        'cor_fundo': VERDE,
        'proxima': 'd7_r2_c14',
    },
    'd7_r2_c14': {
        'dia': 7,
        'titulo': 'DIA 7 - ENTRADA NA BASE / FINAL SOBREVIVENTE: REENCONTROS',
        'texto': (
            'Na base, eles veem sobreviventes de outras rotas: um ônibus no pátio, feridos da escola '
            'e mensagens sobre helicópteros no estádio.'
        ),
        'cor_fundo': VERDE,
        'proxima': 'd7_r2_c15',
    },
    'd7_r2_c15': {
        'dia': 7,
        'titulo': 'DIA 7 - ENTRADA NA BASE / FINAL SOBREVIVENTE: NOVO COMEÇO',
        'texto': (
            'O personagem recebe uma manta e um copo de água. Ele não salvou todos, mas chegou. Isso '
            'basta para continuar vivo.'
        ),
        'cor_fundo': VERDE,
        'proxima': 'd7_r2_fim_1',
    },
    'd7_r3_fim_1': {
        'dia': 7,
        'titulo': 'FIM DO DIA 7',
        'texto': (
            'Final Sobrevivente Preparado — embarca no helicóptero do estádio, vivo graças aos itens '
            'raros e decisões cautelosas.'
        ),
        'tipo': 'vitoria',
        'final_jogo': True,
        'cor_fundo': VERDE_CLARO,
    },
    'd7_r3_c1': {
        'dia': 7,
        'titulo': 'DIA 7 - A CORRIDA FINAL / ESTÁDIO: AVENIDA PRINCIPAL',
        'texto': (
            'O estádio fica a quatro quarteirões. A avenida direta está tomada por horda. Há becos, '
            'galerias de esgoto e, se obtida, a caminhonete.'
        ),
        'cor_fundo': VERDE,
        'opcoes': [
            {
                'texto': 'Entrar no esgoto.',
                'resultado': 'A decisão leva ao próximo momento: Galeria de Esgoto.',
                'proxima': 'd7_r3_c2',
                'efeitos': {
                    'energia': -4,
                },
                'itens_add': ['caminhonete'],
            },
            {
                'texto': 'Seguir pelos becos.',
                'resultado': 'A decisão leva ao próximo momento: Galeria de Esgoto.',
                'proxima': 'd7_r3_c2',
                'efeitos': {
                    'energia': -4,
                },
                'itens_add': ['caminhonete'],
            },
            {
                'texto': 'Usar caminhonete.',
                'resultado': 'A decisão leva ao próximo momento: Galeria de Esgoto.',
                'proxima': 'd7_r3_c2',
                'efeitos': {
                    'energia': -4,
                },
                'itens_add': ['caminhonete'],
            },
        ],
    },
    'd7_r3_c2': {
        'dia': 7,
        'titulo': 'DIA 7 - A CORRIDA FINAL / ESTÁDIO: GALERIA DE ESGOTO',
        'texto': (
            'O esgoto é escuro, contaminado e abafado. A lanterna e pastilhas de cloro podem impedir '
            'que o caminho vire sentença de morte.'
        ),
        'cor_fundo': VERDE,
        'opcoes': [
            {
                'texto': 'Usar lanterna e purificador.',
                'resultado': 'A escolha cobra seu preço antes que exista tempo para voltar atrás.',
                'final': {
                    'tipo': 'derrota',
                    'titulo': 'MORTE 1',
                    'texto': 'Avançar no esgoto sem lanterna e purificador; perde-se e morre por infecção e exaustão.',
                },
                'efeitos': {
                    'vida': -100,
                },
                'qualidade': 'morte',
            },
            {
                'texto': 'Avançar sem itens.',
                'resultado': 'A decisão leva ao próximo momento: Becos da Avenida.',
                'proxima': 'd7_r3_c3',
                'efeitos': {
                    'energia': -8,
                },
                'itens_add': ['lanterna'],
            },
        ],
    },
    'd7_r3_c3': {
        'dia': 7,
        'titulo': 'DIA 7 - A CORRIDA FINAL / ESTÁDIO: BECOS DA AVENIDA',
        'texto': (
            'Os becos evitam a horda, mas um grupo de saqueadores bloqueia passagem. Eles atiram '
            'antes de perguntar.'
        ),
        'cor_fundo': VERDE,
        'opcoes': [
            {
                'texto': 'Avançar com colete.',
                'resultado': 'A decisão leva ao próximo momento: Caminhonete.',
                'proxima': 'd7_r3_c4',
                'efeitos': {
                    'energia': -8,
                },
                'itens_add': ['colete balístico'],
            },
            {
                'texto': 'Tentar negociar.',
                'resultado': 'A escolha cobra seu preço antes que exista tempo para voltar atrás.',
                'final': {
                    'tipo': 'derrota',
                    'titulo': 'MORTE 2',
                    'texto': 'Tentar negociar com saqueadores nos becos; é baleado antes de terminar a frase.',
                },
                'efeitos': {
                    'vida': -100,
                },
                'qualidade': 'morte',
            },
        ],
    },
    'd7_r3_c4': {
        'dia': 7,
        'titulo': 'DIA 7 - A CORRIDA FINAL / ESTÁDIO: CAMINHONETE',
        'texto': (
            'A caminhonete atropela os primeiros infectados, mas o impacto destrói para-choque e '
            'motor. O estádio ainda está longe demais para relaxar.'
        ),
        'cor_fundo': VERDE,
        'opcoes': [
            {
                'texto': 'Acelerar até a rampa.',
                'resultado': 'A decisão leva ao próximo momento: Estacionamento Interno.',
                'proxima': 'd7_r3_c5',
                'efeitos': {
                    'energia': -4,
                },
                'itens_add': ['caminhonete'],
            },
            {
                'texto': 'Abandonar veículo antes do impacto.',
                'resultado': 'A decisão leva ao próximo momento: Estacionamento Interno.',
                'proxima': 'd7_r3_c5',
                'efeitos': {
                    'energia': -4,
                    'moral': -4,
                    'confianca': -1,
                },
                'itens_add': ['caminhonete'],
            },
        ],
    },
    'd7_r3_c5': {
        'dia': 7,
        'titulo': 'DIA 7 - A CORRIDA FINAL / ESTÁDIO: ESTACIONAMENTO INTERNO',
        'texto': (
            'Quem sai pelo esgoto chega ao estacionamento interno. Soldados correm para evacuar civis '
            'e gritam que o último helicóptero partirá em minutos.'
        ),
        'cor_fundo': VERDE,
        'proxima': 'd7_r3_c6',
    },
    'd7_r3_c6': {
        'dia': 7,
        'titulo': 'DIA 7 - A CORRIDA FINAL / ESTÁDIO: GRADE DO ESTÁDIO',
        'texto': (
            'Quem vem pelos becos precisa escalar uma grade alta. O colete, se usado, já pode estar '
            'destruído por tiros.'
        ),
        'cor_fundo': VERDE,
        'opcoes': [
            {
                'texto': 'Escalar imediatamente.',
                'resultado': 'A decisão leva ao próximo momento: Rampa de Acesso.',
                'proxima': 'd7_r3_c7',
                'efeitos': {
                    'energia': -4,
                },
                'itens_add': ['colete balístico'],
            },
            {
                'texto': 'Procurar portão aberto.',
                'resultado': 'A decisão leva ao próximo momento: Rampa de Acesso.',
                'proxima': 'd7_r3_c7',
                'efeitos': {
                    'energia': -4,
                    'comida': 1,
                    'agua': 1,
                },
                'itens_add': ['colete balístico'],
            },
        ],
    },
    'd7_r3_c7': {
        'dia': 7,
        'titulo': 'DIA 7 - A CORRIDA FINAL / ESTÁDIO: RAMPA DE ACESSO',
        'texto': (
            'Quem chega de caminhonete bate na rampa. Vidros explodem, o personagem perde fôlego e '
            'precisa sair antes que infectados alcancem o carro.'
        ),
        'cor_fundo': VERDE,
        'opcoes': [
            {
                'texto': 'Correr ferido.',
                'resultado': 'A decisão leva ao próximo momento: Triagem Rápida.',
                'proxima': 'd7_r3_c8',
                'efeitos': {
                    'energia': -8,
                },
                'itens_add': ['caminhonete'],
            },
            {
                'texto': 'Procurar mochila no banco traseiro.',
                'resultado': 'A escolha cobra seu preço antes que exista tempo para voltar atrás.',
                'final': {
                    'tipo': 'derrota',
                    'titulo': 'MORTE 3',
                    'texto': 'Procurar mochila após batida da caminhonete; infectados alcançam a rampa.',
                },
                'efeitos': {
                    'vida': -100,
                },
                'qualidade': 'morte',
            },
        ],
    },
    'd7_r3_c8': {
        'dia': 7,
        'titulo': 'DIA 7 - A CORRIDA FINAL / ESTÁDIO: TRIAGEM RÁPIDA',
        'texto': (
            'Soldados procuram mordidas. O personagem mostra ferimentos, itens e coordenadas '
            'anotadas. O preparo prova que ele não chegou por acaso.'
        ),
        'cor_fundo': VERDE,
        'opcoes': [
            {
                'texto': 'Cooperar com soldados.',
                'resultado': 'A decisão leva ao próximo momento: Último Helicóptero.',
                'proxima': 'd7_r3_c9',
                'efeitos': {
                    'energia': -4,
                    'moral': 5,
                    'confianca': 2,
                },
                'itens_add': ['coordenadas'],
            },
            {
                'texto': 'Mentir sobre ferimentos.',
                'resultado': 'A escolha cobra seu preço antes que exista tempo para voltar atrás.',
                'final': {
                    'tipo': 'derrota',
                    'titulo': 'MORTE 4',
                    'texto': (
                        'Mentir sobre ferimentos na triagem; soldados descobrem e o retiram da fila quando a '
                        'horda invade.'
                    ),
                },
                'efeitos': {
                    'vida': -100,
                },
                'qualidade': 'morte',
            },
        ],
    },
    'd7_r3_c9': {
        'dia': 7,
        'titulo': 'DIA 7 - A CORRIDA FINAL / ESTÁDIO: ÚLTIMO HELICÓPTERO',
        'texto': (
            'O rotor levanta poeira e gritos. Civis empurram, soldados selecionam por ordem de '
            'chegada e condição física.'
        ),
        'cor_fundo': VERDE,
        'opcoes': [
            {
                'texto': 'Entrar quando chamado.',
                'resultado': 'A decisão leva ao próximo momento: Saqueadores no Portão.',
                'proxima': 'd7_r3_c10',
                'efeitos': {
                    'energia': -4,
                },
                'itens_add': [],
            },
            {
                'texto': 'Voltar para buscar desconhecido.',
                'resultado': 'A decisão leva ao próximo momento: Saqueadores no Portão.',
                'proxima': 'd7_r3_c10',
                'efeitos': {
                    'energia': -4,
                },
                'itens_add': [],
            },
        ],
    },
    'd7_r3_c10': {
        'dia': 7,
        'titulo': 'DIA 7 - A CORRIDA FINAL / ESTÁDIO: SAQUEADORES NO PORTÃO',
        'texto': (
            'Saqueadores tentam invadir atrás dos sobreviventes. Eles vêm da mesma lógica brutal '
            'vista no posto e na escola.'
        ),
        'cor_fundo': VERDE,
        'opcoes': [
            {
                'texto': 'Abaixar e seguir ordens.',
                'resultado': 'A decisão leva ao próximo momento: Horda no Gramado.',
                'proxima': 'd7_r3_c11',
                'efeitos': {
                    'energia': -4,
                },
                'itens_add': [],
            },
            {
                'texto': 'Tentar enfrentá-los.',
                'resultado': 'A decisão leva ao próximo momento: Horda no Gramado.',
                'proxima': 'd7_r3_c11',
                'efeitos': {
                    'energia': -4,
                },
                'itens_add': [],
            },
        ],
    },
    'd7_r3_c11': {
        'dia': 7,
        'titulo': 'DIA 7 - A CORRIDA FINAL / ESTÁDIO: HORDA NO GRAMADO',
        'texto': (
            'Infectados entram por um portão lateral quebrado. O estádio inteiro treme com a massa de '
            'corpos.'
        ),
        'cor_fundo': VERDE,
        'proxima': 'd7_r3_c12',
    },
    'd7_r3_c12': {
        'dia': 7,
        'titulo': 'DIA 7 - A CORRIDA FINAL / ESTÁDIO: CORREDOR DOS VESTIÁRIOS',
        'texto': (
            'O personagem é guiado por vestiários até a área de pouso. As paredes exibem cartazes '
            'antigos de jogos, agora manchados de sangue.'
        ),
        'cor_fundo': VERDE,
        'proxima': 'd7_r3_c13',
    },
    'd7_r3_c13': {
        'dia': 7,
        'titulo': 'DIA 7 - A CORRIDA FINAL / ESTÁDIO: ESCOLHA DE PESO',
        'texto': (
            'Um soldado pergunta se ele tem alguém para declarar como família. O personagem, sozinho '
            'há sete dias, percebe que preparo salvou sua vida, mas não criou laços.'
        ),
        'cor_fundo': VERDE,
        'opcoes': [
            {
                'texto': 'Declarar que está sozinho.',
                'resultado': 'A decisão leva ao próximo momento: Decolagem.',
                'proxima': 'd7_r3_c14',
                'efeitos': {
                    'energia': -4,
                    'moral': -4,
                    'confianca': -1,
                },
                'itens_add': [],
            },
            {
                'texto': 'Procurar nomes nos registros.',
                'resultado': 'A decisão leva ao próximo momento: Decolagem.',
                'proxima': 'd7_r3_c14',
                'efeitos': {
                    'energia': -4,
                    'comida': 1,
                    'agua': 1,
                },
                'itens_add': [],
            },
        ],
    },
    'd7_r3_c14': {
        'dia': 7,
        'titulo': 'DIA 7 - A CORRIDA FINAL / ESTÁDIO: DECOLAGEM',
        'texto': (
            'O helicóptero sobe. Pela janela, a cidade parece uma ferida aberta. O prédio onde tudo '
            'começou é apenas uma mancha de fumaça.'
        ),
        'cor_fundo': VERDE,
        'proxima': 'd7_r3_c15',
    },
    'd7_r3_c15': {
        'dia': 7,
        'titulo': 'DIA 7 - A CORRIDA FINAL / ESTÁDIO: SOBREVIVENTE PREPARADO',
        'texto': (
            'O personagem alcança a evacuação por ter administrado recursos, itens raros e riscos. '
            'Ele não foi o mais heroico, nem o mais frio. Foi o mais preparado.'
        ),
        'cor_fundo': VERDE,
        'proxima': 'd7_r3_fim_1',
    },
    'd7_r4_fim_1': {
        'dia': 7,
        'titulo': 'FIM DO DIA 7',
        'texto': (
            'Final Heroico — o personagem entra na zona segura com o grupo e salva dezenas de '
            'pessoas.'
        ),
        'tipo': 'vitoria',
        'final_jogo': True,
        'cor_fundo': VERDE_CLARO,
    },
    'd7_r4_c1': {
        'dia': 7,
        'titulo': (
            'DIA 7 - SALVAR SOBREVIVENTES FORA DO PORTÃO / FINAL HEROICO: PESSOAS PRESAS FORA DO '
            'PORTÃO'
        ),
        'texto': (
            'A base está cercada por filas e soldados. Sobreviventes gritam do lado de fora enquanto '
            'a horda aparece na estrada.'
        ),
        'cor_fundo': VERDE,
        'opcoes': [
            {
                'texto': 'Salvar criança primeiro.',
                'resultado': 'A decisão leva ao próximo momento: Criança, Ferido e Aliado.',
                'proxima': 'd7_r4_c2',
                'efeitos': {
                    'energia': -4,
                    'moral': 5,
                    'confianca': 2,
                },
                'itens_add': [],
            },
            {
                'texto': 'Entrar na base com o grupo.',
                'resultado': 'A decisão leva ao próximo momento: Criança, Ferido e Aliado.',
                'proxima': 'd7_r4_c2',
                'efeitos': {
                    'energia': -4,
                },
                'itens_add': [],
            },
        ],
    },
    'd7_r4_c2': {
        'dia': 7,
        'titulo': 'DIA 7 - SALVAR SOBREVIVENTES FORA DO PORTÃO / FINAL HEROICO: CRIANÇA, FERIDO E ALIADO',
        'texto': (
            'Entre carros e barricadas há uma criança, um ferido e um aliado do comboio cercados. O '
            'portão principal não abrirá para eles.'
        ),
        'cor_fundo': VERDE,
        'proxima': 'd7_r4_c3',
    },
    'd7_r4_c3': {
        'dia': 7,
        'titulo': 'DIA 7 - SALVAR SOBREVIVENTES FORA DO PORTÃO / FINAL HEROICO: PORTÃO LATERAL',
        'texto': (
            'Um portão lateral pode ser aberto manualmente por uma guarita exposta. O caminho passa '
            'perto em excesso da horda.'
        ),
        'cor_fundo': VERDE,
        'opcoes': [
            {
                'texto': 'Abrir portão lateral.',
                'resultado': 'A decisão leva ao próximo momento: Guarita Exposta.',
                'proxima': 'd7_r4_c4',
                'efeitos': {
                    'energia': -4,
                },
                'itens_add': [],
            },
            {
                'texto': 'Esperar ordem dos soldados.',
                'resultado': 'A escolha cobra seu preço antes que exista tempo para voltar atrás.',
                'final': {
                    'tipo': 'derrota',
                    'titulo': 'MORTE 1',
                    'texto': 'Esperar ordem dos soldados; a horda chega antes do portão lateral abrir.',
                },
                'efeitos': {
                    'vida': -100,
                },
                'qualidade': 'morte',
            },
        ],
    },
    'd7_r4_c4': {
        'dia': 7,
        'titulo': 'DIA 7 - SALVAR SOBREVIVENTES FORA DO PORTÃO / FINAL HEROICO: GUARITA EXPOSTA',
        'texto': (
            'O mecanismo funciona, mas precisa ser puxado e mantido. O personagem não consegue fazer '
            'tudo sozinho.'
        ),
        'cor_fundo': VERDE,
        'opcoes': [
            {
                'texto': 'Pedir ajuda.',
                'resultado': 'A decisão leva ao próximo momento: Horda se Aproxima.',
                'proxima': 'd7_r4_c5',
                'efeitos': {
                    'energia': -4,
                },
                'itens_add': [],
            },
            {
                'texto': 'Tentar sozinho.',
                'resultado': 'A escolha cobra seu preço antes que exista tempo para voltar atrás.',
                'final': {
                    'tipo': 'derrota',
                    'titulo': 'MORTE 2',
                    'texto': 'Tentar operar a guarita sozinho; infectados o alcançam antes da cobertura chegar.',
                },
                'efeitos': {
                    'vida': -100,
                },
                'qualidade': 'morte',
            },
        ],
    },
    'd7_r4_c5': {
        'dia': 7,
        'titulo': 'DIA 7 - SALVAR SOBREVIVENTES FORA DO PORTÃO / FINAL HEROICO: HORDA SE APROXIMA',
        'texto': (
            'A horda desce como maré de corpos. Soldados gritam, civis empurram e o portão principal '
            'fecha.'
        ),
        'cor_fundo': VERDE,
        'proxima': 'd7_r4_c6',
    },
    'd7_r4_c6': {
        'dia': 7,
        'titulo': 'DIA 7 - SALVAR SOBREVIVENTES FORA DO PORTÃO / FINAL HEROICO: QUEM ALCANÇAR PRIMEIRO',
        'texto': (
            'O ferido está perto de um carro, a criança presa na grade e o aliado cercado por dois '
            'infectados.'
        ),
        'cor_fundo': VERDE,
        'opcoes': [
            {
                'texto': 'Alcançar a criança.',
                'resultado': 'A decisão leva ao próximo momento: Soldado se Recusa.',
                'proxima': 'd7_r4_c7',
                'efeitos': {
                    'energia': -4,
                },
                'itens_add': [],
            },
            {
                'texto': 'Alcançar o ferido.',
                'resultado': 'A decisão leva ao próximo momento: Soldado se Recusa.',
                'proxima': 'd7_r4_c7',
                'efeitos': {
                    'energia': -4,
                },
                'itens_add': [],
            },
            {
                'texto': 'Alcançar o aliado.',
                'resultado': 'A decisão leva ao próximo momento: Soldado se Recusa.',
                'proxima': 'd7_r4_c7',
                'efeitos': {
                    'energia': -4,
                },
                'itens_add': [],
            },
        ],
    },
    'd7_r4_c7': {
        'dia': 7,
        'titulo': 'DIA 7 - SALVAR SOBREVIVENTES FORA DO PORTÃO / FINAL HEROICO: SOLDADO SE RECUSA',
        'texto': 'Um soldado diz que a ordem é fechar a base. Ele não abrirá por civis fora do protocolo.',
        'cor_fundo': VERDE,
        'opcoes': [
            {
                'texto': 'Usar distração.',
                'resultado': 'A decisão leva ao próximo momento: Cobertura dos Aliados.',
                'proxima': 'd7_r4_c8',
                'efeitos': {
                    'energia': -4,
                },
                'itens_add': ['rações'],
            },
            {
                'texto': 'Discutir com o soldado.',
                'resultado': 'A escolha cobra seu preço antes que exista tempo para voltar atrás.',
                'final': {
                    'tipo': 'derrota',
                    'titulo': 'MORTE 3',
                    'texto': 'Discutir com o soldado; ele o detém enquanto sobreviventes são tomados pela horda.',
                },
                'efeitos': {
                    'vida': -100,
                },
                'qualidade': 'morte',
            },
        ],
    },
    'd7_r4_c8': {
        'dia': 7,
        'titulo': 'DIA 7 - SALVAR SOBREVIVENTES FORA DO PORTÃO / FINAL HEROICO: COBERTURA DOS ALIADOS',
        'texto': (
            'Helena e sobreviventes do ônibus dão cobertura. A mulher e a criança salvas no Dia 1 '
            'ajudam a guiar pessoas pelo portão lateral.'
        ),
        'cor_fundo': VERDE,
        'proxima': 'd7_r4_c9',
    },
    'd7_r4_c9': {
        'dia': 7,
        'titulo': 'DIA 7 - SALVAR SOBREVIVENTES FORA DO PORTÃO / FINAL HEROICO: PORTÃO ABRE PARCIALMENTE',
        'texto': 'O portão range e abre só para uma pessoa por vez. O mecanismo ameaça travar.',
        'cor_fundo': VERDE,
        'opcoes': [
            {
                'texto': 'Segurar portão.',
                'resultado': 'A decisão leva ao próximo momento: Nem Todos Conseguem.',
                'proxima': 'd7_r4_c10',
                'efeitos': {
                    'energia': -4,
                },
                'itens_add': [],
            },
            {
                'texto': 'Passar primeiro.',
                'resultado': 'A decisão leva ao próximo momento: Nem Todos Conseguem.',
                'proxima': 'd7_r4_c10',
                'efeitos': {
                    'energia': -4,
                },
                'itens_add': [],
            },
        ],
    },
    'd7_r4_c10': {
        'dia': 7,
        'titulo': 'DIA 7 - SALVAR SOBREVIVENTES FORA DO PORTÃO / FINAL HEROICO: NEM TODOS CONSEGUEM',
        'texto': (
            'A horda se aproxima rápido em excesso. Alguns tropeçam, outros voltam por familiares. O '
            'personagem entende que heroísmo não salva todos.'
        ),
        'cor_fundo': VERDE,
        'opcoes': [
            {
                'texto': 'Esperar todos próximos.',
                'resultado': 'A decisão leva ao próximo momento: Segurando a Passagem.',
                'proxima': 'd7_r4_c11',
                'efeitos': {
                    'energia': -4,
                },
                'itens_add': ['peça do ônibus'],
            },
            {
                'texto': 'Fechar imediatamente.',
                'resultado': 'A decisão leva ao próximo momento: Segurando a Passagem.',
                'proxima': 'd7_r4_c11',
                'efeitos': {
                    'energia': -4,
                },
                'itens_add': ['peça do ônibus'],
            },
        ],
    },
    'd7_r4_c11': {
        'dia': 7,
        'titulo': 'DIA 7 - SALVAR SOBREVIVENTES FORA DO PORTÃO / FINAL HEROICO: SEGURANDO A PASSAGEM',
        'texto': (
            'Os braços tremem, a alavanca corta a mão e infectados chegam perto o suficiente para '
            'respirar no pescoço dos vivos.'
        ),
        'cor_fundo': VERDE,
        'opcoes': [
            {
                'texto': 'Revistar resgatados.',
                'resultado': 'A decisão leva ao próximo momento: Infectado no Grupo.',
                'proxima': 'd7_r4_c12',
                'efeitos': {
                    'energia': -4,
                },
                'itens_add': [],
            },
            {
                'texto': 'Deixar todos entrarem sem checar.',
                'resultado': 'A decisão leva ao próximo momento: Infectado no Grupo.',
                'proxima': 'd7_r4_c12',
                'efeitos': {
                    'energia': -4,
                },
                'itens_add': [],
            },
        ],
    },
    'd7_r4_c12': {
        'dia': 7,
        'titulo': 'DIA 7 - SALVAR SOBREVIVENTES FORA DO PORTÃO / FINAL HEROICO: INFECTADO NO GRUPO',
        'texto': 'Um resgatado revela mordida escondida. O pânico quase explode dentro da passagem.',
        'cor_fundo': VERDE,
        'opcoes': [
            {
                'texto': 'Revelar infectado aos soldados.',
                'resultado': 'A decisão leva ao próximo momento: Base em Alerta.',
                'proxima': 'd7_r4_c13',
                'efeitos': {
                    'energia': -4,
                    'moral': 5,
                    'confianca': 2,
                },
                'itens_add': [],
            },
            {
                'texto': 'Esconder-se para evitar a execução.',
                'resultado': 'A escolha cobra seu preço antes que exista tempo para voltar atrás.',
                'final': {
                    'tipo': 'derrota',
                    'titulo': 'MORTE 4',
                    'texto': 'Esconder o infectado no grupo; ele se transforma dentro da passagem e causa massacre.',
                },
                'efeitos': {
                    'vida': -100,
                },
                'qualidade': 'morte',
            },
        ],
    },
    'd7_r4_c13': {
        'dia': 7,
        'titulo': 'DIA 7 - SALVAR SOBREVIVENTES FORA DO PORTÃO / FINAL HEROICO: BASE EM ALERTA',
        'texto': (
            'A base entra em alerta máximo. Helena explica que o personagem salvou vidas e impediu '
            'contaminação.'
        ),
        'cor_fundo': VERDE,
        'opcoes': [
            {
                'texto': 'Entrar na base com o grupo.',
                'resultado': 'A decisão leva ao próximo momento: Confiança dos Soldados.',
                'proxima': 'd7_r4_c14',
                'efeitos': {
                    'energia': -4,
                },
                'itens_add': ['aliado Lena', 'aliado Helena'],
            },
            {
                'texto': 'Ficar fora para procurar mais gente.',
                'resultado': 'A decisão leva ao próximo momento: Confiança dos Soldados.',
                'proxima': 'd7_r4_c14',
                'efeitos': {
                    'energia': -4,
                    'comida': 1,
                    'agua': 1,
                },
                'itens_add': ['aliado Lena', 'aliado Helena'],
            },
        ],
    },
    'd7_r4_c14': {
        'dia': 7,
        'titulo': 'DIA 7 - SALVAR SOBREVIVENTES FORA DO PORTÃO / FINAL HEROICO: CONFIANÇA DOS SOLDADOS',
        'texto': (
            'Os soldados percebem que o personagem salvou sobreviventes e também protegeu a base. As '
            'armas abaixam alguns centímetros.'
        ),
        'cor_fundo': VERDE,
        'proxima': 'd7_r4_c15',
    },
    'd7_r4_c15': {
        'dia': 7,
        'titulo': 'DIA 7 - SALVAR SOBREVIVENTES FORA DO PORTÃO / FINAL HEROICO: DECISÃO FINAL',
        'texto': (
            'Helicópteros se preparam para partir. O personagem vê Helena, a mulher, a criança e '
            'dezenas de vivos que só chegaram ali porque alguém decidiu ajudar no primeiro dia.'
        ),
        'cor_fundo': VERDE,
        'opcoes': [
            {
                'texto': 'Ficar com o grupo.',
                'resultado': 'Essa decisão encerra o caminho iniciado neste dia.',
                'proxima': 'd7_r4_fim_1',
                'efeitos': {
                    'energia': -4,
                    'moral': 10,
                    'confianca': 3,
                },
                'itens_add': ['aliado Lena', 'aliado Helena'],
                'qualidade': 'boa',
            },
            {
                'texto': 'Ir embora sozinho.',
                'resultado': 'Essa decisão encerra o caminho iniciado neste dia.',
                'proxima': 'd7_r4_fim_1',
                'efeitos': {
                    'energia': -4,
                    'moral': 6,
                    'confianca': 2,
                },
                'itens_add': ['aliado Lena', 'aliado Helena'],
                'qualidade': 'boa',
            },
        ],
    },
}
# =========================
# MOTOR DO JOGO
# =========================
pygame.init()
pygame.display.set_caption(TITULO_JANELA)
tela = pygame.display.set_mode((LARGURA, ALTURA))
relogio = pygame.time.Clock()

fonte_titulo = pygame.font.SysFont("arial", 34, bold=True)
fonte_subtitulo = pygame.font.SysFont("arial", 24, bold=True)
fonte_texto = pygame.font.SysFont("arial", 22)
fonte_texto_pequena = pygame.font.SysFont("arial", 18)
fonte_status = pygame.font.SysFont("arial", 20)
fonte_botao = pygame.font.SysFont("arial", 20, bold=True)
fonte_input = pygame.font.SysFont("arial", 30, bold=True)

estado_inicial = {
    "vida": 100,
    "energia": 100,
    "comida": 3,
    "agua": 3,
    "moral": 50,
    "confianca": 0,
    "municao": 0,
}

estado = estado_inicial.copy()
itens = []
cena_atual = "inicio"
entradas_aplicadas = set()
resultado_pendente = None
botoes_atuais = []

# Dados da rodada atual
nome_jogador = ""
tela_nome = True
tela_ranking = False
pontuacao = 0
dias_concluidos = set()
pontuacao_salva = False

# Pontuacao
PONTOS_ESCOLHA_BOA = 75
PONTOS_ESCOLHA_MEDIA = 50
PONTOS_MORTE = 0
PONTOS_DIA_CONCLUIDO = 100
ARQUIVO_PONTUACOES = "data/ranking.txt"
MAX_RANKING = 10


def nome_atual():
    nome = nome_jogador.strip()
    return nome if nome else "Sobrevivente"


def texto_personalizado(texto):
    texto = str(texto)
    substituicoes = {
        "Rafael": nome_atual(),
        "O personagem": nome_atual(),
        "o personagem": nome_atual(),
        "O jogador": nome_atual(),
        "o jogador": nome_atual(),
    }
    for antigo, novo in substituicoes.items():
        texto = texto.replace(antigo, novo)
    return texto


def texto_com_nome(texto):
    # Mantido como apelido caso alguma parte antiga do codigo use este nome.
    return texto_personalizado(texto)


def iniciar_rodada():
    global estado, itens, cena_atual, entradas_aplicadas, resultado_pendente
    global nome_jogador, tela_nome, tela_ranking, pontuacao, dias_concluidos, pontuacao_salva

    nome_jogador = nome_atual()
    estado = estado_inicial.copy()
    itens = []
    cena_atual = "inicio"
    entradas_aplicadas = set()
    resultado_pendente = None
    pontuacao = 0
    dias_concluidos = set()
    pontuacao_salva = False
    tela_nome = False
    tela_ranking = False
    entrar_na_cena("inicio")


def qualidade_automatica(opcao):
    final = opcao.get("final")
    if final and final.get("tipo") == "derrota":
        return "morte"

    qualidade = opcao.get("qualidade")
    if qualidade in ("boa", "media", "morte"):
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
    qualidade = qualidade_automatica(opcao)
    if qualidade == "boa":
        return PONTOS_ESCOLHA_BOA
    if qualidade == "media":
        return PONTOS_ESCOLHA_MEDIA
    return PONTOS_MORTE


def registrar_pontos_escolha(opcao):
    global pontuacao
    pontuacao += pontos_da_escolha(opcao)


def registrar_dia_concluido(dia):
    global pontuacao
    if dia and dia not in dias_concluidos:
        dias_concluidos.add(dia)
        pontuacao += PONTOS_DIA_CONCLUIDO


def caminho_arquivo_pontuacoes():
    pasta = os.path.dirname(os.path.abspath(__file__))
    return os.path.join(pasta, ARQUIVO_PONTUACOES)


def salvar_pontuacao_final(tipo_final, titulo_final):
    global pontuacao_salva
    if pontuacao_salva:
        return

    pontuacao_salva = True
    caminho = caminho_arquivo_pontuacoes()
    linha = (
        f"Nome: {nome_atual()} | "
        f"Pontuacao: {pontuacao} | "
        f"Dias concluidos: {len(dias_concluidos)} | "
        f"Resultado: {tipo_final} | "
        f"Final: {titulo_final}\n"
    )

    try:
        with open(caminho, "a", encoding="utf-8") as arquivo:
            arquivo.write(linha)
    except OSError as erro:
        print(f"Nao foi possivel salvar a pontuacao: {erro}")


def extrair_valor_ranking(parte, chave, padrao=""):
    """Extrai valores de uma linha do arquivo pontuacoes.txt."""
    prefixo = chave + ":"
    for pedaco in parte.split("|"):
        pedaco = pedaco.strip()
        if pedaco.startswith(prefixo):
            return pedaco[len(prefixo):].strip()
    return padrao


def ler_pontuacoes(maximo=MAX_RANKING):
    """Le o arquivo de pontuacoes e devolve o ranking ordenado pela maior pontuacao."""
    caminho = caminho_arquivo_pontuacoes()
    ranking = []

    if not os.path.exists(caminho):
        return ranking

    try:
        with open(caminho, "r", encoding="utf-8") as arquivo:
            linhas = arquivo.readlines()
    except OSError as erro:
        print(f"Nao foi possivel ler o ranking: {erro}")
        return ranking

    for linha in linhas:
        nome = extrair_valor_ranking(linha, "Nome", "Sobrevivente")
        pontuacao_texto = extrair_valor_ranking(linha, "Pontuacao", "0")
        dias_texto = extrair_valor_ranking(linha, "Dias concluidos", "0")
        resultado = extrair_valor_ranking(linha, "Resultado", "final")
        final = extrair_valor_ranking(linha, "Final", "Final desconhecido")

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


def descrever_requisitos(opcao):
    requisitos = []
    requer_item = opcao.get("requer_item")

    if isinstance(requer_item, str):
        requisitos.append(requer_item)
    elif isinstance(requer_item, (list, tuple, set)):
        requisitos.extend(str(item) for item in requer_item)

    municao_minima = opcao.get("municao_minima", 0)
    if municao_minima:
        requisitos.append(f"{municao_minima} municao")

    return ", ".join(requisitos)


def opcao_disponivel(opcao):
    """Verifica se o jogador possui os itens ou recursos exigidos por uma escolha."""
    requer_item = opcao.get("requer_item")

    if isinstance(requer_item, str) and requer_item not in itens:
        return False

    if isinstance(requer_item, (list, tuple, set)):
        for item in requer_item:
            if item not in itens:
                return False

    municao_minima = opcao.get("municao_minima", 0)
    if municao_minima and estado.get("municao", 0) < municao_minima:
        return False

    return True


def criar_resultado_bloqueado(opcao):
    requisito = descrever_requisitos(opcao) or "um recurso necessario"
    return {
        "titulo": "Opcao bloqueada",
        "texto": f"{nome_atual()} ainda nao possui {requisito}. Escolha outro caminho ou encontre esse recurso antes.",
        "destino": cena_atual,
        "final": None,
        "cor_fundo": cenas[cena_atual].get("cor_fundo", VERDE),
    }


def limitar_status(nome, valor):
    """Evita valores quebrando a interface."""
    if nome in ("vida", "energia", "moral"):
        return max(0, min(100, valor))
    if nome in ("comida", "agua", "municao"):
        return max(0, valor)
    if nome == "confianca":
        return max(-10, min(20, valor))
    return valor


def aplicar_efeitos(efeitos=None):
    if not efeitos:
        return
    for chave, delta in efeitos.items():
        if chave not in estado:
            estado[chave] = 0
        estado[chave] = limitar_status(chave, estado[chave] + delta)


def adicionar_itens(novos_itens=None):
    if not novos_itens:
        return
    for item in novos_itens:
        if item not in itens:
            itens.append(item)


def alterar_municao(delta=0):
    if delta:
        estado["municao"] = limitar_status("municao", estado["municao"] + delta)


def entrar_na_cena(nome_cena):
    global cena_atual, resultado_pendente
    cena_atual = nome_cena
    resultado_pendente = None

    cena = cenas.get(cena_atual)
    if cena and cena_atual not in entradas_aplicadas:
        aplicar_efeitos(cena.get("efeitos_entrada"))
        entradas_aplicadas.add(cena_atual)

    if cena and cena.get("fim_dia"):
        registrar_dia_concluido(cena.get("dia"))

    if cena and cena.get("final_jogo"):
        if cena.get("tipo") == "vitoria":
            registrar_dia_concluido(cena.get("dia"))
        salvar_pontuacao_final(cena.get("tipo", "final"), cena.get("titulo", "Final"))


def reiniciar_jogo():
    global estado, itens, cena_atual, entradas_aplicadas, resultado_pendente
    global tela_nome, tela_ranking, nome_jogador, pontuacao, dias_concluidos, pontuacao_salva

    estado = estado_inicial.copy()
    itens = []
    cena_atual = "inicio"
    entradas_aplicadas = set()
    resultado_pendente = None
    nome_jogador = ""
    tela_nome = True
    tela_ranking = False
    pontuacao = 0
    dias_concluidos = set()
    pontuacao_salva = False


def criar_cena_final_generica():
    return {
        "titulo": "Fim da Jornada",
        "texto": "Rafael nao resistiu aos ferimentos e sua jornada terminou antes de encontrar uma saida.",
        "final": True,
        "tipo": "derrota",
        "cor_fundo": VERMELHO_ESCURO,
    }


def criar_resultado(opcao):
    """Mostra o texto de resultado antes de mudar de cena ou abrir um final."""
    registrar_pontos_escolha(opcao)
    aplicar_efeitos(opcao.get("efeitos"))
    adicionar_itens(opcao.get("itens_add"))
    alterar_municao(opcao.get("municao_delta", 0))

    final = opcao.get("final")
    if estado.get("vida", 0) <= 0 and not final:
        final = {
            "tipo": "derrota",
            "titulo": "Morte - Ferimentos demais",
            "texto": "Rafael tentou continuar, mas o corpo nao respondeu. A cidade cobrou caro demais por cada escolha.",
        }

    return {
        "titulo": "Consequencia",
        "texto": opcao.get("resultado", "A escolha foi feita."),
        "destino": opcao.get("proxima"),
        "final": final,
        "cor_fundo": cenas[cena_atual].get("cor_fundo", VERDE),
    }


def resolver_resultado():
    global resultado_pendente
    if not resultado_pendente:
        return

    if resultado_pendente.get("final"):
        final = resultado_pendente["final"]
        chave_final = "__final_atual__"
        cenas[chave_final] = {
            "dia": cenas.get(cena_atual, {}).get("dia"),
            "titulo": final.get("titulo", "Final"),
            "texto": final.get("texto", "A historia terminou."),
            "tipo": final.get("tipo", "derrota"),
            "final_jogo": True,
            "cor_fundo": VERDE_CLARO if final.get("tipo") == "vitoria" else VERMELHO_ESCURO,
            "imagem": final.get("imagem", os.path.join(PASTA_ASSETS, f"{chave_final}.png")),
        }
        entrar_na_cena(chave_final)
    elif resultado_pendente.get("destino"):
        entrar_na_cena(resultado_pendente["destino"])
    else:
        resultado_pendente = None


def texto_quebrado(texto, fonte, largura_maxima):
    """Quebra texto por largura real da fonte e respeita quebras de linha manuais."""
    linhas = []

    for paragrafo in str(texto).split("\n"):
        palavras = paragrafo.split()
        linha_atual = ""

        if not palavras:
            linhas.append("")
            continue

        for palavra in palavras:
            teste = palavra if not linha_atual else linha_atual + " " + palavra
            if fonte.size(teste)[0] <= largura_maxima:
                linha_atual = teste
            else:
                if linha_atual:
                    linhas.append(linha_atual)
                linha_atual = palavra

        if linha_atual:
            linhas.append(linha_atual)

    return linhas


def desenhar_texto_em_caixa(superficie, texto, fonte, cor, retangulo, espaco_linha=6, limite_linhas=None):
    linhas = texto_quebrado(texto_personalizado(texto), fonte, retangulo.width - 22)
    if limite_linhas:
        linhas = linhas[:limite_linhas]

    y = retangulo.y + 12
    for linha in linhas:
        if y + fonte.get_height() > retangulo.bottom - 8:
            break
        render = fonte.render(linha, True, cor)
        superficie.blit(render, (retangulo.x + 12, y))
        y += fonte.get_height() + espaco_linha


def caminho_imagem_da_cena(chave_cena, cena):
    return cena.get("imagem", os.path.join(PASTA_ASSETS, f"{chave_cena}.png"))


def carregar_imagem(chave_cena, cena):
    caminho = caminho_imagem_da_cena(chave_cena, cena)
    if not caminho:
        return None, caminho

    if not os.path.isabs(caminho):
        caminho = os.path.join(os.path.dirname(__file__), caminho)

    if not os.path.exists(caminho):
        return None, caminho

    try:
        imagem = pygame.image.load(caminho).convert_alpha()
        return imagem, caminho
    except pygame.error:
        return None, caminho


def desenhar_imagem(chave_cena, cena):
    pygame.draw.rect(tela, (18, 18, 18), RET_IMAGEM, border_radius=12)
    pygame.draw.rect(tela, CINZA_CLARO, RET_IMAGEM, 2, border_radius=12)

    imagem, caminho = carregar_imagem(chave_cena, cena)
    if imagem:
        imagem = pygame.transform.smoothscale(imagem, (RET_IMAGEM.width, RET_IMAGEM.height))
        tela.blit(imagem, RET_IMAGEM.topleft)
    else:
        titulo = fonte_subtitulo.render("Espaco reservado para imagem", True, BRANCO)
        tela.blit(titulo, (RET_IMAGEM.centerx - titulo.get_width() // 2, RET_IMAGEM.centery - 35))

        caminho_relativo = caminho
        if caminho and os.path.isabs(caminho):
            try:
                caminho_relativo = os.path.relpath(caminho, os.path.dirname(__file__))
            except ValueError:
                caminho_relativo = caminho

        dica = fonte_texto_pequena.render(str(caminho_relativo), True, CINZA_CLARO)
        tela.blit(dica, (RET_IMAGEM.centerx - dica.get_width() // 2, RET_IMAGEM.centery + 5))


def desenhar_status():
    pygame.draw.rect(tela, (28, 33, 30), RET_STATUS, border_radius=12)
    pygame.draw.rect(tela, CINZA_CLARO, RET_STATUS, 2, border_radius=12)

    y = RET_STATUS.y + 22
    titulo = fonte_subtitulo.render("Status", True, BRANCO)
    tela.blit(titulo, (RET_STATUS.x + 18, y))
    y += 48

    status_linhas = [
        f"Nome: {nome_atual()}",
        f"Pontuacao: {pontuacao}",
        f"Dias passados: {len(dias_concluidos)}",
        f"Vida: {estado.get('vida', 0)}",
        f"Energia: {estado.get('energia', 0)}",
        f"Comida: {estado.get('comida', 0)}",
        f"Agua: {estado.get('agua', 0)}",
        f"Moral: {estado.get('moral', 0)}",
        f"Confianca: {estado.get('confianca', 0)}",
        f"Municao: {estado.get('municao', 0)}",
    ]

    for linha in status_linhas:
        texto = fonte_status.render(linha, True, BRANCO)
        tela.blit(texto, (RET_STATUS.x + 18, y))
        y += 32

    y += 18
    titulo_itens = fonte_subtitulo.render("Itens", True, BRANCO)
    tela.blit(titulo_itens, (RET_STATUS.x + 18, y))
    y += 42

    if itens:
        for item in itens[-14:]:
            texto = fonte_texto_pequena.render(f"- {item}", True, AMARELO_CLARO)
            tela.blit(texto, (RET_STATUS.x + 18, y))
            y += 25
    else:
        texto = fonte_texto_pequena.render("Nenhum item ainda", True, CINZA_CLARO)
        tela.blit(texto, (RET_STATUS.x + 18, y))


def desenhar_ranking():
    tela.fill((18, 24, 20))

    titulo = fonte_titulo.render("Ranking de Sobreviventes", True, BRANCO)
    tela.blit(titulo, (LARGURA // 2 - titulo.get_width() // 2, 70))

    subtitulo = fonte_texto.render("Top pontuacoes salvas em pontuacoes.txt", True, AMARELO_CLARO)
    tela.blit(subtitulo, (LARGURA // 2 - subtitulo.get_width() // 2, 120))

    ranking = ler_pontuacoes(MAX_RANKING)
    caixa = pygame.Rect(170, 175, LARGURA - 340, 560)
    pygame.draw.rect(tela, (235, 232, 215), caixa, border_radius=12)
    pygame.draw.rect(tela, BRANCO, caixa, 2, border_radius=12)

    if not ranking:
        mensagem = fonte_subtitulo.render("Nenhuma pontuacao salva ainda.", True, PRETO)
        tela.blit(mensagem, (caixa.centerx - mensagem.get_width() // 2, caixa.centery - 25))
    else:
        cabecalho = "#   Nome                 Pontos   Dias   Resultado        Final"
        render = fonte_status.render(cabecalho, True, PRETO)
        tela.blit(render, (caixa.x + 28, caixa.y + 24))

        y = caixa.y + 70
        for posicao, item in enumerate(ranking, start=1):
            nome = item["nome"][:18]
            resultado = item["resultado"][:12]
            final = item["final"][:42]
            linha = f"{posicao:>2}. {nome:<18} {item['pontuacao']:>6}   {item['dias']:>2}    {resultado:<12}   {final}"
            render = fonte_status.render(linha, True, PRETO)
            tela.blit(render, (caixa.x + 28, y))
            y += 42

    rodape = fonte_texto.render("Pressione F1, Backspace ou ESC para voltar", True, BRANCO)
    tela.blit(rodape, (LARGURA // 2 - rodape.get_width() // 2, ALTURA - 95))


def desenhar_tela_nome():
    tela.fill((18, 24, 20))

    titulo = fonte_titulo.render("Seven Days of Fear", True, BRANCO)
    tela.blit(titulo, (LARGURA // 2 - titulo.get_width() // 2, 190))

    subtitulo = fonte_subtitulo.render("Digite o nome do personagem", True, AMARELO_CLARO)
    tela.blit(subtitulo, (LARGURA // 2 - subtitulo.get_width() // 2, 255))

    caixa = pygame.Rect(LARGURA // 2 - 360, 325, 720, 68)
    pygame.draw.rect(tela, (235, 232, 215), caixa, border_radius=12)
    pygame.draw.rect(tela, BRANCO, caixa, 2, border_radius=12)

    texto_nome = nome_jogador if nome_jogador else "Seu nome aqui"
    cor_nome = PRETO if nome_jogador else CINZA
    render_nome = fonte_input.render(texto_nome, True, cor_nome)
    tela.blit(render_nome, (caixa.x + 20, caixa.y + caixa.height // 2 - render_nome.get_height() // 2))

    instrucoes = [
        "Pressione Enter para iniciar a rodada.",
        "Pressione F1 para abrir o ranking salvo.",
        "A pontuacao sera salva automaticamente em pontuacoes.txt ao morrer ou vencer.",
        "Escolhas boas valem 75 pontos, escolhas medias valem 50 e mortes valem 0.",
        "Cada dia concluido adiciona mais 100 pontos.",
    ]

    y = 445
    for linha in instrucoes:
        render = fonte_texto.render(linha, True, BRANCO)
        tela.blit(render, (LARGURA // 2 - render.get_width() // 2, y))
        y += 36

    dica = fonte_texto_pequena.render("ESC sai do jogo | Backspace apaga o nome | F1 ranking", True, CINZA_CLARO)
    tela.blit(dica, (LARGURA // 2 - dica.get_width() // 2, ALTURA - 70))


def tratar_nome(evento):
    global nome_jogador, tela_ranking

    if evento.key == pygame.K_ESCAPE:
        pygame.quit()
        sys.exit()

    if evento.key == pygame.K_F1:
        tela_ranking = True
        return

    if evento.key == pygame.K_RETURN:
        iniciar_rodada()
        return

    if evento.key == pygame.K_BACKSPACE:
        nome_jogador = nome_jogador[:-1]
        return

    caractere = evento.unicode
    if caractere and caractere.isprintable() and len(nome_jogador) < 20:
        nome_jogador += caractere


def criar_botao(texto, retangulo, acao, indice=None, disponivel=True):
    return {"texto": texto, "rect": retangulo, "acao": acao, "indice": indice, "disponivel": disponivel}


def desenhar_botao(botao, mouse_pos):
    ret = botao["rect"]
    mouse_em_cima = ret.collidepoint(mouse_pos)
    if not botao.get("disponivel", True):
        cor = (70, 70, 70)
    else:
        cor = (70, 96, 75) if mouse_em_cima else (48, 66, 52)
    pygame.draw.rect(tela, cor, ret, border_radius=10)
    pygame.draw.rect(tela, BRANCO, ret, 2, border_radius=10)

    prefixo = ""
    if botao.get("indice") is not None:
        prefixo = f"{botao['indice'] + 1}. "

    texto = prefixo + botao["texto"]
    linhas = texto_quebrado(texto, fonte_botao, ret.width - 24)
    altura_total = len(linhas) * fonte_botao.get_height() + max(0, len(linhas) - 1) * 2
    y = ret.centery - altura_total // 2

    for linha in linhas[:2]:
        render = fonte_botao.render(linha, True, BRANCO)
        tela.blit(render, (ret.x + 14, y))
        y += fonte_botao.get_height() + 2


def desenhar_cena():
    global botoes_atuais
    botoes_atuais = []

    if resultado_pendente:
        cena = resultado_pendente
        chave = cena_atual
        titulo = cena.get("titulo", "Consequencia")
        texto = texto_com_nome(cena.get("texto", ""))
        cor_fundo = cena.get("cor_fundo", VERDE)
        opcoes = []
    else:
        cena = cenas.get(cena_atual, criar_cena_final_generica())
        chave = cena_atual
        titulo = cena.get("titulo", "Cena")
        texto = texto_com_nome(cena.get("texto", ""))
        cor_fundo = cena.get("cor_fundo", VERDE)
        opcoes = cena.get("opcoes", [])

    tela.fill(cor_fundo)

    # Cabecalho
    titulo_render = fonte_titulo.render(titulo, True, PRETO if cor_fundo == BRANCO else BRANCO)
    tela.blit(titulo_render, (MARGEM, 24))

    dia = cena.get("dia")
    if dia:
        dia_render = fonte_subtitulo.render(f"Dia {dia}", True, PRETO if cor_fundo == BRANCO else BRANCO)
        tela.blit(dia_render, (RET_STATUS.x, 32))

    desenhar_imagem(chave, cena)

    # Texto da cena
    pygame.draw.rect(tela, (235, 232, 215), RET_TEXTO, border_radius=12)
    pygame.draw.rect(tela, PRETO, RET_TEXTO, 2, border_radius=12)
    desenhar_texto_em_caixa(tela, texto, fonte_texto, PRETO, RET_TEXTO)

    # Opcoes ou botoes de continuacao
    pygame.draw.rect(tela, (30, 38, 32), RET_OPCOES, border_radius=12)
    pygame.draw.rect(tela, CINZA_CLARO, RET_OPCOES, 2, border_radius=12)

    mouse_pos = pygame.mouse.get_pos()

    if resultado_pendente:
        botao = criar_botao("Continuar", pygame.Rect(RET_OPCOES.x + 18, RET_OPCOES.y + 72, RET_OPCOES.width - 36, 58), "resolver_resultado")
        botoes_atuais.append(botao)
    elif cena.get("final_jogo") and cena.get("tipo") == "derrota":
        instrucao_morte = (
            f"Fim de jogo, {nome_atual()}. Pontuacao final: {pontuacao}.\n"
            "A pontuacao desta rodada foi salva em pontuacoes.txt.\n"
            "Pressione R para reiniciar, F1 para ranking ou ESC para sair."
        )
        desenhar_texto_em_caixa(tela, instrucao_morte, fonte_texto, BRANCO, RET_OPCOES)
    elif cena.get("final_jogo"):
        texto_final = (
            f"Pontuacao final: {pontuacao}.\n"
            "A pontuacao desta rodada foi salva em pontuacoes.txt."
        )
        desenhar_texto_em_caixa(
            tela,
            texto_final,
            fonte_texto,
            BRANCO,
            pygame.Rect(RET_OPCOES.x + 18, RET_OPCOES.y + 12, RET_OPCOES.width - 36, 58),
        )
        botao_reiniciar = criar_botao("Reiniciar jogo", pygame.Rect(RET_OPCOES.x + 18, RET_OPCOES.y + 78, RET_OPCOES.width - 36, 42), "reiniciar")
        botao_ranking = criar_botao("Ver ranking", pygame.Rect(RET_OPCOES.x + 18, RET_OPCOES.y + 126, RET_OPCOES.width - 36, 42), "ranking")
        botao_sair = criar_botao("Sair", pygame.Rect(RET_OPCOES.x + 18, RET_OPCOES.y + 174, RET_OPCOES.width - 36, 42), "sair")
        botoes_atuais.extend([botao_reiniciar, botao_ranking, botao_sair])
    elif opcoes:
        quantidade = len(opcoes)
        espaco = 8
        altura_botao = min(48, (RET_OPCOES.height - 28 - (quantidade - 1) * espaco) // quantidade)
        y = RET_OPCOES.y + 14

        for indice, opcao in enumerate(opcoes):
            ret = pygame.Rect(RET_OPCOES.x + 18, y, RET_OPCOES.width - 36, altura_botao)
            disponivel = opcao_disponivel(opcao)
            texto_opcao = opcao["texto"]
            if not disponivel:
                texto_opcao = f"{texto_opcao} (precisa de {descrever_requisitos(opcao)})"
            botoes_atuais.append(criar_botao(texto_opcao, ret, "opcao", indice, disponivel))
            y += altura_botao + espaco
    elif cena.get("fim_dia"):
        botao = criar_botao("Avancar para o proximo dia", pygame.Rect(RET_OPCOES.x + 18, RET_OPCOES.y + 72, RET_OPCOES.width - 36, 58), "proxima_dia")
        botoes_atuais.append(botao)
    elif cena.get("proxima"):
        botao = criar_botao("Continuar", pygame.Rect(RET_OPCOES.x + 18, RET_OPCOES.y + 72, RET_OPCOES.width - 36, 58), "proxima")
        botoes_atuais.append(botao)
    else:
        botao = criar_botao("Reiniciar jogo", pygame.Rect(RET_OPCOES.x + 18, RET_OPCOES.y + 72, RET_OPCOES.width - 36, 58), "reiniciar")
        botoes_atuais.append(botao)

    for botao in botoes_atuais:
        desenhar_botao(botao, mouse_pos)

    desenhar_status()

    dica = fonte_texto_pequena.render("Mouse | 1-4 escolhas | Enter/Espaco continuar | F1 ranking | ESC sair", True, BRANCO if cor_fundo != BRANCO else PRETO)
    tela.blit(dica, (MARGEM, ALTURA - 24))


def executar_acao_botao(botao):
    global resultado_pendente, tela_ranking
    acao = botao["acao"]

    if acao == "sair":
        pygame.quit()
        sys.exit()
    elif acao == "reiniciar":
        reiniciar_jogo()
    elif acao == "ranking":
        tela_ranking = True
    elif acao == "resolver_resultado":
        resolver_resultado()
    elif acao == "opcao":
        cena = cenas[cena_atual]
        indice = botao["indice"]
        if indice is not None and 0 <= indice < len(cena.get("opcoes", [])):
            opcao = cena["opcoes"][indice]
            if not opcao_disponivel(opcao):
                resultado_pendente = criar_resultado_bloqueado(opcao)
            else:
                resultado_pendente = criar_resultado(opcao)
    elif acao == "proxima":
        proxima = cenas[cena_atual].get("proxima")
        if proxima:
            entrar_na_cena(proxima)
    elif acao == "proxima_dia":
        proxima = cenas[cena_atual].get("proxima_dia")
        if proxima:
            entrar_na_cena(proxima)


def tratar_teclado(evento):
    global tela_ranking

    if evento.key == pygame.K_ESCAPE:
        pygame.quit()
        sys.exit()

    if evento.key == pygame.K_F1:
        tela_ranking = True
        return

    cena = cenas.get(cena_atual, {})
    if cena.get("final_jogo") and cena.get("tipo") == "derrota":
        if evento.key == pygame.K_r:
            reiniciar_jogo()
        return

    if pygame.K_1 <= evento.key <= pygame.K_4:
        indice = evento.key - pygame.K_1
        for botao in botoes_atuais:
            if botao.get("acao") == "opcao" and botao.get("indice") == indice:
                executar_acao_botao(botao)
                return

    if evento.key in (pygame.K_RETURN, pygame.K_SPACE):
        for botao in botoes_atuais:
            if botao.get("acao") in ("resolver_resultado", "proxima", "proxima_dia"):
                executar_acao_botao(botao)
                return


def loop_principal():
    global tela_ranking

    while True:
        relogio.tick(FPS)

        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if tela_ranking:
                if evento.type == pygame.KEYDOWN and evento.key in (pygame.K_F1, pygame.K_ESCAPE, pygame.K_BACKSPACE):
                    tela_ranking = False
                continue

            if tela_nome:
                if evento.type == pygame.KEYDOWN:
                    tratar_nome(evento)
                continue

            if evento.type == pygame.MOUSEBUTTONDOWN and evento.button == 1:
                for botao in botoes_atuais:
                    if botao["rect"].collidepoint(evento.pos):
                        executar_acao_botao(botao)
                        break
            elif evento.type == pygame.KEYDOWN:
                tratar_teclado(evento)

        if tela_ranking:
            desenhar_ranking()
        elif tela_nome:
            desenhar_tela_nome()
        else:
            desenhar_cena()

        pygame.display.flip()


if __name__ == "__main__":
    loop_principal()
