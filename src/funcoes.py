def get_exames_por_paciente(nome, pacientes):
    for paciente in pacientes:
        if paciente["nome"].lower() == nome.lower():
            return paciente["exames"]
    return None

def listar_exames_fora_do_limite(paciente):
    exames_fora = []
    for exame in paciente["exames"]:
        valor = exame["valor"]
        minimo, maximo = exame["referencia"]
        if valor < minimo or valor > maximo:
            exames_fora.append(exame)
    return exames_fora

def gerar_dicionario_paciente(nome, pacientes):
    for paciente in pacientes:
        if paciente["nome"].lower() == nome.lower():
            return {
                "nome": paciente["nome"],
                "ra": paciente["ra"],
                "exames": paciente["exames"]
            }
    return None

def exibir_relatorio_formatado(paciente):
    print("\n📋 RELATÓRIO DO PACIENTE")
    print(f"Nome: {paciente['nome'].capitalize()}")
    print(f"RA: {paciente['ra']}")
    print("Exames:")

    for exame in paciente["exames"]:
        nome = exame["nome"]
        valor = exame["valor"]
        ref_min, ref_max = exame["referencia"]

        if valor < ref_min or valor > ref_max:
            status = "⚠️ Fora do limite"
        else:
            status = "✓ Dentro do limite"

        print(f"- {nome}: {valor} (ref: {ref_min} a {ref_max}) {status}")

def ordenar_exames_por_nome(exames):
    return sorted(exames, key=lambda exame: exame["nome"].lower())

def buscar_exame_por_nome(nome_exame, exames_ordenados):
    inicio = 0
    fim = len(exames_ordenados) - 1

    while inicio <= fim:
        meio = (inicio + fim) // 2
        nome_atual = exames_ordenados[meio]["nome"].lower()

        if nome_exame.lower() == nome_atual:
            return exames_ordenados[meio]
        elif nome_exame.lower() < nome_atual:
            fim = meio - 1
        else:
            inicio = meio + 1

    return None
