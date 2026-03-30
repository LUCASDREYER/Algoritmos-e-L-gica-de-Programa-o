from functions import (
    criar_estado,
    cadastrar_peca,
    listar_aprovadas,
    listar_reprovadas,
    remover_peca,
    listar_caixas_fechadas,
    gerar_relatorio
)

from interface import (
    mostrar_menu,
    ler_dados_peca,
    mostrar_mensagem,
    mostrar_lista_pecas,
    ler_id_remocao,
    mostrar_caixas_fechadas,
    mostrar_relatorio
)


def main():
    estado = criar_estado()

    while True:
        mostrar_menu()
        opcao = input("Escolha uma opção: ").strip()

        if opcao == "1":
            try:
                id_peca, peso, cor, comprimento = ler_dados_peca()
                sucesso, mensagem = cadastrar_peca(
                    estado, id_peca, peso, cor, comprimento
                )
                mostrar_mensagem(mensagem)
            except ValueError:
                mostrar_mensagem("Erro: peso e comprimento devem ser números válidos.")

        elif opcao == "2":
            aprovadas = listar_aprovadas(estado)
            reprovadas = listar_reprovadas(estado)
            mostrar_lista_pecas(aprovadas, reprovadas)

        elif opcao == "3":
            id_peca = ler_id_remocao()
            removida, dados = remover_peca(estado, id_peca)
            if removida:
                mostrar_mensagem(f"Peça {id_peca} removida com sucesso.")
            else:
                mostrar_mensagem("Peça não encontrada.")

        elif opcao == "4":
            caixas = listar_caixas_fechadas(estado)
            mostrar_caixas_fechadas(caixas)

        elif opcao == "5":
            relatorio = gerar_relatorio(estado)
            mostrar_relatorio(relatorio)

        elif opcao == "0":
            mostrar_mensagem("Encerrando o sistema.")
            break

        else:
            mostrar_mensagem("Opção inválida. Tente novamente.")


if __name__ == "__main__":
    main()