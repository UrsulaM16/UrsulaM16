# Ejercicios de Python

Selección de prácticas del curso IFCD0112, adaptadas para ejecutarse de forma independiente con **Python 3.10 o posterior**. Son ejercicios de aprendizaje, no productos terminados.

| Ejercicio | Qué practica | Ejecución desde la raíz del repositorio |
| --- | --- | --- |
| [Fábrica de vehículos](poo/fabrica.py) | Clases, constructores, herencia y representación de objetos | `python3 ejercicios-python/poo/fabrica.py` |
| [Piedra, papel o tijera](funciones/piedra_papel_tijera.py) | Funciones, condicionales, conjuntos, validación de entradas | `python3 ejercicios-python/funciones/piedra_papel_tijera.py` |

## Pruebas automatizadas

Piedra, papel o tijera tiene **cinco pruebas con `unittest`**, ejecutadas correctamente en una comprobación local (incluyen empates, ganadores, mayúsculas, espacios y entradas no válidas).

Desde la raíz del repositorio:

```bash
python3 -m unittest discover -s ejercicios-python/funciones -p 'test_*.py' -v
```

### Contrato de `run(player1, player2)`

- Acepta `rock`, `paper` y `scissors`, ignorando mayúsculas y espacios exteriores.
- Devuelve `0` si hay empate, `1` si gana el primer jugador y `2` si gana el segundo.
- Lanza `ValueError` ante una jugada no válida.

## Alcance

Estos scripts se muestran como evidencia de fundamentos de Python y programación orientada a objetos. El repositorio privado `myproject` contiene otras prácticas de clase que todavía requieren revisión de calidad y privacidad; **no forma parte del portafolio público**.
