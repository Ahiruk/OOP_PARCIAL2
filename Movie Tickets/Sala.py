class Sala:
    def __init__(self) -> None:
        self.disponibilidad= 32
        self.numero_asiento =None
    @property
    def disponibilidad(self):
        return self.disponibilidad
    @property
    def numero_asiento(self):
        return self.numero_asiento

    def reserva(self, disponibilidad : int):
        disponibilidad=disponibilidad-1
        return disponibilidad
    def cancelar(self, disponibilidad : int):
        disponibilidad=disponibilidad+1
        return disponibilidad



