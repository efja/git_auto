########################################################################################################################
# Librerías importadas
########################################################################################################################
import os

########################################################################################################################
# Repo
########################################################################################################################
class Repo():
    """Información básico do repo.

    Empregase para configurar o nome de usuario e o email para notificar os commits.

    Atributos:
        (str) nome              : descripción do repo
        (str) rama              : do repo que coa que se quere automatizar
        (str) remoto            : nome do repo remoto
        (str) uri               : URI do repo remoto
        (str) directorio        : directorio onde se está o repo
        (bool) ten_submodulos   : Indica se ten submóludos configurados, empregase só no clonado. Se é contén submóludos e ó
                                mesmo tempo é un submódulo de outro repo configurado recomendase poñer a False
        (bool) e_submodulo      : Indica se o repo é un submóludo e se debe tratar como tal

    """
    # ------------------------------------------------------------------------------------------------------------------
    # CONTRUCTOR
    # ------------------------------------------------------------------------------------------------------------------
    def __init__(self, nome, rama, remoto, uri, directorio, ten_submodulos = False, e_submodulo = False, remotes = None):
        self.__nome = nome
        self.__rama = rama
        self.__remoto = remoto
        self.__uri = uri
        self.__directorio = directorio
        self.__ten_submodulos = ten_submodulos
        self.__e_submodulo = e_submodulo

        if remotes != None:
            self.__remotes = remotes
        else:
            self.__remotes = []

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
    def ten_submodulos(self):
        return self.__ten_submodulos

    @ten_submodulos.setter
    def ten_submodulos(self, ten_submodulos):
        self.__ten_submodulos = ten_submodulos

    @property
    def e_submodulo(self):
        return self.__e_submodulo

    @e_submodulo.setter
    def e_submodulo(self, e_submodulo):
        self.__e_submodulo = e_submodulo

    @property
    def remotes(self):
        return self.__remotes

    @remotes.setter
    def remotes(self, remotes):
        self.__remotes = remotes

    # ------------------------------------------------------------------------------------------------------------------
    # MÉTODOS
    # ------------------------------------------------------------------------------------------------------------------
    def clone(self):
        """Executa o parámetro 'clone'.

        Executa:
            git clone [--recurse-submodules] <uri> <directorio>

        """
        submodule_str = ""

        if (not self.e_submodulo):
            # Se ten ten_submodulos descarganse os recursos
            if (self.ten_submodulos):
                submodule_str = "--recurse-submodules"

            comando_str = "git clone -b {} {} {} {}".format(self.rama, submodule_str, self.uri, self.directorio)

            # Para volver o directorio actual
            dir_actual = os.getcwd()

            os.system(comando_str)

            # Cambia ó directorio do repo
            os.chdir(dir_actual)

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

        os.system(comando_str)

        # Volve ó directorio actual
        os.chdir(dir_actual)

    def status(self):
        """Executa 'git status' a través de 'self.comando_git()'."""

        self.comando_git("status")

    def checkout(self):
        """Executa 'git checkout' a través de 'self.comando_git()'."""

        self.comando_git("checkout", rama=True)

    def fetch(self):
        """Executa 'git fetch' a través de 'self.comando_git()'."""

        self.checkout()
        self.comando_git("fetch", remoto=True)

    def pull(self):
        """Executa 'git pull' a través de 'self.comando_git()'."""

        self.checkout()
        self.comando_git("pull", remoto=True, rama=True)

    def set_remotes(self):
        """Executa 'git remote add' coa lista de obxectos da clase 'remote' a través de 'self.comando_git()'."""

        self.checkout()

        for remote in self.remotes:
            self.comando_git(remote.get_remote_add, remoto=False, rama=False)

    def add_remote(self, remote):
        """Engade un remoto á lista de remotos e executa 'git remote add' para este remoto."""

        self.checkout()

        self.remotes.push(remote)
        self.comando_git(remote.get_remote_add, remoto=False, rama=False)

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
        saida += "É submodulo\t: {}"

        return saida.format(
            self.nome,
            self.rama,
            self.remoto,
            self.uri,
            self.directorio,
            self.ten_submodulos,
            self.e_submodulo
        )
