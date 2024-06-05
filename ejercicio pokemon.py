import csv
import msvcrt
import os

pokemones = ""
with open('pokemon_primera_generacion.csv',newline='', encoding='utf-8') as a:
    datos = csv.reader(a,delimiter=",")
    pokemones = list(datos)

while True:
    print("<<Press any key>>")
    msvcrt.getch()
    os.system('cls')
    print("""\033[33m
    Sistema Gestión Pokémon
    ═══════════════════════
    1) Mostrar todos los Pokémon disponibles
    2) Buscar un Pokémon por nombre
    3) Agregar un Pokémon al cinturón
    4) Mostrar los Pokémon en el cinturón
    5) Quitar un Pokémon en el cinturón
    0) Salir \033[0m""")
    opcion = int(input("Seleccione una opción: "))
    if opcion==0:
        break
    elif opcion==1:
        for i in range(1,len(pokemones)):
            print(f"{i+1}.- \033[34mNOMBRE: {pokemones[i][1]}\033[0m  ║ \033[33mTIPO: {pokemones[i][2]}\033[0m ║ \033[32mALTURA: {pokemones[i][3]}\033[0m ║ \033[35mPESO: {pokemones[i][4]}\033[0m ║")
    elif opcion==2:
        print("\033[33mBuscar Pokémon\033[0m")
        nombre = input("Ingrese el nombre para buscar : ")
        centinela = False
        for pok in pokemones:
            if pok[1]==nombre:
                print(f"Pokémon Encontrado \033[33mTIPO: {pokemones[i][2]}\033[0m ║ \033[32mALTURA: {pokemones[i][3]}\033[0m ║ \033[35mPESO: {pokemones[i][4]}\033[0m")
                centinela = True
        if centinela==False:
            print("\033[31mPokémon no encontrado \033[0m")
    elif opcion==3:
        print("\033[34mAgregar Estudiante\033[0m")
        nombre = input("Ingrese Nombre y Apellido")
        if len(nombre)>=5:
    else:
        print("\033[31mOpción no válida\033[0m")