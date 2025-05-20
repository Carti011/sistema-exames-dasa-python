from dados import pacientes
from funcoes import (
    get_exames_por_paciente,
    listar_exames_fora_do_limite,
    gerar_dicionario_paciente,
    exibir_relatorio_formatado
)

def main():
    nome = input("Digite o nome do paciente: ")
    exames = get_exames_por_paciente(nome, pacientes)

    if exames:
        print(f"\nExames de {nome}:")
        for exame in exames:
            print(f"- {exame['nome']}: {exame['valor']} (ref: {exame['referencia'][0]} a {exame['referencia'][1]})")
    else:
        print("Paciente não encontrado.")

    print("\nExames fora da referência:")
    exames_fora = listar_exames_fora_do_limite({"exames": exames})
    if exames_fora:
        for exame in exames_fora:
            print(f"- {exame['nome']}: {exame['valor']} (ref: {exame['referencia'][0]} a {exame['referencia'][1]})")
    else:
        print("Todos os exames estão dentro da referência.")

    dicionario = gerar_dicionario_paciente(nome, pacientes)
    print("\nRelatório formatado do paciente:")
    exibir_relatorio_formatado(dicionario)


if __name__ == "__main__":
    main()
