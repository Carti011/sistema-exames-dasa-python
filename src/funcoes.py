def get_exames_por_paciente(nome, pacientes):
    for paciente in pacientes:
        if paciente["nome"].lower() == nome.lower():
            return paciente["exames"]
    return None
