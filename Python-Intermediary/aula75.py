def dupli(duplicar):
    print(f'O dobro de {duplicar} é = {duplicar * 2} ')

def triple(numero):
    print(f'O dobro de {numero} é = {numero * 3} ')

def quadru(number):
    print(f'O quadruplo de {number} é = {number * 4} ')
    


valor = 2

dupli(valor)
triple(valor)
quadru(valor)

# Exercícios
# Crie funções que duplicam, triplicam e quadruplicam
# o número recebido como parâmetro.
# def duplicar(numero):
#     return numero * 2


# def triplicar(numero):
#     return numero * 3


# def quadruplicar(numero):
#     return numero * 4
def criar_multiplicador(multiplicador):
    def multiplicar(numero):
        return numero * multiplicador
    return multiplicar


duplicar = criar_multiplicador(2)
triplicar = criar_multiplicador(3)
quadruplicar = criar_multiplicador(4)

print(duplicar(2))
print(triplicar(2))
print(quadruplicar(2))