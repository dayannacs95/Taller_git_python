def leer_archivo(nombre_archivo):
    diccionario_palabras = {}
    archivo=open(nombre_archivo,"r",encoding="utf-8")
    for linea in archivo:
        palabras = linea.split()
        for palabra in palabras:
            palabra = palabra.lower().strip('.,;:"\'()!?')
            if palabra in diccionario_palabras:
                diccionario_palabras[palabra] += 1
            else:
                diccionario_palabras[palabra] = 1
    return diccionario_palabras

def guardar_diccionario(diccionario, nuevo_archivo):
    archivo2=open(nuevo_archivo,"w",encoding="utf-8")
    for palabra, frecuencia in diccionario.items():
        archivo2.write(f'{palabra}: {frecuencia}\n')

""""
diccpalabras=leer_archivo("texto.txt")
print(diccpalabras)
frecuencia_palabras=guardar_diccionario(diccpalabras, "diccionario.txt")
"""