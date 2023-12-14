lista = []
while 1:
    o = input("[i]nserir  [a]pagar  [l]listar  [s]air: ")
    if o == "i": lista.append(input("Digite o item: "))
    elif o == "a": lista and lista.pop(int(input("Item para apagar: ")) - 1) or print("Lista vazia.")
    elif o == "l": [print(f"{i + 1} --- {item}") for i, item in enumerate(lista)] or print("Lista vazia.")
    elif o == "s": break
    else: print("Opção inválida.")
print("Programa encerrado.")