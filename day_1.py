# Specifically, they need you to find the two entries
# that sum to 2020 and then multiply those two numbers
# together.
f = open("day_1_input.txt", "r")
text = f.read()
lista = text.split("\n")[:-1]
lista_final = [int(i) for i in lista]

objetivo = 2020

lista_operador_segundo = [objetivo - i for i in lista_final]


lista_respuesta = []
for elemento in lista_final:
    if elemento in lista_operador_segundo:
        lista_respuesta.append(elemento)
respuesta = lista_respuesta[0] * lista_respuesta[1]
print(respuesta)
