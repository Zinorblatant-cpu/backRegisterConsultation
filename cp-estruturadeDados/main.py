import json

class Paciente:
    def __init__(self, nome, email, cpf, senha, categoria, ativo):
        self.nome = nome
        self.email = email
        self.cpf = cpf
        self.senha = senha
        self.categoria = categoria
        self.ativo = ativo

    def __str__(self):
        return f"{self.nome} ({self.email})"

class Medico:
    def __init__(self, nome, email, cpf, senha, categoria, ativo, especialidade):
        self.nome = nome
        self.email = email
        self.cpf = cpf
        self.senha = senha
        self.categoria = categoria
        self.ativo = ativo
        self.especialidade = especialidade

    def __str__(self):
        return f"{self.nome} - {self.especialidade}"

class Consulta:
    def __init__(self, paciente, medico, data, horario):
        self.paciente = paciente
        self.medico = medico
        self.data = data
        self.horario = horario

    def __str__(self):
        return f"Consulta: {self.paciente.nome} com Dr(a). {self.medico.nome} em {self.data} às {self.horario}"

def carregar_dados():
    try:
        with open("dados.json", "r", encoding="utf-8") as arquivo:
            dados = json.load(arquivo)
    except FileNotFoundError:
        dados = {"pacientes": [], "medicos": []}
    return dados

def salvar_dados(dados):
    with open("dados.json", "w", encoding="utf-8") as arquivo:
        json.dump(dados, arquivo, ensure_ascii=False, indent=4)

def cadastrar_paciente(pacientes):
    print("\n--- Cadastro de Paciente ---")
    nome = input("Insira seu nome: ")
    email = input("Insira seu e-mail: ")
    cpf = input("Insira seu CPF: ")
    senha = input("Insira sua senha: ")
    categoria = input("Insira a categoria (ex.: cliente): ")
    ativo = True

    paciente = Paciente(nome, email, cpf, senha, categoria, ativo)
    pacientes.append(paciente)
    print("Paciente cadastrado com sucesso!")

def cadastrar_medico(medicos):
    print("\n--- Cadastro de Médico ---")
    nome = input("Insira seu nome: ")
    email = input("Insira seu e-mail: ")
    cpf = input("Insira seu CPF: ")
    senha = input("Insira sua senha: ")
    categoria = input("Insira a categoria (ex.: médico): ")
    especialidade = input("Insira sua especialidade: ")
    ativo = True

    medico = Medico(nome, email, cpf, senha, categoria, ativo, especialidade)
    medicos.append(medico)
    print("Médico cadastrado com sucesso!")

def marcar_consulta(pacientes, medicos, consultas):
    print("\n--- Marcar Consulta ---")
    if not pacientes or not medicos:
        print("É necessário cadastrar pelo menos um paciente e um médico antes de marcar uma consulta.")
        return

    print("Pacientes disponíveis:")
    for i, paciente in enumerate(pacientes):
        print(f"{i + 1}. {paciente}")

    escolha_paciente = int(input("Escolha o número do paciente: ")) - 1
    if escolha_paciente < 0 or escolha_paciente >= len(pacientes):
        print("Escolha inválida.")
        return
    paciente = pacientes[escolha_paciente]

    print("\nMédicos disponíveis:")
    for i, medico in enumerate(medicos):
        print(f"{i + 1}. {medico}")

    escolha_medico = int(input("Escolha o número do médico: ")) - 1
    if escolha_medico < 0 or escolha_medico >= len(medicos):
        print("Escolha inválida.")
        return
    medico = medicos[escolha_medico]

    data = input("Data da consulta (DD/MM/AAAA): ")
    horario = input("Horário da consulta (HH:MM): ")

    consulta = Consulta(paciente, medico, data, horario)
    consultas.append(consulta)
    print("Consulta marcada com sucesso!")

def menu():
    dados = carregar_dados()
    pacientes = [Paciente(**p) for p in dados["pacientes"]]
    medicos = [Medico(**m) for m in dados["medicos"]]
    consultas = []

    while True:
        print("\n--- Sistema de Marcação de Consultas ---")
        print("1. Cadastrar Paciente")
        print("2. Cadastrar Médico")
        print("3. Marcar Consulta")
        print("4. Listar Consultas")
        print("5. Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            cadastrar_paciente(pacientes)

        elif opcao == "2":
            cadastrar_medico(medicos)

        elif opcao == "3":
            marcar_consulta(pacientes, medicos, consultas)

        elif opcao == "4":
            if not consultas:
                print("Nenhuma consulta marcada.")
            else:
                print("\n--- Consultas Marcadas ---")
                for consulta in consultas:
                    print(consulta)

        elif opcao == "5":
            dados["pacientes"] = [
                {
                    "nome": p.nome,
                    "email": p.email,
                    "cpf": p.cpf,
                    "senha": p.senha,
                    "categoria": p.categoria,
                    "ativo": p.ativo,
                }
                for p in pacientes
            ]
            dados["medicos"] = [
                {
                    "nome": m.nome,
                    "email": m.email,
                    "cpf": m.cpf,
                    "senha": m.senha,
                    "categoria": m.categoria,
                    "ativo": m.ativo,
                    "especialidade": m.especialidade,
                }
                for m in medicos
            ]
            salvar_dados(dados)
            print("Dados salvos com sucesso!")
            print("Saindo do sistema...")
            break

        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    menu()