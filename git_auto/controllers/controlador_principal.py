#!/usr/bin/python3

########################################################################################################################
# Librerías importadas
########################################################################################################################
# Para procesar os parámetros que se lle pasan ó scrip
import argparse

# Modelo
from models.Datos import *
from models.Repo import *
from views.vista import *

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
    resultados =  []

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
        resultados = datos.config()
    elif args.clone:
        resultados = datos.clone()
    elif args.fetch:
        resultados = datos.fetch()
    elif args.pull:
        resultados = datos.pull()
    elif args.rama:
        resultados = datos.checkout()
    elif args.status:
        resultados = datos.status()
    elif args.info:
            resultados.append(
                {
                    "saida": str(datos),
                    "operacion": "info",
                    "obxecto": None
                }
            )
    else:
        if (len(unknown) > 0):
            if (len(unknown) > 1):
                msgError = msgError.format("n", "s", "s") # Para imprimir a mensaxe en plural

            parser.error(msgError.format("", "", "") + str(unknown))
        else:
            resultados = datos.pull()

    imprimir_datos(resultados)
