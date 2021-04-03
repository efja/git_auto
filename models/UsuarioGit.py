########################################################################################################################
# Librerías importadas
########################################################################################################################
import os

########################################################################################################################
# UsuarioGit
########################################################################################################################
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
