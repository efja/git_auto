#!/usr/bin/python3

########################################################################################################################
# Librerías importadas
########################################################################################################################
# Para procesar os parámetros que se lle pasan ó scrip
import argparse

# Modelo
import models.Datos as Datos

########################################################################################################################
# CONSTANTES
########################################################################################################################
_FICHEIRO_REPOS = 'data/repos.json'

########################################################################################################################
# Función principal
########################################################################################################################
def main(argv):
    datos= Datos(_FICHEIRO_REPOS)
    datos.cargar_datos()

    msgError = "Non se recoñece{} o{} parámetro{}: "

    parser = argparse.ArgumentParser(description="Sen argumentos é equivalente a pasarlle o parámetro [-p]")

    # Argumentos
    parser.add_argument("--clone", help="Clona os repos nos directorios asigandos e cambia a rama á definida", action="store_true")
    parser.add_argument("-c", "--config", help="Aplica a configuración de git: <user.name> e <user.email>", action="store_true")
    parser.add_argument("-f", "--fetch", help="Fai un fetch en tódolos repos", action="store_true")
    parser.add_argument("-p", "--pull", help="Fai un pull en tódolos repos", action="store_true")
    parser.add_argument("-r", "--rama", help="Pon o HEAD nas ramas principais en tódolos repos", action="store_true")
    parser.add_argument("-s", "--status", help="Recorre os repos e executa <git status>", action="store_true")
    parser.add_argument("-i", "--info", help="Imprime a información do ficheiro de datos", action="store_true")

    args, unknown = parser.parse_known_args()
    # Accións dos argumenteos

    if args.config:
        datos.config()
    elif args.clone:
        datos.clone()
    elif args.fetch:
        datos.fetch()
    elif args.pull:
        datos.pull()
    elif args.rama:
        datos.checkout()
    elif args.status:
        datos.status()
    elif args.info:
        print(datos)
    else:
        if (len(unknown) > 0):
            if (len(unknown) > 1):
                msgError = msgError.format("n", "s", "s") # Para imprimir a mensaxe en plural

            parser.error(msgError.format("", "", "") + str(unknown))
        else:
            datos.pull()
