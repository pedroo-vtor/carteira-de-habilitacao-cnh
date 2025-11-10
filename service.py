import model as models
from model import Carteira

#Listar todas as carteiras (READ).
def listar_carteiras():
    return models.listar()

#Adicionar carteira (CREATE).
def adicionar_carteira(dados):
    carteira = Carteira(
        dados["nome"],
        dados["sobrenome"],
        dados["cpf"],
        dados["data_emissao"],
        dados["validade"]
    )
    return models.adicionar(carteira)

#Atualizar as informações da carteira (UPDATE).
def atualizar_carteira(carteira_id, dados):
    if not models.buscar_id(carteira_id):
        raise IndexError("Carteira não encontrada.")
    return models.atualizar(
        carteira_id,
        novo_nome=dados.get("nome"),
        novo_sobrenome=dados.get("sobrenome"),
        nova_data_emissao=dados.get("data_emissao"),
        nova_validade=dados.get("validade")
    )

# Deletar carteira (DELETE).
def deletar_carteira(carteira_id):
    carteira_removida = models.deletar(carteira_id)
    if not carteira_removida:
        raise IndexError("Carteira não encontrada.")
    return carteira_removida