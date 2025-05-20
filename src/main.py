from dados import pacientes
from funcoes import get_exames_por_paciente

def main():
    nome = input("Digite o nome do paciente: ")
    exames = get_exames_por_paciente(nome, pacientes)

    if exames:
        print(f"\nExames de {nome}:")
        for exame in exames:
            print(f"- {exame['nome']}: {exame['valor']} (ref: {exame['referencia'][0]} a {exame['referencia'][1]})")
    else:
        print("Paciente não encontrado.")

if __name__ == "__main__":
    main()
