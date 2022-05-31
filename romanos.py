
def convertir_en_romano(numero):
    """
    Restricciones:
        -Es un número natural
        -El número está entre 0 y 3999
            -no es negativo
            -no es mayor que 3999
    Resultado es una cadena que contiene (I, V, X, L, C, D, M)

    Ideas para comprobaar un entero:
        -   (X)isdigit(): porque no aplica a cualquier cosa que no sea cadena
        - (v)convertir a int y si no se puede , error.
        - (v)isinstance()
            - (v)type()
            - (x)isnumeric()

    Pasos:
        1. Validar la entrada
        2a si es válido: lo convierto
        2b si no es váliddo: muestro error.
    """

    if not isinstance(numero, int):
        return "No has introducido un número"
    if numero < 1 or numero > 3999:
        return "El número no es válido (debe ser positivo y menor que 4000)"

#Continuamos con la conversión

simbolos = {
    "I": 1,
    "V": 5,
    "X": 10,
    "L": 50,
    "C": 100,
    "D": 500,
    "M": 1000
}

# Descomponer "numero" en uniades, decenas, centenas, y unidades de millar.
# opción 1; división entera + módulo en cascada
# opción 2: convertir en cadena y en función de la longitud y la posición obtener u, d, c y um


print(convertir_en_romano("3a3"))
print(convertir_en_romano(-3))
print(convertir_en_romano(3333))

# convertir_en_romano("a")