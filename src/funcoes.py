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
