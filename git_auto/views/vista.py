#!/usr/bin/python3

########################################################################################################################
# Librerías importadas
########################################################################################################################
import sys

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
