def busqueda_lineal (data, a_buscar):
    n= len(data)
    i = 0
    while i < len(data):
        if data[i] == numero:
            return i
        i += 1
    return -1

def busqueda_lineal_centinela (data, a_buscar):
    data.append(a_buscar)

    i = 0
    while data[i] != numero:
        i += 1

    data.pop()

    if i < len(data):
        return i
    else:
        return -1

def busqueda_binaria(data, numero):

    i = 0
    fin = len(data) - 1

    while i <= fin:
        medio = (i + fin) // 2

        if data[medio] == numero:
            return medio

        elif data[medio] > numero:
            fin = medio - 1

        else:
            i = medio + 1

    return -1


lista = [7,4,37,55,77,104,256,512]
numero = 104
resultado = busqueda_lineal_centinela(lista, numero)

busqueda_lineal_centinela(lista, numero)


if resultado != -1:
    print(f"Elemento encontrado en el índice: {resultado}")
else:
    print("Elemento no encontrado")