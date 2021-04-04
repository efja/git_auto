########################################################################################################################
# Librerías importadas
########################################################################################################################
import os

# Para capturar a saída por consola
import pexpect

########################################################################################################################
# Lóxica
########################################################################################################################
def exec_command(comando_str, directorio = "."):
    """Executa o comando pasdo no string 'command_str' no directorio pasado como argumento, captura o resultado e
    devolveo como un array de bytes.

    Argumentos:
        (str) comando_str   : o literal do commando a executar
        (str) directorio    : indica se hai que cambiar de directorio para executar o comando

    """
    resultado = {}

    # Para volver o directorio actual
    dir_actual = os.getcwd()

    # Cambia ó directorio no que se quere executar o comando
    os.chdir(directorio)

    # Executa o comando
    resultado["saida"], resultado["status"], = pexpect.runu(comando_str, withexitstatus=1)

    # Volve ó directorio actual
    os.chdir(dir_actual)

    return resultado
