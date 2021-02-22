# git_auto

Script en Python para automatizar a descarga de información dun conxunto de repositorios de GIT coa información almacenada nun ficheiro JSON.

**Formato do ficheiro de datos:**

```js
{
    "usuario": {
        "usuario"   : "exemplo",
        "email"     : "exemplo@exemplo.gl"
    },
    "repos" : [
        {
            "nome"              : "git_auto.py",
            "rama"              : "main",
            "remoto"            : "origin",
            "uri"               : "git@github.com:efja/git_auto.git",
            "directorio"        : ".",
            "ten_submodulos"    : false,
            "e_submodulo"       : false
        }
    ]
}
```
