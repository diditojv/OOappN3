import database as db
import os

def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')

def pausar():
    input("\nPressione Enter para continuar...")

def adicionar_paciente_ui():
    limpar_tela()
    print("--- Adicionar Novo Paciente ---")
    nome = input("Nome: ")
    cpf = input("CPF (somente números): ")
    telefone = input("Telefone: ")
    
    if not nome or not cpf:
        print("Erro: Nome e CPF são obrigatórios.")
    elif db.adicionar_paciente(nome, cpf, telefone):
        print("\nPaciente adicionado com sucesso!")
    else:
        print("\nErro: CPF já cadastrado.")
    pausar()

def listar_pacientes_ui():
    limpar_tela()
    print("--- Lista de Pacientes Cadastrados ---")
    pacientes = db.listar_pacientes()
    if not pacientes:
        print("Nenhum paciente cadastrado.")
    else:
        for p in pacientes:
            print(f"ID: {p['id']} | Nome: {p['nome']} | CPF: {p['cpf']} | Tel: {p['telefone']}")
    return pacientes

def menu_pacientes():
    while True:
        limpar_tela()
        print("--- Gerenciar Pacientes ---")
        print("1. Adicionar Paciente")
        print("2. Listar Pacientes")
        print("0. Voltar ao Menu Principal")
        escolha = input("Escolha uma opção: ")
        
        if escolha == '1':
            adicionar_paciente_ui()
        elif escolha == '2':
            listar_pacientes_ui()
            pausar()
        elif escolha == '0':
            break
        else:
            print("Opção inválida.")
            pausar()

def adicionar_medico_ui():
    limpar_tela()
    print("--- Adicionar Novo Médico ---")
    nome = input("Nome: ")
    crm = input("CRM (somente números): ")
    especialidade = input("Especialidade: ")
    
    if not nome or not crm:
        print("Erro: Nome e CRM são obrigatórios.")
    elif db.adicionar_medico(nome, crm, especialidade):
        print("\nMédico adicionado com sucesso!")
    else:
        print("\nErro: CRM já cadastrado.")
    pausar()

def listar_medicos_ui():
    limpar_tela()
    print("--- Lista de Médicos Cadastrados ---")
    medicos = db.listar_medicos()
    if not medicos:
        print("Nenhum médico cadastrado.")
    else:
        for m in medicos:
            print(f"ID: {m['id']} | Nome: {m['nome']} | CRM: {m['crm']} | Espec: {m['especialidade']}")
    return medicos

def menu_medicos():
    while True:
        limpar_tela()
        print("--- Gerenciar Médicos ---")
        print("1. Adicionar Médico")
        print("2. Listar Médicos")
        print("0. Voltar ao Menu Principal")
        escolha = input("Escolha uma opção: ")
        
        if escolha == '1':
            adicionar_medico_ui()
        elif escolha == '2':
            listar_medicos_ui()
            pausar()
        elif escolha == '0':
            break
        else:
            print("Opção inválida.")
            pausar()

def agendar_consulta_ui():
    limpar_tela()
    print("--- Agendar Nova Consulta ---")
    
    print("\nPacientes disponíveis:")
    listar_pacientes_ui()
    try:
        paciente_id = int(input("\nDigite o ID do Paciente: "))
    except ValueError:
        print("ID inválido.")
        pausar()
        return

    print("\nMédicos disponíveis:")
    listar_medicos_ui()
    try:
        medico_id = int(input("\nDigite o ID do Médico: "))
    except ValueError:
        print("ID inválido.")
        pausar()
        return

    data = input("Digite a Data (DD/MM/AAAA): ")
    hora = input("Digite a Hora (HH:MM): ")

    if not data or not hora:
        print("Erro: Data e Hora são obrigatórios.")
    elif db.agendar_consulta(paciente_id, medico_id, data, hora):
        print("\nConsulta agendada com sucesso!")
    else:
        print("\nErro ao agendar consulta (verifique se os IDs existem).")
    pausar()

def listar_consultas_ui():
    limpar_tela()
    print("--- Lista de Consultas Agendadas ---")
    consultas = db.listar_consultas()
    
    if not consultas:
        print("Nenhuma consulta agendada.")
    else:
        for c in consultas:
            print(f"ID: {c['id']} | Data: {c['data']} {c['hora']} | Paciente: {c['paciente_nome']} | Médico: {c['medico_nome']}")
    pausar()

def menu_consultas():
    while True:
        limpar_tela()
        print("--- Gerenciar Consultas ---")
        print("1. Agendar Nova Consulta")
        print("2. Listar Consultas Agendadas")
        print("0. Voltar ao Menu Principal")
        escolha = input("Escolha uma opção: ")
        
        if escolha == '1':
            agendar_consulta_ui()
        elif escolha == '2':
            listar_consultas_ui()
        elif escolha == '0':
            break
        else:
            print("Opção inválida.")
            pausar()

def limpar_banco_ui():
    """Pede confirmação e chama a função para limpar o banco."""
    limpar_tela()
    print("--- ATENÇÃO: Limpar Banco de Dados ---")
    print("Esta ação apagará TODOS os pacientes, médicos e consultas.")
    print("A operação não pode ser desfeita.")
    
    confirmacao = input("Você tem certeza absoluta? (digite 'sim' para confirmar): ")
    
    if confirmacao.lower() == 'sim':
        db.limpar_dados()
    else:
        print("\nOperação cancelada.")
    
    pausar()

def main_menu():
    while True:
        limpar_tela()
        print("--- Sistema de Gestão de Clínica (Terminal) ---")
        print("1. Gerenciar Pacientes")
        print("2. Gerenciar Médicos")
        print("3. Gerenciar Consultas")
        print("4. Limpar Banco de Dados (CUIDADO!)") 
        print("0. Sair do Sistema") 
        
        escolha = input("Escolha uma opção: ")
        
        if escolha == '1':
            menu_pacientes()
        elif escolha == '2':
            menu_medicos()
        elif escolha == '3':
            menu_consultas()
        elif escolha == '4':
            limpar_banco_ui()
        elif escolha == '0':
            print("Saindo do sistema...")
            break
        else:
            print("Opção inválida.")
            pausar()