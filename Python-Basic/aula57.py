salas = [
    ["Maria", "Helena", ],

    ["Elaine", ],

    ["Luiz", "João", "Eduarda", (0, 10, 20, 30, 40) ],
 ]

print(salas[1][0])
print(salas[0][1])
print(salas[2][2])
print(salas[2][3][3])

for sala in salas:
    for alunos in sala:
        print(alunos)
