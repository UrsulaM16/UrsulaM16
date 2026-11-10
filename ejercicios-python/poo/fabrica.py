"""Ejercicio de herencia con dos tipos de vehículos."""


class Fabrica:
    def __init__(self, llantas: int, color: str, precio: float) -> None:
        self.llantas = llantas
        self.color = color
        self.precio = precio


class Moto(Fabrica):
    def __init__(self, color: str, precio: float) -> None:
        super().__init__(2, color, precio)

    def __str__(self) -> str:
        return f"Moto de color {self.color}, {self.llantas} llantas, {self.precio:.2f} €"


class Carro(Fabrica):
    def __init__(self, color: str, precio: float) -> None:
        super().__init__(4, color, precio)

    def __str__(self) -> str:
        return f"Carro de color {self.color}, {self.llantas} llantas, {self.precio:.2f} €"


if __name__ == "__main__":
    print(Moto("rojo", 1330.0))
    print(Carro("azul", 3450.0))
