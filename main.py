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
PASTA_ASSETS = "assets"

# Cores
BRANCO = (235, 235, 225)
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

RET_IMAGEM = pygame.Rect(MARGEM, 82, AREA_PRINCIPAL_LARGURA, 315)
RET_TEXTO = pygame.Rect(MARGEM, 412, AREA_PRINCIPAL_LARGURA, 120)
RET_OPCOES = pygame.Rect(MARGEM, 550, AREA_PRINCIPAL_LARGURA, 220)
RET_STATUS = pygame.Rect(MARGEM * 2 + AREA_PRINCIPAL_LARGURA, 82, STATUS_LARGURA, 688)

# =========================
# ROTEIRO / CENAS
# =========================
cenas = {
    "inicio": {
        "dia": 1,
        "titulo": "DIA 1 - O Inicio",
        "texto": " Rafael acorda no sofa com o som de sirenes cortando a madrugada. A televisao esta sem sinal, o celular nao tem rede e a ultima mensagem da irma diz: nao saia de casa, eles estao mordendo as pessoas.",
        "cor_fundo": BRANCO,
        "proxima": "d1_apartamento"
    },
    "d1_apartamento": {
        "dia": 1,
        "titulo": "O Apartamento Trancado",
        "texto": "A porta do corredor treme com pancadas lentas. Na rua, carros batem, pessoas gritam e sombras se jogam sobre corpos caidos. Rafael tem poucos segundos para decidir como vai reagir.",
        "cor_fundo": VERDE,
        "opcoes": [
            {"texto": "Olhar pelo olho magico", "resultado": "Rafael chega perto da porta e ve o vizinho do 32 parado no corredor. O pescoco dele esta aberto e os olhos parecem vazios.", "proxima": "d1_olho", "efeitos": {"moral": -3}},
            {"texto": "Pegar suprimentos na cozinha", "resultado": "Ele enfia agua, biscoitos, documentos e uma faca velha na mochila antes que a porta comece a rachar.", "proxima": "d1_suprimentos", "itens_add": ["faca", "mochila"], "efeitos": {"energia": -4}},
            {"texto": "Fugir pela janela dos fundos", "resultado": "Rafael abre a janela da area de servico e salta sobre sacos de lixo no beco. O cheiro de sangue vem da rua lateral.", "proxima": "d1_janela", "efeitos": {"vida": -5, "energia": -8}},
            {"texto": "Gritar perguntando quem esta la", "resultado": "A resposta vem como um rosnado. A madeira estala e a fechadura quase se solta.", "proxima": "d1_gritar", "efeitos": {"moral": -5}}
        ]
    },
    "d1_olho": {
        "dia": 1,
        "titulo": "O Vizinho no Corredor",
        "texto": "O vizinho bate a testa contra a porta como se nao sentisse dor. Outros passos arrastados se aproximam pelo corredor. A porta aguenta, mas nao por muito tempo.",
        "cor_fundo": VERDE,
        "opcoes": [
            {"texto": "Abrir uma fresta para ajudar", "resultado": "Rafael abre a porta e percebe tarde demais que nao ha mais pessoa ali.", "final": {"tipo": "derrota", "titulo": "Morte - A primeira mordida", "texto": "O vizinho atravessa a fresta, derruba Rafael no chao da sala e morde seu ombro. As sirenes continuam tocando enquanto a consciencia dele some."}, "efeitos": {"vida": -100}},
            {"texto": "Ficar em silencio e reforcar a porta", "resultado": "Ele prende o sofa contra a entrada e espera os mortos seguirem outro barulho. Depois, corre para a escada externa.", "proxima": "d1_telhado", "efeitos": {"energia": -6}},
            {"texto": "Subir para o telhado", "resultado": "Rafael corre pelas escadas internas. Um infectado surge no quarto andar, mas ele passa antes de ser agarrado.", "proxima": "d1_lia", "efeitos": {"energia": -10, "moral": -2}}
        ]
    },
    "d1_telhado": {
        "dia": 1,
        "titulo": "Ar Frio no Telhado",
        "texto": "Do alto, a cidade parece um incendio vivo. Helicopteros cruzam o ceu e uma luz pisca no predio vizinho. Alguem esta pedindo ajuda entre duas caixas d'agua.",
        "cor_fundo": VERDE,
        "opcoes": [
            {"texto": "Ajudar a sobrevivente", "resultado": "Rafael amarra lencois e atravessa ate o outro predio. A jovem se chama Lia e sabe que existe um abrigo na zona norte.", "proxima": "d1_fim_lia", "itens_add": ["aliada Lia"], "efeitos": {"confianca": 2, "moral": 8, "energia": -10}},
            {"texto": "Ignorar e procurar saida sozinho", "resultado": "Ele se afasta dos gritos e encontra uma escada de emergencia que desce ate uma rua menos tomada.", "proxima": "d1_fim_solo", "efeitos": {"moral": -8, "energia": -5}},
            {"texto": "Gritar para afastar os mortos dela", "resultado": "Os mortos mudam de direcao, mas tambem encontram Rafael. A porta do telhado se abre com violencia.", "final": {"tipo": "derrota", "titulo": "Morte - Barulho demais", "texto": "Rafael corre ate a borda, escorrega no cascalho molhado e cai antes que possa se segurar. A cidade engole seu ultimo grito."}, "efeitos": {"vida": -100}}
        ]
    },
    "d1_lia": {
        "dia": 1,
        "titulo": "A Garota da Caixa d'Agua",
        "texto": "A jovem presa no outro predio grita por socorro. Dois infectados rodam a caixa d'agua. Rafael pode salva-la, mas qualquer ruido trara mais mortos.",
        "cor_fundo": VERDE,
        "opcoes": [
            {"texto": "Usar lencois como corda", "resultado": "A corda improvisada quase rasga, mas Lia consegue atravessar. Ela aperta a mao de Rafael e promete ajudar.", "proxima": "d1_fim_lia", "itens_add": ["aliada Lia"], "efeitos": {"confianca": 3, "moral": 7, "energia": -12}},
            {"texto": "Esperar os mortos se afastarem", "resultado": "A demora custa caro. Lia se machuca, mas os dois conseguem descer pela lavanderia coletiva.", "proxima": "d1_fim_lia", "itens_add": ["aliada Lia"], "efeitos": {"vida": -5, "confianca": 1, "energia": -8}},
            {"texto": "Fugir sem ajudar", "resultado": "Os gritos dela atraem uma horda para o telhado. Rafael nao encontra rota segura.", "final": {"tipo": "derrota", "titulo": "Morte - Sem volta", "texto": "Ao tentar descer correndo, Rafael se depara com mortos subindo a escada. Ele fica preso entre o telhado e a porta quebrada."}, "efeitos": {"vida": -100}}
        ]
    },
    "d1_suprimentos": {
        "dia": 1,
        "titulo": "A Mochila de Emergencia",
        "texto": "A porta finalmente arrebenta. Dona Marta, a vizinha do andar de cima, entra cambaleando. A boca dela esta suja de sangue e seus dedos arranham a parede.",
        "cor_fundo": VERDE,
        "opcoes": [
            {"texto": "Enfrentar Dona Marta", "resultado": "Rafael hesita ao reconhecer a vizinha. A hesitacao e suficiente.", "final": {"tipo": "derrota", "titulo": "Morte - Hesitacao", "texto": "Dona Marta agarra o braco de Rafael e morde fundo. A febre vem rapido demais para que ele consiga fugir."}, "efeitos": {"vida": -100}},
            {"texto": "Fugir pela cozinha", "resultado": "Ele passa por cima da mesa, quebra a janela da cozinha e cai no telhado baixo da garagem.", "proxima": "d1_garagem", "efeitos": {"vida": -8, "energia": -10}},
            {"texto": "Procurar o radio antigo", "resultado": "Rafael pega o radio do pai na estante e foge pela area de servico antes da criatura alcancar a cozinha.", "proxima": "d1_radio", "itens_add": ["radio"], "efeitos": {"energia": -8, "moral": 3}}
        ]
    },
    "d1_garagem": {
        "dia": 1,
        "titulo": "A Garagem Escura",
        "texto": "A garagem esta cheia de carros abandonados. Um alarme pisca em silencio. No canto, um garoto se esconde atras de uma lixeira e um cachorro magro rosna baixo.",
        "cor_fundo": VERDE,
        "opcoes": [
            {"texto": "Ligar o carro mais proximo", "resultado": "O motor pega, mas o alarme dispara. Os mortos descem a rampa em massa.", "final": {"tipo": "derrota", "titulo": "Morte - Alarme", "texto": "O carro morre no portao. Maos quebram os vidros, e Rafael nao consegue destravar o cinto a tempo."}, "efeitos": {"vida": -100}},
            {"texto": "Chamar o garoto escondido", "resultado": "O garoto se chama Nico e conhece um caminho ate uma mercearia pelos fundos do bairro.", "proxima": "d1_fim_nico", "itens_add": ["aliado Nico"], "efeitos": {"confianca": 2, "moral": 4, "comida": 1}},
            {"texto": "Acalmar o cachorro", "resultado": "Rafael divide um biscoito com o animal. Ele passa a segui-lo, farejando perigos antes que aparecam.", "proxima": "d1_fim_cinza", "itens_add": ["cao Cinza"], "efeitos": {"comida": -1, "moral": 6}}
        ]
    },
    "d1_radio": {
        "dia": 1,
        "titulo": "Mensagem Cortada",
        "texto": "O radio chia entre interferencias. Uma voz militar repete: evacuacao suspensa, evitem hospitais, permaneçam longe de mordidos. A mensagem corta antes de dizer para onde ir.",
        "cor_fundo": AZUL_CLARO,
        "proxima": "d1_fim_radio"
    },
    "d1_janela": {
        "dia": 1,
        "titulo": "O Beco dos Fundos",
        "texto": "Rafael cai no beco e prende a respiracao. Dois infectados devoram um policial caido. A poucos metros, uma loja de ferramentas esta com a porta semiaberta.",
        "cor_fundo": VERDE,
        "opcoes": [
            {"texto": "Pegar a arma do policial", "resultado": "A arma esta no coldre, mas o policial ainda se mexe. Quando Rafael se aproxima, ele segura sua perna.", "final": {"tipo": "derrota", "titulo": "Morte - Arma vazia", "texto": "A pistola nao tem municao. O barulho da luta chama os infectados, e Rafael cai antes de conseguir correr."}, "itens_add": ["arma de fogo"], "efeitos": {"vida": -100}},
            {"texto": "Entrar na loja de ferramentas", "resultado": "Ele passa por baixo da porta de metal, encontra um pe de cabra e bloqueia a vitrine com prateleiras.", "proxima": "d1_fim_ferramentas", "itens_add": ["pe de cabra"], "efeitos": {"energia": -6, "moral": 4}},
            {"texto": "Subir no predio comercial", "resultado": "Rafael sobe ate uma sala de seguranca. As cameras mostram uma rota livre ate a escola municipal.", "proxima": "d1_fim_cameras", "itens_add": ["mapa improvisado"], "efeitos": {"energia": -7, "moral": 5}}
        ]
    },
    "d1_gritar": {
        "dia": 1,
        "titulo": "A Porta Cedendo",
        "texto": "O grito de Rafael ecoa pelo corredor. A criatura do outro lado responde com pancadas violentas. A tranca nao aguenta mais um minuto.",
        "cor_fundo": VERDE,
        "opcoes": [
            {"texto": "Segurar a porta com o corpo", "resultado": "A madeira se parte e uma mao ensanguentada atravessa a fresta.", "final": {"tipo": "derrota", "titulo": "Morte - Porta quebrada", "texto": "Rafael e puxado contra a porta. Quando ela cai, tres infectados entram juntos e o arrastam pela sala."}, "efeitos": {"vida": -100}},
            {"texto": "Esconder-se no quarto", "resultado": "Ele se enfia debaixo da cama. A criatura entra no quarto, para perto dele e fareja o ar.", "proxima": "d1_quarto", "efeitos": {"moral": -5}},
            {"texto": "Sair pela janela do quarto", "resultado": "Rafael quebra o vidro, pula para a varanda vizinha e se corta no braco.", "proxima": "d1_janela", "efeitos": {"vida": -10, "energia": -6}}
        ]
    },
    "d1_quarto": {
        "dia": 1,
        "titulo": "Debaixo da Cama",
        "texto": "O infectado fica parado ao lado da cama. Um grito na rua o distrai. Quando tudo fica silencioso, Rafael sai e encontra as chaves do carro sobre o armario.",
        "cor_fundo": VERDE,
        "opcoes": [
            {"texto": "Usar as chaves e dormir no carro", "resultado": "Ele desce pela escada externa, entra no carro da garagem e trava as portas com a faca no colo.", "proxima": "d1_fim_carro", "itens_add": ["chave de carro"], "efeitos": {"moral": 3, "energia": -5}},
            {"texto": "Vasculhar o apartamento destruido", "resultado": "Rafael encontra pilhas e um isqueiro antes de sair pela cozinha quebrada.", "proxima": "d1_fim_radio", "itens_add": ["isqueiro"], "efeitos": {"energia": -6, "moral": 2}}
        ]
    },

    # Finais do Dia 1
    "d1_fim_lia": {"dia": 1, "titulo": "Telhado Seguro", "texto": "Rafael e Lia passam a noite no telhado, protegidos pela altura. A cidade queima abaixo deles, mas pela primeira vez Rafael nao esta sozinho.", "cor_fundo": VERDE_CLARO, "fim_dia": True, "proxima_dia": "d2_inicio"},
    "d1_fim_solo": {"dia": 1, "titulo": "Sozinho na Escada", "texto": "Rafael se esconde em uma escada de incendio. As sirenes param perto do amanhecer, e o silencio parece ainda mais perigoso.", "cor_fundo": VERDE_CLARO, "fim_dia": True, "proxima_dia": "d2_inicio"},
    "d1_fim_nico": {"dia": 1, "titulo": "Mercearia dos Fundos", "texto": "Rafael e Nico dormem no estoque de uma mercearia. Ha poucas latas, mas as portas de metal seguram os mortos do lado de fora.", "cor_fundo": VERDE_CLARO, "fim_dia": True, "proxima_dia": "d2_inicio"},
    "d1_fim_cinza": {"dia": 1, "titulo": "Companhia no Escuro", "texto": "Rafael termina o dia atras de um carro virado. O cachorro Cinza dorme perto de seus pes, atento a qualquer ruido no beco.", "cor_fundo": VERDE_CLARO, "fim_dia": True, "proxima_dia": "d2_inicio"},
    "d1_fim_radio": {"dia": 1, "titulo": "Radio no Chiado", "texto": "Com o radio no ouvido, Rafael ouve ordens quebradas e nomes de bairros que ja nao existem como lugares seguros.", "cor_fundo": VERDE_CLARO, "fim_dia": True, "proxima_dia": "d2_inicio"},
    "d1_fim_ferramentas": {"dia": 1, "titulo": "Loja de Ferramentas", "texto": "A loja vira um pequeno abrigo. Rafael aprende a valorizar cada parafuso, cada porta travada e cada segundo de silencio.", "cor_fundo": VERDE_CLARO, "fim_dia": True, "proxima_dia": "d2_inicio"},
    "d1_fim_cameras": {"dia": 1, "titulo": "Sala de Seguranca", "texto": "Pelas cameras, Rafael ve ruas tomadas, mas tambem uma rota ate a escola municipal. Ele desenha o caminho em um pedaço de papelao.", "cor_fundo": VERDE_CLARO, "fim_dia": True, "proxima_dia": "d2_inicio"},
    "d1_fim_carro": {"dia": 1, "titulo": "Carro Trancado", "texto": "Ele dorme dentro do carro com as portas travadas. Cada batida no capô parece o aviso de que o mundo acabou.", "cor_fundo": VERDE_CLARO, "fim_dia": True, "proxima_dia": "d2_inicio"},

    # DIA 2
    "d2_inicio": {
        "dia": 2,
        "titulo": "DIA 2 - A Busca por Comida",
        "texto": "A manha nasce sem sirenes. O silencio e pior. Rafael sente fome e sede, e sabe que precisa encontrar comida antes que outros sobreviventes encontrem primeiro.",
        "cor_fundo": BRANCO,
        "efeitos_entrada": {"comida": -1, "agua": -1, "energia": -5},
        "proxima": "d2_ruas"
    },
    "d2_ruas": {
        "dia": 2,
        "titulo": "Quatro Rotas Possiveis",
        "texto": "Fumaca sobe do mercado central. A escola municipal parece silenciosa. Uma farmacia ainda tem luz de emergencia. Nos becos, setas pintadas apontam para o norte.",
        "cor_fundo": VERDE,
        "opcoes": [
            {"texto": "Ir ao mercado pela rua principal", "resultado": "Rafael segue entre carros batidos. A entrada do mercado esta quebrada, e uma ambulancia tombada bloqueia metade da avenida.", "proxima": "d2_mercado", "efeitos": {"energia": -6}},
            {"texto": "Entrar na escola municipal", "resultado": "A escola esta estranhamente vazia. No quadro de uma sala, alguem escreveu: eles ouvem barulho.", "proxima": "d2_escola", "efeitos": {"moral": -2}},
            {"texto": "Seguir ate a farmacia", "resultado": "O cheiro de alcool e sangue toma a farmacia. Uma mulher de jaleco aponta uma tesoura para Rafael.", "proxima": "d2_farmacia", "efeitos": {"energia": -4}},
            {"texto": "Seguir as setas dos becos", "resultado": "As setas levam a vielas estreitas. Alguem observa Rafael de uma janela quebrada.", "proxima": "d2_becos", "efeitos": {"energia": -5, "moral": -1}}
        ]
    },
    "d2_mercado": {
        "dia": 2,
        "titulo": "Mercado Central",
        "texto": "Prateleiras estao caidas e o piso esta cheio de vidro. Da ambulancia vem um arranhado fraco. Dentro do mercado, latas ainda restam perto do caixa.",
        "cor_fundo": VERDE,
        "opcoes": [
            {"texto": "Abrir a ambulancia", "resultado": "Um paramedico infectado cai sobre Rafael. A maca prende sua perna e ele nao consegue se soltar.", "final": {"tipo": "derrota", "titulo": "Morte - Ambulancia", "texto": "Rafael encontra remedios, mas tambem encontra dentes. Preso pela maca, ele vira mais uma vitima da rua principal."}, "efeitos": {"vida": -100}},
            {"texto": "Pegar latas e sair rapido", "resultado": "Ele evita a ambulancia, enche a mochila com latas e sai antes que os mortos da avenida percebam.", "proxima": "d2_fim_mercado", "efeitos": {"comida": 4, "agua": 1, "energia": -8}},
            {"texto": "Usar o pe de cabra nas portas internas", "requer_item": "pe de cabra", "resultado": "Rafael forca o deposito e encontra garrafas de agua, pilhas e um pacote de curativos.", "proxima": "d2_fim_deposito", "itens_add": ["curativos"], "efeitos": {"comida": 2, "agua": 3, "energia": -10, "moral": 4}}
        ]
    },
    "d2_escola": {
        "dia": 2,
        "titulo": "Corredores da Escola",
        "texto": "Mochilas infantis continuam penduradas nas cadeiras. A cantina fica no fim do corredor. A secretaria pode ter mapas e registros de rotas de evacuacao.",
        "cor_fundo": VERDE,
        "opcoes": [
            {"texto": "Procurar comida na cantina", "resultado": "Uma panela cai no chao e o som ecoa pelo refeitorio. As portas do fundo comecam a bater por dentro.", "final": {"tipo": "derrota", "titulo": "Morte - Refeitorio", "texto": "Rafael tenta correr, mas dezenas de criancas infectadas saem do refeitorio. A escola guarda seu pior segredo."}, "efeitos": {"vida": -100}},
            {"texto": "Procurar mapas na secretaria", "resultado": "Rafael encontra mapas da cidade e uma anotacao sobre um abrigo antigo perto da zona norte.", "proxima": "d2_fim_mapa", "itens_add": ["mapa da cidade"], "efeitos": {"moral": 5, "energia": -5}},
            {"texto": "Ficar na biblioteca ate anoitecer", "resultado": "Ele bloqueia a porta com estantes e descobre uma sala de professores com agua esquecida.", "proxima": "d2_fim_biblioteca", "efeitos": {"agua": 2, "energia": 8, "moral": 2}}
        ]
    },
    "d2_farmacia": {
        "dia": 2,
        "titulo": "Helena",
        "texto": "A enfermeira se chama Helena. Ela diz que febre apos mordida significa contaminacao, mas tambem que alguns resistem mais tempo. Os remedios estao atras dela.",
        "cor_fundo": VERDE,
        "opcoes": [
            {"texto": "Confiar em Helena", "resultado": "Rafael abaixa a faca. Helena trata seus cortes e aceita seguir com ele ate encontrar lugar seguro.", "proxima": "d2_fim_helena", "itens_add": ["aliada Helena"], "efeitos": {"vida": 10, "confianca": 3, "moral": 5}},
            {"texto": "Dividir os suprimentos", "resultado": "Eles separam remedios, agua oxigenada e faixas. Helena entrega um frasco de antibiotico para emergencias.", "proxima": "d2_fim_remedios", "itens_add": ["antibioticos"], "efeitos": {"vida": 5, "confianca": 2, "moral": 3}},
            {"texto": "Expulsar Helena e pegar tudo", "resultado": "Helena grita por medo. Os mortos da rua ouvem e batem nas vitrines.", "final": {"tipo": "derrota", "titulo": "Morte - Ganancia", "texto": "Rafael consegue os remedios, mas fica preso entre prateleiras e vidros quebrados. Os mortos entram pela vitrine."}, "efeitos": {"vida": -100, "confianca": -3}}
        ]
    },
    "d2_becos": {
        "dia": 2,
        "titulo": "Setas no Muro",
        "texto": "As setas levam a um deposito fechado. Um homem armado aparece na janela e pergunta se Rafael foi mordido. A arma treme na mao dele.",
        "cor_fundo": VERDE,
        "opcoes": [
            {"texto": "Mostrar a mochila e negociar", "resultado": "O homem aceita trocar duas latas por informacoes. Ele ouviu uma transmissao vinda de uma torre de radio.", "proxima": "d2_fim_deposito_grupo", "efeitos": {"comida": 2, "confianca": 1, "moral": 3}},
            {"texto": "Mentir dizendo que e militar", "resultado": "O homem percebe a mentira e chama outros sobreviventes armados.", "final": {"tipo": "derrota", "titulo": "Morte - Mentira", "texto": "Rafael e confundido com saqueador. O tiro ecoa pelo beco antes que ele consiga explicar qualquer coisa."}, "efeitos": {"vida": -100}},
            {"texto": "Apagar as setas para despistar outros", "resultado": "Rafael apaga metade das marcas e escapa, mas perde a chance de encontrar ajuda. Ainda assim acha uma caixa de agua.", "proxima": "d2_fim_beco_solo", "efeitos": {"agua": 2, "confianca": -1, "moral": -4}}
        ]
    },
    "d2_fim_mercado": {"dia": 2, "titulo": "Latas na Mochila", "texto": "Rafael dorme atras de um caixa quebrado, com comida suficiente para continuar. Ao longe, um radio transmite algo sobre uma torre.", "cor_fundo": VERDE_CLARO, "fim_dia": True, "proxima_dia": "d3_inicio"},
    "d2_fim_deposito": {"dia": 2, "titulo": "Deposito Trancado", "texto": "A porta reforcada segura os mortos. Rafael passa a noite contando suprimentos e ouvindo passos no estacionamento.", "cor_fundo": VERDE_CLARO, "fim_dia": True, "proxima_dia": "d3_inicio"},
    "d2_fim_mapa": {"dia": 2, "titulo": "Mapa da Cidade", "texto": "O mapa mostra uma torre de radio no centro comercial. Talvez dali ainda seja possivel ouvir instrucoes reais.", "cor_fundo": VERDE_CLARO, "fim_dia": True, "proxima_dia": "d3_inicio"},
    "d2_fim_biblioteca": {"dia": 2, "titulo": "Biblioteca Silenciosa", "texto": "Entre livros e carteiras viradas, Rafael entende que o conhecimento agora vale tanto quanto comida.", "cor_fundo": VERDE_CLARO, "fim_dia": True, "proxima_dia": "d3_inicio"},
    "d2_fim_helena": {"dia": 2, "titulo": "Uma Enfermeira no Grupo", "texto": "Helena vigia enquanto Rafael descansa. Ela nao promete salvacao, mas sabe manter alguem vivo por mais um dia.", "cor_fundo": VERDE_CLARO, "fim_dia": True, "proxima_dia": "d3_inicio"},
    "d2_fim_remedios": {"dia": 2, "titulo": "Remedios e Duvidas", "texto": "Rafael termina o dia com remedios e uma duvida terrivel: talvez nem todos virem monstros na mesma velocidade.", "cor_fundo": VERDE_CLARO, "fim_dia": True, "proxima_dia": "d3_inicio"},
    "d2_fim_deposito_grupo": {"dia": 2, "titulo": "Deposito dos Desconfiados", "texto": "O grupo divide pouca comida e muita suspeita. Mesmo assim, todos falam da mesma torre de radio.", "cor_fundo": VERDE_CLARO, "fim_dia": True, "proxima_dia": "d3_inicio"},
    "d2_fim_beco_solo": {"dia": 2, "titulo": "Rota Apagada", "texto": "Rafael dorme em uma lavanderia abandonada. As setas apagadas somem na chuva, junto com a chance de ajuda facil.", "cor_fundo": VERDE_CLARO, "fim_dia": True, "proxima_dia": "d3_inicio"},

    # DIA 3
    "d3_inicio": {
        "dia": 3,
        "titulo": "DIA 3 - O Radio da Torre",
        "texto": "De madrugada, uma transmissao atravessa o chiado: quem estiver vivo, torre, zona norte, antes do setimo dia. A mensagem se repete ate morrer no silencio.",
        "cor_fundo": BRANCO,
        "efeitos_entrada": {"comida": -1, "agua": -1, "energia": -6},
        "proxima": "d3_avenida"
    },
    "d3_avenida": {
        "dia": 3,
        "titulo": "A Avenida Tomada",
        "texto": "A torre fica do outro lado de uma avenida cheia de mortos. Ha um carro abandonado, uma boca de esgoto aberta, um shopping escuro e predios ligados por telhados.",
        "cor_fundo": VERDE,
        "opcoes": [
            {"texto": "Usar um carro abandonado", "resultado": "Rafael encontra uma caminhonete com a chave no contato. O tanque esta quase vazio.", "proxima": "d3_carro", "efeitos": {"energia": -3}},
            {"texto": "Atravessar pelos esgotos", "resultado": "O cheiro e insuportavel. A agua bate nos joelhos e algo se mexe em tuneis laterais.", "proxima": "d3_esgoto", "efeitos": {"moral": -4}},
            {"texto": "Entrar pelo shopping", "resultado": "O shopping parece intacto demais. Manequins e corpos se confundem atras das vitrines.", "proxima": "d3_shopping", "efeitos": {"energia": -4}},
            {"texto": "Seguir pelos telhados", "resultado": "Rafael sobe pelas escadas de incendio. O vento assovia entre antenas e janelas quebradas.", "proxima": "d3_telhados", "efeitos": {"energia": -8}}
        ]
    },
    "d3_carro": {
        "dia": 3,
        "titulo": "Motor Frio",
        "texto": "A caminhonete pode atravessar metade da avenida, mas o motor fara barulho. Empurrar primeiro sera lento, cansativo e mais seguro.",
        "cor_fundo": VERDE,
        "opcoes": [
            {"texto": "Ligar direto e acelerar", "resultado": "O motor falha no meio da avenida e a horda fecha todos os lados.", "final": {"tipo": "derrota", "titulo": "Morte - Motor falho", "texto": "Os vidros quebram. Rafael tenta trocar de marcha, mas as maos entram primeiro e o arrancam do banco."}, "efeitos": {"vida": -100}},
            {"texto": "Empurrar antes de ligar", "resultado": "Ele empurra a caminhonete ladeira abaixo, liga apenas no fim e cruza sem chamar a horda inteira.", "proxima": "d3_fim_predio_torre", "efeitos": {"energia": -15, "moral": 4}}
        ]
    },
    "d3_esgoto": {
        "dia": 3,
        "titulo": "Debaixo da Cidade",
        "texto": "O tunel se divide em tres. Sem luz, qualquer passo pode ser uma queda. Com luz, qualquer brilho pode entregar a posicao.",
        "cor_fundo": VERDE,
        "opcoes": [
            {"texto": "Acender a lanterna", "resultado": "A luz revela marcas pintadas nas paredes e uma escada que sobe perto da torre.", "proxima": "d3_fim_esgoto", "efeitos": {"energia": -8, "moral": 3}},
            {"texto": "Andar no escuro", "resultado": "Rafael pisa onde nao devia. O chao desaparece sob seus pes.", "final": {"tipo": "derrota", "titulo": "Morte - Queda no escuro", "texto": "A perna quebra no fundo do canal. Os mortos nao precisam correr; basta seguir o som da dor."}, "efeitos": {"vida": -100}},
            {"texto": "Seguir a corrente de ar", "resultado": "O vento frio leva Rafael ate uma saida estreita atras do predio da torre.", "proxima": "d3_fim_esgoto", "efeitos": {"energia": -10, "vida": -4}}
        ]
    },
    "d3_shopping": {
        "dia": 3,
        "titulo": "Shopping Vazio",
        "texto": "As portas principais estao trincadas. O estacionamento subterraneo parece mais escuro, mas talvez tenha uma escada de servico para a torre.",
        "cor_fundo": VERDE,
        "opcoes": [
            {"texto": "Entrar pela porta principal", "resultado": "O alarme dispara e ecoa em todos os corredores.", "final": {"tipo": "derrota", "titulo": "Morte - Alarme do shopping", "texto": "Rafael corre por vitrines apagadas, mas todas as saidas se enchem de mortos atraidos pelo som."}, "efeitos": {"vida": -100}},
            {"texto": "Entrar pelo estacionamento", "resultado": "Entre carros abandonados, Rafael encontra uma escada de servico e uma mochila com pilhas.", "proxima": "d3_fim_shopping", "itens_add": ["pilhas"], "efeitos": {"energia": -8, "moral": 4}},
            {"texto": "Contornar o shopping", "resultado": "Ele perde tempo, mas evita o alarme e chega ao predio da torre por uma rua lateral.", "proxima": "d3_fim_predio_torre", "efeitos": {"energia": -12, "moral": 1}}
        ]
    },
    "d3_telhados": {
        "dia": 3,
        "titulo": "Pontes de Concreto",
        "texto": "Tabuas ligam predios vizinhos. Em uma marquise, um mecanico chamado Samuel esta preso, segurando uma caixa de ferramentas.",
        "cor_fundo": VERDE,
        "opcoes": [
            {"texto": "Ajudar Samuel", "resultado": "Rafael puxa Samuel pela marquise. O mecanico conhece motores, portas e geradores.", "proxima": "d3_fim_samuel", "itens_add": ["aliado Samuel"], "efeitos": {"confianca": 2, "moral": 6, "energia": -10}},
            {"texto": "Continuar sem parar", "resultado": "Rafael ignora o pedido de ajuda e chega mais rapido a torre, mas a decisao pesa durante a noite.", "proxima": "d3_fim_predio_torre", "efeitos": {"moral": -6, "energia": -5}},
            {"texto": "Pular para o predio vizinho", "resultado": "A distancia parece menor do que realmente e.", "final": {"tipo": "derrota", "titulo": "Morte - Salto impossivel", "texto": "Rafael toca a beirada com os dedos, mas nao consegue segurar. O impacto acaba com sua jornada antes da torre."}, "efeitos": {"vida": -100}}
        ]
    },
    "d3_fim_predio_torre": {"dia": 3, "titulo": "A Base da Torre", "texto": "Rafael chega ao predio da torre quando a noite cai. Subir agora seria suicidio. Ele bloqueia a porta e descansa.", "cor_fundo": VERDE_CLARO, "fim_dia": True, "proxima_dia": "d4_inicio"},
    "d3_fim_esgoto": {"dia": 3, "titulo": "Saida Suja", "texto": "Coberto de lama e cheiro de esgoto, Rafael encontra a escada externa da torre. Pelo menos esta vivo.", "cor_fundo": VERDE_CLARO, "fim_dia": True, "proxima_dia": "d4_inicio"},
    "d3_fim_shopping": {"dia": 3, "titulo": "Suprimentos do Shopping", "texto": "Ele chega a torre com pilhas novas e comida achada numa mochila. Sinais de outro grupo aparecem nas paredes.", "cor_fundo": VERDE_CLARO, "fim_dia": True, "proxima_dia": "d4_inicio"},
    "d3_fim_samuel": {"dia": 3, "titulo": "Samuel e a Torre", "texto": "Samuel ajuda a travar a porta do predio. Rafael percebe que aliados podem valer mais que armas.", "cor_fundo": VERDE_CLARO, "fim_dia": True, "proxima_dia": "d4_inicio"},

    # DIA 4
    "d4_inicio": {
        "dia": 4,
        "titulo": "DIA 4 - A Primeira Verdade",
        "texto": "Rafael sobe ate a sala de transmissao. Entre papeis rasgados, encontra uma gravacao militar: o abrigo norte caiu. Nova evacuacao no porto, dia sete.",
        "cor_fundo": BRANCO,
        "efeitos_entrada": {"comida": -1, "agua": -1, "energia": -7, "moral": -3},
        "proxima": "d4_decisao"
    },
    "d4_decisao": {
        "dia": 4,
        "titulo": "O Porto do Outro Lado",
        "texto": "O porto fica longe, alem de bairros inteiros tomados. No mapa da torre tambem aparecem uma delegacia, uma clinica privada e rotas para reencontrar sobreviventes.",
        "cor_fundo": VERDE,
        "opcoes": [
            {"texto": "Ir direto ao porto", "resultado": "Rafael desce a torre e segue pelo caminho mais curto. O hospital fica no meio da rota.", "proxima": "d4_porto_direto", "efeitos": {"energia": -5}},
            {"texto": "Voltar para buscar aliados", "resultado": "Ele retorna pelas ruas menores, procurando qualquer pessoa que tenha cruzado seu caminho nos ultimos dias.", "proxima": "d4_aliados", "efeitos": {"energia": -8, "moral": 4}},
            {"texto": "Procurar armas na delegacia", "resultado": "A delegacia esta cercada por viaturas queimadas. Algumas celas ainda fazem barulho.", "proxima": "d4_delegacia", "efeitos": {"energia": -6}},
            {"texto": "Investigar a clinica privada", "resultado": "Os papeis citam um laboratorio sob a clinica. Talvez ali exista a origem da praga.", "proxima": "d4_laboratorio", "efeitos": {"moral": -2, "energia": -6}}
        ]
    },
    "d4_porto_direto": {
        "dia": 4,
        "titulo": "Atalho pelo Hospital",
        "texto": "O caminho mais curto atravessa o hospital municipal. As janelas estao marcadas com sangue por dentro. Uma rota maior segue pelo cemiterio.",
        "cor_fundo": VERDE,
        "opcoes": [
            {"texto": "Cortar caminho pelo hospital", "resultado": "Os corredores estao cheios de pacientes trancados. Quando Rafael entende, ja esta cercado.", "final": {"tipo": "derrota", "titulo": "Morte - Hospital", "texto": "O hospital virou uma armadilha. Rafael morre entre macas, portas batendo e monitores sem energia."}, "efeitos": {"vida": -100}},
            {"texto": "Dar a volta pelo cemiterio", "resultado": "Entre lapides quebradas, Rafael evita a horda do hospital e ve os guindastes do porto ao longe.", "proxima": "d4_fim_rio", "efeitos": {"energia": -12, "moral": 2}}
        ]
    },
    "d4_aliados": {
        "dia": 4,
        "titulo": "A Verdade Doi",
        "texto": "Rafael encontra sobreviventes assustados. Todos perguntam pelo abrigo norte. Ele precisa decidir se conta que o abrigo caiu.",
        "cor_fundo": VERDE,
        "opcoes": [
            {"texto": "Contar toda a verdade", "resultado": "A noticia derruba o grupo, mas ninguem perde tempo com ilusoes. Todos aceitam seguir para o porto.", "proxima": "d4_fim_grupo", "efeitos": {"confianca": 3, "moral": 4, "energia": -5}},
            {"texto": "Esconder que o abrigo caiu", "resultado": "A mentira dura pouco. Quando descobrem, a discussao vira gritaria.", "final": {"tipo": "derrota", "titulo": "Morte - Mentira no grupo", "texto": "Os mortos ouvem a briga e invadem o deposito. Rafael cai tentando explicar o que deveria ter dito antes."}, "efeitos": {"vida": -100, "confianca": -5}},
            {"texto": "Pedir voluntarios sem explicar tudo", "resultado": "Alguns seguem Rafael, outros ficam. O grupo e menor, mas se move rapido e em silencio.", "proxima": "d4_fim_grupo_pequeno", "efeitos": {"confianca": 1, "moral": 1, "energia": -4}}
        ]
    },
    "d4_delegacia": {
        "dia": 4,
        "titulo": "Delegacia Cercada",
        "texto": "O arsenal fica no fundo. A sala de documentos fica ao lado. As celas estao cheias de infectados batendo nas grades.",
        "cor_fundo": VERDE,
        "opcoes": [
            {"texto": "Abrir o arsenal", "resultado": "A trava sonora dispara. As celas se abrem uma a uma.", "final": {"tipo": "derrota", "titulo": "Morte - Arsenal", "texto": "Rafael segura a arma, mas nao tem tempo de carregar. A delegacia inteira acorda ao mesmo tempo."}, "efeitos": {"vida": -100}},
            {"texto": "Procurar documentos primeiro", "resultado": "Relatorios mostram que o governo sabia da infeccao antes das sirenes. Rafael pega uma pistola esquecida na mesa.", "proxima": "d4_fim_provas", "itens_add": ["arma de fogo", "provas militares"], "municao_delta": 4, "efeitos": {"moral": -2, "energia": -7}},
            {"texto": "Pegar apenas munição no balcao", "resultado": "Rafael evita o fundo da delegacia, encontra municao solta e sai antes de mexer nas celas.", "proxima": "d4_fim_municao", "municao_delta": 3, "efeitos": {"energia": -4, "moral": 2}}
        ]
    },
    "d4_laboratorio": {
        "dia": 4,
        "titulo": "Laboratorio Subterraneo",
        "texto": "Sob a clinica, luzes de emergencia iluminam macas vazias. Um arquivo cita o Soro Sete e pacientes que resistiram a transformacao por dias.",
        "cor_fundo": VERDE,
        "opcoes": [
            {"texto": "Pegar as amostras do Soro Sete", "resultado": "Rafael guarda os frascos em uma maleta fria. Se isso for real, o porto precisa saber.", "proxima": "d4_fim_soro", "itens_add": ["soro sete"], "efeitos": {"moral": 8, "energia": -8}},
            {"texto": "Assistir as gravacoes dos testes", "resultado": "As imagens mostram pessoas lutando contra a febre. A cura nao existe, mas ha uma forma de atrasar a transformacao.", "proxima": "d4_fim_dados", "itens_add": ["dados do laboratorio"], "efeitos": {"moral": 5, "energia": -5}},
            {"texto": "Entrar na ala de isolamento", "resultado": "A porta fecha sozinha. Algo respira no escuro atras do vidro quebrado.", "final": {"tipo": "derrota", "titulo": "Morte - Isolamento", "texto": "Rafael descobre tarde demais que alguns pacientes ainda andam. A ala de isolamento nao prende mais ninguem."}, "efeitos": {"vida": -100}}
        ]
    },
    "d4_fim_rio": {"dia": 4, "titulo": "Perto do Rio", "texto": "Rafael dorme sob uma ponte menor, ouvindo o porto distante e o estalo de tiros do outro lado da cidade.", "cor_fundo": VERDE_CLARO, "fim_dia": True, "proxima_dia": "d5_inicio"},
    "d4_fim_grupo": {"dia": 4, "titulo": "Grupo Unido", "texto": "A verdade pesa, mas une. Rafael termina o dia com pessoas dispostas a caminhar ate o porto ao seu lado.", "cor_fundo": VERDE_CLARO, "fim_dia": True, "proxima_dia": "d5_inicio"},
    "d4_fim_grupo_pequeno": {"dia": 4, "titulo": "Poucos Passos", "texto": "Nem todos acreditam, mas alguns seguem Rafael. Um grupo menor faz menos barulho e deixa menos rastros.", "cor_fundo": VERDE_CLARO, "fim_dia": True, "proxima_dia": "d5_inicio"},
    "d4_fim_provas": {"dia": 4, "titulo": "Provas e Arma", "texto": "Rafael sai da delegacia com uma arma, poucas balas e provas de que a cidade foi abandonada de proposito.", "cor_fundo": VERDE_CLARO, "fim_dia": True, "proxima_dia": "d5_inicio"},
    "d4_fim_municao": {"dia": 4, "titulo": "Balas Soltas", "texto": "Ele evita o pior da delegacia e dorme num carro de patrulha tombado. Tres balas podem ser tres chances.", "cor_fundo": VERDE_CLARO, "fim_dia": True, "proxima_dia": "d5_inicio"},
    "d4_fim_soro": {"dia": 4, "titulo": "A Maleta Fria", "texto": "O Soro Sete vibra dentro da maleta termica. Rafael nao sabe se carrega salvacao ou apenas outra mentira.", "cor_fundo": VERDE_CLARO, "fim_dia": True, "proxima_dia": "d5_inicio"},
    "d4_fim_dados": {"dia": 4, "titulo": "Dados do Laboratorio", "texto": "Os arquivos mostram que a mordida nao mata todos no mesmo tempo. Essa informacao pode mudar o destino de muita gente.", "cor_fundo": VERDE_CLARO, "fim_dia": True, "proxima_dia": "d5_inicio"},

    # DIA 5
    "d5_inicio": {
        "dia": 5,
        "titulo": "DIA 5 - O Caminho se Divide",
        "texto": "A cidade muda de comportamento. Os mortos seguem sons, cercam portas e parecem lembrar caminhos. O porto fica mais perto, mas cada rota cobra um preco.",
        "cor_fundo": BRANCO,
        "efeitos_entrada": {"comida": -1, "agua": -1, "energia": -6},
        "proxima": "d5_cruzamento"
    },
    "d5_cruzamento": {
        "dia": 5,
        "titulo": "Quatro Caminhos",
        "texto": "A frente, o metro abandonado. A direita, uma ponte quebrada. A esquerda, o bairro militar. No chao, uma tampa leva a tuneis de manutencao.",
        "cor_fundo": VERDE,
        "opcoes": [
            {"texto": "Seguir pelo metro abandonado", "resultado": "Os tuneis do metro estao frios. Vagoes parados guardam malas, sangue seco e celulares sem bateria.", "proxima": "d5_metro", "efeitos": {"energia": -5}},
            {"texto": "Tentar a ponte quebrada", "resultado": "A ponte principal foi bombardeada. Carros pendem sobre o rio e luzes militares piscam do outro lado.", "proxima": "d5_ponte", "efeitos": {"moral": -2}},
            {"texto": "Atravessar o bairro militar", "resultado": "Barricadas cercam o bairro. Cartazes dizem: ninguem entra, ninguem sai.", "proxima": "d5_militar", "efeitos": {"energia": -4}},
            {"texto": "Descer pelo tunel de manutencao", "resultado": "O tunel passa sob quarteiroes inteiros. Marcas recentes mostram que alguem passou ali pela manha.", "proxima": "d5_tunel", "efeitos": {"energia": -6}}
        ]
    },
    "d5_metro": {
        "dia": 5,
        "titulo": "Estacao Sem Luz",
        "texto": "Um trem parado bloqueia a linha. Dentro dele ha pessoas escondidas. Pelos trilhos, talvez seja possivel contornar sem falar com ninguem.",
        "cor_fundo": VERDE,
        "opcoes": [
            {"texto": "Entrar no trem e conversar", "resultado": "Os sobreviventes estao famintos, mas nao hostis. Eles conhecem uma passagem lacrada ate perto do porto.", "proxima": "d5_metro_trem", "efeitos": {"confianca": 1, "moral": 3}},
            {"texto": "Andar pelos trilhos", "resultado": "Rafael evita o grupo e encontra uma caixa de ferramentas esquecida ao lado da linha.", "proxima": "d5_fim_metro_trilhos", "itens_add": ["ferramentas"], "efeitos": {"energia": -10, "moral": 1}}
        ]
    },
    "d5_metro_trem": {
        "dia": 5,
        "titulo": "Sobreviventes no Trem",
        "texto": "Eles pedem comida em troca da rota. Alguns olham para a mochila de Rafael com desespero demais.",
        "cor_fundo": VERDE,
        "opcoes": [
            {"texto": "Dividir comida", "resultado": "A partilha acalma o vagao. Em troca, eles mostram uma saida secreta pela estacao norte.", "proxima": "d5_fim_metro_aliados", "efeitos": {"comida": -1, "confianca": 3, "moral": 5}},
            {"texto": "Roubar enquanto dormem", "resultado": "Um sobrevivente acorda e dispara uma arma no escuro.", "final": {"tipo": "derrota", "titulo": "Morte - Tiro no tunel", "texto": "O tiro nao mata Rafael, mas chama a horda que vivia no metro. Ninguem consegue correr o bastante."}, "efeitos": {"vida": -100, "confianca": -5}}
        ]
    },
    "d5_ponte": {
        "dia": 5,
        "titulo": "A Ponte Bombardeada",
        "texto": "Os destrocos ainda formam uma passagem perigosa. No rio abaixo, um barco de pesca bate contra as pilastras.",
        "cor_fundo": VERDE,
        "opcoes": [
            {"texto": "Atravessar pelos destrocos", "resultado": "O concreto range sob os pes. Cada passo parece fazer a ponte afundar mais.", "proxima": "d5_ponte_destrocos", "efeitos": {"moral": -3}},
            {"texto": "Descer e procurar o barco", "resultado": "Rafael corta uma corda, empurra o barco e atravessa o rio remando devagar.", "proxima": "d5_fim_barco", "itens_add": ["corda"], "efeitos": {"energia": -12, "moral": 4}}
        ]
    },
    "d5_ponte_destrocos": {
        "dia": 5,
        "titulo": "Concreto Cedendo",
        "texto": "A saida esta do outro lado. A horda tambem percebeu a travessia e comeca a subir pela ponte quebrada.",
        "cor_fundo": VERDE,
        "opcoes": [
            {"texto": "Correr", "resultado": "A vibracao faz a estrutura ceder de uma vez.", "final": {"tipo": "derrota", "titulo": "Morte - Queda no rio", "texto": "Rafael cai preso entre ferragens. A agua escura sobe enquanto mortos se jogam da ponte atras dele."}, "efeitos": {"vida": -100}},
            {"texto": "Ir devagar e prender a respiracao", "resultado": "Ele se move no ritmo da ponte, esperando cada tremor passar antes do proximo passo.", "proxima": "d5_fim_ponte", "efeitos": {"energia": -14, "moral": 7}}
        ]
    },
    "d5_militar": {
        "dia": 5,
        "titulo": "Bairro Militar",
        "texto": "Corpos de soldados estao espalhados perto da guarita. Um uniforme limpo demais fica dentro de um jipe. A barreira ainda tem sentinelas vivos.",
        "cor_fundo": VERDE,
        "opcoes": [
            {"texto": "Pegar o uniforme de soldado", "resultado": "O uniforme abre caminho pela primeira barreira, mas Rafael tera que sustentar a mentira.", "proxima": "d5_uniforme", "itens_add": ["uniforme militar"], "efeitos": {"energia": -5, "moral": -1}},
            {"texto": "Entrar como civil", "resultado": "Os guardas restantes nao confiam em ninguem que venha da cidade.", "final": {"tipo": "derrota", "titulo": "Morte - Sem perguntas", "texto": "Rafael levanta as maos, mas o medo dos soldados fala primeiro. O tiro derruba qualquer chance de explicacao."}, "efeitos": {"vida": -100}},
            {"texto": "Contornar o bairro", "resultado": "O desvio e longo, mas evita os homens armados. Rafael encontra uma caixa com sinalizadores.", "proxima": "d5_fim_sinalizadores", "itens_add": ["sinalizadores"], "efeitos": {"energia": -14, "moral": 2}}
        ]
    },
    "d5_uniforme": {
        "dia": 5,
        "titulo": "Dentro da Barreira",
        "texto": "Os soldados falam em abandonar civis ao amanhecer. Um caminhao esta abastecido, mas vigiado por um recruta nervoso.",
        "cor_fundo": VERDE,
        "opcoes": [
            {"texto": "Fingir que esta na evacuacao", "resultado": "Rafael entra no caminhao e sai durante a troca de turno. Leva culpa, mas tambem uma chance.", "proxima": "d5_fim_caminhao", "itens_add": ["caminhao militar"], "municao_delta": 2, "efeitos": {"moral": -4, "energia": -6}},
            {"texto": "Revelar que e sobrevivente", "resultado": "O recruta hesita, mas o oficial nao. Para eles, todos de fora sao risco.", "final": {"tipo": "derrota", "titulo": "Morte - Ordem militar", "texto": "Rafael e retirado da fila e levado para tras da guarita. Ninguem no bairro militar quer testemunhas."}, "efeitos": {"vida": -100}}
        ]
    },
    "d5_tunel": {
        "dia": 5,
        "titulo": "Tunel de Manutencao",
        "texto": "Marcas de giz seguem pela parede. O som da cidade fica distante. O chao, porem, esta molhado e a agua parece subir devagar.",
        "cor_fundo": VERDE,
        "opcoes": [
            {"texto": "Seguir as marcas", "resultado": "As marcas levam a um pequeno abrigo subterraneo e a um mapa de drenagem da cidade.", "proxima": "d5_fim_mapa_sub", "itens_add": ["mapa subterraneo"], "efeitos": {"moral": 6, "energia": -8}},
            {"texto": "Apagar as marcas depois de passar", "resultado": "Rafael apaga o caminho para evitar perseguidores, mas tambem dificulta voltar se precisar.", "proxima": "d5_fim_tunel_solo", "efeitos": {"moral": -2, "energia": -10}},
            {"texto": "Montar acampamento no tunel", "resultado": "A escolha parece segura ate a agua comecar a subir durante a madrugada.", "final": {"tipo": "derrota", "titulo": "Morte - Tunel alagado", "texto": "Rafael acorda tarde demais. A agua apaga a lanterna e leva o ar junto com a esperanca."}, "efeitos": {"vida": -100}}
        ]
    },
    "d5_fim_metro_trilhos": {"dia": 5, "titulo": "Trilhos Frios", "texto": "Rafael dorme numa sala de manutencao. O metro geme como se a cidade respirasse por baixo da terra.", "cor_fundo": VERDE_CLARO, "fim_dia": True, "proxima_dia": "d6_inicio"},
    "d5_fim_metro_aliados": {"dia": 5, "titulo": "Estacao Lacrada", "texto": "A passagem secreta aproxima Rafael do porto. Pessoas famintas ainda conseguem dividir esperanca.", "cor_fundo": VERDE_CLARO, "fim_dia": True, "proxima_dia": "d6_inicio"},
    "d5_fim_barco": {"dia": 5, "titulo": "Barco no Rio", "texto": "O barco fica preso sob a margem oposta. Rafael ouve motores do porto pela primeira vez sem interferencia.", "cor_fundo": VERDE_CLARO, "fim_dia": True, "proxima_dia": "d6_inicio"},
    "d5_fim_ponte": {"dia": 5, "titulo": "Sob a Ponte", "texto": "Rafael cruza sem correr. Passa a noite sob concreto quebrado, perto o bastante para ouvir tiros no porto.", "cor_fundo": VERDE_CLARO, "fim_dia": True, "proxima_dia": "d6_inicio"},
    "d5_fim_sinalizadores": {"dia": 5, "titulo": "Luzes de Emergencia", "texto": "Os sinalizadores podem salvar ou condenar. Rafael guarda cada um como se fosse uma bala de luz.", "cor_fundo": VERDE_CLARO, "fim_dia": True, "proxima_dia": "d6_inicio"},
    "d5_fim_caminhao": {"dia": 5, "titulo": "Caminhao Roubado", "texto": "Rafael dorme na cabine de um caminhao militar. O motor ainda esta quente, e a culpa tambem.", "cor_fundo": VERDE_CLARO, "fim_dia": True, "proxima_dia": "d6_inicio"},
    "d5_fim_mapa_sub": {"dia": 5, "titulo": "Mapa Subterraneo", "texto": "O mapa revela uma linha de drenagem que passa sob o muro da cidade. Talvez o porto nao seja a unica saida.", "cor_fundo": VERDE_CLARO, "fim_dia": True, "proxima_dia": "d6_inicio"},
    "d5_fim_tunel_solo": {"dia": 5, "titulo": "Caminho Apagado", "texto": "Rafael dorme com a sensacao de ter fechado uma porta para os outros e talvez para si mesmo.", "cor_fundo": VERDE_CLARO, "fim_dia": True, "proxima_dia": "d6_inicio"},

    # DIA 6
    "d6_inicio": {
        "dia": 6,
        "titulo": "DIA 6 - Antes do Fim",
        "texto": "Alto-falantes espalhados pela cidade ligam ao mesmo tempo: evacuacao final no porto ao nascer do sol. Cidadaos contaminados serao recusados.",
        "cor_fundo": BRANCO,
        "efeitos_entrada": {"comida": -1, "agua": -1, "energia": -7, "moral": -2},
        "proxima": "d6_escolha"
    },
    "d6_escolha": {
        "dia": 6,
        "titulo": "Ultima Preparacao",
        "texto": "Rafael tem apenas um dia antes da evacuacao. Pode ir ao porto, buscar provas da cura, salvar gente presa ou tentar uma saida fora do controle militar.",
        "cor_fundo": VERDE,
        "opcoes": [
            {"texto": "Ir imediatamente ao porto", "resultado": "Ele chega a zona portuaria e ve filas enormes. Soldados examinam ferimentos e medem febre.", "proxima": "d6_porto", "efeitos": {"energia": -8}},
            {"texto": "Voltar ao laboratorio pelo Soro Sete", "resultado": "A clinica esta mais escura do que antes. O gerador falha e portas automaticas batem sozinhas.", "proxima": "d6_cura", "efeitos": {"energia": -10, "moral": -2}},
            {"texto": "Salvar sobreviventes presos", "resultado": "Gritos de criancas vem de um onibus escolar tombado perto da avenida.", "proxima": "d6_onibus", "efeitos": {"energia": -7}},
            {"texto": "Procurar outra saida da cidade", "resultado": "O mapa e os tuneis indicam uma linha de drenagem sob o muro sul.", "proxima": "d6_saida", "efeitos": {"energia": -8, "moral": 2}}
        ]
    },
    "d6_porto": {
        "dia": 6,
        "titulo": "Triagem Militar",
        "texto": "A fila quase nao anda. Um soldado pergunta se Rafael foi ferido. Um scanner termico examina cada pessoa antes dos portoes.",
        "cor_fundo": VERDE,
        "opcoes": [
            {"texto": "Esconder qualquer ferimento", "resultado": "O scanner acusa febre por causa do cansaco e dos cortes inflamados.", "final": {"tipo": "derrota", "titulo": "Morte - Suspeito de infeccao", "texto": "Rafael e separado da fila. Os soldados nao esperam explicacoes quando a horda ja aparece nas ruas atras do porto."}, "efeitos": {"vida": -100}},
            {"texto": "Contar a verdade", "resultado": "O soldado manda Rafael para quarentena em vez de executa-lo. Ainda ha uma chance de embarcar no dia seguinte.", "proxima": "d6_fim_quarentena", "efeitos": {"confianca": 1, "moral": 3, "energia": -3}}
        ]
    },
    "d6_cura": {
        "dia": 6,
        "titulo": "Soro Sete",
        "texto": "No laboratorio, uma maleta fria permanece ligada a uma bateria. Ha frascos suficientes para teste, mas a dosagem e incerta.",
        "cor_fundo": VERDE,
        "opcoes": [
            {"texto": "Aplicar o soro em si mesmo", "resultado": "A dose queima nas veias e o corpo de Rafael nao aguenta a reacao.", "final": {"tipo": "derrota", "titulo": "Morte - Dose errada", "texto": "Rafael nao vira um morto comum, mas tambem nao continua humano. O laboratorio guarda mais uma falha."}, "efeitos": {"vida": -100}},
            {"texto": "Levar o soro ao porto", "resultado": "Rafael protege a maleta fria e segue pela cidade como se carregasse o ultimo fosforo do mundo.", "proxima": "d6_fim_soro_porto", "itens_add": ["soro sete"], "efeitos": {"moral": 8, "energia": -10}}
        ]
    },
    "d6_onibus": {
        "dia": 6,
        "titulo": "Onibus Escolar Tombado",
        "texto": "As criancas estao presas entre bancos amassados. Os mortos se aproximam pela rua. Abrir a porta vai fazer barulho.",
        "cor_fundo": VERDE,
        "opcoes": [
            {"texto": "Abrir a porta com cuidado", "requer_item": "pe de cabra", "resultado": "Rafael usa o pe de cabra e tira as criancas uma a uma. Uma delas conhece uma entrada lateral do porto.", "proxima": "d6_fim_criancas", "itens_add": ["chave do porto"], "efeitos": {"confianca": 4, "moral": 10, "energia": -12}},
            {"texto": "Ignorar e seguir sozinho", "resultado": "Rafael foge dos gritos. Ele chega mais cedo ao porto, mas o som fica preso na memoria.", "proxima": "d6_fim_sozinho", "efeitos": {"moral": -12, "energia": -4}},
            {"texto": "Atirar na fechadura", "municao_minima": 1, "resultado": "O disparo abre a porta, mas tambem chama a horda inteira.", "final": {"tipo": "derrota", "titulo": "Morte - Disparo errado", "texto": "Rafael salva segundos e perde a vida. O barulho prende todos entre o onibus e a avenida."}, "efeitos": {"vida": -100}, "municao_delta": -1}
        ]
    },
    "d6_saida": {
        "dia": 6,
        "titulo": "Linha de Drenagem",
        "texto": "A rota subterranea passa sob o muro da cidade. Um grupo de soldados tambem procura o mapa e oferece passagem em troca dele.",
        "cor_fundo": VERDE,
        "opcoes": [
            {"texto": "Usar a linha de drenagem", "resultado": "Rafael entra na agua escura e marca o caminho ate uma saida fora dos muros.", "proxima": "d6_fim_drenagem", "itens_add": ["rota subterranea"], "efeitos": {"moral": 7, "energia": -12}},
            {"texto": "Vender o mapa aos militares", "resultado": "Os soldados pegam o mapa, agradecem e fecham o portao antes que Rafael entre.", "final": {"tipo": "derrota", "titulo": "Morte - Traido no portao", "texto": "Sem mapa e sem abrigo, Rafael fica do lado de fora quando a horda chega ao muro sul."}, "efeitos": {"vida": -100, "confianca": -5}}
        ]
    },
    "d6_fim_quarentena": {"dia": 6, "titulo": "Quarentena", "texto": "Rafael passa a noite atras de grades medicas, olhando os navios. A liberdade esta a poucos metros e a um dia de distancia.", "cor_fundo": VERDE_CLARO, "fim_dia": True, "proxima_dia": "d7_inicio"},
    "d6_fim_soro_porto": {"dia": 6, "titulo": "Maleta no Peito", "texto": "Rafael dorme perto do porto com o Soro Sete preso ao peito. Se a maleta quebrar, quebra tambem uma esperanca.", "cor_fundo": VERDE_CLARO, "fim_dia": True, "proxima_dia": "d7_inicio"},
    "d6_fim_criancas": {"dia": 6, "titulo": "Entrada dos Pescadores", "texto": "As criancas guiam Rafael ate um portao lateral usado por pescadores. Salvar pessoas abriu um caminho que mapas nao mostravam.", "cor_fundo": VERDE_CLARO, "fim_dia": True, "proxima_dia": "d7_inicio"},
    "d6_fim_sozinho": {"dia": 6, "titulo": "Cedo Demais, Vazio Demais", "texto": "Rafael chega ao porto antes de muitos, mas a culpa transforma cada minuto de espera em uma condenacao silenciosa.", "cor_fundo": VERDE_CLARO, "fim_dia": True, "proxima_dia": "d7_inicio"},
    "d6_fim_drenagem": {"dia": 6, "titulo": "Sob a Cidade", "texto": "A rota subterranea funciona. Acima dela, milhares de mortos se movem como tempestade. A escolha final vira ao amanhecer.", "cor_fundo": VERDE_CLARO, "fim_dia": True, "proxima_dia": "d7_inicio"},

    # DIA 7
    "d7_inicio": {
        "dia": 7,
        "titulo": "DIA 7 - O Fim da Historia",
        "texto": "O sol nasce vermelho atras dos predios em chamas. As sirenes voltam a tocar, mas agora nao sao aviso. Sao despedida. O porto esta cercado.",
        "cor_fundo": BRANCO,
        "efeitos_entrada": {"comida": -1, "agua": -1, "energia": -5, "moral": -2},
        "proxima": "d7_portao"
    },
    "d7_portao": {
        "dia": 7,
        "titulo": "Quatro Finais Possiveis",
        "texto": "Navios apitam, helicopteros sobem e os mortos descem pelas avenidas. Rafael tem tempo para uma unica decisao antes que os portoes se fechem para sempre.",
        "cor_fundo": VERDE,
        "opcoes": [
            {"texto": "Entrar no navio de evacuacao", "resultado": "Rafael passa pela triagem e entra no navio enquanto os portoes fecham atras dele.", "final": {"tipo": "vitoria", "titulo": "Final 1 - Sobrevivencia Amarga", "texto": "O navio deixa a cidade enquanto o porto e engolido pelos mortos. Rafael sobrevive, mas ve pessoas ficando para tras. Ele escapou da morte, nao da culpa. Uma parte dele fica naquela cidade."}, "efeitos": {"moral": -8, "energia": -3}},
            {"texto": "Entregar o Soro Sete aos cientistas", "requer_item": "soro sete", "resultado": "Rafael entrega a maleta e aceita o risco de provar que o soro pode atrasar a transformacao.", "final": {"tipo": "vitoria", "titulo": "Final 2 - A Cura", "texto": "A febre quase vence Rafael, mas baixa antes do amanhecer seguinte. O soro nao salva todos, mas compra tempo. A cidade caiu, porem a humanidade ganha uma chance real de lutar."}, "efeitos": {"vida": -20, "moral": 15, "confianca": 5}},
            {"texto": "Salvar os sobreviventes fora do portao", "requer_item": "sinalizadores", "resultado": "Rafael cria uma distracao com combustivel, sinalizadores e coragem. A horda muda de direcao.", "final": {"tipo": "vitoria", "titulo": "Final 3 - O Heroi que Ficou", "texto": "Dezenas embarcam por causa de Rafael. Ele fica no cais em chamas, ferido e cercado, mas sorri ao ver o navio partir. Ele nao venceu os mortos; venceu o medo."}, "efeitos": {"vida": -60, "moral": 20, "confianca": 5}},
            {"texto": "Recusar a evacuacao e usar a rota subterranea", "requer_item": "rota subterranea", "resultado": "Rafael reune quem ainda acredita nele e desce para a drenagem antes do porto cair.", "final": {"tipo": "vitoria", "titulo": "Final 4 - Um Novo Comeco", "texto": "O grupo emerge fora dos muros ao amanhecer, coberto de lama e cinzas. A cidade ficou para tras. O mundo continua quebrado, mas agora eles nao procuram apenas sobreviver: procuram reconstruir."}, "itens_add": ["novo acampamento"], "efeitos": {"energia": -15, "moral": 18, "confianca": 4}}
        ]
    }
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
ARQUIVO_PONTUACOES = "pontuacoes.txt"
MAX_RANKING = 10


def nome_atual():
    nome = nome_jogador.strip()
    return nome if nome else "Sobrevivente"


def texto_personalizado(texto):
    return str(texto).replace("Rafael", nome_atual())


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
        escala = min(RET_IMAGEM.width / imagem.get_width(), RET_IMAGEM.height / imagem.get_height())
        nova_largura = int(imagem.get_width() * escala)
        nova_altura = int(imagem.get_height() * escala)
        imagem = pygame.transform.smoothscale(imagem, (nova_largura, nova_altura))
        x = RET_IMAGEM.centerx - nova_largura // 2
        y = RET_IMAGEM.centery - nova_altura // 2
        tela.blit(imagem, (x, y))
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
