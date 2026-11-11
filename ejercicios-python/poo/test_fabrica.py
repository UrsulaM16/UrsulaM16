"""Pruebas de herencia y representación de vehículos."""
import unittest
from fabrica import Fabrica, Moto, Carro


class TestFabrica(unittest.TestCase):
    def test_moto_hereda_y_tiene_dos_llantas(self):
        moto = Moto("rojo", 1330.0)
        self.assertIsInstance(moto, Fabrica)
        self.assertEqual(moto.llantas, 2)

    def test_carro_hereda_y_tiene_cuatro_llantas(self):
        carro = Carro("azul", 3450.0)
        self.assertIsInstance(carro, Fabrica)
        self.assertEqual(carro.llantas, 4)

    def test_representacion(self):
        self.assertEqual(str(Moto("rojo", 1330.0)), "Moto de color rojo, 2 llantas, 1330.00 €")
        self.assertEqual(str(Carro("azul", 3450.0)), "Carro de color azul, 4 llantas, 3450.00 €")


if __name__ == "__main__":
    unittest.main()
