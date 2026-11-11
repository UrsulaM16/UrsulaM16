"""Determina el ganador de una ronda de piedra, papel o tijera."""

OPCIONES = {"rock", "paper", "scissors"}


def run(player1: str, player2: str) -> int:
    """Devuelve 0 si hay empate, 1 si gana el primero o 2 si gana el segundo.

    Las jugadas deben ser rock, paper o scissors (sin importar mayúsculas
    ni espacios alrededor). Lanza ValueError para jugadas no válidas.
    """
    p1 = player1.strip().lower()
    p2 = player2.strip().lower()

    if p1 not in OPCIONES or p2 not in OPCIONES:
        raise ValueError("Jugadas válidas: rock, paper, scissors")

    if p1 == p2:
        return 0

    gana_primero = {
        ("rock", "scissors"),
        ("scissors", "paper"),
        ("paper", "rock"),
    }
    return 1 if (p1, p2) in gana_primero else 2


if __name__ == "__main__":
    print(run("rock", "scissors"))
