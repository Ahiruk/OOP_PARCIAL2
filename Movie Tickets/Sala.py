class Sala:
    def __init__(self) -> None:
        self.disponibilidad= 32
        self.numero_asiento =None
    def reserva(self, disponibilidad : int):
        disponibilidad=disponibilidad-1

