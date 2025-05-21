# 🧬 Sistema de Exames - Dasa (Python)
[![Python](https://img.shields.io/badge/Python-3.10-blue?logo=python&logoColor=white)](https://www.python.org/)

Projeto em Python desenvolvido como parte do desafio acadêmico da disciplina **Dynamic Programming** da FIAP, em parceria com a empresa **Dasa**.

---

## 🚀 Funcionalidades

- 📌 Cadastro de médicos/pacientes com nome, RA e exames
- 🧪 Cadastro e exibição dos exames com valores e faixas de referência
- ⚠️ Identificação de exames fora do limite
- 📋 Geração de relatório formatado no terminal
- 🗂️ Exportação do relatório para arquivo `.txt`
- 🔍 Busca binária de exame por nome
- ✅ Entrada interativa com validações

---

## 🧱 Estrutura do Projeto

* src/
* ├── dados.py # Dados fictícios dos pacientes
* ├── funcoes.py # Lógica e funções reutilizáveis
* ├── main.py # Execução principal do sistema

---
## 💻 Como Executar

1. Clone o repositório:
```bash
git clone https://github.com/SEU_USUARIO/sistema-exames-dasa-python.git
```

2. Execute o main.py:
- python src/main.py

---

## 📎 Exemplo de saída no terminal
Digite o nome do paciente: vitoria

Exames de vitoria:
- Glicemia: 95 (ref: 70 a 99)
- Colesterol: 210 (ref: 0 a 200)

Exames fora da referência:
- Colesterol: 210 (ref: 0 a 200)

📋 RELATÓRIO DO PACIENTE
Nome: Vitoria
RA: 1234567
Exames:
- Glicemia: 95 (ref: 70 a 99) ✓ Dentro do limite
- Colesterol: 210 (ref: 0 a 200) ⚠️ Fora do limite

Relatório salvo como: relatorio_paciente.txt

---

## 📝 Sobre o relatório em .txt
O relatório é salvo automaticamente no mesmo diretório como:
```bash
relatorio_paciente.txt
```
Você pode abrir o arquivo e visualizar os exames com os mesmos dados exibidos no terminal.

---

## 👨‍💻 Autor
<table> <tr> <td><strong>Weslley Cardoso</strong></td> </tr> <tr> <td> 📧 <a href="mailto:weslleycardoso011@gmail.com">weslleycardoso011@gmail.com</a><br> 🌐 <a href="https://github.com/Carti011" target="_blank">GitHub: Carti011</a><br> 💼 <a href="https://www.linkedin.com/in/seu-usuario" target="_blank">LinkedIn: https://www.linkedin.com/in/weslleycarti/</a> </td> </tr> </table>

---
### 📜 Licença
Este projeto é de uso educacional e demonstrativo, criado como parte de um desafio acadêmico.
Você pode utilizar, modificar e compartilhar livremente para fins de aprendizado e portfólio.