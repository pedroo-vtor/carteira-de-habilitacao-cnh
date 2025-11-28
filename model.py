from dataclasses import dataclass
from database import get_connection

# Classe Carteira.
@dataclass
class Carteira:
    id: int
    nome: str
    sobrenome: str
    cpf: str
    nacionalidade: str
    categoria: str
    data_emissao: str = None # formato 'YYYY-MM-DD' ou None
    validade: str = None # formato 'YYYY-MM-DD' ou None

    def to_dict(self):
        """Transforma o objeto em dicionário (para JSON)."""
        return{
            "id": self.id,
            "nome": self.nome,
            "sobrenome": self.sobrenome,
            "cpf": self.cpf,
            "nacionalidade": self.nacionalidade,
            "categoria": self.categoria,
            "data_emissao": self.data_emissao,
            "validade": self.validade,
            }
    
def carteira_from_row(row):
    return Carteira(
        id=row["id"],
        nome=row["nome"],
        sobrenome=row["sobrenome"],
        cpf=row["cpf"],
        nacionalidade=row["nacionalidade"],
        categoria=row["categoria"],
        data_emissao=row["data_emissao"],
        validade=row["validade"],
    )

#Funções de acesso ao banco de dados.

#Listar todas as carteiras (READ).
def listar_carteiras():
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("SELECT * FROM carteiras_habilitacao")
    rows = cur.fetchall()
    conn.close()
    return [carteira_from_row(r) for r in rows]

#Buscar Carteira por ID (READ).
def obter_carteira_por_id(id_carteira):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("SELECT * FROM carteiras_habilitacao WHERE id = ?", (id_carteira,))
    row = cur.fetchone()
    conn.close()
    if row:
        return carteira_from_row(row)
    return None

#Adicionar carteira (CREATE).
def criar_carteira(nome, sobrenome, cpf, nacionalidade, categoria, data_emissao = None, validade=None):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute(
        """
        INSERT INTO carteiras_habilitacao (nome, sobrenome, cpf, nacionalidade, categoria, data_emissao, validade)
        VALUES (?, ?, ?, ?, ?, ?, ?)
        """,
        (nome, sobrenome, cpf, nacionalidade, categoria, data_emissao, validade),
    )
    conn.commit()
    new_id = cur.lastrowid
    conn.close()
    return obter_carteira_por_id(new_id)

#Atualizar as informações da carteira (UPDATE).
def atualizar_carteira(carteira):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute(
        """
        UPDATE carteiras_habilitacao
           SET nome = ?, sobrenome = ?, cpf = ?, nacionalidade = ?, categoria = ?, data_emissao = ?, validade = ?
         WHERE id = ?
        """,
        (carteira.nome, carteira.sobrenome, carteira.cpf, carteira.nacionalidade, carteira.categoria, carteira.data_emissao, carteira.validade, carteira.id),
    )
    conn.commit()
    conn.close()
    return carteira

#Deletar carteira (DELETE).
def deletar_carteira(id_carteira):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("DELETE FROM carteiras_habilitacao WHERE id = ?", (id_carteira,))
    conn.commit()
    deletou = cur.rowcount > 0
    conn.close()
    return deletou