import sqlite3

DB_NAME = 'clinica.db'

def get_db_conn():
    conn = sqlite3.connect(DB_NAME)
    conn.row_factory = sqlite3.Row
    return conn

def init_db():
    conn = get_db_conn()
    cursor = conn.cursor()
    
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS pacientes (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT NOT NULL,
        cpf TEXT NOT NULL UNIQUE,
        telefone TEXT
    )
    ''')
    
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS medicos (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT NOT NULL,
        crm TEXT NOT NULL UNIQUE,
        especialidade TEXT
    )
    ''')
    
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS consultas (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        paciente_id INTEGER NOT NULL,
        medico_id INTEGER NOT NULL,
        data TEXT NOT NULL,
        hora TEXT NOT NULL,
        FOREIGN KEY (paciente_id) REFERENCES pacientes (id),
        FOREIGN KEY (medico_id) REFERENCES medicos (id)
    )
    ''')
    
    conn.commit()
    conn.close()
    print("Banco de dados inicializado com sucesso.")

def adicionar_paciente(nome, cpf, telefone):
    try:
        conn = get_db_conn()
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO pacientes (nome, cpf, telefone) VALUES (?, ?, ?)",
            (nome, cpf, telefone)
        )
        conn.commit()
        conn.close()
        return True
    except sqlite3.IntegrityError:
        return False

def listar_pacientes():
    conn = get_db_conn()
    cursor = conn.cursor()
    cursor.execute("SELECT id, nome, cpf, telefone FROM pacientes")
    pacientes = cursor.fetchall()
    conn.close()
    return pacientes

def adicionar_medico(nome, crm, especialidade):
    try:
        conn = get_db_conn()
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO medicos (nome, crm, especialidade) VALUES (?, ?, ?)",
            (nome, crm, especialidade)
        )
        conn.commit()
        conn.close()
        return True
    except sqlite3.IntegrityError:
        return False

def listar_medicos():
    conn = get_db_conn()
    cursor = conn.cursor()
    cursor.execute("SELECT id, nome, crm, especialidade FROM medicos")
    medicos = cursor.fetchall()
    conn.close()
    return medicos

def agendar_consulta(paciente_id, medico_id, data, hora):
    try:
        conn = get_db_conn()
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO consultas (paciente_id, medico_id, data, hora) VALUES (?, ?, ?, ?)",
            (paciente_id, medico_id, data, hora)
        )
        conn.commit()
        conn.close()
        return True
    except sqlite3.Error as e:
        print(f"Erro ao agendar consulta: {e}")
        return False


def listar_consultas():
    conn = get_db_conn()
    cursor = conn.cursor()
    
    sql = """
    SELECT 
        c.id, c.data, c.hora,
        p.nome as paciente_nome,
        m.nome as medico_nome
    FROM 
        consultas c
    JOIN 
        pacientes p ON c.paciente_id = p.id
    JOIN 
        medicos m ON c.medico_id = m.id
    ORDER BY
        c.data, c.hora
    """
    cursor.execute(sql)
    consultas = cursor.fetchall()
    conn.close()


    return consultas



def limpar_dados():
    """Apaga todos os registros de todas as tabelas, mas mantém a estrutura."""
    conn = get_db_conn()
    cursor = conn.cursor()
    
    
    cursor.execute("DELETE FROM consultas")
    cursor.execute("DELETE FROM medicos")
    cursor.execute("DELETE FROM pacientes")
    
   
    cursor.execute("DELETE FROM sqlite_sequence WHERE name IN ('pacientes', 'medicos', 'consultas')")
    
    conn.commit()
    conn.close()
    print("Todos os dados foram limpos do banco de dados.")