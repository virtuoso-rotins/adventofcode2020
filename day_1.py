# Specifically, they need you to find the two entries
# that sum to 2020 and then multiply those two numbers
# together.
f = open("day_1_input.txt", "r")
text = f.read()
lista = text.split("\n")[:-1]
lista_final = [int(i) for i in lista]

objetivo = 2020

lista_operador_segundo = [objetivo - i for i in lista_final]


lista_respuesta_1 = []
for elemento in lista_final:
    if elemento in lista_operador_segundo:
        lista_respuesta_1.append(elemento)
respuesta_1 = lista_respuesta_1[0] * lista_respuesta_1[1]
print("Respuesta primer problema:")
print(respuesta_1)


# lista_ejemplo = [1721, 979, 366, 299, 675, 1456]
# lista_ejemplo_operador_segundo = [objetivo - i for i in lista_ejemplo]

lista_candidatos = []
for i in range(len(lista_final)):
    for j in range(len(lista_final)):
        if lista_final[i] + lista_final[j] < objetivo:
            for k in range(len(lista_final)):
                if lista_final[i] + lista_final[j] + lista_final[k] == objetivo:
                    lista_candidatos.append(lista_final[i])
                    lista_candidatos.append(lista_final[j])
                    lista_candidatos.append(lista_final[k])
numeros_finales = set(lista_candidatos)

import math
respuesta_2 = math.prod(numeros_finales)
print("Numeros_finales:")
print(numeros_finales)
print("Respuesta segundo problema:")
print(respuesta_2)
