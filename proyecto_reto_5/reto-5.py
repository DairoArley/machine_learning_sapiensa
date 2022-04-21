# python version 3.9.0
import statistics
import math
import time
import os

listaEstudiantes = []


def limpiarConsola():
    command = 'clear'
    if os.name in ('nt', 'dos'):
        command = 'cls'
    os.system(command)


def mostrarMenuPrincipal():
    retornar = False
    while not retornar:
        limpiarConsola()
        print("\n\t\t\t\t\t\t\t\t\tADMINISTRACIÓN DE ESTUDIANTES")
        print("\t\t\t•    1  =>	Agregar estudiante")
        print("\t\t\t•    2  =>	Buscar estudiante")
        print("\t\t\t•    3  =>	Modificar notas de estudiante")
        print("\t\t\t•    4  =>	Cancelar materia")
        print("\t\t\t•    5  =>	Resultados por estudiante")
        print("\t\t\t•    6  =>	Informe de grupo")
        print("\t\t\t•    7  =>	Mostrar todos los estudiantes")
        print("\t\t\t•    0  =>	Salir del programa")
        opcion = input("\n\t\t\t\t\tElija la opcion deseada: ")
        if not opcion or not str.isdigit(opcion) or int(opcion) > 7 or int(opcion) < 0:
            limpiarConsola()
            print("\n\n\n\t\t\t\t\t\t\tOpción no válida, digite nuevamente ")
            time.sleep(3)
        else:
            retornar = True
    return int(opcion)


def buscarestudiante(identificacion):
    estudianteEncontrado = list(filter(
        lambda estudiante: estudiante.get('identificacion') == identificacion, listaEstudiantes))
    if estudianteEncontrado:
        return estudianteEncontrado[0]
    else:
        return 0


def tomarNota(indice):
    retorno = False
    while not retorno:
        limpiarConsola()
        print("\n\t\t\t\t\t\t\t\t\tADMINISTRACIÓN DE ESTUDIANTES")
        print("\t\t\t\t\t\t\t\t\t\tIngresar notas\n\t\t\t")
        aux = "\t\t\t•    Ingrese la nota "+str(indice)+" : "
        nota = input(aux)
        if not nota or not str.isdigit(nota):
            limpiarConsola()
            print("\n\n\n\t\t\t\t\t\t\t\tOpción no válida")
            time.sleep(3)
        elif int(nota) > 5 and int(nota) < 0:
            limpiarConsola()
            print("\n\n\n\t\t\t\t\t\t\t\tOpción no válida")
            time.sleep(3)
        else:
            return nota


def agregarEstudiante():
    retornar = False
    estudiante = {}
    indentificacion = ""
    nombre = ""
    correo = ""
    telefono = ""
    fechaNacimiento = ""
    while not retornar:
        limpiarConsola()
        print("\n\t\t\t\t\t\t\t\t\tADMINISTRACIÓN DE ESTUDIANTES")
        print("\t\t\t\t\t\t\t\t\t\tAgregar estudiante")
        indentificacion = input(
            "\n\t\t\t•    Ingrese la identificación del estudiante sin puntos ni comas: ")
        if not indentificacion or not str.isdigit(indentificacion):
            limpiarConsola()
            print("\n\n\n\t\t\t\t\t\t\t\tOpción no válida, digite nuevamente")
            time.sleep(3.5)
        else:
            if listaEstudiantes:
                listaIdentificaciones = list(
                    map(lambda e: e.get("identificacion"), listaEstudiantes))
                if indentificacion in listaIdentificaciones:
                    limpiarConsola()
                    print(
                        "\n\n\n\t\t\t\t\t\t\t\tYa existe el estudiante en base de datos, para modificar elija la opcion en el menú principal")
                    time.sleep(3)
                else:
                    retornar = True
            else:
                retornar = True

    retornar = False
    while not retornar:
        limpiarConsola()
        print("\n\t\t\t\t\t\t\t\t\tADMINISTRACIÓN DE ESTUDIANTES")
        print("\t\t\t\t\t\t\t\t\t\tAgregar estudiante")
        nombre = input("\n\t\t\t•    Ingrese el nombre del estudiante: ")
        if not nombre or str.isdigit(nombre):
            limpiarConsola()
            print("\n\n\n\t\t\t\t\t\t\t\tOpción no válida, digite nuevamente")
            time.sleep(3.5)
        else:
            retornar = True

    retornar = False
    while not retornar:
        limpiarConsola()
        print("\n\t\t\t\t\t\t\t\t\tADMINISTRACIÓN DE ESTUDIANTES")
        print("\t\t\t\t\t\t\t\t\t\tAgregar estudiante")
        correo = input("\n\t\t\t•    Ingrese el correo del estudiante: ")
        if not correo or str.isdigit(correo) or "@" not in correo:
            limpiarConsola()
            print("\n\n\n\t\t\t\t\t\t\t\tOpción no válida o correo sin @")
            time.sleep(3.5)
        else:
            retornar = True

    retornar = False
    while not retornar:
        limpiarConsola()
        print("\n\t\t\t\t\t\t\t\t\tADMINISTRACIÓN DE ESTUDIANTES")
        print("\t\t\t\t\t\t\t\t\t\tAgregar estudiante")
        telefono = input("\n\t\t\t•    Ingrese el teléfono del estudiante: ")
        if not telefono or not str.isdigit(telefono):
            limpiarConsola()
            print("\n\n\n\t\t\t\t\t\t\t\tOpción no válida, no es númerico")
            time.sleep(3.5)
        else:
            retornar = True

    retornar = False
    while not retornar:
        limpiarConsola()
        print("\n\t\t\t\t\t\t\t\t\tADMINISTRACIÓN DE ESTUDIANTES")
        print("\t\t\t\t\t\t\t\t\t\tAgregar estudiante")
        fechaNacimiento = input(
            "\n\t\t\t•    Ingrese la fecha de nacimiento del estudiante con la mascara dd/mm/yyyy: ")
        if not fechaNacimiento or str.isdigit(fechaNacimiento):
            limpiarConsola()
            print("\n\n\n\t\t\t\t\t\t\t\tOpción no válida")
            time.sleep(3.5)
        else:
            retornar = True

    estudiante.update({"identificacion": indentificacion})
    estudiante.update({"nombre": nombre.title()})
    estudiante.update({"correo": correo})
    estudiante.update({"telefono": telefono})
    estudiante.update({"fechaNacimiento": fechaNacimiento})

    retornar = False
    while not retornar:
        limpiarConsola()
        print("\n\t\t\t\t\t\t\t\t\tADMINISTRACIÓN DE ESTUDIANTES")
        print("\t\t\t\t\t\t\t\t\t\tAgregar estudiante")
        for i in range(1, 6):
            nota = tomarNota(i)
            clave = "nota-"+str(i)
            estudiante.update({clave: nota})
        retornar = True
    limpiarConsola()
    print("\n\t\t\t\t\t\t\t\t\tADMINISTRACIÓN DE ESTUDIANTES")
    print("\t\t\t\t\t\t\t\t\t\tAgregar estudiante")
    print(estudiante)
    listaEstudiantes.append(estudiante)
    time.sleep(3)
    return


def pedirIdEstudianteYBuscar():
    retornar = False
    while not retornar:
        limpiarConsola()
        print("\n\t\t\t\t\t\t\t\t\tADMINISTRACIÓN DE ESTUDIANTES")
        print("\t\t\t\t\t\t\t\t\t\tBuscar estudiante")
        indentificacion = input(
            "\n\t•    Ingrese la identificación del estudiante que desea buscar, sin puntos ni comas: ")
        if not indentificacion or not str.isdigit(indentificacion):
            limpiarConsola()
            print("\n\n\n\t\t\t\t\t\t\t\tOpción no válida, digite nuevamente")
            time.sleep(2)
        else:
            if bool(listaEstudiantes):
                estudianteAux = buscarestudiante(indentificacion)
                if estudianteAux == 0:
                    print(
                        "\n\n\n\t\t\t\t\t\t\t\tEl estudiante no existe en base de datos")
                    time.sleep(3.5)
                else:
                    print("\n", estudianteAux)
                    time.sleep(3.5)
                    break
            else:
                print(
                    "\n\n\n\t\t\t\t\t\tAún no hay estudiantes matriculados, elija la opción Ingresar estudiante")
                time.sleep(3.5)
                break
    return estudianteAux


def modificarEstudiante(estudiante):
    limpiarConsola()
    print("\n\t\t\t\t\t\t\t\t\tADMINISTRACIÓN DE ESTUDIANTES")
    print("\t\t\t\t\t\t\t\t\t\tModificar notas de estudiante")
    print(estudiante)
    time.sleep(2)

    for i in range(1, 6):
        nota = tomarNota(i)
        clave = "nota-"+str(i)
        estudiante.update({clave: nota})

    for i, estudianteAux in enumerate(listaEstudiantes):
        if estudianteAux.get("identificacion") == estudiante.get("identificacion"):
            listaEstudiantes[i] = estudiante
    return estudiante


def pedirIdEstudianteYmodificar():
    retornar = False
    while not retornar:
        limpiarConsola()
        print("\n\t\t\t\t\t\t\t\t\tADMINISTRACIÓN DE ESTUDIANTES")
        print("\t\t\t\t\t\t\t\t\tModificar notas de estudiante")
        indentificacion = input(
            "\n\t\t\t•    Ingrese la identificación del estudiante que desea modificarle las notas, sin puntos ni comas: ")
        if not indentificacion or not str.isdigit(indentificacion):
            limpiarConsola()
            print("\n\n\n\t\t\t\t\t\t\t\tOpción no válida, digite nuevamente")
            time.sleep(2)
        else:
            if bool(listaEstudiantes):
                estudianteBuscado = buscarestudiante(indentificacion)
                print(estudianteBuscado)
                if estudianteBuscado == 0:
                    print(
                        "\n\n\n\t\t\t\t\t\t\tEl estudiante no existe en base de datos")
                    time.sleep(2)
                else:
                    estudianteModificado = modificarEstudiante(
                        estudianteBuscado)
                    limpiarConsola()
                    print("\n\t\t\t\t\t\t\t\t\tADMINISTRACIÓN DE ESTUDIANTES")
                    print("\t\t\t\t\t\t\t\t\tModificar notas de estudiante")
                    print("\n\n\n", estudianteModificado)
                    time.sleep(3)
                    break
            else:
                print(
                    "\n\n\n\t\t\t\t\tAún no hay estudiantes matriculados, elija la opción Ingresar estudiante")
                time.sleep(3)
                break


def mostrarTodosLosEstudiantes(lista):
    limpiarConsola()
    print("\n\t\t\t\t\t\t\t\t\tADMINISTRACIÓN DE ESTUDIANTES")
    print("\t\t\t\t\t\t\t\t\tMostrar todos los estudiantes")
    [print(estudiante) for estudiante in lista]
    time.sleep(6)


def eliminarEstudiante(estudiante):
    listaEstudiantes.remove(estudiante)


def cancelacionMateria():
    retornar = False
    while not retornar:
        limpiarConsola()
        print("\n\t\t\t\t\t\t\t\t\tADMINISTRACIÓN DE ESTUDIANTES")
        print("\t\t\t\t\t\t\t\t\tCancelación de materia")
        indentificacion = input(
            "\n\t\t\t•    Ingrese la identificación del estudiante que desea cancelarle la materia, sin puntos ni comas: ")
        if not indentificacion or not str.isdigit(indentificacion):
            limpiarConsola()
            print("\n\n\n\t\t\t\t\t\t\t\tOpción no válida, digite nuevamente")
            time.sleep(2)
        else:
            if bool(listaEstudiantes):
                estudianteBuscado = buscarestudiante(indentificacion)
                if estudianteBuscado == 0:
                    print(
                        "\n\n\n\t\t\t\t\t\t\tEl estudiante no existe en base de datos")
                    time.sleep(2)
                else:
                    print("Estudiante encontrado: \n", estudianteBuscado)
                    time.sleep(2)
                    respuesta = input(
                        "\n\t\t\t•    Desea eliminar el estudiante? Si / No: ")
                    if respuesta.upper() == "SI":
                        eliminarEstudiante(estudianteBuscado)
                        print("\t\t\t\tEstudiante eliminado")
                        time.sleep(3)
                        break
                    elif respuesta.upper() == "NO":
                        break
                    else:
                        print("\t\t\t\tOpcion no encontrada")
                        time.sleep(3)
            else:
                print(
                    "\n\n\n\t\t\t\t\tAún no hay estudiantes matriculados, elija la opción Ingresar estudiante")
                time.sleep(3)
                break


def calcularNotafinal(estudiante):
    nota1 = int(estudiante.get("nota-1"))
    nota2 = int(estudiante.get("nota-2"))
    nota3 = int(estudiante.get("nota-3"))
    nota4 = int(estudiante.get("nota-4"))
    nota5 = int(estudiante.get("nota-5"))
    return (nota1+nota2+nota3+nota4+nota5)/5


def calcularNotaPromedio(lista):
    promedios = list(
        map(lambda estudiante: calcularNotafinal(estudiante), lista))

    return sum(promedios)/len(lista)


def calcularPercentil(lista, percentil):
    promedios = list(
        map(lambda estudiant: calcularNotafinal(estudiant), lista))
    size = len(promedios)
    return sorted(promedios)[int(math.ceil((size * percentil) / 100)) - 1]


def resultadosPorEstudiante():
    retornar = False
    while not retornar:
        limpiarConsola()
        print("\n\t\t\t\t\t\t\t\t\tADMINISTRACIÓN DE ESTUDIANTES")
        print("\t\t\t\t\t\t\t\t\tResultados por estudiante")
        indentificacion = input(
            "\n\t\t\t•    Ingrese la identificación del estudiante que le desea realizar los cálculos, sin puntos ni comas: ")
        if not indentificacion or not str.isdigit(indentificacion):
            limpiarConsola()
            print("\n\n\n\t\t\t\t\t\t\t\tOpción no válida, digite nuevamente")
            time.sleep(2)
        else:
            if bool(listaEstudiantes):
                estudianteBuscado = buscarestudiante(indentificacion)
                if estudianteBuscado == 0:
                    print(
                        "\n\n\n\t\t\t\t\t\t\tEl estudiante no existe en base de datos")
                    time.sleep(2)
                else:
                    print("Estudiante encontrado: \n", estudianteBuscado)
                    time.sleep(2)

                    notaFinal = calcularNotafinal(estudianteBuscado)
                    print("La nota final del estudiante ", estudianteBuscado.get(
                        "nombre"), " Machine Learning es de ", notaFinal)
                    time.sleep(1)
                    notaPromedio = calcularNotaPromedio(listaEstudiantes)
                    print(
                        "La nota promedio del grupo de Machine Learning es de ", notaPromedio)
                    time.sleep(1)
                    if notaFinal >= notaPromedio:
                        print("El estudiante ", estudianteBuscado.get("nombre"), " estuvo por encima del promedio: ",
                              notaFinal, " >= ", notaPromedio)
                        time.sleep(1)
                    else:
                        print("El estudiante ", estudianteBuscado.get("nombre"), " estuvo por debajo del promedio: ",
                              notaFinal, " < ", notaPromedio)
                        time.sleep(1)
                    if notaFinal >= 3:
                        print(
                            "El estudiante ", estudianteBuscado.get("nombre"), " ganó el curso de Machine Learning en: ", notaFinal)
                        time.sleep(1)
                    else:
                        print(
                            "El estudiante ", estudianteBuscado.get("nombre"), " perdió el curso de Machine Learning en: ", notaFinal)
                        time.sleep(1)
                    percentil_25 = calcularPercentil(listaEstudiantes, 25)
                    percentil_50 = calcularPercentil(listaEstudiantes, 50)
                    percentil_75 = calcularPercentil(listaEstudiantes, 75)
                    percentil_100 = calcularPercentil(listaEstudiantes, 100)
                    promedio = calcularNotafinal(estudianteBuscado)
                    if promedio >= 0 and promedio <= percentil_25:
                        print("El estudiante ", estudianteBuscado.get(
                            "nombre"), " está en el percentil ", percentil_25)
                    elif promedio > percentil_25 and promedio <= percentil_50:
                        print("El estudiante ", estudianteBuscado.get(
                            "nombre"), " está en el percentil ", percentil_50)
                    elif promedio > percentil_50 and promedio <= percentil_75:
                        print("El estudiante ", estudianteBuscado.get(
                            "nombre"), " está en el percentil ", percentil_75)
                    elif promedio > percentil_75 and promedio <= percentil_100:
                        print("El estudiante ", estudianteBuscado.get(
                            "nombre"), " está en el percentil ", percentil_100)
                    time.sleep(5)
                    break
            else:
                print(
                    "\n\n\n\t\t\t\t\tAún no hay estudiantes matriculados, elija la opción Ingresar estudiante")
                time.sleep(3)
                break


def ejecutarInformeDeGrupo():
    retornar = False
    while not retornar:
        limpiarConsola()
        print("\n\t\t\t\t\t\t\t\t\tADMINISTRACIÓN DE ESTUDIANTES")
        print("\t\t\t\t\t\t\t\t\tInforme de grupo")

        if bool(listaEstudiantes):
            notasFinales = list(
                map(lambda estudiante: calcularNotafinal(estudiante), listaEstudiantes))
            nombres = list(
                map(lambda estudiante: estudiante.get("nombre"), listaEstudiantes))
            [print("La nota final del estudiante ", nom, " Machine Learning es de ", notaF)
             for nom, notaF in zip(nombres, notasFinales)]
            time.sleep(1)
            notaPromedio = calcularNotaPromedio(listaEstudiantes)
            print("La nota promedio del grupo de Machine Learning es de ", notaPromedio)
            time.sleep(1)
            estudiantesPorDebajo = list(
                filter(lambda nota: nota < notaPromedio, notasFinales))
            estudiantesPorEncima = list(
                filter(lambda nota: nota >= notaPromedio, notasFinales))
            print("La cantidad de estudiantes que estuvieron por encima del promedio fueron ",  len(
                estudiantesPorEncima))
            time.sleep(1)
            print("La cantidad de estudiantes que estuvieron por debajo del promedio fueron ",  len(
                estudiantesPorDebajo))
            time.sleep(1)
            estudiantesGanadores = list(
                filter(lambda nota: nota < 3, notasFinales))
            estudiantesPerdedores = list(
                filter(lambda nota: nota >= 3, notasFinales))
            print("La cantidad de estudiantes que ganaron la materia fueron ",  len(
                estudiantesGanadores))
            time.sleep(1)
            print("La cantidad de estudiantes que perdieron la materia fueron ",  len(
                estudiantesPerdedores))
            time.sleep(1)
            print("El porcentaje de estudiantes que ganaron es de ",
                  (len(estudiantesGanadores)*100)/len(nombres))
            time.sleep(1)
            print("El porcentaje de estudiantes que perdieron es de ",
                  (len(estudiantesPerdedores)*100)/len(nombres))
            time.sleep(1)

            percentil_25 = calcularPercentil(listaEstudiantes, 25)
            percentil_50 = calcularPercentil(listaEstudiantes, 50)
            percentil_75 = calcularPercentil(listaEstudiantes, 75)
            percentil_100 = calcularPercentil(listaEstudiantes, 100)
            estudiantes25 = list(
                filter(lambda nota: nota >= 0 and nota <= percentil_25, notasFinales))
            estudiantes50 = list(
                filter(lambda nota: nota > percentil_25 and nota <= percentil_50, notasFinales))
            estudiantes75 = list(
                filter(lambda nota: nota > percentil_50 and nota <= percentil_75, notasFinales))
            estudiantes100 = list(filter(
                lambda nota: nota > percentil_75 and nota <= percentil_100, notasFinales))
            print("Hay ", len(estudiantes25),
                  " estudiantes en el percentil ", percentil_25)
            print("Hay ", len(estudiantes50),
                  " estudiantes en el percentil ", percentil_50)
            print("Hay ", len(estudiantes75),
                  " estudiantes en el percentil ", percentil_75)
            print("Hay ", len(estudiantes100),
                  " estudiantes en el percentil ", percentil_100)

            print("La moda de las notas es ", statistics.mode(notasFinales))
            print("La mediana de las notas es ",
                  statistics.median(notasFinales))
            print("La desviación estandar de las notas es ",
                  statistics.stdev(notasFinales))
            time.sleep(8)
            break
        else:
            print(
                "\n\n\n\t\t\t\t\tAún no hay estudiantes matriculados, elija la opción Ingresar estudiante")
            time.sleep(2)
            break


def ejecutarOpcionMenuPrincipal(opcion):
    if opcion == 1:
        agregarEstudiante()
    elif opcion == 2:
        pedirIdEstudianteYBuscar()
    elif opcion == 3:
        pedirIdEstudianteYmodificar()
    elif opcion == 4:
        cancelacionMateria()
    elif opcion == 5:
        resultadosPorEstudiante()
    elif opcion == 6:
        ejecutarInformeDeGrupo()
    else:
        mostrarTodosLosEstudiantes(listaEstudiantes)


salir = False
while not salir:
    opcionPrincipal = mostrarMenuPrincipal()
    if opcionPrincipal == 0:
        limpiarConsola()
        print("\n\n\n\t\t\t\t\tFin del programa")
        time.sleep(2)
        exit()
    else:
        ejecutarOpcionMenuPrincipal(opcionPrincipal)
