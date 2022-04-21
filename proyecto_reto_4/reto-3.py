import os
import time

# Limpia la consola para que sea más fácil de leer la info


def limpiarConsola():
    command = 'clear'
    if os.name in ('nt', 'dos'):  # If Machine is running on Windows, use cls
        command = 'cls'
    os.system(command)

# toma los dtos iniciales del cultivo


def tomarDatosDelCultivo(cultivos):
    print("\t\t\t\t\t\t ERP ADMINISTRACIÓN DE FINCAS\n")
    nombreCultivo = input(
        "Ingrese el nombre del cultivo: ").capitalize().strip()
    nombres = map(lambda cultivo: cultivo.get(
        "nombreCultivo"), cultivos)
    if nombreCultivo in nombres:
        entrar = True
        while entrar:
            limpiarConsola()
            print("\t\t\t\t\t\t ERP ADMINISTRACIÓN DE FINCAS\n")
            nombreCultivo = input(
                "Ingrese otro nombre para el cultivo, este ya existe en la base de datos: ").capitalize().strip()
            if not nombreCultivo in nombres:
                entrar = False

    horarioMantenimiento = input(
        "Ingrese los dias y Horario de Mantenimiento: ")
    horarioRegado = input("Ingrese los dias y Horario de Regado: ")
    horarioAbono = input("Ingrese los dias y Horario de Abono: ")
    etapa = input("Ingrese la Etapa del cultivo e intervalos: ")
    cultivo = {
        "nombreCultivo": nombreCultivo,
        "horarioMantenimiento":  horarioMantenimiento,
        "horarioRegado": horarioRegado,
        "horarioAbono": horarioAbono,
        "etapa": etapa,
    }
    limpiarConsola()
    print("\t\t\t\t\t\t ERP ADMINISTRACIÓN DE FINCAS\n\n")
    print(cultivo)
    time.sleep(3)
    return cultivo

# Muestra las opciones del menú principal


def mostrarMenuPrincipal():
    print("\t\t\t\t\t\t ERP ADMINISTRACIÓN DE FINCAS\n")
    opcion = input(
        "\t1 => Para recolectar información del cultivo \n\t2 => Para administrar los cultivos \n\t0 => Para salir \n\t\t\t\tOPCION: ")
    if not opcion:
        opcion = 100
    opcionLimpia = int(opcion)
    return opcionLimpia

# Muestra las opciones del menu de administración


def mostrarMenuAdministracion():
    print("\t\t\t\t\t\t ERP ADMINISTRACIÓN DE FINCAS\n")
    opcion = input(
        "\t1 => Horario de Gestión de Cultivo \n\t2 => Etapas del Cultivo \n\t3 => Información Contable \n\t4 => Regresar al menu principal  \n\t0 => Para terminar \n\t\t\t\tOPCION: ")
    if not opcion:
        opcion = 100
    opcionLimpia = int(opcion)
    return opcionLimpia

# Elige el cultivo a quien se le va aplicar la gestion


def elegirCultivo(listaCultivos):
    limpiarConsola()
    print("\t\t\t\t\t\t ERP ADMINISTRACIÓN DE FINCAS\n")
    nombres = map(lambda cultivo: cultivo.get(
        "nombreCultivo"), listaCultivos)
    for indice, nombre in enumerate(nombres):
        print(f'{nombre} \t => \t {indice}')
    numeroCultivo = input(
        "\t\t\t\t\tElija el número del cultivo a gestionar : ")
    # if not nombres[numeroCultivo]:
    ##    print("No está en la lista")
    limpiarConsola()
    return int(numeroCultivo)

# Imprime los horarios del cultivo


def mostrarHorarioGestionCultivo(cultivo):
    limpiarConsola()
    print("\t\t\t\t\t\t ERP ADMINISTRACIÓN DE FINCAS\n")
    print("\tNombre: ", cultivo.get("nombreCultivo"))
    print("\tHorario de mantenimiento del cultivo: ",
          cultivo.get("horarioMantenimiento"))
    print("\tHorario de regado del cultivo: ", cultivo.get("horarioRegado"))
    print("\tHorario de abono del cultivo: ", cultivo.get("horarioAbono"))
    time.sleep(5)

# Imprime las etaps del cultivo


def mostrarEtapasCultivo(cultivo):
    limpiarConsola()
    print("\t\t\t\t\t\t ERP ADMINISTRACIÓN DE FINCAS\n")
    print("\tNombre: ", cultivo.get("nombreCultivo"))
    print("\tEtapas del cultivo: ", cultivo.get("etapa"))
    time.sleep(3)

# toma la información adicional de contabilidad del usuario


def tomarInformacionContable():
    limpiarConsola()
    print("\t\t\t\t\t\t ERP ADMINISTRACIÓN DE FINCAS\n")
    medicamentos = input("Ingrese los gastos en medicamentos para cultivo: ")
    imprevistos = input("Ingrese los gastos en imprevistos de los cultivo: ")

    manoDeObra = input("\nIngrese los costos de mano de obra del cultivo: ")
    abono = input("Ingrese los costos en abono del cultivo: ")
    agua = input("Ingrese los costos en agua del cultivo: ")
    mantenimiento = input("Ingrese los costos en mantenimiento del cultivo: ")

    valorArroba = input("\nIngrese el valor por arroba del cultivo: ")
    cantidadrecolectada = input("Ingrese la cantidad en kilos recolectada: ")

    cultivoContable = {
        "medicamentos": int(medicamentos),
        "imprevistos":  int(imprevistos),
        "manoDeObra": int(manoDeObra),
        "abono": int(abono),
        "agua": int(agua),
        "mantenimiento": int(mantenimiento),
        "valorArroba": int(valorArroba),
        "cantidadrecolectada": int(cantidadrecolectada),
    }
    return cultivoContable

# muestra el informe economico


def mostrarInfomeEconomico(cultivo):
    limpiarConsola()
    meses = 5
    print("\t\t\t\t\t\t ERP ADMINISTRACIÓN DE FINCAS: INFORME ECONÓMICO\n")
    print("\tEl siguiente informe hace referencia a los gastos del ciclo de cosecha de los 5 meses.\n ", )
    print("\tNombre: ", cultivo.get("nombreCultivo"))
    print("\tCosto total de mano de obra: ", cultivo.get("manoDeObra")*meses)
    print("\tEl mes ", meses, " no hubo gastos")
    print("\tEl mes ", meses, " hubo menos gastos")
    print("\tEl promedio por mes de los costos Fijos: ", (cultivo.get("manoDeObra") +
          cultivo.get("abono")+cultivo.get("agua")+cultivo.get("mantenimiento"))/meses)
    print("\tEl promedio por mes de los costos variables: ",
          (cultivo.get("medicamentos") + cultivo.get("imprevistos"))/meses)

    ventas = cultivo.get("valorArroba")*cultivo.get("cantidadrecolectada")
    insumos = (cultivo.get("manoDeObra") + cultivo.get("abono")+cultivo.get("agua") +
               cultivo.get("mantenimiento")+cultivo.get("medicamentos") + cultivo.get("imprevistos"))*meses
    cosecha = ventas-insumos
    if cosecha > 0:
        print("\tLas ganancias son $ ", cosecha, " euros")
    elif cosecha == 0:
        print("\tLas ganancias fueron igual a los gastos")
    else:
        print("\tSe perdió $", cosecha * -1, " euros")

    cosecha37 = cosecha*1.37
    if cosecha37 > 0:
        print("\tLas ganancias si se incrementa el valor del kilo en un 37 porciento  $ ",
              cosecha37, " euros")
    elif cosecha37 == 0:
        print("\tLas ganancias si se incrementa el valor del kilo en un 37 porciento fueron igual a los gastos")
    else:
        print("\tSi se incrementa el valor del kilo en un 37 porciento se pierde $",
              cosecha37 * -1, " euros")

    cosecha5and63 = (ventas)*0.63-(insumos)*0.95
    if cosecha5and63 > 0:
        print("\tSi las ganancias disminuyen 63 porciento y los insumos 5 porciento la ganancias son $ ",
              cosecha5and63, " euros")
    elif cosecha5and63 == 0:
        print("\tLas ganancias si se incrementa el valor del kilo en un 37 porciento fueron igual a los gastos")
    else:
        print("\tSi se incrementa el valor del kilo en un 37 porciento se pierde $",
              cosecha5and63 * -1, " euros")
    time.sleep(50)


##
listaCultivos = []
salir = False
# Existen 3 while uno exterior y dos en su interior
# Menu principal
while not salir:
    limpiarConsola()
    opcionMenuPrincipal = mostrarMenuPrincipal()
    if opcionMenuPrincipal == 0:
        print("Fin del programa")
        exit()
    opcionCultivos = False

    while opcionMenuPrincipal != 0 and opcionCultivos != True:
        if opcionMenuPrincipal == 1:
            limpiarConsola()
            cultivo = tomarDatosDelCultivo(listaCultivos)
            listaCultivos.append(cultivo)
            break
        if opcionMenuPrincipal == 2:
            limpiarConsola()
            cultivoElegido = {}
            if not listaCultivos:
                print("\n\n\t\t\t\t\tDebe Ingresar por lo menos un cultivo")
                time.sleep(3)
                limpiarConsola()
                break
            else:
                opcionCultivos = True  # Para salir al segundo menu
        else:
            limpiarConsola()
            print("\n\n\t\t\t\t\t\tOrden no encontrada")
            time.sleep(3.5)
            break
    while opcionCultivos:
        limpiarConsola()
        opcionAdm = mostrarMenuAdministracion()
        if opcionAdm == 1:      # mostrar Horario de Gestion del Cultivo
            cultivo = elegirCultivo(listaCultivos)
            cultivoElegido = listaCultivos[cultivo]
            mostrarHorarioGestionCultivo(cultivoElegido)

        if opcionAdm == 2:      # mostrar Etapas del Cultivo
            cultivo = elegirCultivo(listaCultivos)
            cultivoElegido = listaCultivos[cultivo]
            mostrarEtapasCultivo(cultivoElegido)

        if opcionAdm == 3:      # infome economico
            cultivo = elegirCultivo(listaCultivos)
            cultivoElegido = listaCultivos[cultivo]
            informacionContable = tomarInformacionContable()
            cultivoElegido.update(informacionContable)
            mostrarInfomeEconomico(cultivoElegido)
        if opcionAdm == 4:  # regresar al menu principal
            opcionCultivos = False
        if opcionAdm == 0:  # salir
            print("Fin del programa")
            exit()
