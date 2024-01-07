import copy

# copy, sorted, produtos.sort
# Exercícios
# Aumente os preços dos produtos a seguir em 10%
# Gere novos_produtos por deep copy (cópia profunda)
produtos = [
    {'nome': 'Produto 5', 'preco': 10.00},
    {'nome': 'Produto 3', 'preco': 10.11},
    {'nome': 'Produto 2', 'preco': 105.87},
    {'nome': 'Produto 4', 'preco': 69.90},
]
def aumento(a):
    acrescimo = (a / 100) * 10
    return a + acrescimo

produtos_alterados = copy.deepcopy(produtos)

for produto in produtos_alterados:
    preco = float(produto['preco'])
    preco_com_juros = aumento(preco)
    produto['preco'] = preco_com_juros

print(produtos_alterados)

# Ordene os produtos por nome decrescente (do maior para menor)
# Gere produtos_ordenados_por_nome por deep copy (cópia profunda)

# Ordene os produtos por preco crescente (do menor para maior)
# Gere produtos_ordenados_por_preco por deep copy (cópia profunda)