#!/usr/bin/python3

########################################################################################################################
# Librerías importadas
########################################################################################################################
import sys

########################################################################################################################
# CONSTANTES
########################################################################################################################

## Cores
COR_NORMAL = "\x1b[0m"
COR_RESALTADO = "\x1b[1m"

COR_LINHA = ""

COR_TITULO = "\x1b[32m"
COR_TITULO2 = "\x1b[96m"
COR_SUBTITULO = "\x1b[93m"
COR_OPERACION = COR_NORMAL

## Decoración
ANCHO = 100
CHAR_SEPARADOR1 = "#"
CHAR_SEPARADOR2 = "-"

SEPARADOR1 = COR_RESALTADO + COR_LINHA + (CHAR_SEPARADOR1 * ANCHO ) + COR_NORMAL
SEPARADOR2 = COR_RESALTADO + COR_LINHA + (CHAR_SEPARADOR2 * ANCHO) + COR_NORMAL

SEPARADOR_TITULO = COR_RESALTADO + COR_LINHA + (CHAR_SEPARADOR1 * 2) + COR_NORMAL

TITULO = SEPARADOR_TITULO + COR_RESALTADO + COR_TITULO + " {}" + COR_TITULO2 + " (rama: {})" + COR_NORMAL
OPERACION = SEPARADOR_TITULO + COR_RESALTADO + COR_OPERACION + " {}" + COR_NORMAL
SUBTITULO = SEPARADOR_TITULO + COR_SUBTITULO + " {}" + COR_NORMAL

def imprimir_datos(datos):
    for dato in datos:
        if type(dato) is list:
            for resultado in dato:
                imprimir_resultados(resultado)
        else:
            imprimir_resultados(dato)

def imprimir_resultados(resultado):
    saida = resultado["saida"]

    if resultado["obxecto"] is not None:
        nome = resultado["obxecto"].nome
        rama = resultado["obxecto"].rama
        directorio = resultado["obxecto"].directorio

        operacion = resultado["operacion"]

        print(SEPARADOR1)
        print(OPERACION.format(operacion))
        print(TITULO.format(nome, rama, operacion))
        print(SEPARADOR_TITULO)
        print(SUBTITULO.format(directorio))
        print(SEPARADOR1)
        print()
        print(saida)
        print(SEPARADOR2)
        print()
    else:
        print(saida)
