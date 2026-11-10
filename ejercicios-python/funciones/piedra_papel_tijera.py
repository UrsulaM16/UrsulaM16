"""Devuelve el ganador de una ronda de piedra, papel o tijera."""


def run(player1: str, player2: str) -> int:
    """Devuelve 0 si hay empate, 1 si gana el primero o 2 si gana el segundo."""
    p1 = player1.lower()
    p2 = player2.lower()
    if p1 == p2:
        return 0
    if (
        (p1 == "rock" and p2 == "scissors")
        or (p1 == "scissors" and p2 == "paper")
        or (p1 == "paper" and p2 == "rock")
    ):
        return 1
    return 2


if __name__ == "__main__":
    print(run("rock", "scissors"))
