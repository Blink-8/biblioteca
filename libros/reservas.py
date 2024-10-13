# libros/reservas.py
class ReservasSingleton:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(ReservasSingleton, cls).__new__(cls)
            cls._instance.reservas = []
        return cls._instance

    def agregar_reserva(self, libro):
        self.reservas.append(libro)

    def obtener_reservas(self):
        return self.reservas

reservas_singleton = ReservasSingleton()
