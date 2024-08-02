# Verificador de Triángulos

Este es un programa de consola en Python que permite verificar el tipo de triángulo ingresando los valores de sus lados. El programa identifica si un triángulo es equilátero, isósceles o escaleno.

## Instrucciones

Para ejecutar el programa, abre una terminal en la carpeta del proyecto y ejecuta: `python verificador_triangulos.py`.

### Requisitos

- Python instalado en tu sistema. Puedes usar cualquier entorno de desarrollo que soporte Python, como Visual Studio Code o PyCharm.

### Instalación

1. Clona este repositorio en tu máquina local ejecutando el siguiente comando en tu terminal: `git clone https://github.com/digrajeda10/verificador-triangulos.git`.

2. Alternativamente, puedes simplemente descargar el archivo `verificador_triangulos.py` desde el repositorio.

### Ejemplos de uso

- **Triángulo equilátero:**  
  Ingrese los lados: 5, 5, 5  
  Salida esperada: El triángulo es equilátero.

- **Triángulo isósceles:**  
  Ingrese los lados: 7, 7, 4  
  Salida esperada: El triángulo es isósceles.

- **Triángulo escaleno:**  
  Ingrese los lados: 8, 6, 7  
  Salida esperada: El triángulo es escaleno.

- **Lados inválidos:**  
  Ingrese los lados: 1, 2, 10  
  Salida esperada: Los lados ingresados no forman un triángulo válido.

- **Datos incorrectos:**  
  Ingrese valores no numéricos, como letras o símbolos: a, b, c  
  Salida esperada: El valor ingresado no es un número válido.

  Ingrese valores negativos: -3, 4, 5  
  Salida esperada: El valor debe ser un número positivo.

  Ingrese un lado con valor cero: 0, 4, 5  
  Salida esperada: El valor debe ser un número positivo.
