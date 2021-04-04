########################################################################################################################
# Librerías importadas
########################################################################################################################
import json

# Modelo
from models.Repo import *
from models.UsuarioGit import *

########################################################################################################################
# Datos
########################################################################################################################
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

    def clone(self):
        """Executa 'git clone' e despois 'git checkout' de cada Repo."""
        for repo in self.repos:
            print()
            repo.clone()

        self.checkout()

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
        except  json.decoder.JSONDecodeError as e:
            print("json in error: {}".format(e.msg))
        except FileNotFoundError as e:
            print(e)

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
                                aux["ten_submodulos"],
                                aux["e_submodulo"]
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
