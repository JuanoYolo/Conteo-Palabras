# Análisis de Frecuencia de Palabras

## Autor: Juan Monroy - Ingeniero de Sistemas

Este código en Python analiza la frecuencia de las palabras en un archivo de texto llamado "libro2.txt" o "libro.txt". El código realiza las siguientes tareas:

1. Elimina la puntuación y las "stop words" (palabras comunes que no aportan mucho significado) de cada palabra en el archivo.
2. Cuenta la frecuencia de cada palabra única.
3. Crea un gráfico de barras que muestra la frecuencia de las palabras.

![Conteo de palabras](/img/grafica.png)

## Requisitos

Para ejecutar este código, necesitarás tener instaladas las siguientes bibliotecas de Python:

- `unicodedata`
- `matplotlib.pyplot`
- `numpy`
- `string`

Puedes instalarlas usando `pip`:

## Uso

1. Guarda el código en un archivo, por ejemplo, `word_frequency.py`.
2. Asegúrate de que el archivo "libro2.txt" esté en el mismo directorio que el código.
3. Ejecuta el código:

El código leerá el archivo "libro2.txt", analizará la frecuencia de las palabras y mostrará un gráfico de barras.

## Personalización

Puedes personalizar el código de las siguientes formas:

- Cambiar la lista de "stop words" en la función `eliminar_puntuacion_y_stopwords()`.
- Modificar el título y los ejes del gráfico en las últimas líneas del código.
- Guardar el gráfico en un archivo en lugar de mostrarlo en pantalla.

## Contribución

Si encuentras algún problema o tienes sugerencias de mejora, no dudes en abrir un issue o enviar un pull request en el repositorio de GitHub.