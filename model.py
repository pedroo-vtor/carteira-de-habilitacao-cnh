# Classe Carteira.
class Carteira:
    _id_counter = 1 # contador estático para gerar IDs

    def __init__(self, nome, sobrenome, cpf, nacionalidade, categoria, data_emissao, validade):
        self.id = Carteira._id_counter
        self.nome = nome
        self.sobrenome = sobrenome
        self.cpf = cpf
        self.nacionalidade = nacionalidade
        self.categoria = categoria
        self.data_emissao = data_emissao
        self.validade = validade
        Carteira._id_counter += 1

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
            "validade": self.validade
            }

#"Banco de dados" em memória.
bd_carteiras = [
    Carteira("Maria", "Oliveira", "12345678901", "Brasileira", "B", "2024-01-15", "2030-01-15"),
    Carteira("Carlos", "Santos", "98765432100", "Brasileiro", "B", "2023-11-02", "2029-11-02")
]

#Funções de acesso aos dados.
#Listar todas as carteiras (READ).
def listar():
    return [carteira.to_dict() for carteira in bd_carteiras]

#Adicionar carteira (CREATE).
def adicionar(carteira: Carteira):
    bd_carteiras.append(carteira)
    return carteira.to_dict()

#Buscar ID da Carteira.
def buscar_id(carteira_id):
    for carteira in bd_carteiras:
        if carteira.id == carteira_id:
            return carteira
    return None

#Atualizar as informações da carteira (UPDATE).
def atualizar(carteira_id, 
              novo_nome=None, 
              novo_sobrenome=None, 
              novo_cpf=None,
              nova_nacionalidade=None,
              nova_categoria=None,
              nova_data_emissao=None, 
              nova_validade=None):
    carteira = buscar_id(carteira_id)
    if carteira:
        if novo_nome:
            carteira.nome = novo_nome
        if novo_sobrenome:
            carteira.sobrenome = novo_sobrenome
        if novo_cpf:
            carteira.cpf = novo_cpf
        if nova_nacionalidade:
            carteira.nacionalidade = nova_nacionalidade
        if nova_categoria:
            carteira.categoria = nova_categoria
        if nova_data_emissao:
            carteira.data_emissao = nova_data_emissao
        if nova_validade:
            carteira.validade = nova_validade
        return carteira.to_dict()
    return None

#Deletar carteira (DELETE).
def deletar(carteira_id):
    carteira = buscar_id(carteira_id)
    if carteira:
        bd_carteiras.remove(carteira)
        return carteira.to_dict()
    return None