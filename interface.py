def mostrar_menu():
    print("\n" + "=" * 50)
    print(" SISTEMA DE CONTROLE DE PEÇAS INDUSTRIAIS ")
    print("=" * 50)
    print("1. Cadastrar nova peça")
    print("2. Listar peças aprovadas e reprovadas")
    print("3. Remover peça cadastrada")
    print("4. Listar caixas fechadas")
    print("5. Gerar relatório final")
    print("0. Sair")
    print("=" * 50)


def ler_dados_peca():
    print("\n--- CADASTRO DE PEÇA ---")
    id_peca = input("ID da peça: ").strip()
    peso = float(input("Peso da peça (g): "))
    cor = input("Cor da peça: ").strip()
    comprimento = float(input("Comprimento da peça (cm): "))
    return id_peca, peso, cor, comprimento


def mostrar_mensagem(mensagem):
    print(f"\n{mensagem}")


def mostrar_lista_pecas(aprovadas, reprovadas):
    print("\n--- PEÇAS APROVADAS ---")
    if not aprovadas:
        print("Nenhuma peça aprovada.")
    else:
        for peca in aprovadas:
            print(
                f"ID: {peca['id']} | Peso: {peca['peso']}g | "
                f"Cor: {peca['cor']} | Comprimento: {peca['comprimento']}cm"
            )

    print("\n--- PEÇAS REPROVADAS ---")
    if not reprovadas:
        print("Nenhuma peça reprovada.")
    else:
        for peca in reprovadas:
            print(
                f"ID: {peca['id']} | Peso: {peca['peso']}g | "
                f"Cor: {peca['cor']} | Comprimento: {peca['comprimento']}cm"
            )
            print("Motivos:", ", ".join(peca["motivos"]))


def ler_id_remocao():
    print("\n--- REMOVER PEÇA ---")
    return input("Digite o ID da peça a remover: ").strip()


def mostrar_caixas_fechadas(caixas):
    print("\n--- CAIXAS FECHADAS ---")
    if not caixas:
        print("Nenhuma caixa foi fechada ainda.")
        return

    for i, caixa in enumerate(caixas, start=1):
        print(f"\nCaixa {i} - Total de peças: {len(caixa)}")
        for peca in caixa:
            print(
                f"  ID: {peca['id']} | Peso: {peca['peso']}g | "
                f"Cor: {peca['cor']} | Comprimento: {peca['comprimento']}cm"
            )


def mostrar_relatorio(relatorio):
    print("\n--- RELATÓRIO FINAL ---")
    print(f"Total de peças aprovadas: {relatorio['total_aprovadas']}")
    print(f"Total de peças reprovadas: {relatorio['total_reprovadas']}")
    print(f"Quantidade de caixas fechadas: {relatorio['quantidade_caixas']}")
    print(f"Peças na caixa atual: {relatorio['pecas_na_caixa_atual']}")

    print("\nMotivos de reprovação:")
    if not relatorio["motivos_reprovacao"]:
        print("Nenhuma reprovação registrada.")
    else:
        for motivo, quantidade in relatorio["motivos_reprovacao"].items():
            print(f"- {motivo}: {quantidade}")