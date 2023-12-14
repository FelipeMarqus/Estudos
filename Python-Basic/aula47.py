palavra_secreta = "Shazam"
letras_certas = ""

while True:
    letra_digitada = input("Digite sua letra: ")

    if len(letra_digitada) > 1:
        print("Digite apenas uma letra.")
        continue

    if letra_digitada in palavra_secreta:
        letras_certas += letra_digitada

    for letras_secreta in palavra_secreta:
        print(letras_secreta)
     