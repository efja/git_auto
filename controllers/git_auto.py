#!/usr/bin/python3
"""git_auto
    :autor      : Fco. Javier González Campos
    :propósito  : Montar un script para automatizar a descarga de información dun conxunto de repositorios de GIT coa
    información almacenada nun ficheiro JSON

    :version    : v0.0.2

"""

########################################################################################################################
# Librerías importadas
########################################################################################################################
import sys

# Para procesar os parámetros que se lle pasan ó scrip
import argparse

# Modelo
import Datos

########################################################################################################################
# CONSTANTES
########################################################################################################################
_FICHEIRO_REPOS = 'repos.json'

## Cores
COR_NORMAL = "\x1b[0m"
COR_RESALTADO = "\x1b[1m"

COR_LINHA = ""

COR_TITULO = "\x1b[32m"
COR_TITULO2 = "\x1b[96m"
COR_SUBTITULO = "\x1b[93m"

## Decoración
ANCHO = 100
CHAR_SEPARADOR1 = "#"
CHAR_SEPARADOR2 = "-"

SEPARADOR1 = COR_RESALTADO + COR_LINHA + (CHAR_SEPARADOR1 * ANCHO ) + COR_NORMAL
SEPARADOR2 = COR_RESALTADO + COR_LINHA + (CHAR_SEPARADOR2 * ANCHO) + COR_NORMAL

SEPARADOR_TITULO = COR_RESALTADO + COR_LINHA + (CHAR_SEPARADOR1 * 2) + COR_NORMAL

TITULO = SEPARADOR_TITULO + COR_RESALTADO + COR_TITULO + " {}" + COR_NORMAL + COR_TITULO2 + " rama: {}" + COR_NORMAL
SUBTITULO = SEPARADOR_TITULO + COR_SUBTITULO + " {}" + COR_NORMAL

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

########################################################################################################################
# Execución principal
########################################################################################################################
if __name__ == '__main__':
    main(sys.argv[1:])
