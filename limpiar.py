import unicodedata
import matplotlib.pyplot as plt
import numpy as np
import string


def eliminar_puntuacion_y_stopwords(mini):
    # Definir una lista de stop words
    stopwords = ['de', 'la', 'los', 'el', 'las', 'un', 'y', 'al']
    
    # Remover puntuación usando la tabla de traducción de str.translate
    tabla_puntuacion = str.maketrans('', '', string.punctuation)
    palabra_sin_puntuacion = palabra.translate(tabla_puntuacion)
    
    # Remover stop words
    if palabra_sin_puntuacion.lower() in stopwords:
        return ''
    else:
        return palabra_sin_puntuacion
    
# Abrir el archivo en modo lectura
with open('libro2.txt', 'r', encoding='utf-8') as f:
    # Leer el archivo línea por línea
    palabras = []
    conteo_palabras = {}
    for line in f:
        line_palabras = line.split()
        for palabra in line_palabras:
            palabra_limpia = eliminar_puntuacion_y_stopwords(palabra)
            if palabra_limpia:
                palabras.append(palabra_limpia)
                conteo_palabras[palabra_limpia] = conteo_palabras.get(palabra_limpia, 0) + 1

#print(len(conteo_palabras))
palabras = list(conteo_palabras.keys())
conteo = list(conteo_palabras.values())

# Crear un gráfico de barras
fig, ax = plt.subplots()
ax.bar(palabras, conteo)

# Ajustar los límites del eje x para que los rótulos de las palabras no se solapen
plt.xticks(rotation=45)
ax.set_xlabel('Palabras')
ax.set_ylabel('Conteo')
ax.set_title('Conteo de palabras')

# Mostrar el gráfico
plt.tight_layout()
plt.show()




    
         

      
