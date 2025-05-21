# Lista de pacientes simulados com seus respectivos exames clínicos
pacientes = [
    {
        "nome": "vitoria",  # nome em minúsculo para facilitar comparações
        "ra": "1234567",
        "exames": [
            {
                "nome": "Glicemia",
                "valor": 95,
                "referencia": [70, 99]  # faixa de referência considerada normal
            },
            {
                "nome": "Colesterol",
                "valor": 210,
                "referencia": [0, 200]
            }
        ]
    },
    {
        "nome": "joao",
        "ra": "7654321",
        "exames": [
            {
                "nome": "Triglicerídeos",
                "valor": 180,
                "referencia": [0, 150]
            },
            {
                "nome": "Glicemia",
                "valor": 105,
                "referencia": [70, 99]
            }
        ]
    }
]
