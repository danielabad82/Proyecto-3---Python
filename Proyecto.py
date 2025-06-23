"""1.  Escribe una función que reciba una cadena de texto como parámetro y devuelva un diccionario con las frecuencias de cada letra
 en la cadena. Los espacios no deben ser considerados."""

def frecuencias_letras(cadena):
    diccionario = {}
    for letra in cadena:
        if letra != " ":
            diccionario[letra] = diccionario.get(letra, 0) + 1
    return diccionario

# Uso de la función
texto = "ejercicio primero de la kata"
print(frecuencias_letras(texto))


"""2. Dada una lista de números, obtén una nueva lista con el doble de cada valor. Usa la función map()."""

def doblar_lista(lista):
    return list(map(lambda x: x * 2, lista))

# Uso de la función
numeros = [1, 2, 3, 4, 5]
doblados = doblar_lista(numeros)
print(doblados)


"""3. Escribe una función que tome una lista de palabras y una palabra objetivo como parámetros. 
La función debe devolver una lista con todas las palabras de la lista original que contengan la palabra objetivo."""

def palabras_con_objetivo(lista_palabras, objetivo):
    return [palabra for palabra in lista_palabras if objetivo in palabra]

# Uso de la función
palabras = ["manzana", "banana", "melón", "naranja", "albaricoque","mandarina", "sandía"]
objetivo = "an"
resultado = palabras_con_objetivo(palabras, objetivo)
print(resultado)


"""4. Genera una función que calcule la diferencia entre los valores de dos listas. Usa la función map()."""

def diferencia_listas(lista1, lista2):
    return list(map(lambda x, y: x - y, lista1, lista2))

# Uso de la función
l1 = [10, 20, 30, 40]
l2 = [1, 2, 3, 4]
diferencias = diferencia_listas(l1, l2)
print(diferencias)


"""5. Escribe una función que tome una lista de números como parámetro y un valor opcional nota_aprobado, que por
defecto es 5. La función debe calcular la media de los números en la lista y determinar si la media es mayor o igual
que nota aprobado. Si es así, el estado será "aprobado", de lo contrario, será "suspenso". La función debe devolver
una tupla que contenga la media y el estado."""

def estado_media(lista, nota_aprobado=5):
    if not lista:
        return (None, "sin datos")
    media = sum(lista) / len(lista)
    estado = "aprobado" if media >= nota_aprobado else "suspenso"
    return (media, estado)

# Uso de la función
notas = [6, 7, 5, 8, 4]
print(estado_media(notas))
print(estado_media(notas, nota_aprobado=7))


"""6. Escribe una función que calcule el factorial de un número de manera recursiva."""

def factorial(n):
    if n < 0:
        raise ValueError("El número debe ser no negativo")
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)

# Uso de la función
print(factorial(6))


"""7. Genera una función que convierta una lista de tuplas a una lista de strings. Usa la función map()."""

def tuplas_a_strings(lista_tuplas):
    return list(map(lambda t: str(t), lista_tuplas))

# Uso de la función
lista = [(1, 2), (3, 4), ("a", "b")]
resultado = tuplas_a_strings(lista)
print(resultado)


"""8. Escribe un programa que pida al usuario dos números e intente dividirlos. Si el usuario ingresa un valor no numérico
o intenta dividir por cero, maneja esas excepciones de manera adecuada. Asegúrate de mostrar un mensaje
indicando si la división fue exitosa o no."""

try:
    num1 = float(input("Introduce el primer número: "))
    num2 = float(input("Introduce el segundo número: "))
    resultado = num1 / num2
except ValueError:
    print("Error: Debes introducir valores numéricos.")
except ZeroDivisionError:
    print("Error: No se puede dividir por cero.")
else:
    print(f"La división fue exitosa. Resultado: {resultado}")
finally:
    print(f"Programa finalizado.")


"""9. Escribe una función que tome una lista de nombres de mascotas como parámetro y devuelva una nueva lista
excluyendo ciertas mascotas prohibidas en España. La lista de mascotas a excluir es ["Mapache", "Tigre",
"Serpiente Pitón", "Cocodrilo", "Oso"].Usa la función filter()"""

def filtrar_mascotas(lista_mascotas):
    prohibidas = ["Mapache", "Tigre", "Serpiente Pitón", "Cocodrilo", "Oso"]
    return list(filter(lambda mascota: mascota not in prohibidas, lista_mascotas))

# Uso de la función
mascotas = ["Perro", "Gato", "Tigre", "Canario", "Mapache", "Conejo", "Oso"]
mascotas_filtradas = filtrar_mascotas(mascotas)
print(mascotas_filtradas)

"""10.Escribe una función que reciba una lista de números y calcule su promedio. Si la lista está vacía, lanza una
excepción personalizada y maneja el error adecuadamente."""

class ListaVaciaError(Exception):
    pass

def promedio_lista(lista):
    if not lista:
        raise ListaVaciaError("La lista está vacía. No se puede calcular el promedio.")
    return sum(lista) / len(lista)

# Uso de la función
try:
    print(promedio_lista([2, 4, 6, 8]))
    print(promedio_lista([]))
except ListaVaciaError as e:
    print(f"Error: {e}")


"""11. Escribe un programa que pida al usuario que introduzca su edad. Si el usuario ingresa un valor no numérico o un
valor fuera del rango esperado (por ejemplo, menor que 0 o mayor que 120), maneja las excepciones adecuadamente."""
try:
    edad = int(input("Introduce tu edad: "))
    if edad < 0 or edad > 120:
        raise ValueError("La edad debe estar entre 0 y 120 años.")
except ValueError as e:
    print(f"Error: {e}")
else:
    print(f"Edad introducida correctamente: {edad}")
finally:
    print("Programa finalizado.")

"""12. Genera una función que al recibir una frase devuelva una lista con la longitud de cada palabra. Usa la función map()"""

def longitudes_palabras(frase):
    palabras = frase.split()
    return list(map(len, palabras))

# Uso de la función
frase = "Ayer fuí a la piscina pero había mucha gente y me volví pronto a casa"
print(longitudes_palabras(frase))


"""13. Genera una función la cual, para un conjunto de caracteres, devuelva una lista de tuplas con cada letra en
mayúsculas y minúsculas. Las letras no pueden estar repetidas .Usa la función map()"""

def mayus_minus_tuplas(conjunto):
    unicas = set(conjunto)
    return list(map(lambda c: (c.upper(), c.lower()), unicas))

# Uso de la función
caracteres = "abracadabra"
print(mayus_minus_tuplas(caracteres))


"""14.  Crea una función que retorne las palabras de una lista de palabras que comience con una letra en especifico. Usa la
función filter()."""

def palabras_con_letra(lista_palabras, letra):
    return list(filter(lambda palabra: palabra.startswith(letra), lista_palabras))

# Uso de la función
palabras = ["manzana", "melón", "pera", "mango", "plátano", "mandarina"]
print(palabras_con_letra(palabras, "m"))



"""15. Crea una función lambda que sume 3 a cada número de una lista dada."""

sumar_tres = lambda lista: list(map(lambda x: x + 3, lista))

# Uso de la función
numeros = [1, 2, 3, 4, 5]
print(sumar_tres(numeros))


"""16. Escribe una función que tome una cadena de texto y un número entero n como parámetros y devuelva una lista de
todas las palabras que sean más largas que n. Usa la función filter()."""

def palabras_mas_largas_que(texto, n):
    palabras = texto.split()
    return list(filter(lambda palabra: len(palabra) > n, palabras))

# Uso de la función
frase = "El conocimiento es poder y la práctica hace al maestro"
print(palabras_mas_largas_que(frase, 6))


"""17. Crea una función que tome una lista de dígitos y devuelva el número correspondiente. Por ejemplo, (5,7,2)
corresponde al número quinientos setenta y dos (572). Usa la función reduce()."""

from functools import reduce

def digitos_a_numero(lista_digitos):
    return reduce(lambda x, y: x * 10 + y, lista_digitos)

# Uso de la función
digitos = [5, 7, 2]
print(digitos_a_numero(digitos))


"""18. Escribe un programa en Python que cree una lista de diccionarios que contenga información de estudiantes
(nombre, edad, calificación) y use la función filter para extraer a los estudiantes con una calificación mayor o igual a
90. Usa la función filter()"""

estudiantes = [
    {"nombre": "Ana", "edad": 20, "calificacion": 95},
    {"nombre": "Luis", "edad": 22, "calificacion": 88},
    {"nombre": "Marta", "edad": 21, "calificacion": 91},
    {"nombre": "Pedro", "edad": 23, "calificacion": 76},
    {"nombre": "Lucía", "edad": 20, "calificacion": 90}
]

aprobados_90 = list(filter(lambda est: est["calificacion"] >= 90, estudiantes))
print(aprobados_90)


"""19. Crea una función lambda que filtre los números impares de una lista dada."""

filtrar_impares = lambda lista: list(filter(lambda x: x % 2 != 0, lista))

# Uso de la función
numeros = [1, 2, 3, 4, 5, 6, 15, 18, 19]
print(filtrar_impares(numeros))


"""20.  Para una lista con elementos tipo integer y string obtén una nueva lista sólo con los valores int. Usa la función
filter()."""

def filtrar_enteros(lista):
    return list(filter(lambda x: isinstance(x, int), lista))

# Uso de la función
elementos = [1, "dos", 3, "cuatro", 5, "seis", 7]
print(filtrar_enteros(elementos))


"""21. Crea una función que calcule el cubo de un número dado mediante una función lambda."""
cubo = lambda x: x ** 3

# Uso de la función
print(cubo(2))
print(cubo(5))

"""22. Dada una lista numérica, obtén el producto total de los valores de dicha lista.Usa la función reduce()."""
from functools import reduce

def producto_total(lista):
    return reduce(lambda x, y: x * y, lista)

# Uso de la función
numeros = [2, 3, 4, 5]
print(producto_total(numeros))


"""23. Función que concatena una lista de palabras usando reduce()."""
from functools import reduce

def concatenar_palabras(lista):
    return reduce(lambda x, y: x + y, lista)

# Uso de la función
palabras = ["Hoy", " ", "ya", " no", " hay", " colegios", "!"]
print(concatenar_palabras(palabras))


"""24. Calcula la diferencia total en los valores de una lista. Usa la función reduce()."""
from functools import reduce

def diferencia_total(lista):
    return reduce(lambda x, y: x - y, lista)

# Uso de la función
numeros = [20, 5, 3, 2]
print(diferencia_total(numeros))


"""25. Función que cuenta el número de caracteres en una cadena de texto dada."""
def contar_caracteres(cadena):
    return len(cadena)

# Uso de la función
texto = "Se acercan las vacaciones"
print(contar_caracteres(texto))


"""26. Crea una función lambda que calcule el resto de la división entre dos números dados."""
resto = lambda x, y: x % y

# Uso de la función
print(resto(10, 3))
print(resto(25, 7))


"""27. Crea una función que calcule el promedio de una lista de números."""
def promedio(lista):
    if not lista:
        return None
    return sum(lista) / len(lista)

# Uso de la función
numeros = [4, 8, 15, 16, 23, 42]
print(promedio(numeros))


"""28. Crea una función que busque y devuelva el primer elemento duplicado en una lista dada."""
def primer_duplicado(lista):
    vistos = set()
    for elemento in lista:
        if elemento in vistos:
            return elemento
        vistos.add(elemento)
    return None

# Uso de la función
valores = [3, 5, 1, 4, 5, 2, 3]
print(primer_duplicado(valores))


"""29. Crea una función que convierta una variable en una cadena de texto y enmascare todos los caracteres con el
carácter '#', excepto los últimos cuatro."""
def enmascarar_variable(var):
    s = str(var)
    if len(s) <= 4:
        return s
    return '#' * (len(s) - 4) + s[-4:]

# Uso de la función
texto = "está nublado"
print(enmascarar_variable(texto))


"""30. Crea una función que determine si dos palabras son anagramas, es decir, si están formadas por las mismas letras
pero en diferente orden."""
def son_anagramas(palabra1, palabra2):
    return sorted(palabra1.replace(' ', '').lower()) == sorted(palabra2.replace(' ', '').lower())

# Uso de la función
print(son_anagramas("roma", "amor"))
print(son_anagramas("verano", "invierno"))


"""31. Crea una función que solicite al usuario ingresar una lista de nombres y luego solicite un nombre para buscar en
esa lista. Si el nombre está en la lista, se imprime un mensaje indicando que fue encontrado, de lo contrario, se
lanza una excepción."""
class NombreNoEncontrado(Exception):
    pass

def buscar_nombre():
    lista = input("Introduce una lista de nombres separados por comas: ").split(",")
    lista = [nombre.strip() for nombre in lista]
    nombre = input("Introduce el nombre a buscar: ").strip()
    if nombre in lista:
        print(f"El nombre '{nombre}' fue encontrado en la lista.")
    else:
        raise NombreNoEncontrado(f"El nombre '{nombre}' no está en la lista.")

# Uso de la función
try:
    buscar_nombre()
except NombreNoEncontrado as e:
    print(f"Error: {e}")


"""32. Crea una función que tome un nombre completo y una lista de empleados, busque el nombre completo en la lista y
devuelve el puesto del empleado si está en la lista, de lo contrario, devuelve un mensaje indicando que la persona
no trabaja aquí."""
def buscar_puesto(nombre_completo, empleados):
    for empleado in empleados:
        if empleado["nombre"] == nombre_completo:
            return empleado["puesto"]
    return f"{nombre_completo} no trabaja aquí."

# Uso de la función
empleados = [
    {"nombre": "Ana García", "puesto": "Analista"},
    {"nombre": "Luis Pérez", "puesto": "Desarrollador"},
    {"nombre": "Marta López", "puesto": "Gerente"}
]
print(buscar_puesto("Luis Pérez", empleados)) 
print(buscar_puesto("Pedro Ruiz", empleados))


"""33.  Crea una función lambda que sume elementos correspondientes de dos listas dadas."""
sumar_listas = lambda l1, l2: list(map(lambda x, y: x + y, l1, l2))

# Uso de la función
lista1 = [1, 2, 3]
lista2 = [4, 5, 6]
print(sumar_listas(lista1, lista2))

"""34. Crea la clase Arbol , define un árbol genérico con un tronco y ramas como atributos. Los métodos disponibles son:
crecer_tronco , nueva_rama , crecer_ramas , quitar_rama e info_arbol . El objetivo es implementar estos métodos para
manipular la estructura del árbol."""
class Arbol:
    def __init__(self):
        self.tronco = 1
        self.ramas = []

    def crecer_tronco(self):
        self.tronco += 1

    def nueva_rama(self):
        self.ramas.append(1)

    def crecer_ramas(self):
        self.ramas = [rama + 1 for rama in self.ramas]

    def quitar_rama(self, posicion):
        if 0 <= posicion < len(self.ramas):
            self.ramas.pop(posicion)
        else:
            print("Posición de rama no válida.")

    def info_arbol(self):
        return {
            "longitud_tronco": self.tronco,
            "numero_ramas": len(self.ramas),
            "longitudes_ramas": self.ramas
        }

# Caso de uso
arbol = Arbol()
arbol.crecer_tronco()
arbol.nueva_rama()
arbol.nueva_rama()
arbol.crecer_ramas()
arbol.quitar_rama(0)
print(arbol.info_arbol())


# No existe el ejercicio 35.


"""36. Crea la clase UsuarioBanco ,representa a un usuario de un banco con su nombre, saldo y si tiene o no cuenta
corriente. Proporciona métodos para realizar operaciones como retirar dinero, transferir dinero desde otro usuario y
agregar dinero al saldo."""
class UsuarioBanco:
    def __init__(self, nombre, saldo, cuenta_corriente):
        self.nombre = nombre
        self.saldo = saldo
        self.cuenta_corriente = cuenta_corriente

    def retirar_dinero(self, cantidad):
        if cantidad > self.saldo:
            raise ValueError(f"{self.nombre} no tiene suficiente saldo para retirar {cantidad}.")
        self.saldo -= cantidad

    def transferir_dinero(self, otro_usuario, cantidad):
        if cantidad > self.saldo:
            raise ValueError(f"{self.nombre} no tiene suficiente saldo para transferir {cantidad}.")
        self.saldo -= cantidad
        otro_usuario.saldo += cantidad

    def agregar_dinero(self, cantidad):
        self.saldo += cantidad

    def __str__(self):
        return f"Usuario: {self.nombre}, Saldo: {self.saldo}, Cuenta Corriente: {self.cuenta_corriente}"

# Caso de uso
alicia = UsuarioBanco("Alicia", 100, True)
bob = UsuarioBanco("Bob", 50, True)

bob.agregar_dinero(20)
print(f"Bob tras agregar 20: {bob.saldo}")

try:
    bob.transferir_dinero(alicia, 80)
    print(f"Alicia tras recibir 80 de Bob: {alicia.saldo}")
    print(f"Bob tras transferir 80 a Alicia: {bob.saldo}")
except ValueError as e:
    print(f"Error en transferencia: {e}")

try:
    alicia.retirar_dinero(50)
    print(f"Alicia tras retirar 50: {alicia.saldo}")
except ValueError as e:
    print(f"Error al retirar: {e}")

#Este ejercicio ha sido más dificil ya que me daba un error al no poder  trasnferir 80 unidades de Bob a Alicia, 
# ya que este después de los puntos 1 y 2 de los Casos de uso, tenía 70 unidades y no conseguía que me realizará 
# el punto 4 de los Casos de uso. En este caso usé la IA.

"""37. Crea una función llamada procesar_texto que procesa un texto según la opción especificada: contar_palabras,
reemplazar_palabras , eliminar_palabra . Estas opciones son otras funciones que tenemos que definir primero y llamar dentro
de la función procesar_texto."""
def contar_palabras(texto):
    palabras = texto.split()
    conteo = {}
    for palabra in palabras:
        conteo[palabra] = conteo.get(palabra, 0) + 1
    return conteo

def reemplazar_palabras(texto, palabra_original, palabra_nueva):
    return texto.replace(palabra_original, palabra_nueva)

def eliminar_palabra(texto, palabra):
    palabras = texto.split()
    palabras_filtradas = [p for p in palabras if p != palabra]
    return ' '.join(palabras_filtradas)

def procesar_texto(texto, opcion, *args):
    if opcion == "contar":
        return contar_palabras(texto)
    elif opcion == "reemplazar":
        if len(args) != 2:
            raise ValueError("Para 'reemplazar' se requieren dos argumentos: palabra_original y palabra_nueva.")
        return reemplazar_palabras(texto, args[0], args[1])
    elif opcion == "eliminar":
        if len(args) != 1:
            raise ValueError("Para 'eliminar' se requiere un argumento: palabra a eliminar.")
        return eliminar_palabra(texto, args[0])
    else:
        raise ValueError("Opción no válida. Usa 'contar', 'reemplazar' o 'eliminar'.")

# Caso de uso
texto = "el cielo es azul y el sol es amarillo"
print(procesar_texto(texto, "contar"))
print(procesar_texto(texto, "reemplazar", "azul", "rojo"))
print(procesar_texto(texto, "eliminar", "el"))


"""38. Genera un programa que nos diga si es de noche, de día o tarde según la hora proporcionada por el usuario."""
try:
    hora = int(input("Introduce la hora (0-23): "))
    if hora < 0 or hora > 23:
        print("Hora no válida. Debe estar entre 0 y 23.")
    elif 6 <= hora < 12:
        print("Es de día (mañana).")
    elif 12 <= hora < 20:
        print("Es de tarde.")
    else:
        print("Es de noche.")
except ValueError:
    print("Debes introducir un número entero para la hora.")


"""39. Escribe un programa que determine qué calificación en texto tiene un alumno en base a su calificación numérica."""
try:
    nota = int(input("Introduce la calificación numérica del alumno (0-100): "))
    if nota < 0 or nota > 100:
        print("La calificación debe estar entre 0 y 100.")
    elif nota < 70:
        print("insuficiente")
    elif nota < 80:
        print("bien")
    elif nota < 90:
        print("muy bien")
    else:
        print("excelente")
except ValueError:
    print("Debes introducir un número entero para la calificación.")


"""40. Escribe una función que tome dos parámetros: figura (una cadena que puede ser "rectangulo" , "circulo" o
"triangulo" ) y datos (una tupla con los datos necesarios para calcular el área de la figura)."""
import math

def area_figura(figura, datos):
    figura = figura.lower()
    if figura == "rectangulo":
        base, altura = datos
        return base * altura
    elif figura == "circulo":
        (radio,) = datos
        return math.pi * radio ** 2
    elif figura == "triangulo":
        base, altura = datos
        return (base * altura) / 2
    else:
        raise ValueError("Figura no soportada. Usa 'rectangulo', 'circulo' o 'triangulo'.")

# Uso de la función
print(area_figura("rectangulo", (4, 5)))
print(area_figura("circulo", (3,)))
print(area_figura("triangulo", (6, 2)))


"""41. Programa que calcula el monto final de una compra aplicando un descuento si hay cupón, usando if, elif y else."""
try:
    precio = float(input("Introduce el precio original del artículo: "))
    tiene_cupon = input("¿Tienes un cupón de descuento? (sí/no): ").strip().lower()
    if tiene_cupon == "sí" or tiene_cupon == "si":
        descuento = float(input("Introduce el valor del cupón de descuento: "))
        if descuento > 0:
            precio_final = precio - descuento
            if precio_final < 0:
                precio_final = 0
            print(f"Precio final tras aplicar el cupón: {precio_final} €")
        elif descuento == 0:
            print(f"El cupón no tiene valor. Precio final: {precio} €")
        else:
            print(f"Cupón no válido (valor negativo). Precio final: {precio} €")
    elif tiene_cupon == "no":
        print(f"Precio final sin descuento: {precio} €")
    else:
        print("Respuesta no válida. Escribe 'sí' o 'no'.")
except ValueError:
    print("Por favor, introduce valores numéricos válidos.")











































