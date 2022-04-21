from math import log
import statistics
import math
import time
import os

# limpiar consola


def limpiarConsola():
    command = 'clear'
    if os.name in ('nt', 'dos'):  # If Machine is running on Windows, use cls
        command = 'cls'
    os.system(command)

# muestra las opciones de menu principal, las operaciones


def elegirOpcionMenuprincipal():
    print("\t\t\t•    1  =>	Operaciones aritméticas básicas")
    print("\t\t\t•    2  =>	Operaciones aritméticas extendidas")
    print("\t\t\t•    3  =>	Operaciones Trigonométricas")
    print("\t\t\t•    4  =>	Operaciones estadísticas Básicas")
    print("\t\t\t•    0  =>	Salir del programa")
    opcion = input("\n\t\t\t\t\tElija la opcion deseada: ")
    if not opcion:
        print("Elija al menos una opción: ")
    if not isinstance(opcion, int):
        print("Elija una opción númerica: ")
    return int(opcion)

# este submenu muestra las opciones de las operaciones aritmeticas basicas


def elegirOpcionesBasicas():
    retornar = False
    while not retornar:
        limpiarConsola()
        print("\n\t\t\t\t\t\t\t\t\tCALCULADORA CIENTÍFICA")
        print("\n\t\t\t\t\t\t\t\tOperaciones aritméticas básicas")
        print("\t\t\t•    1  =>	Suma")
        print("\t\t\t•    2  =>	Resta")
        print("\t\t\t•    3  =>	Multiplicación")
        print("\t\t\t•    4  =>	División")
        print("\t\t\t•    0  =>	Salir al menú principal")
        opcion = input("\n\t\t\t\t\tElija la opcion deseada: ")
        if not opcion or not str.isdigit(opcion) or int(opcion) > 4 or int(opcion) < 0:
            limpiarConsola()
            print("\n\t\t\t\t\t\t\tOpción no válida, digite nuevamente: ")
            time.sleep(3.5)
        else:
            retornar = True
    return int(opcion)

# Suma dos numeros


def sumar(a, b):
    return a+b

# resta dos números


def restar(a, b):
    return a-b

# multiplica dos numeros


def multiplicar(a, b):
    return a*b

# divide dos numeros, a divido b


def dividir(a, b):
    if b == 0:
        print("No se puede dividir por 0")
        return 0
    return a/b

# retorna el residuo que resulta de dividir a entre b


def residuo(a, b):
    return a % b

# retorna a elevado a la b


def exponenciar(a, b):
    return pow(a, b)

# retorna el logaritmo de a en base b


def logaritmo(a, b):
    return log(a, b)

# retorna el factorial de un número a


def factorial(a):
    if a == 0:
        return 1
    else:
        return a * factorial(a-1)

# retorna el rsultado de 1 dividido a


def unoEntreNumero(a):
    return 1/a

# retorna el valor absoluto de un número


def valorAbsoluto(a):
    if a >= 0:
        return a
    else:
        return -1*a

# solicita la dos números para ejecutar la suma e imprime el resultado


def tomarNumerosSuma():
    print("\n\t\t\t\t\t\t\t\t\t\tSuma")
    a = int(input("\n\t\t\tIngrese el primer número a sumar: "))
    b = int(input("\t\t\tIngrese el segundo número a sumar: "))
    suma = sumar(a, b)
    print("\n\t\t\tLa suma ", a, " + ", b, " = ", suma)
    time.sleep(3.5)

# solicita la dos números para ejecutar la resta e imprime el resultado


def tomarNumerosResta():
    print("\n\t\t\t\t\t\t\t\t\t\tResta")
    a = int(input("\n\t\t\tIngrese el primer número a restar: "))
    b = int(input("\t\t\tIngrese el segundo número a restar: "))
    resta = restar(a, b)
    print("\n\t\t\tLa resta ", a, " - ", b, " = ", resta)
    time.sleep(3.5)

# solicita la dos números para ejecutar la multiplicacion e imprime el resultado


def tomarNumerosMultiplicacion():
    print("\n\t\t\t\t\t\t\t\t\t\tMultiplicación")
    a = int(input("\n\t\t\tIngrese el primer número a multiplicar: "))
    b = int(input("\t\t\tIngrese el segundo número a multiplicar: "))
    producto = multiplicar(a, b)
    print("\n\t\t\tEl producto de ", a, " * ", b, " = ", producto)
    time.sleep(3.5)

# solicita la dos números para ejecutar la suma e imprime el resultado


def tomarNumerosDivision():
    print("\n\t\t\t\t\t\t\t\t\tDivisión")
    a = int(input("\n\t\t\tIngrese el dividendo: "))
    b = int(input("\t\t\tIngrese el divisor: "))
    division = dividir(a, b)
    print("\n\t\t\tLa división de ", a, " / ", b, " = ", division)
    time.sleep(3.5)

# solicita la dos números para ejecutar la division e imprime el resultado


def tomarNumerosDivisionEntera():
    print("\n\t\t\t\t\t\t\t\tDivisión por entero")
    a = int(input("\n\t\t\tIngrese el dividendo Entero: "))
    b = int(input("\t\t\tIngrese el divisor Entero: "))
    if residuo(a, b) != 0:
        limpiarConsola()
        print("\n\n\n\t\t\t La división no es entera")
    else:
        division = dividir(a, b)
        print("\n\t\t\tLa división entera de ", a, " / ", b, " = ", division)
    time.sleep(3.5)

# solicita la dos números para ejecutar el residuo e imprime el resultado


def tomarNumerosResiduo():
    print("\t\t\t\t\t\t\t\t\tResiduo")
    a = int(input("\n\t\t\tIngrese el primer número: "))
    b = int(input("\t\t\tIngrese el segundo número: "))
    resultado = residuo(a, b)
    print("\n\t\t\tEl residuo de ", a, " % ", b, " = ", resultado)
    time.sleep(3.5)

# solicita la dos números para ejecutar la exponenciación e imprime el resultado


def tomarNumerosExponenciacionEnesima():
    print("\t\t\t\t\t\t\t\tExponenciación Enésima")
    a = int(input("\n\t\t\tIngrese la base: "))
    b = int(input("\t\t\tIngrese el exponente: "))
    resultado = exponenciar(a, b)
    print("\n\t\t\tLa potencia de ", a, " ^ ", b, " = ", resultado)
    time.sleep(3.5)

# solicita el número para ejecutar el logaritmo en base 10 e imprime el resultado


def tomarNumerosLogaritmoBaseDiez():
    print("\t\t\t\t\t\t\t\tLogaritmo en base 10")
    a = int(input("\n\t\t\tIngrese el argumento: "))
    if a < 0:
        print("\t\t\t\t\t\tArgumento negativo, no se puede hacer la operación")
    else:
        resultado = logaritmo(a, 10)
        print("\n\t\t\tLogaritmo en base 10 de ", a, " = ", resultado)
    time.sleep(3.5)

# solicita la dos números para ejecutar el logaritmo enésimo e imprime el resultado


def tomarNumerosLogaritmoEnesimo():
    print("\t\t\t\t\t\t\t\tLogaritmo enésimo")
    a = int(input("\n\t\t\tIngrese el argumento: "))
    b = int(input("\n\t\t\tIngrese la base: "))
    if a < 0:
        print("\t\t\t\t\t\tArgumento negativo, no se puede hacer la operación")
    else:
        resultado = logaritmo(a, b)
        print("\n\t\t\tLogaritmo en base ", b, " de ", a, " = ", resultado)
    time.sleep(3.5)

# solicita la dos números para ejecutar la ra´z enésima e imprime el resultado


def tomarNumerosRaizEnesima():
    print("\t\t\t\t\t\t\t\tRaíz Enésima")
    a = int(input("\n\t\t\tIngrese la argumento: "))
    b = int(input("\t\t\tIngrese la raíz: "))
    if residuo(b, 2) == 0 and a < 0:
        print("\t\t\t\t\t\t No se puede sacar raíz par de un argumento negativo")
    else:
        raiz = exponenciar(a, 1/b)
        print("\n\t\t\tLa raíz ", b, " de ", a, " = ", raiz)
    time.sleep(3.5)

# solicita el número para ejecutar el valor absoluto e imprime el resultado


def tomarNumeroValorAbsoluto():
    print("\t\t\t\t\t\t\t\tValor Absoluto")
    a = int(input("\n\t\t\tIngrese la número: "))
    absoluto = valorAbsoluto(a)
    print("\n\t\t\tEl valor absoluto de ", a, " = ", absoluto)
    time.sleep(3.5)

# solicita el número para ejecutar la función 1/n e imprime el resultado


def tomarNumeroUnoDivididoN():
    print("\n\t\t\t\t\t\t\t\tf(n) = 1/n")
    a = int(input("\n\t\t\tIngrese el número: "))
    if a == 0:
        limpiarConsola()
        print("\n\n\n\t\t\t La división por 0 no es posible")
    else:
        division = dividir(1, a)
        print("\n\t\t\tf(n) = 1/n de ", a, " es = ", division)
    time.sleep(3.5)

# solicita el número para ejecutar el factorial e imprime el resultado


def tomarNumeroFactorial():
    print("\n\t\t\t\t\t\t\t\tFactorial")
    a = int(input("\n\t\t\tIngrese el número: "))
    if a < 0:
        limpiarConsola()
        print("\n\n\n\t\t\t El factorial sólo aplica para números enteros")
    else:
        resultado = factorial(a)
        print("\n\t\t\tel factorial de ", a, " es = ", resultado)
    time.sleep(3.5)

# recibe la opcion elegida para ejecutar la operación básica


def ejecutarOperacionBasica(opcion):
    limpiarConsola()
    print("\n\t\t\t\t\t\t\t\t\tCALCULADORA CIENTÍFICA")
    print("\t\t\t\t\t\t\t\tOperaciones aritméticas básicas")
    if opcion == 1:
        tomarNumerosSuma()
    elif opcion == 2:
        tomarNumerosResta()
    elif opcion == 3:
        tomarNumerosMultiplicacion()
    else:
        tomarNumerosDivision()

# Muestra el menú de operacione aritneticas extendidas y retorna la opcion elegida


def elegirOpcionesAritmeticasExtendida():
    retornar = False
    while not retornar:
        limpiarConsola()
        print("\n\t\t\t\t\t\t\t\t\tCALCULADORA CIENTÍFICA")
        print("\n\t\t\t\t\t\t\t\tOperaciones aritméticas extendidas")
        print("\t\t\t•    1  =>	División entera")
        print("\t\t\t•    2  =>	Residuo")
        print("\t\t\t•    3  =>	Exponenciación enésima")
        print("\t\t\t•    4  =>	Raíz enésima")
        print("\t\t\t•    5  =>	Logaritmo en base 10")
        print("\t\t\t•    6  =>	Logaritmo enésimo")
        print("\t\t\t•    7  =>	Valor absoluto")
        print("\t\t\t•    8  =>	f(n) = 1/n")
        print("\t\t\t•    9  =>	Factorial")
        print("\t\t\t•    0  =>	Salir al menú principal")
        opcion = input("\n\t\t\t\t\tElija la opcion deseada: ")
        if not opcion or not str.isdigit(opcion) or int(opcion) > 9 or int(opcion) < 0:
            limpiarConsola()
            print("\n\t\t\t\t\t\t\t\tOpción no válida, digite nuevamente: ")
            time.sleep(3.5)
        else:
            retornar = True
    return int(opcion)

# Ejecuta la operacione aritneticas extendidas seleccionada


def ejecutarOperacionesAritmeticasExtendidas(opcion):
    limpiarConsola()
    print("\n\t\t\t\t\t\t\t\t\tCALCULADORA CIENTÍFICA")
    print("\n\t\t\t\t\t\t\t\tOperaciones aritméticas extendidas")
    if opcion == 1:
        tomarNumerosDivisionEntera()
    elif opcion == 2:
        tomarNumerosResiduo()
    elif opcion == 3:
        tomarNumerosExponenciacionEnesima()
    elif opcion == 4:
        tomarNumerosRaizEnesima()
    elif opcion == 5:
        tomarNumerosLogaritmoBaseDiez()
    elif opcion == 6:
        tomarNumerosLogaritmoEnesimo()
    elif opcion == 7:
        tomarNumeroValorAbsoluto()
    elif opcion == 8:
        tomarNumeroUnoDivididoN()
    else:
        tomarNumeroFactorial()

# Muestra el menú de operaciones trigonométricas y retorna la opcion elegida


def elegirOpcionestrogonometricas():
    retornar = False
    while not retornar:
        limpiarConsola()
        print("\n\t\t\t\t\t\t\t\t\tCALCULADORA CIENTÍFICA")
        print("\n\t\t\t\t\t\t\t\tOperaciones Trigonométricas")
        print("\t\t\t•    1  =>	Función Seno")
        print("\t\t\t•    2  =>	Función Tangente")
        print("\t\t\t•    0  =>	Salir al menú principal")
        opcion = input("\n\t\t\t\t\tElija la opcion deseada: ")
        if not opcion or not str.isdigit(opcion) or int(opcion) > 2 or int(opcion) < 0:
            limpiarConsola()
            print("\n\t\t\t\t\t\t\t\tOpción no válida, digite nuevamente: ")
            time.sleep(3.5)
        else:
            retornar = True
    return int(opcion)

# solicita el angulo para ejecutar la función seno e imprime el resultado


def tomarNumeroFuncionSeno():
    operar = False
    print("\n\t\t\t\t\t\t\t\tFunción Seno")
    while not operar:
        print("\t\t\t•    1  =>	Ingresar angulo en radines")
        print("\t\t\t•    2  =>	Ingresar angulo en grados")
        opcion = int(input("\n\t\t\t\t\tElija la opcion deseada: "))
        if not opcion or not isinstance(opcion, int) or int(opcion) > 2 or int(opcion) < 0:
            limpiarConsola()
            print("\n\t\t\t\t\t\t\t\tOpción no válida, digite nuevamente: ")
            time.sleep(3.5)
        else:
            operar = True
    angulo = int(input("\n\t\t\tIngrese el ángulo: "))

    if opcion == 2:
        angulo = (angulo * math.pi)/180
    else:
        seno = math.sin(angulo)
        print("\n\t\t\tel seno de ", angulo, " es = ", seno)
    time.sleep(3.5)

# solicita el angulo para ejecutar la función tangente e imprime el resultado


def tomarNumeroTangente():
    operar = False
    print("\n\t\t\t\t\t\t\t\tFunción Seno")
    while not operar:
        print("\t\t\t•    1  =>	Ingresar angulo en radines")
        print("\t\t\t•    2  =>	Ingresar angulo en grados")
        opcion = int(input("\n\t\t\t\t\tElija la opcion deseada: "))
        if not opcion or not isinstance(opcion, int) or int(opcion) > 2 or int(opcion) < 0:
            limpiarConsola()
            print("\n\t\t\t\t\t\t\t\tOpción no válida, digite nuevamente: ")
            time.sleep(3.5)
        else:
            operar = True
    angulo = int(input("\n\t\t\tIngrese el ángulo: "))

    if opcion == 2:
        angulo = (angulo * math.pi)/180
    else:
        seno = math.tan(angulo)
        print("\n\t\t\tLa tangente de ", angulo, " es = ", seno)
    time.sleep(3.5)

# Ejecuta la operacion trigonometrica seleccionada


def ejecutarOperacionesTrigonometricas(opcion):
    limpiarConsola()
    print("\n\t\t\t\t\t\t\t\t\tCALCULADORA CIENTÍFICA")
    print("\t\t\t\t\t\t\t\tOperaciones Trigonométricas")
    if opcion == 1:
        tomarNumeroFuncionSeno()
    else:
        tomarNumeroTangente()

# Muestra el menú de operaciones de estadisticas y retorna la opcion elegida


def elegirOpcionesEstadistica():
    retornar = False
    while not retornar:
        limpiarConsola()
        print("\n\t\t\t\t\t\t\t\t\tCALCULADORA CIENTÍFICA")
        print("\n\t\t\t\t\t\t\t\tOperaciones estadísticas Básicas")
        print("\t\t\t•    1  =>	Promedio")
        print("\t\t\t•    2  =>	Media")
        print("\t\t\t•    3  =>	Mediana")
        print("\t\t\t•    4  =>	Moda")
        print("\t\t\t•    0  =>	Salir al menú principal")
        opcion = input("\n\t\t\t\t\tElija la opcion deseada: ")
        if not opcion or not str.isdigit(opcion) or int(opcion) > 4 or int(opcion) < 0:
            limpiarConsola()
            print("\n\t\t\t\t\t\t\t\tOpción no válida, digite nuevamente: ")
            time.sleep(3.5)
        else:
            retornar = True
    return int(opcion)

# solicita el grupo de datos para encontrar la media e imprime el resultado


def tomarDatosMedia():
    operar = False
    lista = []
    while not operar:
        limpiarConsola()
        print("\n\t\t\t\t\t\t\t\t\tCALCULADORA CIENTÍFICA")
        print("\t\t\t\t\t\t\t\tOperaciones estadísticas Básicas")
        print("\t\t\t\t\t\t\t\tMedia")
        print("\t\t\t•    n  =>	Ingresa el un número del grupo de datos")
        print("\t\t\t•    m  =>	Ingresa la letra m para calcular la media")
        print("\t\t\t•    e  =>	Ingresa la letra e para salir")
        opcion = input("\n\t\t\t\t\tElija la opcion deseada: ")
        if not opcion:
            limpiarConsola()
            print("\n\t\t\t\t\t\t\t\tOpción no válida, digite nuevamente: ")
            time.sleep(3.5)
        elif opcion == "m" or opcion == "M":
            if not bool(lista):
                print("\n\t\t\t\t\t\t\t\tLa media es 0")
                time.sleep(3.5)
            else:
                mean = statistics.mean(lista)
                print("\n\t\t\t\t\t\t\t\tLa media de ", lista, " es ", mean)
                time.sleep(3.5)
            operar = True
        elif opcion == "e" or opcion == "E":
            limpiarConsola()
            print("\n\t\t\t\t\t\t\t\tRegresando al menú")
            time.sleep(3.5)
            return
        elif str.isdigit(opcion):
            opcion = int(opcion)
            lista.append(opcion)
        else:
            print("\n\t\t\t\t\t\t\t\tOpcion no válida")
            time.sleep(3.5)

# solicita el grupo de datos para encontrar la mediana e imprime el resultado


def tomarDatosMediana():
    operar = False
    lista = []
    while not operar:
        limpiarConsola()
        print("\n\t\t\t\t\t\t\t\t\tCALCULADORA CIENTÍFICA")
        print("\t\t\t\t\t\t\t\tOperaciones estadísticas Básicas")
        print("\t\t\t\t\t\t\t\tMediana")
        print("\t\t\t•    n  =>	Ingresa el un número del grupo de datos")
        print("\t\t\t•    m  =>	Ingresa la letra m para calcular la mediana")
        print("\t\t\t•    e  =>	Ingresa la letra e para salir")
        opcion = input("\n\t\t\t\t\tElija la opcion deseada: ")
        if not opcion:
            limpiarConsola()
            print("\n\t\t\t\t\t\t\t\tOpción no válida, digite nuevamente: ")
            time.sleep(3.5)
        elif opcion == "m" or opcion == "M":
            if not bool(lista):
                print("\n\t\t\t\t\t\t\t\tLa mediana es 0")
                time.sleep(3.5)
            else:
                repetidos = set(lista)
                median = statistics.median(repetidos)
                print("\n\t\t\t\t\t\t\t\tLa mediana de ", lista, " es ", median)
                time.sleep(3.5)
            operar = True
        elif opcion == "e" or opcion == "E":
            limpiarConsola()
            print("\n\t\t\t\t\t\t\t\tRegresando al menú")
            time.sleep(3.5)
            return
        elif str.isdigit(opcion):
            opcion = int(opcion)
            lista.append(opcion)
        else:
            print("\n\t\t\t\t\t\t\t\tOpcion no válida")
            time.sleep(3.5)

# solicita el grupo de datos para encontrar la moda e imprime el resultado


def tomarDatosModa():
    operar = False
    lista = []
    while not operar:
        limpiarConsola()
        print("\n\t\t\t\t\t\t\t\t\tCALCULADORA CIENTÍFICA")
        print("\t\t\t\t\t\t\t\tOperaciones estadísticas Básicas")
        print("\t\t\t\t\t\t\t\tModa")
        print("\t\t\t•    n  =>	Ingresa el un número del grupo de datos")
        print("\t\t\t•    m  =>	Ingresa la letra m para calcular la moda")
        print("\t\t\t•    e  =>	Ingresa la letra e para salir")
        opcion = input("\n\t\t\t\t\tElija la opcion deseada: ")
        if not opcion:
            limpiarConsola()
            print("\n\t\t\t\t\t\t\t\tOpción no válida, digite nuevamente: ")
            time.sleep(3.5)
        elif opcion == "m" or opcion == "M":
            if not bool(lista):
                print("\n\t\t\t\t\t\t\t\tLa moda es 0")
                time.sleep(3.5)
            else:
                moda = statistics.mode(lista)
                print("\n\t\t\t\t\t\t\t\tLa moda de ", lista, " es ", moda)
                time.sleep(3.5)
            operar = True
        elif opcion == "e" or opcion == "E":
            limpiarConsola()
            print("\n\t\t\t\t\t\t\t\tRegresando al menú")
            time.sleep(3.5)
            return
        elif str.isdigit(opcion):
            opcion = int(opcion)
            lista.append(opcion)
        else:
            print("\n\t\t\t\t\t\t\t\tOpcion no válida")
            time.sleep(3.5)

# solicita el grupo de datos para encontrar el promedio e imprime el resultado


def tomarDatosPromedio():
    operar = False
    lista = []
    while not operar:
        limpiarConsola()
        print("\n\t\t\t\t\t\t\t\t\tCALCULADORA CIENTÍFICA")
        print("\t\t\t\t\t\t\t\tOperaciones estadísticas Básicas")
        print("\t\t\t\t\t\t\t\tPromedio")
        print("\t\t\t•    n  =>	Ingresa el un número del grupo de datos")
        print("\t\t\t•    p  =>	Ingresa la letra m para calcular la promedio")
        print("\t\t\t•    e  =>	Ingresa la letra e para salir")
        opcion = input("\n\t\t\t\t\tElija la opcion deseada: ")
        if not opcion:
            limpiarConsola()
            print("\n\t\t\t\t\t\t\t\tOpción no válida, digite nuevamente: ")
            time.sleep(3.5)
        elif opcion == "p" or opcion == "P":
            if not bool(lista):
                print("\n\t\t\t\t\t\t\t\tEl promedio es 0")
                time.sleep(3.5)
            else:
                mean = statistics.mean(lista)
                print("\n\t\t\t\t\t\t\t\tel promedio de ", lista, " es ", mean)
                time.sleep(5)
            operar = True
        elif opcion == "e" or opcion == "E":
            limpiarConsola()
            print("\n\t\t\t\t\t\t\t\tRegresando al menú")
            time.sleep(3.5)
            return
        elif str.isdigit(opcion):
            numero = int(opcion)
            lista.append(numero)
        else:
            print("\n\t\t\t\t\t\t\t\tOpcion no válida")
            time.sleep(3.5)

# Ejecuta las operaciones de estadística seleccionada


def ejecutarOperacionesEstadistica(opcion):
    if opcion == 1:
        tomarDatosPromedio()
    elif opcion == 2:
        tomarDatosMedia()
    elif opcion == 3:
        tomarDatosMediana()
    else:
        tomarDatosModa()


# ejecución del ciclo principal, muestra las opciones principales
salir = False  # Salir del menú principal?
salirMenus = True  # Salir de los submenús principal?
opcionbasica = 0  # se inicializa una variable
while not salir:
    limpiarConsola()
    print("\n\t\t\t\t\t\t\t\t\tCALCULADORA CIENTÍFICA")
    opcionPrincipal = elegirOpcionMenuprincipal()
    if opcionPrincipal == 1:
        salirMenus = False
        while not salirMenus:
            opcionbasica = elegirOpcionesBasicas()
            if opcionbasica != 0:
                ejecutarOperacionBasica(opcionbasica)
            else:
                salirMenus = True
    elif opcionPrincipal == 2:
        salirMenus = False
        while not salirMenus:
            opcionExtendida = elegirOpcionesAritmeticasExtendida()
            if opcionExtendida != 0:
                ejecutarOperacionesAritmeticasExtendidas(opcionExtendida)
            else:
                salirMenus = True
    elif opcionPrincipal == 3:
        salirMenus = False
        while not salirMenus:
            opcionTrigonometrica = elegirOpcionestrogonometricas()
            if opcionTrigonometrica != 0:
                ejecutarOperacionesTrigonometricas(opcionTrigonometrica)
            else:
                salirMenus = True
    elif opcionPrincipal == 4:
        salirMenus = False
        while not salirMenus:
            opcionEstadistica = elegirOpcionesEstadistica()
            if opcionEstadistica != 0:
                ejecutarOperacionesEstadistica(opcionEstadistica)
            else:
                salirMenus = True
    elif opcionPrincipal == 0:
        limpiarConsola()
        print("\n\t\tFin del programa")
        time.sleep(3.5)
        exit()
    else:
        limpiarConsola()
        print("\n\n\t\t\t\t\t\tOrden no encontrada")
        time.sleep(3.5)
