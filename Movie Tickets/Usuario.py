class Usuario:
    def __init__(self) -> None:
        self.name= None
        self.preferencia =None
    @property
    def name(self):
        return self.name

    @property
    def preferencia(self):
        return self.preferencia
    def registro(self, name : str, preferencia : int):
        Lista_Usuarios= open("Usuarios.txt","w")
        New_usuario= Lista_Usuarios.write(f"{name},{preferencia}")
        Lista_Usuarios.close()




