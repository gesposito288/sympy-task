import sympy
from typing import Dict

# Controlla il file readme.md per i dettagli su ciascun sub-task

def calcola_derivata(espressione: str, variabile: str) -> sympy.Expr:
    """Sub-task 1: Calcolare una Derivata."""

    # Converte la variabile in simbolo SymPy
    var = sympy.Symbol(variabile)

    # Converte la stringa in espressione matematica SymPy
    expr = sympy.sympify(espressione)

    # Calcola e restituisce la derivata
    derivata = sympy.diff(expr, var)

    return derivata

def main():
    # Esempio di utilizzo
    espressione = "x**3"
    variabile = "x"

    risultato = calcola_derivata(espressione, variabile)

    print("Derivata:", risultato)

    pass


def calcola_integrale_definito(espressione: str, variabile: str, estremo_inf: float, estremo_sup: float
) -> sympy.Expr:
    """Sub-task 2: Calcolare un Integrale Definito."""

    # Converte la variabile in simbolo SymPy
    var = sympy.Symbol(variabile)

    # Converte la stringa in espressione matematica SymPy
    expr = sympy.sympify(espressione)

    # Calcola l'integrale definito
    integrale = sympy.integrate(expr, (var, estremo_inf, estremo_sup))

    return integrale

def main():
    # Esempio di utilizzo
    print("Integrale:", calcola_integrale_definito("x", "x", 0.0, .0))

    pass


def calcola_limite(espressione: str, variabile: str, punto: str) -> sympy.Expr:
    """Sub-task 3: Calcolare un Limite."""

    # Converte la variabile in simbolo SymPy
    var = sympy.Symbol(variabile)

    # Converte il punto in espressione SymPy
    punto_limite = sympy.sympify(punto)

    # Converte la stringa in espressione matematica SymPy
    expr = sympy.sympify(espressione)

    # Calcola il limite
    limite = sympy.limit(expr, var, punto_limite)

    return limite


def main():
    # Esempio di utilizzo
    print("Limite:", calcola_limite("sin(x)/x", "x", "0"))
    pass

def calcola_polinomio_taylor(espressione: str, variabile: str, punto: float, ordine: int) -> sympy.Expr:
    """Sub-task 4: Calcolare una Serie di Taylor."""
    pass

def risolvi_sistema_lineare(eq1: str, eq2: str, var1: str, var2: str) -> Dict[sympy.Symbol, sympy.Expr]:
    """Sub-task 5: Risolvere un Sistema Lineare."""
    pass

def main():
    print("Sub-task 1:", calcola_derivata("x**3", "x"))
    print("Sub-task 2:", calcola_integrale_definito("x", "x", 0.0, 1.0))
    print("Sub-task 3:", calcola_limite("sin(x)/x", "x", "0"))
    print("Sub-task 4:", calcola_polinomio_taylor("exp(x)", "x", 0.0, 4))
    print("Sub-task 5:", risolvi_sistema_lineare("x + y - 3", "x - y - 1", "x", "y"))

if __name__ == "__main__":
    main()
