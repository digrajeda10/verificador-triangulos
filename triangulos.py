def es_numero_valido(valor):
    try:
        numero = float(valor)
        if numero > 0:
            return numero
        else:
            print("El valor debe ser un número positivo.")
            return None
    except ValueError:
        print("El valor ingresado no es un número válido.")
        return None

def validar_triangulo(lado_a, lado_b, lado_c):
    if (lado_a + lado_b > lado_c) and (lado_a + lado_c > lado_b) and (lado_b + lado_c > lado_a):
        return True
    else:
        print("Los lados ingresados no forman un triángulo válido.")
        return False

def determinar_tipo_triangulo(lado_a, lado_b, lado_c):
    if lado_a == lado_b == lado_c:
        return "El triángulo es equilátero."
    elif lado_a == lado_b or lado_a == lado_c or lado_b == lado_c:
        return "El triángulo es isósceles."
    else:
        return "El triángulo es escaleno."

def verificar_triangulo():
    print("Verificador de Triángulos")
    lado_a = lado_b = lado_c = None

    while lado_a is None:
        lado_a = es_numero_valido(input("Ingrese el lado A del triángulo: "))

    while lado_b is None:
        lado_b = es_numero_valido(input("Ingrese el lado B del triángulo: "))

    while lado_c is None:
        lado_c = es_numero_valido(input("Ingrese el lado C del triángulo: "))

    if validar_triangulo(lado_a, lado_b, lado_c):
        print(determinar_tipo_triangulo(lado_a, lado_b, lado_c))
    else:
        print("Intente nuevamente con valores válidos.")

if __name__ == "__main__":
    verificar_triangulo()
