# 1) ¿Pueden existir funciones dentro de funciones?
def foo():
    # Intentamos llamar a bar antes de que sea creada
    try:
        bar()
    except:
        print('Soy "foo" intentando llamar a "bar" antes de ser creada, no se puede.')
    # Declaramos bar dentro de foo

    def bar():
        print('Hola soy "bar".')

    # Intentamos llamar a bar de nuevo
    print('Hola soy "foo" llamando a "bar" de nuevo.')
    bar()


# Llamamos a foo
foo()

# Intentamos llamar a bar desde fuera de foo
try:
    bar()
except:
    print('No he podido llamar a "bar" desde fuera de "foo".')

# 2) ¿Se puede enviar como parámetro de una función otra función con retorno?
enteros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
def cubo(n): return n**3


cubos = list(map(lambda x: cubo(x), enteros))
print(cubos)

# 3) ¿Qué sucede si dentro de una función se hace un llamado a sí misma?


def fibonacci(n):
    if n > 2:
        return fibonacci(n-1) + fibonacci(n-2)
    else:
        return n


for i in range(1, 10, 1):
    print("fibonacci de ", i, " es ", fibonacci(i))

# 4) ¿Una variable creada como global dentro de una función, ¿sigue existiendo fuera de la función?


def saludar():
    hola = "Hola, cómo estás"
    print(hola, " desde adentro de la función")


saludar()

# Intentamos llamar a bar desde fuera de foo
try:
    print(hola, " desde afuera de la función")
except:
    print('No he podido llamar a "hola" desde fuera de "saludar".')

# 5) Después de indicar una variable en una función como global, ¿hay alguna manera de volver a usar la variable local?

contador = 10


def reiniciar_contador():
    global contador
    contador = 0


print(f'Contador antes es {contador}')
reiniciar_contador()
print(f'Contador después es {contador}')
