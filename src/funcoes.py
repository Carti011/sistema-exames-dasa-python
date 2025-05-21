def get_exames_por_paciente(nome, pacientes):
    """
    Retorna a lista de exames de um paciente com base no nome informado.

    Parâmetros:
        nome (str): Nome do paciente a ser buscado.
        pacientes (list): Lista de pacientes com seus dados.

    Retorna:
        list: Lista de exames do paciente, ou None se não encontrado.
    """
    for paciente in pacientes:
        if paciente["nome"].lower() == nome.lower():
            return paciente["exames"]
    return None

def listar_exames_fora_do_limite(paciente):
    """
    Retorna todos os exames do paciente que estão fora da faixa de referência.

    Parâmetros:
        paciente (dict): Dicionário com chave "exames" contendo uma lista de exames.

    Retorna:
        list: Lista de exames que estão fora do limite.
    """
    exames_fora = []
    for exame in paciente["exames"]:
        valor = exame["valor"]
        minimo, maximo = exame["referencia"]
        if valor < minimo or valor > maximo:
            exames_fora.append(exame)
    return exames_fora

def gerar_dicionario_paciente(nome, pacientes):
    """
    Gera um dicionário completo contendo nome, RA e exames de um paciente.

    Parâmetros:
        nome (str): Nome do paciente a ser buscado.
        pacientes (list): Lista de dicionários com pacientes e seus exames.

    Retorna:
        dict: Dicionário com os dados do paciente ou None se não encontrado.
    """
    for paciente in pacientes:
        if paciente["nome"].lower() == nome.lower():
            return {
                "nome": paciente["nome"],
                "ra": paciente["ra"],
                "exames": paciente["exames"]
            }
    return None

def exibir_relatorio_formatado(paciente):
    """
    Exibe no terminal um relatório com nome, RA e exames do paciente,
    indicando quais estão fora ou dentro da faixa de referência.

    Parâmetros:
        paciente (dict): Dicionário com dados do paciente e seus exames.
    """
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
    """
    Ordena a lista de exames em ordem alfabética pelo nome do exame.

    Parâmetros:
        exames (list): Lista de exames.

    Retorna:
        list: Lista ordenada de exames.
    """
    return sorted(exames, key=lambda exame: exame["nome"].lower())

def buscar_exame_por_nome(nome_exame, exames_ordenados):
    """
    Realiza uma busca binária pelo nome do exame na lista de exames ordenada.

    Parâmetros:
        nome_exame (str): Nome do exame a ser buscado.
        exames_ordenados (list): Lista de exames já ordenados por nome.

    Retorna:
        dict: Exame encontrado ou None se não estiver na lista.
    """

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

def salvar_relatorio_em_arquivo(paciente, nome_arquivo="relatorio_paciente.txt"):
    """
    Salva em um arquivo de texto um relatório completo do paciente,
    com nome, RA e status de todos os exames.

    Parâmetros:
        paciente (dict): Dicionário com dados do paciente.
        nome_arquivo (str): Nome do arquivo a ser gerado (padrão: relatorio_paciente.txt).
    """
    with open(nome_arquivo, "w", encoding="utf-8") as arquivo:
        arquivo.write("📋 RELATÓRIO DO PACIENTE\n")
        arquivo.write(f"Nome: {paciente['nome'].capitalize()}\n")
        arquivo.write(f"RA: {paciente['ra']}\n")
        arquivo.write("Exames:\n")

        for exame in paciente["exames"]:
            nome = exame["nome"]
            valor = exame["valor"]
            ref_min, ref_max = exame["referencia"]

            if valor < ref_min or valor > ref_max:
                status = "⚠️ Fora do limite"
            else:
                status = "✓ Dentro do limite"

            arquivo.write(f"- {nome}: {valor} (ref: {ref_min} a {ref_max}) {status}\n")

    print(f"\nRelatório salvo como: {nome_arquivo}")
