"""Pruebas de las reglas y errores de piedra, papel o tijera."""
import unittest
from piedra_papel_tijera import run


class TestPiedraPapelTijera(unittest.TestCase):
    def test_empates(self):
        for jugada in ("rock", "paper", "scissors"):
            with self.subTest(jugada=jugada):
                self.assertEqual(run(jugada, jugada), 0)

    def test_gana_primero(self):
        for p1, p2 in (("rock", "scissors"), ("scissors", "paper"), ("paper", "rock")):
            with self.subTest(p1=p1, p2=p2):
                self.assertEqual(run(p1, p2), 1)

    def test_gana_segundo(self):
        for p1, p2 in (("scissors", "rock"), ("paper", "scissors"), ("rock", "paper")):
            with self.subTest(p1=p1, p2=p2):
                self.assertEqual(run(p1, p2), 2)

    def test_mayusculas_y_espacios(self):
        self.assertEqual(run(" ROCK ", "Scissors"), 1)

    def test_jugadas_invalidas(self):
        for p1, p2 in (("lizard", "rock"), ("rock", ""), ("", "")):
            with self.subTest(p1=p1, p2=p2):
                with self.assertRaises(ValueError):
                    run(p1, p2)


if __name__ == "__main__":
    unittest.main()
