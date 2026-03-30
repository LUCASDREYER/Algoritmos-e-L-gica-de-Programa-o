CAIXA_CAPACIDADE = 10


def criar_estado():
    return {
        "pecas_aprovadas": [],
        "pecas_reprovadas": [],
        "caixa_atual": [],
        "caixas_fechadas": []
    }


def avaliar_peca(peso, cor, comprimento):
    motivos = []

    if not (95 <= peso <= 105):
        motivos.append("Peso fora do padrão (95g a 105g)")

    if cor.lower() not in ["azul", "verde"]:
        motivos.append("Cor fora do padrão (azul ou verde)")

    if not (10 <= comprimento <= 20):
        motivos.append("Comprimento fora do padrão (10cm a 20cm)")

    aprovada = len(motivos) == 0
    return aprovada, motivos


def id_ja_existe(estado, id_peca):
    for peca in estado["pecas_aprovadas"]:
        if peca["id"] == id_peca:
            return True

    for peca in estado["pecas_reprovadas"]:
        if peca["id"] == id_peca:
            return True

    for peca in estado["caixa_atual"]:
        if peca["id"] == id_peca:
            return True

    for caixa in estado["caixas_fechadas"]:
        for peca in caixa:
            if peca["id"] == id_peca:
                return True

    return False


def armazenar_em_caixa(estado, peca):
    estado["caixa_atual"].append(peca)

    if len(estado["caixa_atual"]) == CAIXA_CAPACIDADE:
        estado["caixas_fechadas"].append(estado["caixa_atual"].copy())
        estado["caixa_atual"].clear()
        return True

    return False


def cadastrar_peca(estado, id_peca, peso, cor, comprimento):
    if id_ja_existe(estado, id_peca):
        return False, "Já existe uma peça com esse ID."

    aprovada, motivos = avaliar_peca(peso, cor, comprimento)

    peca = {
        "id": id_peca,
        "peso": peso,
        "cor": cor,
        "comprimento": comprimento
    }

    if aprovada:
        estado["pecas_aprovadas"].append(peca)
        caixa_fechada = armazenar_em_caixa(estado, peca)

        if caixa_fechada:
            return True, "Peça aprovada e caixa fechada com 10 peças."
        return True, "Peça aprovada e armazenada na caixa atual."

    peca["motivos"] = motivos
    estado["pecas_reprovadas"].append(peca)
    return True, "Peça reprovada: " + "; ".join(motivos)


def listar_aprovadas(estado):
    return estado["pecas_aprovadas"]


def listar_reprovadas(estado):
    return estado["pecas_reprovadas"]


def listar_caixas_fechadas(estado):
    return estado["caixas_fechadas"]


def remover_peca(estado, id_peca):
    for lista_nome in ["pecas_aprovadas", "pecas_reprovadas"]:
        lista = estado[lista_nome]
        for i, peca in enumerate(lista):
            if peca["id"] == id_peca:
                removida = lista.pop(i)

                if lista_nome == "pecas_aprovadas":
                    for j, peca_caixa in enumerate(estado["caixa_atual"]):
                        if peca_caixa["id"] == id_peca:
                            estado["caixa_atual"].pop(j)
                            break

                return True, removida

    for i, peca in enumerate(estado["caixa_atual"]):
        if peca["id"] == id_peca:
            estado["caixa_atual"].pop(i)
            for j, peca_aprovada in enumerate(estado["pecas_aprovadas"]):
                if peca_aprovada["id"] == id_peca:
                    removida = estado["pecas_aprovadas"].pop(j)
                    return True, removida

    return False, None


def gerar_relatorio(estado):
    total_aprovadas = len(estado["pecas_aprovadas"])
    total_reprovadas = len(estado["pecas_reprovadas"])
    quantidade_caixas = len(estado["caixas_fechadas"])

    motivos_reprovacao = {}
    for peca in estado["pecas_reprovadas"]:
        for motivo in peca["motivos"]:
            if motivo in motivos_reprovacao:
                motivos_reprovacao[motivo] += 1
            else:
                motivos_reprovacao[motivo] = 1

    return {
        "total_aprovadas": total_aprovadas,
        "total_reprovadas": total_reprovadas,
        "quantidade_caixas": quantidade_caixas,
        "pecas_na_caixa_atual": len(estado["caixa_atual"]),
        "motivos_reprovacao": motivos_reprovacao
    }