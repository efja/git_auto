########################################################################################################################
# Remote
########################################################################################################################
class Remote():
    """Información dun servidor remoto de git."""

    # ------------------------------------------------------------------------------------------------------------------
    # CONTRUCTOR
    # ------------------------------------------------------------------------------------------------------------------
    def __init__(self, alias, uri):
        self.__alias = alias
        self.__uri = uri

    # ------------------------------------------------------------------------------------------------------------------
    # GETTERS + SETTERS
    # ------------------------------------------------------------------------------------------------------------------
    @property
    def alias(self):
        return self.__alias

    @alias.setter
    def alias(self, alias):
        self.__alias = alias

    @property
    def uri(self):
        return self.__uri

    @uri.setter
    def uri(self, uri):
        self.__uri = uri

    # ------------------------------------------------------------------------------------------------------------------
    # MÉTODOS
    # ------------------------------------------------------------------------------------------------------------------
    def get_remote_add(self):
        """Devolve o literal para executar o comando 'git remote add alias uri' sen 'git'
        """
        return "remote add " + self.alias + " " + self.uri
