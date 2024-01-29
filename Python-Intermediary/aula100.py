import copy

# Exercícios
# Aumente os preços dos produtos a seguir em 10%
# Gere novos_produtos por deep copy (cópia profunda)

produtos = [
    {'nome': 'Produto 5', 'preco': 10.00},
    {'nome': 'Produto 3', 'preco': 10.11},
    {'nome': 'Produto 2', 'preco': 105.87},
    {'nome': 'Produto 4', 'preco': 69.90},
]

nova_lista = copy.deepcopy(produtos)

def aumento(a):
    porcentagem = a / 100 * 10
    return a + porcentagem


for i, produto in enumerate(produtos):
    novo_aumento = aumento(float(produto['preco']))
    nova_lista[i]['preco'] = novo_aumento






# Ordene os produtos por nome decrescente (do maior para menor)
# Gere produtos_ordenados_por_nome por deep copy (cópia profunda)

produtos_ordenados_por_nome = sorted(copy.deepcopy(nova_lista), key=lambda x: x['nome'], reverse= True)

print(produtos_ordenados_por_nome)


# Ordene os produtos por preco crescente (do menor para maior)
# Gere produtos_ordenados_por_preco por deep copy (cópia profunda)

produtos_ordenados_por_preco = sorted(copy.deepcopy(nova_lista), key=lambda x: x['preco'])

print(produtos_ordenados_por_preco)