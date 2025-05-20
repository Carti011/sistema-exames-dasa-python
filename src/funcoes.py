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
