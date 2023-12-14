
# def mult(*args):
#     print(args)
    
#     for numero in args:
#         print(numero)
#         numero * numero

# mult(2,3,3)

def mult(*args):
    total = 1
    for numero in args:
        total *= numero
    return total


mult_de_numeros = mult(3,5,10)
print(mult_de_numeros)

def par(a):
    if a % 2 == 0:
        return print("Este numero é Par")
    else:
        return print("Este numero é Impar")
    
numero = par(15)

        