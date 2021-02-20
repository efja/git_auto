#!/usr/bin/python3
"""git_auto
    :autor      : Fco. Javier González Campos
    :propósito  : Montar un script para automatizar a descarga de información dun conxunto de repositorios de GIT coa
    información almacenada nun ficheiro JSON
    
    :version    : v0.0.1

"""

########################################################################################################################
# Librerías importadas
########################################################################################################################
import sys, os, json

# Para procesar os parámetros que se lle pasan ó scrip
import argparse

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
# Clases
########################################################################################################################

### Usuario
class UsuarioGit():
    """Información básica usuario.
    
    Empregase para configurar o nome de usuario e o email para notificar os commits.
    
    Atributos:
        (str) nome  :
        (str) email :

    """
    # ------------------------------------------------------------------------------------------------------------------
    # CONTRUCTOR
    # ------------------------------------------------------------------------------------------------------------------
    def __init__(self, usuario, email):
        self.__usuario = usuario
        self.__email = email

    # ------------------------------------------------------------------------------------------------------------------
    # GETTERS + SETTERS
    # ------------------------------------------------------------------------------------------------------------------
    @property
    def usuario(self):
        return self.__usuario

    @usuario.setter
    def usuario(self, usuario):
        self.__usuario = usuario

    @property
    def email(self):
        return self.__email

    @email.setter
    def email(self, email):
        self.__email = email
        
    # ------------------------------------------------------------------------------------------------------------------
    # MÉTODOS
    # ------------------------------------------------------------------------------------------------------------------
    def config_usuario(self, config_global = False):
        """Executa o parámetro 'config'.
        
        Executa:
            git config [--global] user.user <nome>
            git config [--global] user.email <email>
        
        Argumentos:
            (bool) config_global: determina se se debe aplicar a configuración de xeito global (True) ou por repo (False)

        """
        GIT_CONFIG_USER = "git {} config user.{} {}."
        global_str = ""
        
        if (config_global):
            global_str = "--global"

        os.system(GIT_CONFIG_USER.format(global_str, "user", self.usuario))
        os.system(GIT_CONFIG_USER.format(global_str, "email", self.email))
        
    # ------------------------------------------------------------------------------------------------------------------
    # MÉTODOS SOBREESCRITOS
    # ------------------------------------------------------------------------------------------------------------------
    def __str__(self):
        saida = "Usuario\t: {}\n" 
        saida += "e-mail\t: {}"
        
        return saida.format(
            self.usuario,
            self.email
        )
        
### Repo
class Repo():
    """Información básico do repo.
    
    Empregase para configurar o nome de usuario e o email para notificar os commits.
    
    Atributos:
        (str) nome          : descripción do repo
        (str) rama          : do repo que coa que se quere automatizar
        (str) remoto        : nome do repo remoto
        (str) uri           : URI do repo remoto
        (str) directorio    : directorio onde se está o repo
        (bool) submodulos   : Indica se ten submóludos configurados, empregase só no clonado. Se é contén submóludos e ó
                            mesmo tempo é un submódulo de outro repo configurado recomendase poñer a False

    """
    # ------------------------------------------------------------------------------------------------------------------
    # CONTRUCTOR
    # ------------------------------------------------------------------------------------------------------------------
    def __init__(self, nome, rama, remoto, uri, directorio, submodulos = False):
        self.__nome = nome
        self.__rama = rama
        self.__remoto = remoto
        self.__uri = uri
        self.__directorio = directorio
        self.__submodulos = submodulos
        
    # ------------------------------------------------------------------------------------------------------------------
    # GETTERS + SETTERS
    # ------------------------------------------------------------------------------------------------------------------
    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def rama(self, nome):
        self.__nome = nome
        
    @property
    def rama(self):
        return self.__rama

    @rama.setter
    def rama(self, rama):
        self.__rama = rama

    @property
    def remoto(self):
        return self.__remoto

    @remoto.setter
    def remoto(self, remoto):
        self.__remoto = remoto

    @property
    def uri(self):
        return self.__uri

    @uri.setter
    def uri(self, uri):
        self.__uri = uri

    @property
    def directorio(self):
        return self.__directorio

    @directorio.setter
    def directorio(self, directorio):
        self.__directorio = directorio

    @property
    def submodulos(self):
        return self.__submodulos

    @submodulos.setter
    def submodulos(self, submodulos):
        self.__submodulos = submodulos
        
    # ------------------------------------------------------------------------------------------------------------------
    # MÉTODOS
    # ------------------------------------------------------------------------------------------------------------------
    def clone(self):
        """Executa o parámetro 'config'.
        
        Executa:
            git config [--global] user.user <nome>
            git config [--global] user.email <email>
        
        Argumentos:
            (bool) config_global: determina se se debe aplicar a configuración de xeito global (True) ou por repo (False)

        """
        submodule_str = ""
        
        # Se ten submodulos descarganse os recursos
        if (self.submodulos):
            submodule_str = "--recurse-submodules"
        
        comando_str = "git clone -b {} {} {} {}".format(self.rama, submodule_str, self.uri, self.dir)
                
        os.system(comando_str)
        
        # Cambia ó directorio do repo
        os.chdir(self.directorio)

    def comando_git(self, operacion, remoto = False, rama = False):
        """Executa unha opeación de git.
        
        Argumentos:
            (str) operacion : o literal da opción a executar por git
            (bool) remoto   : indica se se debe incluír o nome do remoto na operación
            (bool) rama     : indica se se debe incluír o nome da rama na operación

        """
        remoto_str = ""
        rama_str = ""
        
        if (remoto):
            remoto_str = self.remoto
        if (rama):
            rama_str = self.rama
            
        comando_str = "git {} {} {}".format(operacion, remoto_str, rama_str)
        
        # Para volver o directorio actual
        dir_actual = os.getcwd()
        
        # Cambia ó directorio do repo
        os.chdir(self.directorio)
        
        # Volve ó directorio actual
        os.system(comando_str)
        os.chdir(dir_actual)
        
    def status(self):
        """Executa 'git status' a través de 'self.comando_git()'."""
        
        self.imprimir_cabeciera()
        self.comando_git("status")
        self.imprimir_final()
        
    def checkout(self):
        """Executa 'git checkout' a través de 'self.comando_git()'."""
        
        self.imprimir_cabeciera()
        self.comando_git("checkout", rama=True)
        self.imprimir_final()
        
    def fetch(self):
        """Executa 'git fetch' a través de 'self.comando_git()'."""
        
        self.checkout()
        self.comando_git("fetch", remoto=True)
        self.imprimir_final()

    def pull(self):
        """Executa 'git pull' a través de 'self.comando_git()'."""
        
        self.checkout()
        self.comando_git("pull", remoto=True, rama=True)
        self.imprimir_final()
        
    def imprimir_cabeciera(self):
        """Imprime unha cabeceira para mostar os resultados das operaicóns sobre o repo."""
        
        # Para volver o directorio actual
        dir_actual = os.getcwd()
        
        print(SEPARADOR1)
        print(TITULO.format(self.directorio, self.rama))
        print(SEPARADOR_TITULO)
        print(SUBTITULO.format(dir_actual))
        print(SEPARADOR1)
        print()
        
    def imprimir_final(self):
        """Imprime un final de sección para mostar os resultados das operaicóns sobre o repo."""
        
        print(SEPARADOR2)
        print()
    
    # ------------------------------------------------------------------------------------------------------------------
    # MÉTODOS SOBREESCRITOS
    # ------------------------------------------------------------------------------------------------------------------
    def __str__(self):
        saida = "Título\t\t: {}\n" 
        saida += "Rama\t\t: {}\n" 
        saida += "Remoto\t\t: {}\n"
        saida += "URI\t\t: {}\n"
        saida += "Directorio\t: {}\n"
        saida += "Ten submodulos\t: {}"
        
        return saida.format(
            self.nome,
            self.rama,
            self.remoto,
            self.uri,
            self.directorio,
            self.submodulos
        )

### Repo
class Datos():
    """Estructura de información que se manexa no ficheiro JSON.
    
    Empregase para modelar o ficheiro JSON.
    
    Atributos:
        (str) ficheiro          : ficheiro de onde sacar información
        (UsuarioGit) usuario    : información do usuario
        (list Repo) repos       : lista de tódolos repos a manexar

    """
    # ------------------------------------------------------------------------------------------------------------------
    # CONTRUCTOR
    # ------------------------------------------------------------------------------------------------------------------
    def __init__(self, ficheiro):
        self.__ficheiro = ficheiro
        self.__usuario = None
        self.__repos = list()
        
    # ------------------------------------------------------------------------------------------------------------------
    # GETTERS + SETTERS
    # ------------------------------------------------------------------------------------------------------------------
    @property
    def ficheiro(self):
        return self.__ficheiro

    @ficheiro.setter
    def ficheiro(self, ficheiro):
        self.__ficheiro = ficheiro

    @property
    def usuario(self):
        return self.__usuario

    @usuario.setter
    def usuario(self, usuario):
        self.__usuario = usuario
    
    @property
    def repos(self):
        return self.__repos

    @repos.setter
    def repos(self, repos):
        self.__repos = repos

    # ------------------------------------------------------------------------------------------------------------------
    # MÉTODOS
    # ------------------------------------------------------------------------------------------------------------------
    def add_repo(self, repo):
        """Engade un Repo á lista."""
        self.repos.append(repo)
    
    def config(self):
        """Imprime a información do usuario."""
        self.usuario.config_usuario()
        
    def fetch(self):
        """Executa 'git fetch' de cada Repo."""
        for repo in self.repos:
            print()
            repo.fetch()
        
    def pull(self):
        """Executa 'git pull' de cada Repo."""
        for repo in self.repos:
            print()
            repo.pull()
        
    def checkout(self):
        """Executa 'git checkout' de cada Repo."""
        for repo in self.repos:
            print()
            repo.checkout()
        
    def status(self):
        """Executa 'git status' de cada Repo."""
        for repo in self.repos:
            print()
            repo.status()
        
    def __repos_str(self):
        """Recolle o str de cada repo para imprimir o resultado."""
        saida = ""
        
        for repo in self.repos:
            saida += "\n" + str(repo) + "\n"
            
        return saida
    
    # ------------------------------------------------------------------------------------------------------------------
    # Funcións sobre ficheiros
    # ------------------------------------------------------------------------------------------------------------------
    def cargar_json(self):
        """Carga o contido dun ficheiro JSON válido (para o script).
        
        Returns:
            (dict): dicionario
            
        """
        diccionario = {}
        
        try:
            with open(self.ficheiro, mode='r', encoding='utf-8') as file:
                diccionario = json.loads(file.read())
        except (FileNotFoundError, json.decoder.JSONDecodeError):
            print(json.decoder.JSONDecodeError)
            
        return diccionario

    def cargar_datos(self):
        """Parsea o contido dun ficheiro JSON."""
        
        datos_json = self.cargar_json()
        
        for k, v in datos_json.items():
            if (k == "usuario"):
                usuario = v
                self.usuario = UsuarioGit(usuario["usuario"], usuario["email"])
            elif (k == "repos"):
                for item in v:
                    aux = item
                    repo = Repo(
                                aux["nome"],
                                aux["rama"],
                                aux["remoto"],
                                aux["uri"],
                                aux["directorio"],
                                aux["submodulos"]
                            )
                    self.add_repo(repo)

    # ------------------------------------------------------------------------------------------------------------------
    # MÉTODOS SOBREESCRITOS
    # ------------------------------------------------------------------------------------------------------------------
    def __str__(self):
        sep = "-" * 120
        saida = "\n\nUsuario GIT\n" + sep + "\n" + str(self.usuario) + "\n" + sep
        saida += "\n\nREPOS:\n" + sep + "\n"
        saida += self.__repos_str() + sep + "\n"
        
        return saida

########################################################################################################################
# Función principal
########################################################################################################################
def main(argv):
    datos= Datos(_FICHEIRO_REPOS)
    datos.cargar_datos()

    msgError = "Non se recoñece{} o{} parámetro{}: "
    
    parser = argparse.ArgumentParser(description="Sen argumentos é equivalente a pasarlle o parámetro [-p]")
    
    # Argumentos
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
    